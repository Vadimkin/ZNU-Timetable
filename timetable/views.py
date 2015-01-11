# -*- coding: utf-8 -*-
from itertools import chain
from django.http import request

from django.shortcuts import render, get_object_or_404
from django.views import generic
from timetable.models import Teacher, Timetable
from timetable.utils import get_current_week


class IndexView(generic.TemplateView):
    template_name = 'timetable/index.html'


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
        timetable_first = Timetable.objects.filter(teacher_id=self.kwargs['teacher_id'], periodicity__in=[0, get_current_week(1)])
        for one_lesson in timetable_first:
            one_lesson.week = get_current_week(1)
        timetable_second = Timetable.objects.filter(teacher_id=self.kwargs['teacher_id'], periodicity__in=[0, get_current_week(2)])
        for one_lesson in timetable_second:
            one_lesson.week = get_current_week(2)
        context['timetable'] = list(chain(timetable_first, timetable_second))
        return context