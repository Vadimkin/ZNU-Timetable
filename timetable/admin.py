# -*- coding: utf-8 -*-
from datetime import datetime
from django import forms

from django.contrib import admin
from timetable.models import Department, Group, Teacher, Campus, Audience, Lesson, Timetable, Time


class CampusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    exclude = ('last_update',)


class TimetableAdmin(admin.ModelAdmin):
    fields = (('group', 'subgroup'), 'day', 'period', 'lesson', 'teacher', 'audience', 'periodicity', 'lesson_type',
              ('date_start', 'date_end'))
    list_display = ('id', 'get_group', 'lesson', 'last_update', 'teacher')
    list_filter = ('group', 'group__department', 'lesson', 'teacher')
    exclude = ('last_update',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(TimetableAdmin, self).get_form(request, obj, **kwargs)

        previous_data = Timetable.objects.order_by('-pk')[0]
        form.base_fields['group'].initial = previous_data.group
        form.base_fields['day'].initial = previous_data.day
        form.base_fields['period'].initial = previous_data.period

        return form

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


class LessonForm(forms.ModelForm):
    name = forms.CharField(required=False)

    class Meta:
        model = Lesson

    def clean_name(self):
        name = self.cleaned_data['name']
        if Lesson.objects.filter(name=name).exists():
            raise forms.ValidationError("This email already used")
        return name


class LessonAdmin(admin.ModelAdmin):
    form = LessonForm


admin.site.register(Department)
admin.site.register(Group)
admin.site.register(Teacher)
admin.site.register(Time)
admin.site.register(Campus, CampusAdmin)
admin.site.register(Audience)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Timetable, TimetableAdmin)