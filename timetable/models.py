# -*- coding: utf-8 -*-
import datetime

from django.db import models


class Departament(models.Model):
    name = models.CharField(max_length=500, null=False, verbose_name="Факультет")

    def __unicode__(self):
        return u"{0}".format(self.name)

    class Meta:
        verbose_name = "факультет"
        verbose_name_plural = "факультети"


class Group(models.Model):
    departament = models.ForeignKey(Departament, verbose_name="Факультет")
    name = models.CharField(max_length=500, null=False, verbose_name="Номер групи")

    def __unicode__(self):
        return u"{0}".format(self.name)

    class Meta:
        verbose_name = "група"
        verbose_name_plural = "групи"


class Teacher(models.Model):
    name = models.TextField(verbose_name="Ім'я та прізвище викладача")

    def __unicode__(self):
        return u"{0}".format(self.name)

    class Meta:
        verbose_name = "викладач"
        verbose_name_plural = "викладачі"


class Campus(models.Model):
    name = models.TextField(blank=True, default='', verbose_name="Корпус")

    def __unicode__(self):
        return u"{0}".format(self.name)

    class Meta:
        verbose_name = "корпус"
        verbose_name_plural = "корпуси"


class Audience(models.Model):
    campus = models.ForeignKey(Campus, verbose_name="Корпус")
    audience = models.TextField(verbose_name="Аудиторія")

    def __unicode__(self):
        return u"{0}, {1} аудиторія".format(self.campus.name, self.audience)

    class Meta:
        verbose_name = "аудиторія"
        verbose_name_plural = "аудиторії"


class Lesson(models.Model):
    name = models.CharField(max_length=500, null=False, verbose_name="Предмет")

    def __unicode__(self):
        return u"{0}".format(self.name)

    class Meta:
        verbose_name = "предмет"
        verbose_name_plural = "предмети"


class Timetable(models.Model):
    MONDAY_DAY = 1
    TUESDAY_DAY = 2
    WEDNESDAY_DAY = 3
    THURSDAY_DAY = 4
    FRIDAY_DAY = 5
    SATURDAY_DAY = 6
    SUNDAY_DAY = 7
    DAYS_CHOICES = (
        (MONDAY_DAY, 'Понеділок'),
        (TUESDAY_DAY, 'Вівторок'),
        (WEDNESDAY_DAY, 'Середа'),
        (THURSDAY_DAY, 'Четвер'),
        (FRIDAY_DAY, 'П\'ятниця'),
        (SATURDAY_DAY, 'Субота'),
        (SUNDAY_DAY, 'Неділя'),
    )

    ALWAYS_LESSON = 0
    NUMENATOR_LESSON = 1
    DENUMERATOR_LESSON = 2
    PERIODICITY_CHOICES = (
        (ALWAYS_LESSON, 'Завжди'),
        (NUMENATOR_LESSON, 'Чисельник'),
        (DENUMERATOR_LESSON, 'Знаменник')
    )

    NONE_TYPE = 0
    LECTURE_TYPE = 1
    PRACTICE_TYPE = 2
    LABORATORY_TYPE = 3

    LESSON_TYPES = (
        (NONE_TYPE, 'Не задано'),
        (LECTURE_TYPE, 'Лекція'),
        (PRACTICE_TYPE, 'Практика'),
        (LABORATORY_TYPE, 'Лабораторна')
    )

    TIME_TYPES = (
        (datetime.time(hour=8, minute=0, second=0, microsecond=0, tzinfo=None), "08:00 — 1 пара"),
        (datetime.time(hour=9, minute=35, second=0, microsecond=0, tzinfo=None), "09:35 — 2 пара"),
        (datetime.time(hour=11, minute=25, second=0, microsecond=0, tzinfo=None), "11:25 — 3 пара"),
        (datetime.time(hour=12, minute=55, second=0, microsecond=0, tzinfo=None), "12:55 — 4 пара"),
        (datetime.time(hour=14, minute=30, second=0, microsecond=0, tzinfo=None), "14:30 — 5 пара"),
        (datetime.time(hour=16, minute=05, second=0, microsecond=0, tzinfo=None), "16:05 — 6 пара"),
        (datetime.time(hour=17, minute=40, second=0, microsecond=0, tzinfo=None), "17:40 — 7 пара"),
        (datetime.time(hour=19, minute=10, second=0, microsecond=0, tzinfo=None), "19:10 — 8 пара"),
    )

    teacher = models.ForeignKey(Teacher, verbose_name="Викладач", null=True)
    group = models.ForeignKey(Group, verbose_name="Група")
    lesson = models.ForeignKey(Lesson, verbose_name="Предмет")
    day = models.IntegerField(max_length=1, choices=DAYS_CHOICES, default=MONDAY_DAY, verbose_name="День")
    audience = models.ForeignKey(Audience, verbose_name="Аудиторія")
    periodicity = models.IntegerField(max_length=1, choices=PERIODICITY_CHOICES, default=ALWAYS_LESSON, verbose_name="Періодичність")
    date_start = models.DateField(verbose_name="Початок пар")
    date_end = models.DateField(verbose_name="Кінець пар")
    time_start = models.TimeField(verbose_name="Час початку пари", choices=TIME_TYPES)
    lesson_type = models.IntegerField(max_length=1, choices=LESSON_TYPES, default=NONE_TYPE, verbose_name="Тип предмету")

    def __unicode__(self):
        return u"{0}".format(self.lesson.name)

    class Meta:
        verbose_name = "розклад"
        verbose_name_plural = "розклади"