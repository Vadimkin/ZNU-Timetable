# -*- coding: utf-8 -*-
from datetime import datetime
import json

from django.conf.urls import url
from django.core.urlresolvers import reverse
from django.db.models import Max
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from tastypie import fields
from tastypie.contrib.contenttypes import resources
from tastypie.resources import Resource, ALL
from tastypie.utils import trailing_slash
from timetable.models import Department, Group, Teacher, Campus, Audience, Lesson, Timetable, Time
from timetable.utils import get_current_week


def build_content_type(format, encoding='utf-8'):
    """
    Appends character encoding to the provided format if not already present.
    """
    if 'charset' in format:
        return format

    return "%s; charset=%s" % (format, encoding)


class UTFModelResource(resources.ModelResource):
    def create_response(self, request, data, response_class=HttpResponse, **response_kwargs):
        """
        Extracts the common "which-format/serialize/return-response" cycle.
        Mostly a useful shortcut/hook.
        """
        desired_format = self.determine_format(request)
        serialized = self.serialize(request, data, desired_format)
        return response_class(content=serialized, content_type=build_content_type(desired_format), **response_kwargs)


class DepartmentResource(UTFModelResource):
    class Meta:
        queryset = Department.objects.filter(last_update__gt=0)
        include_resource_uri = False
        resource_name = 'department'
        allowed_methods = ['get', ]

    def get_object_list(self, request):
        return super(DepartmentResource, self).get_object_list(request)


class GroupResource(UTFModelResource):
    department = fields.ForeignKey(DepartmentResource, 'department')

    class Meta:
        queryset = Group.objects.all()
        include_resource_uri = False
        resource_name = 'group'
        allowed_methods = ['get', ]

        filtering = {
            'id': ALL,
            'department': ALL
        }

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/search%s$" % (self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_search'), name="api_get_search"),
        ]

    def get_search(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        self.throttle_check(request)

        sqs = Group.objects.filter(name__contains=request.GET.get('s'))

        objects = []

        for result in sqs:
            objects.append({'id': result.id, 'name': result.name, 'department_id': result.department.id,
                            'last_update': result.last_update})

        object_list = {
            'objects': objects,
        }

        self.log_throttled_access(request)
        return self.create_response(request, object_list)

    def dehydrate(self, bundle):
        del bundle.data['department']
        bundle.data['department_id'] = bundle.obj.department.id
        bundle.data['subgroup_count'] = Timetable.objects.filter(group=bundle.obj).aggregate(Max('subgroup'))[
            'subgroup__max']

        if not bundle.data['subgroup_count']:
            bundle.data['subgroup_count'] = 0

        return bundle


class TeacherResource(UTFModelResource):
    class Meta:
        queryset = Teacher.objects.all()
        include_resource_uri = False
        resource_name = 'teacher'
        allowed_methods = ['get', ]

        filtering = {
            'id': ALL,
        }

    def dehydrate(self, bundle):
        if bundle.data['id'] == 50:  # return null teacher as empty variable
            bundle.data['name'] = ''

        return bundle


class CampusResource(UTFModelResource):
    class Meta:
        queryset = Campus.objects.all()
        resource_name = 'campus'
        allowed_methods = ['get', ]

        filtering = {
            'id': ALL,
        }

    def dehydrate(self, bundle):
        if bundle.data['id'] == 9:  # return null campus as empty variable
            bundle.data['name'] = ''

        return bundle


class AudienceResource(UTFModelResource):
    campus = fields.ForeignKey(CampusResource, 'campus')

    class Meta:
        queryset = Audience.objects.all()
        include_resource_uri = False
        resource_name = 'audience'
        allowed_methods = ['get', ]

        filtering = {
            'id': ALL,
            'campus': ALL,
        }

    def dehydrate(self, bundle):
        del bundle.data['campus']
        bundle.data['campus_id'] = bundle.obj.campus.id

        if bundle.data['campus_id'] == 9:  # return null audience as empty variable
            bundle.data['audience'] = ''

        return bundle


class LessonResource(UTFModelResource):
    class Meta:
        queryset = Lesson.objects.all()
        include_resource_uri = False
        resource_name = 'lesson'
        allowed_methods = ['get', ]

        filtering = {
            'id': ALL,
        }


class TimeResource(UTFModelResource):
    class Meta:
        queryset = Time.objects.all()
        include_resource_uri = False
        resource_name = 'time'
        allowed_methods = ['get', ]

        filtering = {
            'id': ALL,
        }


class TimetableResource(UTFModelResource):
    teacher = fields.ForeignKey(TeacherResource, 'teacher', null=True, blank=True)
    lesson = fields.ForeignKey(LessonResource, 'lesson')
    group = fields.ManyToManyField(GroupResource, 'group')

    class Meta:
        queryset = Timetable.objects.all()
        include_resource_uri = False
        resource_name = 'timetable'
        allowed_methods = ['get', ]

        filtering = {
            'periodicity': ALL,
            'group': ALL,
            'teacher': ALL,
        }

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/teachers_by_group%s$" % (self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_teachers_by_group'), name="api_get_teachers_by_group"),
        ]

    def get_teachers_by_group(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        self.throttle_check(request)

        # TODO Validate ID
        sqs = Timetable.objects.filter(group=request.GET.get('group'))

        if sqs.count() == 0:
            return HttpResponseNotFound(json.dumps({'error': '1', 'status': 'Not found'}))

        objects = []

        for result in sqs:
            if result.teacher is not None and result.teacher.id not in objects:
                objects.append(result.teacher.id)

        self.log_throttled_access(request)
        return HttpResponseRedirect(reverse('api_dispatch_list', kwargs={'resource_name': 'timetable',
                                                                         'api_name': 'v1'}) + "?format=json&teacher__in=" + ",".join(
            "{0}".format(n) for n in objects))

    def alter_list_data_to_serialize(self, request, data):
        try:
            if request.GET.get('group', False) is not False:
                data['meta']['subgroup_count'] = \
                    Timetable.objects.filter(group=request.GET['group']).order_by('-subgroup')[0].subgroup
        except IndexError:
            pass
        return data

    def dehydrate(self, bundle):
        del bundle.data['lesson']
        del bundle.data['teacher']

        try:
            extended = bundle.request.GET['extended']
        except MultiValueDictKeyError:
            extended = 0

        if extended:
            bundle.data['teacher'] = bundle.obj.teacher

            bundle.data['group'] = []

            for one_group in bundle.obj.group.all():
                bundle.data['group'].append(one_group)

            try:
                bundle.data['audience_num'] = bundle.obj.audience.audience
                bundle.data['campus'] = bundle.obj.audience.campus
            except AttributeError:
                bundle.data['audience'] = None

            bundle.data['lesson'] = bundle.obj.lesson.name

            if bundle.obj.period:
                bundle.data['time_num'] = bundle.obj.period.num
                bundle.data['time_start'] = bundle.obj.period.time_start
                bundle.data['time_end'] = bundle.obj.period.time_end

        else:
            try:
                bundle.data['teacher_id'] = bundle.obj.teacher.id
            except AttributeError:
                bundle.data['teacher_id'] = None

            bundle.data['group'] = []

            for one_group in bundle.obj.group.all():
                bundle.data['group'].append(one_group.id)

            bundle.data['lesson_id'] = bundle.obj.lesson.id

            try:
                bundle.data['audience_id'] = bundle.obj.audience.id
            except AttributeError:
                bundle.data['audience_id'] = None

            if bundle.obj.period:
                bundle.data['time_id'] = bundle.obj.period.id

        return bundle


class CurrentWeekResource(Resource):
    timetable_week = fields.IntegerField(attribute='timetable_week')
    year_week = fields.IntegerField(attribute='year_week')

    class Meta:
        resource_name = 'current_week'
        include_resource_uri = False
        allowed_methods = ['get', ]

    class DictToObj(object):
        """
        Convert dictionary to object
        @source http://stackoverflow.com/a/1305561/383912
        """

        def __init__(self, d):
            self.__dict__['d'] = d

        def __getattr__(self, key):
            value = self.__dict__['d'][key]
            if type(value) == type({}):
                return self.DictToObj(value)

            return value

    def obj_get_list(self, request=None, **kwargs):
        bundle = []
        current_week = get_current_week()
        week_of_year = datetime.today().isocalendar()[1]
        bundle.append(self.DictToObj({'timetable_week': current_week, 'year_week': week_of_year}))
        return bundle

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del (data_dict['meta'])
            if 'objects' in data_dict:
                data_dict = data_dict['objects'][0]
            return data_dict