# -*- coding: utf-8 -*-
from datetime import datetime

from django.contrib import admin
from timetable.models import Department, Group, Teacher, Campus, Audience, Lesson, Timetable, Time


class CampusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class TimetableAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_group', 'lesson', 'last_update', 'teacher')
    list_filter = ('group', 'group__department', 'lesson', 'teacher')

    def get_group(self, obj):
        return "{0} ({1})".format(obj.group.name, obj.group.department)

    get_group.admin_order_field = 'Група'
    get_group.short_description = 'Група'

    def last_update(self, obj):
        return datetime.datetime.fromtimestamp(
            int(obj.last_update)
        ).strftime('%Y-%m-%d %H:%M:%S')

    last_update.admin_order_field = 'Останнє оновлення'
    last_update.short_description = 'Останнє оновлення'


admin.site.register(Department)
admin.site.register(Group)
admin.site.register(Teacher)
admin.site.register(Time)
admin.site.register(Campus, CampusAdmin)
admin.site.register(Audience)
admin.site.register(Lesson)
admin.site.register(Timetable, TimetableAdmin)