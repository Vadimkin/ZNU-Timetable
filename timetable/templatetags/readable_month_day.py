import datetime
from django import template
from django.utils import dateformat
from timetable.utils import get_current_week
from znu import settings

register = template.Library()


@register.simple_tag
def readable_month_day(lesson):
    week = get_current_week(lesson.week)

    today = datetime.date.today()
    day = today - datetime.timedelta(days=today.weekday()) + datetime.timedelta(days=lesson.day + (week - 1) * 7)
    return dateformat.format(day, settings.DATE_FORMAT)