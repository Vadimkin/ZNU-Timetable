# -*- coding: utf-8 -*-

from django.contrib import admin
from timetable.models import Department, Group, Teacher, Campus, Audience, Lesson, Timetable, Time


class CampusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Department)
admin.site.register(Group)
admin.site.register(Teacher)
admin.site.register(Time)
admin.site.register(Campus, CampusAdmin)
admin.site.register(Audience)
admin.site.register(Lesson)
admin.site.register(Timetable)