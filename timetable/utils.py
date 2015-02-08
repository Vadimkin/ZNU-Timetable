import datetime


def get_current_week(numerator=None, auto_week_change=False):
    if auto_week_change:
        strftime_param = "%W"
    else:
        strftime_param = "%U"

    current_week = ((int(datetime.datetime.today().strftime(strftime_param)) + 1) % 2) + 1 # If first week of year is numerator

    if numerator:
        weeks_order = [1, 2]

        if current_week == numerator:
            return weeks_order[0]
        else:
            return weeks_order[1]
    else:
        return current_week

first_day_of_week = datetime.date.today() - datetime.timedelta(days=datetime.date.today().weekday())