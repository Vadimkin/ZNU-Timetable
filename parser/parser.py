# -*- coding: utf-8 -*-
# !/usr/bin/env python
import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/settings.py')
os.environ['DJANGO_SETTINGS_MODULE'] = 'znu.settings'
django.setup()

import xlrd
from timetable.models import Timetable, Group, Lesson, Audience, Teacher

__author__ = 'vadim'

filename = '8.35914.xls'

week_days = {
    u"Понеділок": 0,
    u"Вівторок": 1,
    u"Середа": 2,
    u"Четвер": 3,
    u"П'ятниця": 4,
    u"Субота": 5
}

numerator = {
    u"чисельник": 1,
    u"знаменник": 2
}

lesson_type = {
    u"лекція": 1,
    u"семінар": 2,
    u"лабораторна": 3,
    u"практика": 3
}

rb = xlrd.open_workbook(os.path.dirname(os.path.abspath(__file__)) + '/data/' + filename, formatting_info=False)
sheet = rb.sheet_by_index(0)

main_info = {}
main_info['faculty'] = sheet.row_values(1)[0]
main_info['group'] = sheet.row_values(1)[1]
main_info['course'] = int(sheet.row_values(1)[2])

main_info['faculty'] = 2

# if group not found, then create it
group, created = Group.objects.get_or_create(department_id=main_info['faculty'], name=main_info['group'],
                                             course=main_info['course'])
main_info['group_id'] = group.id

for rownum in range(3, sheet.nrows):
    row = sheet.row_values(rownum)

    lesson = {}
    print(row[0].strip())
    lesson['week_day'] = week_days[row[0].strip()]
    lesson['time'] = int(row[1])
    lesson['periodicity'] = 0 if row[2] == "" else numerator[row[2].lower()]
    lesson['type'] = 0 if row[3] == "" else lesson_type[row[3].lower()]
    lesson['name'] = row[4]
    lesson['teacher'] = u"—" if row[5] == "" else row[5]
    lesson['audience'] = u"—" if row[6] == "" else row[6]
    lesson['campus'] = 9 if row[7] == "" else int(row[7])
    lesson['subgroup'] = 0 if row[8] == "" else int(row[8])
    lesson['free_trajectory'] = 0 if row[9] == "" else int(row[9])

    lesson_object, created = Lesson.objects.get_or_create(name=lesson['name'])
    lesson['name_id'] = lesson_object.id

    audience_object, created = Audience.objects.get_or_create(campus_id=lesson['campus'], audience=lesson['audience'])
    lesson['audience_id'] = audience_object.id

    teacher_object, created = Teacher.objects.get_or_create(name=lesson['teacher'])
    lesson['teacher_id'] = teacher_object.id

    timetable, created = Timetable.objects.get_or_create(lesson_id=lesson['name_id'], day=lesson['week_day'],
                                                         audience_id=lesson['audience_id'],
                                                         periodicity=lesson['periodicity'], lesson_type=lesson['type'],
                                                         teacher_id=lesson['teacher_id'], period_id=lesson['time'],
                                                         subgroup=lesson['subgroup'],
                                                         free_trajectory=lesson['free_trajectory'])

    timetable.group.add(main_info['group_id'])