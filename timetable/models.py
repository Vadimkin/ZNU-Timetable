# -*- coding: utf-8 -*-

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
    # departament = models.ForeignKey(Departament, verbose_name="Факультет")
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
        return u"{0}".format(self.audience)

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

    group = models.ForeignKey(Group, verbose_name="Група")
    lesson = models.ForeignKey(Lesson, verbose_name="Предмет")
    day = models.CharField(max_length=1, choices=DAYS_CHOICES, default=MONDAY_DAY, verbose_name="День")
    audience = models.ForeignKey(Audience, verbose_name="Аудиторія")
    periodicity = models.CharField(max_length=1, choices=PERIODICITY_CHOICES, default=ALWAYS_LESSON, verbose_name="Періодичність")
    date_start = models.DateField(verbose_name="Початок пар")
    date_end = models.DateField(verbose_name="Кінець пар")
    time_start = models.TimeField(verbose_name="Час початку пари")
    lesson_type = models.CharField(max_length=1, choices=LESSON_TYPES, default=NONE_TYPE, verbose_name="Тип предмету")

    def __unicode__(self):
        return u"{0}".format(self.lesson.name)

    class Meta:
        verbose_name = "розклад"
        verbose_name_plural = "розклади"