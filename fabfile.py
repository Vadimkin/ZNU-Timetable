import os
from fabric.api import *

import sys
sys.path.append(os.path.realpath(os.path.dirname(__file__)))

host = 'root@178.62.252.42'
env.hosts = [host]
env.user = "root"

def get_settings():
    from fabric.contrib import django
    django.settings_module('zno.settings')
    from django.conf import settings
    return settings

@task
def download_db_dump():
    tables = [
        "timetable_report",
        "timetable_audience",
        "timetable_campus",
        "timetable_department",
        "timetable_group",
        "timetable_lesson",
        "timetable_teacher",
        "timetable_time",
        "timetable_timetable",
        "timetable_timetable_group"
    ]

    run('mysqldump -u root znu {} > /tmp/znodump.sql'.format(" ".join(tables)))
    get('/tmp/znodump.sql', '/tmp/znodump.sql')
    run('rm /tmp/znodump.sql')
    with lcd('/tmp/'):
        local('mysql -u root znu < znodump.sql')
        local('rm znodump.sql')


@task
def upload_db_dump():
    tables = [
        "timetable_audience",
        "timetable_campus",
        "timetable_department",
        "timetable_group",
        "timetable_lesson",
        "timetable_teacher",
        "timetable_time",
        "timetable_timetable",
        "timetable_timetable_group"
    ]

    local('mysqldump -u root znu {} > /tmp/znodump.sql'.format(" ".join(tables)))
    put('/tmp/znodump.sql', '/tmp/znodump.sql')
    local('rm /tmp/znodump.sql')
    with cd('/tmp/'):
        run('mysql -u root znu < znodump.sql')
        run('rm znodump.sql')