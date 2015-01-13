# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.core.paginator import InvalidPage
from django.http import Http404

from tastypie import fields
from tastypie.resources import Resource, ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.utils import trailing_slash
from timetable.models import Department, Group, Teacher, Campus, Audience, Lesson, Timetable, Time
from timetable.utils import get_current_week


class DepartmentResource(ModelResource):
    class Meta:
        queryset = Department.objects.all()
        include_resource_uri = False
        resource_name = 'department'

        filtering = {
            'id': ALL_WITH_RELATIONS
        }


class GroupResource(ModelResource):
    department = fields.ForeignKey(DepartmentResource, 'department')

    class Meta:
        queryset = Group.objects.all()
        include_resource_uri = False
        resource_name = 'group'

        filtering = {
            'id': ALL_WITH_RELATIONS,
            'department': ALL_WITH_RELATIONS
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
            objects.append({'id': result.id, 'name': result.name, 'department_id': result.department.id, 'last_update': result.last_update})

        object_list = {
            'objects': objects,
        }

        self.log_throttled_access(request)
        return self.create_response(request, object_list)

    def dehydrate(self, bundle):
        del bundle.data['department']
        bundle.data['department_id'] = bundle.obj.department.id

        return bundle


class TeacherResource(ModelResource):
    class Meta:
        queryset = Teacher.objects.all()
        include_resource_uri = False
        resource_name = 'teacher'

        filtering = {
            'id': ALL_WITH_RELATIONS,
        }


class CampusResource(ModelResource):
    class Meta:
        queryset = Campus.objects.all()
        resource_name = 'campus'

        filtering = {
            'id': ALL_WITH_RELATIONS,
        }


class AudienceResource(ModelResource):
    campus = fields.ForeignKey(CampusResource, 'campus')

    class Meta:
        queryset = Audience.objects.all()
        include_resource_uri = False
        resource_name = 'audience'

        filtering = {
            'id': ALL_WITH_RELATIONS,
            'campus': ALL,
        }

    def dehydrate(self, bundle):
        del bundle.data['campus']
        bundle.data['campus_id'] = bundle.obj.campus.id

        return bundle


class LessonResource(ModelResource):
    class Meta:
        queryset = Lesson.objects.all()
        include_resource_uri = False
        resource_name = 'lesson'

        filtering = {
            'id': ALL_WITH_RELATIONS,
        }


class TimeResource(ModelResource):
    class Meta:
        queryset = Time.objects.all()
        include_resource_uri = False
        resource_name = 'time'

        filtering = {
            'id': ALL_WITH_RELATIONS,
        }


class TimetableResource(ModelResource):
    teacher = fields.ForeignKey(TeacherResource, 'teacher')
    lesson = fields.ForeignKey(LessonResource, 'lesson')
    group = fields.ForeignKey(GroupResource, 'group')

    class Meta:
        queryset = Timetable.objects.all()
        include_resource_uri = False
        resource_name = 'timetable'

        filtering = {
            'periodicity': ALL_WITH_RELATIONS,
            'group': ALL,
            'teacher': ALL
        }

    def dehydrate(self, bundle):
        del bundle.data['lesson']
        del bundle.data['teacher']
        del bundle.data['group']

        bundle.data['teacher_id'] = bundle.obj.teacher.id
        bundle.data['group_id'] = bundle.obj.group.id
        bundle.data['lesson_id'] = bundle.obj.lesson.id
        bundle.data['audience_id'] = bundle.obj.audience.id
        if bundle.obj.period:
            bundle.data['time_id'] = bundle.obj.period.id

        return bundle


class DictToObj(object):
    """
    Convert dictionary to object
    @source http://stackoverflow.com/a/1305561/383912
    """

    def __init__(self, d):
        self.__dict__['d'] = d

    def __getattr__(self, key):
        value = self.__dict__['d'][key]
        if type({}) == type(value):
            return DictToObj(value)

        return value


class CurrentWeekResource(Resource):
    week = fields.CharField(attribute='week')

    class Meta:
        resource_name = 'current_week'
        include_resource_uri = False

    def obj_get_list(self, request=None, **kwargs):
        bundle = []
        current_week = get_current_week()
        bundle.append(DictToObj({'week': current_week}))
        return bundle

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del (data_dict['meta'])
            if 'objects' in data_dict:
                data_dict = data_dict['objects'][0]
            return data_dict