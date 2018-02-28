# https://www.codewars.com/kata/525f277c7103571f47000147
from dateutil import parser


def get_start_time(schedules, duration):
    schedule_dict = [
        (parser.parse('9:00'), 0),
        (parser.parse('19:00'), 1)
    ]
    for schedule in schedules:
        for interval in schedule:
            schedule_dict.append((parser.parse(interval[0]), 1))
            schedule_dict.append((parser.parse(interval[1]), -1))

    sum = 0
    start = None
    for k, v in sorted(schedule_dict, key=lambda x: x[0]):
        if start is not None:
            if (k - start).seconds / 60 >= duration:
                return start.strftime('%H:%M')
            else:
                start = None

        sum += v
        if sum == 0:
            start = k

    return None