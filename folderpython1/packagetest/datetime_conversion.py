#!/usr/bin/python3
# -*- coding: utf-8 -*-
from datetime import datetime, date, timedelta

import matplotlib.pyplot as plt
from matplotlib import markers

plt.style.use('seaborn')


def describe_now(variable):
    typeof = type(variable)
    print("la variable=", variable, "est de type", typeof)


def get_datetime_list(list_string):
    datetime_list = []
    format = "%Y-%m-%dT%H:%M:%S.%f%z"

    for i in list_string:
        datetime_obj = datetime.strptime(i, format)
        datetime_list.append(datetime_obj)
    return datetime_list


def main():
    time2 = "%Y-%m-%d %H:%M:%S %Z%z"
    time3 = "2022-08-18T11:36:56.490856+02:00"
    time4 = "2022-08-18T15:46:56.490856+02:00"
    time5 = "2022-08-18T17:46:58.490840+02:00"
    times_string = [time3, time4, time5]

    value1 = date.fromisoformat('2019-12-04')
    print("le type est ", type(value1), value1);
    format = "%Y-%m-%dT%H:%M:%S.%f%z"
    datetime_obj1 = datetime.strptime(time3, format)
    describe_now(time3)
    describe_now(datetime_obj1)

    bytes_a = [456, 350, 415]
    date_real_list = get_datetime_list(times_string)

    a=plt.plot_date(date_real_list, bytes_a,'P',None,True,False)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
