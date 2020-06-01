# -*- coding: utf-8 -*-

import time
import datetime

from django.utils import timezone
from datetime import timedelta, datetime, date
from apps.agendas.models import Appointment


class DoctorProfileService(object):

    @classmethod
    def week_days(cls, year, week_number):
        days = []
        str_datetime = '{0} {1} 1'.format(year, week_number - 1)
        startdate = time.asctime(time.strptime(str_datetime, '%Y %W %w'))
        first_date = datetime.strptime(startdate, '%a %b %d %H:%M:%S %Y')

        for i in range(7):
            day = first_date + timedelta(days=i)
            days.append({
                'date':  day.strftime('%Y-%m-%d'),
                'label':  day.strftime('%d %b %Y'),
                'day':  day.strftime('%a'),
            })
        return days

    @classmethod
    def get_week_number(cls, date_instance, time_instance):
        calculated_datetime = datetime.combine(date_instance, time_instance)
        year, week_number, day = calculated_datetime.isocalendar()
        return week_number

    @classmethod
    def get_week(cls, year=None, week=None):
        now = timezone.now()
        _year, _week, day = now.isocalendar()

        calculated_week = week or _week
        calculated_year = year or _year

        return {
            'year': calculated_year,
            'week_number': calculated_week,
        }

    @classmethod
    def get_appointments(cls, doctor):
        appointments = Appointment.objects.filter(doctor=doctor).order_by('date', 'time')
        reservations = {}

        for appointment in appointments:
            _date = appointment.date.strftime('%Y-%m-%d')
            _time = appointment.time.strftime('%H:%M')

            if _date not in reservations.keys():
                reservations[_date] = []

            reservations[_date].append(_time)
        return reservations

    @classmethod
    def week_calendar(cls, doctor, year=None, week=None):

        week_days = cls.week_days(**cls.get_week(year, week))
        start_time = doctor.start_time
        end_time = doctor.end_time
        duration = doctor.consultation_duration

        reservations = cls.get_appointments(doctor)

        new_week_days = []
        for day in week_days:
            hours = []
            incremental_time = start_time

            while incremental_time < end_time:
                initial_hour = incremental_time.strftime('%H:%M')
                unavailable = day['date'] in reservations.keys() and initial_hour in reservations[day['date']]
                tmp_incremental_time = datetime.combine(date(1, 1, 1), incremental_time)
                tmp_duration = timedelta(minutes=duration)
                incremental_time = (tmp_incremental_time + tmp_duration).time()

                hours.append({
                    'time': initial_hour,
                    'available': not unavailable,
                })
            new_week_days.append({**day, 'hours': hours})

        return new_week_days

