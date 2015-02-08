import datetime
from django import template
from django.utils import dateformat
from timetable.utils import get_current_week
from znu import settings

register = template.Library()


@register.simple_tag
def readable_month_day(lesson):
    """Modify week on sunday. At site if current day = sunday then showing timetable from new week """
    week = lesson.week + 2 if lesson.week == get_current_week() and datetime.datetime.today().weekday() == 6 else lesson.week

    today = datetime.date.today()
    day = today - datetime.timedelta(days=today.weekday()) + datetime.timedelta(days=lesson.day + (week - 1) * 7)
    return dateformat.format(day, settings.DATE_FORMAT)