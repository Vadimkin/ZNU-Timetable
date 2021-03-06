# -*- coding: utf-8 -*-
from datetime import datetime
from django import forms

from django.contrib import admin
from timetable.models import Department, Group, Teacher, Campus, Audience, Lesson, Timetable, Time, Report


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

    def get_group(self, obj):
        result = ""
        for one_group in obj.group.all():
            result += u"{0} ({1})<br>".format(one_group.name, one_group.department)
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


class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'fixed', 'message', 'contacts', 'timetable', 'get_group_link', 'edit_link')

    def get_group_link(self, obj):
        return u'<a href="/groups/{0}">{1}</a>'.format(obj.group.id, obj.group.name)
    get_group_link.allow_tags = True

    def edit_link(self, obj):
        try:
            return u'<a href="/admin/timetable/timetable/{0}">{1}</a>'.format(obj.timetable.id, 'edit')
        except AttributeError:
            return u'<a href="/admin/timetable/group/{0}">{1}</a>'.format(obj.group.id, 'edit')

    edit_link.allow_tags = True


admin.site.register(Department)
admin.site.register(Group, GroupAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Time)
admin.site.register(Campus, CampusAdmin)
admin.site.register(Audience)
admin.site.register(Report, ReportAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Timetable, TimetableAdmin)