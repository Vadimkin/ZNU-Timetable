# -*- coding: utf-8 -*-
from django.db.models.signals import m2m_changed, pre_delete
from django.dispatch import receiver
from timetable.models import Timetable


@receiver(m2m_changed, sender=Timetable.group.through)
def create_profile(instance, action, **kwargs):
    """Update relations on creating new timetable."""
    if action == "post_add":
        for one_group in instance.group.all():
            one_group.save()

        instance.teacher.save(from_timetable=True)

@receiver(pre_delete, sender=Timetable)
def log_deleted_question(instance, **kwargs):
    """Update relations on deleting new timetable."""
    for one_group in instance.group.all():
        one_group.save()

    instance.teacher.save(from_timetable=True)