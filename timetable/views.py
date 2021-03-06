# -*- coding: utf-8 -*-
from itertools import chain
import json
import urllib
import datetime
import time
from django import http

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist
from django.views import generic
from timetable.models import Teacher, Timetable, Group, Lesson, Report
from timetable.utils import get_current_week, first_day_of_week


class IndexListView(generic.ListView):
    model = Group
    template_name = 'timetable/group_list.html'

    def dispatch(self, request, *args, **kwargs):
        response = super(IndexListView, self).dispatch(request, **kwargs)
        group_info = request.COOKIES.get('groupInfo')
        if group_info:
            group_id = json.loads(urllib.unquote(group_info))['group_id']
            if Group.objects.filter(id=group_id).exists():
                return HttpResponseRedirect(reverse('group_detail', args=[group_id]))
        return response


class LandingTemplateView(generic.TemplateView):
    template_name = 'timetable/landing.html'


class MapView(generic.TemplateView):
    template_name = 'timetable/map.html'


class TeacherListView(generic.ListView):
    model = Teacher

    def get_queryset(self):
        teachers = super(TeacherListView, self).get_queryset().order_by('name')
        for teacher in teachers:
            teacher.first_letter = teacher.name[0:1]
        return teachers


class TeacherDetailView(generic.DetailView):
    model = Teacher
    slug_field = 'id'
    slug_url_kwarg = 'teacher_id'

    def __init__(self, **kwargs):
        super(TeacherDetailView, self).__init__(**kwargs)
        self.kwargs = None

    def get_teacher_timetable(self, current_week, list_append=None):
        current_week_day = 0
        if current_week == get_current_week():
            current_week_day = datetime.date.today().weekday()

        timetable = Timetable.objects.filter(teacher_id=self.kwargs['teacher_id'],
                                             periodicity__in=[0, current_week],
                                             # date_start__lte=first_day_of_week,
                                             # date_end__gte=first_day_of_week,
                                             day__gte=current_week_day, ).order_by('day', 'period', 'subgroup')

        timetable_with_offset = Timetable.objects.filter(teacher_id=self.kwargs['teacher_id'],
                                                         periodicity__in=[0, current_week],
                                                         # date_start__lte=first_day_of_week,
                                                         # date_end__gte=first_day_of_week,
                                                         day__lt=current_week_day, ).order_by('day', 'period',
                                                                                              'subgroup')

        for one_lesson in timetable:
            one_lesson.week = current_week

            if one_lesson.teacher and one_lesson.teacher.name == u"—":
                one_lesson.teacher_id = 50

            if one_lesson.audience is not None and one_lesson.audience.audience == u"—":
                one_lesson.audience_id = 40

        for one_lesson in timetable_with_offset:
            one_lesson.week = current_week + 2

            if one_lesson.teacher and one_lesson.teacher.name == u"—":
                one_lesson.teacher_id = 50

            if one_lesson.audience is not None and one_lesson.audience.audience == u"—":
                one_lesson.audience_id = 40

            if list_append is not None:
                list_append.append(one_lesson)

        return timetable

    def get_context_data(self, **kwargs):
        context = super(TeacherDetailView, self).get_context_data(**kwargs)

        timetable_last = []

        timetable_first = self.get_teacher_timetable(get_current_week(1), list_append=timetable_last)
        timetable_second = self.get_teacher_timetable(get_current_week(2), list_append=timetable_last)

        context['timetable'] = list(chain(timetable_first, timetable_second, timetable_last))
        return context


class GroupListView(generic.ListView):
    model = Group


class GroupDetailView(generic.DetailView):
    model = Group
    slug_field = 'id'
    slug_url_kwarg = 'group_id'

    def __init__(self, **kwargs):
        super(GroupDetailView, self).__init__(**kwargs)
        self.kwargs = None

    def get_group_timetable(self, current_week, list_append=None):
        current_week_day = 0
        if current_week == get_current_week():
            current_week_day = datetime.date.today().weekday()

        timetable = Timetable.objects.filter(group=self.kwargs['group_id'],
                                             periodicity__in=[0, current_week],
                                             # date_start__lte=first_day_of_week,
                                             # date_end__gte=first_day_of_week,
                                             day__gte=current_week_day, ).order_by('day', 'period', 'subgroup')

        timetable_with_offset = Timetable.objects.filter(group=self.kwargs['group_id'],
                                                         periodicity__in=[0, current_week],
                                                         # date_start__lte=first_day_of_week,
                                                         # date_end__gte=first_day_of_week,
                                                         day__lt=current_week_day, ).order_by('day', 'period',
                                                                                              'subgroup')

        for one_lesson in timetable_with_offset:
            one_lesson.week = current_week + 2

            if one_lesson.teacher and one_lesson.teacher.name == u"—":
                one_lesson.teacher_id = 50

            if one_lesson.audience is not None and one_lesson.audience.audience == u"—":
                one_lesson.audience_id = 40

            if list_append is not None:
                list_append.append(one_lesson)

        for one_lesson in timetable:
            one_lesson.week = current_week

            if one_lesson.teacher and one_lesson.teacher.name == u"—":
                one_lesson.teacher_id = 50

            if one_lesson.audience is not None and one_lesson.audience.audience == u"—":
                one_lesson.audience_id = 40

        return timetable

    def get_context_data(self, **kwargs):
        context = super(GroupDetailView, self).get_context_data(**kwargs)

        timetable_last = []

        timetable_first = self.get_group_timetable(get_current_week(1), list_append=timetable_last)
        timetable_second = self.get_group_timetable(get_current_week(2), list_append=timetable_last)

        context['timetable'] = list(chain(timetable_first, timetable_second, timetable_last))
        return context


class APIView(generic.TemplateView):
    template_name = 'timetable/api.html'


class MobileApplicationView(generic.TemplateView):
    template_name = 'timetable/mobile_applications.html'

class AddTimetableView(generic.TemplateView):
    template_name = 'timetable/add_timetable.html'

class ReportView(generic.View):
    def post(self, request):
        result = {}

        try:
            group = request.POST['group_id']
        except MultiValueDictKeyError:
            result['status'] = 0
            result['text'] = 'Не змінюйте параметри :-)'

            return http.HttpResponse(json.dumps(result),
                                     content_type='application/json')

        try:
            timetable = int(request.POST['timetable_id'])
        except (MultiValueDictKeyError, ValueError):
            timetable = None

        try:
            message = request.POST['message']
        except MultiValueDictKeyError:
            message = ""

        try:
            contact = request.POST['contact']
        except MultiValueDictKeyError:
            contact = ""

        try:
            report_group = Group.objects.filter(id=group).get()
            if timetable is not None:
                report_timetable = Timetable.objects.filter(id=timetable).get()
            else:
                report_timetable = None
        except ObjectDoesNotExist:
            result['status'] = 0
            result['text'] = 'Не змінюйте параметри :-)'

            return http.HttpResponse(json.dumps(result),
                                     content_type='application/json')

        user_ip = request.META.get('HTTP_X_REAL_IP')
        if user_ip is None:
            user_ip = '127.0.0.1'

        report = Report(group=report_group, timetable=report_timetable, message=message, contacts=contact, ip=user_ip,
                        last_update=int(time.time()))
        report.save()

        result['status'] = 1

        return http.HttpResponse(json.dumps(result),
                                 content_type='application/json')