# -*- coding: utf-8 -*-

from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
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