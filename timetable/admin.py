# -*- coding: utf-8 -*-
from datetime import datetime
from django import forms

from django.contrib import admin
from timetable.models import Department, Group, Teacher, Campus, Audience, Lesson, Timetable, Time


class CampusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_last_update')
    exclude = ('last_update',)

    def get_last_update(self, obj):
        return datetime.fromtimestamp(
            int(obj.last_update)
        ).strftime('%Y-%m-%d %H:%M:%S')

    get_last_update.admin_order_field = 'Останнє оновлення'
    get_last_update.short_description = 'Останнє оновлення'


class TimetableAdmin(admin.ModelAdmin):
    fields = (('group', 'subgroup', 'free_trajectory'), 'day', 'period', 'lesson', 'teacher', 'audience', 'periodicity',
              'lesson_type',
              ('date_start', 'date_end'))
    list_display = (
        'id', 'get_group', 'get_colored_day', 'lesson', 'teacher', 'subgroup', 'period', 'periodicity',
        'get_last_update')
    list_filter = ('group', 'lesson', 'teacher', 'day')
    exclude = ('last_update',)

    def get_colored_day(self, instance):
        colors = ("#673AB7", "#9C27B0", "#1976D2", "#0277BD", "#009688", "#795548", "#263238")
        return "<span style='color: {0}; font-weight: bold;'>{1}</span>".format(colors[instance.day],
                                                                                instance.DAYS_CHOICES[instance.day][1])

    get_colored_day.allow_tags = True
    get_colored_day.short_description = 'День тижня'

    def get_form(self, request, obj=None, **kwargs):
        form = super(TimetableAdmin, self).get_form(request, obj, **kwargs)

        previous_data = Timetable.objects.order_by('-pk')[0]

        groups_list = []
        for one_group in previous_data.group.all():
            groups_list.append(one_group.id)

        form.base_fields['group'].initial = groups_list
        form.base_fields['day'].initial = previous_data.day
        form.base_fields['period'].initial = previous_data.period

        return form

    def get_group(self, obj):
        result = ""
        for one_group in obj.group.all():
            result += "{0} ({1})<br>".format(one_group.name, one_group.department)
        return result

    get_group.allow_tags = True
    get_group.admin_order_field = 'Група'
    get_group.short_description = 'Група'

    def get_last_update(self, obj):
        return datetime.fromtimestamp(
            int(obj.last_update)
        ).strftime('%Y-%m-%d %H:%M:%S')

    get_last_update.admin_order_field = 'Останнє оновлення'
    get_last_update.short_description = 'Останнє оновлення'


class LessonForm(forms.ModelForm):
    name = forms.CharField(required=True)

    class Meta:
        model = Lesson
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if Lesson.objects.filter(name=name).exists():
            raise forms.ValidationError("Цей предмет вже додано")
        return name


class LessonAdmin(admin.ModelAdmin):
    form = LessonForm
    list_display = ('id', 'name', 'get_last_update')
    exclude = ('last_update',)

    def get_last_update(self, obj):
        return datetime.fromtimestamp(
            int(obj.last_update)
        ).strftime('%Y-%m-%d %H:%M:%S')

    get_last_update.admin_order_field = 'Останнє оновлення'
    get_last_update.short_description = 'Останнє оновлення'


class TeacherForm(forms.ModelForm):
    name = forms.CharField(required=True)

    class Meta:
        model = Teacher
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if self.instance:
            if Teacher.objects.filter(name=name).exists():
                raise forms.ValidationError("Цей викладач вже є")
        return name


class TeacherAdmin(admin.ModelAdmin):
    form = TeacherForm
    list_display = ('id', 'name', 'get_last_update')
    exclude = ('last_update',)

    def get_last_update(self, obj):
        return datetime.fromtimestamp(
            int(obj.last_update)
        ).strftime('%Y-%m-%d %H:%M:%S')

    get_last_update.admin_order_field = 'Останнє оновлення'
    get_last_update.short_description = 'Останнє оновлення'


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course', 'department', 'get_last_update')
    exclude = ('last_update',)
    ordering = ('course', )

    def get_last_update(self, obj):
        return datetime.fromtimestamp(
            int(obj.last_update)
        ).strftime('%Y-%m-%d %H:%M:%S')

    get_last_update.admin_order_field = 'Останнє оновлення'
    get_last_update.short_description = 'Останнє оновлення'


admin.site.register(Department)
admin.site.register(Group, GroupAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Time)
admin.site.register(Campus, CampusAdmin)
admin.site.register(Audience)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Timetable, TimetableAdmin)