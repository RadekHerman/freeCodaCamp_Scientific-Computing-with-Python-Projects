""" https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator
Write a function named add_time that takes in two required parameters and one optional parameter:

a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.
"""


def add_time(start_time, duration_time, week_day=None):
    clock_24 = {
        "12 AM": "00",
        "1 AM": "1",
        "2 AM": "2",
        "3 AM": "3",
        "4 AM": "4",
        "5 AM": "5",
        "6 AM": "6",
        "7 AM": "7",
        "8 AM": "8",
        "9 AM": "9",
        "10 AM": "10",
        "11 AM": "11",
        "12 PM": "12",
        "1 PM": "13",
        "2 PM": "14",
        "3 PM": "15",
        "4 PM": "16",
        "5 PM": "17",
        "6 PM": "18",
        "7 PM": "19",
        "8 PM": "20",
        "9 PM": "21",
        "10 PM": "22",
        "11 PM": "23",
        "12 AM": "00",
    }

    clock_12 = {
        "0": "12 AM",
        "1": "1 AM",
        "2": "2 AM",
        "3": "3 AM",
        "4": "4 AM",
        "5": "5 AM",
        "6": "6 AM",
        "7": "7 AM",
        "8": "8 AM",
        "9": "9 AM",
        "10": "10 AM",
        "11": "11 AM",
        "12": "12 PM",
        "13": "1 PM",
        "14": "2 PM",
        "15": "3 PM",
        "16": "4 PM",
        "17": "5 PM",
        "18": "6 PM",
        "19": "7 PM",
        "20": "8 PM",
        "21": "9 PM",
        "22": "10 PM",
        "23": "11 PM",
        "00": "12 AM",
    }

    # check day time
    if "AM" in start_time:
        pora_dnia = "AM"
    else:
        pora_dnia = "PM"
    # remove daytime form string 
    start_time = start_time[0:-3]

    # PRZELICZENIE GODZINY ROZPOCZĘCIA
    hours, minutes = start_time.split(":")
    # tymczasowe przekształcenie na zegar 24 godzinny
    hours = clock_24[hours + " " + pora_dnia]
    # przelicznenie czasu na float
    hours = int(hours)
    minutes = int(minutes)
    start_time = hours + minutes / 60

    # PRZELICZENIE CZASU TRWANIA na float
    hours_d, minutes_d = duration_time.split(":")
    hours_d = int(hours_d)

    minutes_d = int(minutes_d)
    duration_time = hours_d + minutes_d / 60
    new_time = start_time + duration_time

    """
    PONIŻEJ mamy MINUTY oraz ilość godzin"""
    new_time_minutes = ((new_time - int(new_time)) * 60) / 100
    new_time_minutes = f"{new_time_minutes:.02f}"
    new_time_hours = int(new_time)

    # ilość dni #
    days = int((new_time_hours) / 24)

    # PRZELICZENI Z POWROTEM na ZEGAR 12 godzinny"
    new_hour_24 = new_time_hours - (24 * days)

    # ostateczne przeliczenie nowej godziny minut i pory dnia
    new_hour_24 = str(new_hour_24)
    new_hour_12 = clock_12[new_hour_24]
    new_hour, new_pora_dnia = new_hour_12.split(" ")
    new_minutes = str(new_time_minutes)
    new_minutes = new_minutes[2:]
    full_new_time = new_hour + ":" + new_minutes + " " + new_pora_dnia

    # PRZELICZENIE DNI TYGODNIA zmiennej WEEK_DAY
    week_day_lst = (
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    )
    # "ilość dni do dodatnie wartość powinna być od 0 do 6")
    days_to_add = days % 7

    if week_day:
        week_day = week_day.lower()
        # pokazuje jaka wartość ma dany kolejdy dzień tygodnia, 0 Mon, 1 tue, 2 wedn, 3 thurs, 4 Frid, 5 sat, 6 sun
        day_number = week_day_lst.index(week_day)
        # dodaje do wartości dnia tygodnia day_value = week_day_value(0) + days i sprowadza do lczib pomiędzy 0 i 6
        new_day_value = (day_number + days_to_add) % 7
        new_week_day = (week_day_lst[new_day_value]).capitalize()
        new_week_day = f", {new_week_day}"

    else:
        new_week_day = ""

    ## RESULT
    if days == 1:
        new_full_time = f"{full_new_time}{new_week_day} (next day)"
    elif days > 1:
        new_full_time = f"{full_new_time}{new_week_day} ({days} days later)"
    else:
        new_full_time = full_new_time + new_week_day

    return new_full_time


###
# EXAMPLE
###

print(add_time("11:43 PM", "24:20", "tueSday"))
