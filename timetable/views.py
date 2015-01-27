# -*- coding: utf-8 -*-
from itertools import chain
import json
import urllib

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views import generic
from timetable.models import Teacher, Timetable, Group
from timetable.utils import get_current_week


class IndexListView(generic.ListView):
    model = Group
    template_name = 'timetable/group_list.html'

    def dispatch(self, request, *args, **kwargs):
        response = super(IndexListView, self).dispatch(request, **kwargs)
        group_info = request.COOKIES.get('groupInfo')
        if group_info:
            group_id = json.loads(urllib.unquote(group_info))['group_id']
            return HttpResponseRedirect(reverse('group_detail', args=[group_id]))
        return response


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

    def get_context_data(self, **kwargs):
        context = super(TeacherDetailView, self).get_context_data(**kwargs)
        timetable_first = Timetable.objects.filter(teacher_id=self.kwargs['teacher_id'],
                                                   periodicity__in=[0, get_current_week(1)]).order_by('day', 'period', )
        for one_lesson in timetable_first:
            one_lesson.week = get_current_week(1)
        timetable_second = Timetable.objects.filter(teacher_id=self.kwargs['teacher_id'],
                                                    periodicity__in=[0, get_current_week(2)]).order_by('day',
                                                                                                       'period', )
        for one_lesson in timetable_second:
            one_lesson.week = get_current_week(2)
        context['timetable'] = list(chain(timetable_first, timetable_second))
        return context


class GroupListView(generic.ListView):
    model = Group


class GroupDetailView(generic.DetailView):
    model = Group
    slug_field = 'id'
    slug_url_kwarg = 'group_id'

    def get_context_data(self, **kwargs):
        context = super(GroupDetailView, self).get_context_data(**kwargs)
        timetable_first = Timetable.objects.filter(group_id=self.kwargs['group_id'],
                                                   periodicity__in=[0, get_current_week(1)]).order_by('day', 'period', )
        for one_lesson in timetable_first:
            one_lesson.week = get_current_week(1)
        timetable_second = Timetable.objects.filter(group_id=self.kwargs['group_id'],
                                                    periodicity__in=[0, get_current_week(2)]).order_by('day',
                                                                                                       'period', )
        for one_lesson in timetable_second:
            one_lesson.week = get_current_week(2)
        context['timetable'] = list(chain(timetable_first, timetable_second))
        return context


class APIView(generic.TemplateView):
    template_name = 'timetable/api.html'