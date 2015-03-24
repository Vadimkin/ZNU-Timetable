# -*- coding: utf-8 -*-
# !/usr/bin/env python
import os
import sys
import django
sys.path.append(os.path.dirname(os.path.dirname(os. path.abspath(__file__))) + '/settings.py')
os.environ['DJANGO_SETTINGS_MODULE'] = 'znu.settings'

import xlrd
from timetable.models import Timetable

__author__ = 'vadim'

filename = 'example.xlsx'

rb = xlrd.open_workbook(os.path.dirname(os. path.abspath(__file__)) + '/data/' + filename,formatting_info=False)
sheet = rb.sheet_by_index(0)
for rownum in range(sheet.nrows):
    row = sheet.row_values(rownum)
    print(row)