from datetime import datetime


def get_current_week(numerator=None):
    current_week = (int(datetime.today().strftime("%U")) % 2) + 1  # If first week of year is numerator
    if numerator:
        weeks_order = [1, 2]
        if current_week == numerator:
            return weeks_order[0]
        else:
            return weeks_order[::-1][0]
    else:
        return current_week