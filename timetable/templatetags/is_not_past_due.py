import datetime

from django import template


register = template.Library()

@register.filter
def is_not_past_due(lesson):
    today = datetime.date.today()
    day = today - datetime.timedelta(days=today.weekday()) + datetime.timedelta(days=lesson.day + (lesson.week-1)*7)
    if lesson.date_end > day:
        return True
    else:
        return False