# -*- coding: utf-8 -*-
import datetime
from datetime import date


def get_header_date(my_week: int, my_day: int, my_format: int):
    """
    Created on Fri Nov  8 15:22:21 2019
    A function to return a publication date, based on a business rule of the
    form: the Nth <day_name> of the month, e.g. the 2nd Thursday of the month.

    Parameters
    ----------
    my_week: int This is the week of the month in which publication takes place
    my_day: int  This is the day of the week on which publication takes place
                            0 = Monday
                            1 = Tuesday
                            2 = Wednesday
                            3 = Thursday
                            4 = Friday
                            5 = Saturday
                            6 = Sunday
    my_format: int  This is a parameter which controls the format of the
    returned date

    Returns
    -------
    pub_date: date

    Example
    -------
    get_header_date(2, 3, None)
    14 November 2019

    @author: WITH2
    """
    # Check the input parameters
    if my_week > 5 or my_week < 1:
        return None
    if my_day > 6 or my_day < 0:
        return None
    # Evaluate the lower and upper dates to be checked, given the week
    date1 = (my_week - 1)*7 + 1
    date2 = my_week*7 + 1
    if date2 > 31:
        date2 = 31

    # Read the system date and extract the year and month
    py_sys_date = date.today()
    year = py_sys_date.year
    calc_month = py_sys_date.month

    # Find the required date
    while calc_month < 13:
        calc_day = date1
        while calc_day < date2:
            test_date = datetime.date(year, calc_month, calc_day)
            if test_date.weekday() == my_day:
                if test_date > py_sys_date:
                    pub_date = test_date
                    calc_month = 13
                    calc_day = date2
                    break
                break
            calc_day += 1
        calc_month += 1

    if my_format is None:
        # Like 14 November 2019
        pub_date = pub_date.strftime('%d %B %Y')
        return pub_date
    if my_format == 1:
        # Like 2019-11-14
        pub_date = pub_date.strftime('%Y-%m-%d')
        return pub_date
    else:
        return None
