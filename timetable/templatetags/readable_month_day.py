import datetime
from django import template
from django.utils import dateformat
from znu import settings

register = template.Library()

@register.simple_tag
def readable_month_day(lesson):
    today = datetime.date.today()
    day = today - datetime.timedelta(days=today.weekday()) + datetime.timedelta(days=lesson.day + (lesson.week-1)*7)
    return dateformat.format(day, settings.DATE_FORMAT)