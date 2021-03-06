# -*- coding: utf-8 -*-
import datetime
import time

from django.db import models
from django.db.models.signals import post_save, m2m_changed, pre_delete
from django.dispatch import receiver


class Department(models.Model):
    name = models.CharField(max_length=500, null=False, verbose_name="Факультет")
    last_update = models.IntegerField(default=int(time.time()))

    def __unicode__(self):
        return u"{0}".format(self.name)

    class Meta:
        verbose_name = "факультет"
        verbose_name_plural = "факультети"

    def save(self, from_group=False, *args, **kwargs):
        self.last_update = time.time()

        super(Department, self).save(*args, **kwargs)

        if not from_group:
            group = Group.objects.filter(departament_id=self.id)
            for one_group in group:
                one_group.save()


class Group(models.Model):
    COURSE_TYPES = (
        (1, '1 курс'),
        (2, '2 курс'),
        (3, '3 курс'),
        (4, '4 курс'),
        (5, '5 курс'),
    )

    department = models.ForeignKey(Department, verbose_name="Факультет")
    name = models.CharField(max_length=500, null=False, verbose_name="Номер групи")
    course = models.IntegerField(default=1, choices=COURSE_TYPES)
    last_update = models.IntegerField(default=int(time.time()))

    def __unicode__(self):
        return u"{0}".format(self.name)

    class Meta:
        verbose_name = "група"
        verbose_name_plural = "групи"
        ordering = ["department", "course"]

    def save(self, *args, **kwargs):
        self.last_update = time.time()
        self.department.save(from_group=True)

        super(Group, self).save(*args, **kwargs)


class Teacher(models.Model):
    name = models.TextField(verbose_name="Ім'я та прізвище викладача")
    last_update = models.IntegerField(default=int(time.time()))

    def __unicode__(self):
        return u"{0}".format(self.name)

    class Meta:
        verbose_name = "викладач"
        verbose_name_plural = "викладачі"
        ordering = ["name"]

    def save(self, from_timetable=False, *args, **kwargs):
        self.last_update = time.time()
        super(Teacher, self).save(*args, **kwargs)

        if not from_timetable:
            timetable = Timetable.objects.filter(teacher_id=self.id)
            for one_lesson in timetable:
                one_lesson.save(teacher_save=False)


class Campus(models.Model):
    name = models.TextField(blank=True, default='', verbose_name="Корпус")
    last_update = models.IntegerField(default=int(time.time()))
    longitude = models.FloatField(blank=True, null=True, verbose_name="Longitude")
    latitude = models.FloatField(blank=True, null=True, verbose_name="Latitude")

    def __unicode__(self):
        return u"{0}".format(self.name)

    class Meta:
        verbose_name = "корпус"
        verbose_name_plural = "корпуси"

    def save(self, *args, **kwargs):
        self.last_update = time.time()

        audience = Audience.objects.filter(campus_id=self.id)
        for one_audience in audience:
            one_audience.save()

        super(Campus, self).save(*args, **kwargs)


class Audience(models.Model):
    campus = models.ForeignKey(Campus, verbose_name="Корпус")
    audience = models.TextField(verbose_name="Аудиторія")
    last_update = models.IntegerField(default=int(time.time()))

    def __unicode__(self):
        return u"{0}, {1} аудиторія".format(self.campus.name, self.audience)

    class Meta:
        verbose_name = "аудиторія"
        verbose_name_plural = "аудиторії"
        ordering = ["campus", "audience"]

    def save(self, *args, **kwargs):
        self.last_update = time.time()
        super(Audience, self).save(*args, **kwargs)

        timetable = Timetable.objects.filter(audience_id=self.id)
        for one_lesson in timetable:
            one_lesson.save()


class Lesson(models.Model):
    name = models.CharField(max_length=500, null=False, verbose_name="Предмет")
    last_update = models.IntegerField(default=int(time.time()))

    def __unicode__(self):
        return u"{0}".format(self.name)

    class Meta:
        verbose_name = "предмет"
        verbose_name_plural = "предмети"
        ordering = ["name"]

    def save(self, *args, **kwargs):
        super(Lesson, self).save(*args, **kwargs)

        timetable = Timetable.objects.filter(lesson_id=self.id)
        for one_lesson in timetable:
            one_lesson.save()


class Time(models.Model):
    num = models.IntegerField(max_length=1)
    time_start = models.TimeField(verbose_name="Час початку пари")
    time_end = models.TimeField(verbose_name="Час кінця пари")

    def __unicode__(self):
        return u"{0} пара ({1}–{2})".format(self.num, self.time_start, self.time_end)

    def get_time_start_without_seconds(self):
        return self.time_start.strftime('%H:%M')

    def get_time_end_without_seconds(self):
        return self.time_end.strftime('%H:%M')

    class Meta:
        verbose_name = "час"
        verbose_name_plural = "години"


class Timetable(models.Model):
    MONDAY_DAY = 0
    TUESDAY_DAY = 1
    WEDNESDAY_DAY = 2
    THURSDAY_DAY = 3
    FRIDAY_DAY = 4
    SATURDAY_DAY = 5
    SUNDAY_DAY = 6
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
    CONSULTATION_TYPE = 4
    EXAM_TYPE = 5

    LESSON_TYPES = (
        (NONE_TYPE, 'Не задано'),
        (LECTURE_TYPE, 'Лекція'),
        (PRACTICE_TYPE, 'Семінар'),
        (LABORATORY_TYPE, 'Практика'),
        (CONSULTATION_TYPE, 'Консультація'),
        (EXAM_TYPE, 'Екзамен'),
    )

    SUBGROUP_TYPES = (
        (0, 'Загальна група'),
        (1, '1 підгрупа'),
        (2, '2 підгрупа'),
        (3, '3 підгрупа'),
    )

    teacher = models.ForeignKey(Teacher, verbose_name="Викладач")
    group = models.ManyToManyField(Group, verbose_name="Група")
    subgroup = models.IntegerField(max_length=1, choices=SUBGROUP_TYPES, default=0, verbose_name="Підгрупа")
    lesson = models.ForeignKey(Lesson, verbose_name="Предмет")
    day = models.IntegerField(max_length=1, choices=DAYS_CHOICES, default=MONDAY_DAY, verbose_name="День")
    audience = models.ForeignKey(Audience, verbose_name="Аудиторія")
    periodicity = models.IntegerField(max_length=1, choices=PERIODICITY_CHOICES, default=ALWAYS_LESSON,
                                      verbose_name="Періодичність")
    date_start = models.DateField(verbose_name="Початок пар", default=datetime.date(2015, 8, 1))
    date_end = models.DateField(verbose_name="Кінець пар", default=datetime.date(2015, 12, 29))
    period = models.ForeignKey(Time, verbose_name="Час пар", null=True)
    lesson_type = models.IntegerField(max_length=1, choices=LESSON_TYPES, default=NONE_TYPE,
                                      verbose_name="Тип предмету")
    free_trajectory = models.BooleanField(default=False, verbose_name="Вільна траекторія")
    last_update = models.IntegerField(default=int(time.time()))

    def __unicode__(self):
        return u"{0}".format(self.lesson.name)

    class Meta:
        verbose_name = "розклад"
        verbose_name_plural = "розклади"

    def save(self, teacher_save=True, *args, **kwargs):
        self.last_update = time.time()

        super(Timetable, self).save(*args, **kwargs)

        for one_group in self.group.all():
            one_group.save()

        if teacher_save:
            self.teacher.save(from_timetable=True)

    def get_readable_week_day(self):
        return self.DAYS_CHOICES[self.day][1]

    def get_week_type(self):
        week = (self.week % 2)

        if week == 0:
            week = 2
        else:
            week = 1

        return self.PERIODICITY_CHOICES[week][1]

    def get_readable_month_day(self, week=1):
        today = datetime.date.today()
        day = today - datetime.timedelta(days=today.weekday()) + datetime.timedelta(days=self.day + (week - 1) * 7)
        return day.strftime('%d %B')

    def is_active_day(self, week=1):
        today = datetime.date.today()
        day = today - datetime.timedelta(days=today.weekday()) + datetime.timedelta(days=self.day + (week - 1) * 7)
        return today == day


class Report(models.Model):
    group = models.ForeignKey(Group, verbose_name="Група")
    timetable = models.ForeignKey(Timetable, verbose_name="Розклад", null=True, blank=True)
    message = models.TextField(verbose_name="Текст помилки", blank=True, null=True)
    contacts = models.TextField(verbose_name="Контакти", blank=True, null=True)
    ip = models.IPAddressField(verbose_name="IP")
    fixed = models.BooleanField(verbose_name="Вирішено", default=False)
    last_update = models.IntegerField(verbose_name="Час останнього додавання", default=int(time.time()))

    def __unicode__(self):
        return u"{0}".format(self.message)

    class Meta:
        verbose_name = "баг-репорт"
        verbose_name_plural = "баг-репорти"