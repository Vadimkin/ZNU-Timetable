# -*- coding: utf-8 -*-

from tastypie import fields
from tastypie.resources import Resource, ModelResource, ALL, ALL_WITH_RELATIONS
from timetable.models import Departament, Group, Teacher, Campus, Audience, Lesson, Timetable


class DepartamentResource(ModelResource):
    class Meta:
        queryset = Departament.objects.all()
        resource_name = 'departament'
        # excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        # filtering = {
        # 'username': ALL,
        # }


class GroupResource(ModelResource):
    class Meta:
        queryset = Group.objects.all()
        resource_name = 'group'


class TeacherResource(ModelResource):
    class Meta:
        queryset = Teacher.objects.all()
        include_resource_uri = False
        resource_name = 'teacher'


class CampusResource(ModelResource):
    class Meta:
        queryset = Campus.objects.all()
        resource_name = 'campus'


class AudienceResource(ModelResource):
    class Meta:
        queryset = Audience.objects.all()
        resource_name = 'audience'


class LessonResource(ModelResource):
    class Meta:
        queryset = Lesson.objects.all()
        resource_name = 'lesson'


class TimetableResource(ModelResource):
    # TODO filter by group name

    class Meta:
        queryset = Timetable.objects.all()
        include_resource_uri = False
        resource_name = 'timetable'

        filtering = {
            'periodicity': ALL_WITH_RELATIONS,
            'group': ALL,
        }

    def dehydrate(self, bundle):
        bundle.data['teacher_name'] = bundle.obj.teacher.name
        bundle.data['teacher_id'] = bundle.obj.teacher.id

        bundle.data['group_name'] = bundle.obj.group.name
        bundle.data['group_departament'] = bundle.obj.group.departament.id
        bundle.data['group_departament_name'] = bundle.obj.group.departament.name

        return bundle


class dictToObj(object):
    """
    Convert dictionary to object
    @source http://stackoverflow.com/a/1305561/383912
    """

    def __init__(self, d):
        self.__dict__['d'] = d

    def __getattr__(self, key):
        value = self.__dict__['d'][key]
        if type(value) == type({}):
            return dictToObj(value)

        return value


class CurrentWeekResource(Resource):
    week = fields.CharField(attribute='week')

    class Meta:
        resource_name = 'current_week'
        include_resource_uri = False

    def obj_get_list(self, request=None, **kwargs):
        from datetime import datetime

        bundle = []
        current_week = (int(datetime.today().strftime("%U")) % 2) + 1 # If first week of year is numerator
        bundle.append(dictToObj({'week': current_week}))
        return bundle

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del (data_dict['meta'])
            if 'objects' in data_dict:
                data_dict = data_dict['objects'][0]
            return data_dict