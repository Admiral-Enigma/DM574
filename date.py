from dataclasses import dataclass
from timestamp import (
    TimeStamp,
    make_timestamp,
    skip,
    equals as time_equals,
    copy as time_copy,
    to_string as time_to_string,
)

DAYS_PER_MONTH = 365 // 12


@dataclass
class Date:
    year: int
    month: int
    day: int
    time: TimeStamp


def make_date(
    year: int = 0, month: int = 0, day: int = 0, time: TimeStamp = make_timestamp()
) -> Date:
    return Date(year, month, day, time)


def valid(year: int, month: int, day: int) -> bool:
    return (
        year >= 0 and month < 11 and month >= 0 and day >= 0 and day <= DAYS_PER_MONTH
    )


def skip_day(d: Date) -> None:
    """Skips a day"""
    if (d.day + 1) % DAYS_PER_MONTH == 0:
        # We need to increment months
        skip_month(d)
        d.day = 0
    else:
        d.day += 1


def skip_month(d: Date) -> None:
    """Skip month"""
    if (d.month + 1) % 11 == 0:
        # We need to increment years
        skip_year(d)
        d.month = 0
    else:
        d.month += 1


def skip_year(d: Date) -> None:
    """Skip year"""
    d.year += 1


def skip_time(d: Date, t: TimeStamp) -> None:
    """Skips date's time with t"""
    skip(d.time, t)


def equals(d1: Date, d2: Date) -> bool:
    """Check if two dates are equal"""
    return (
        d1.day == d2.day
        and d1.year == d2.year
        and d1.month == d2.month
        and time_equals(d1.time, d2.time)
    )


def copy(d: Date) -> Date:
    """Returns a copy of Date d"""
    return Date(d.year, d.month, d.day, time_copy(d.time))


def to_string(d: Date) -> str:
    """Returns a string representation of a date"""
    return f"{d.year}-{d.month + 1}-{d.day + 1} {time_to_string(d.time)}"


if __name__ == "__main__":
    d = make_date(2001, 10, 12, make_timestamp(12, 33))
    print(to_string(d))
    skip_month(d)
    skip_month(d)
    print(to_string(d))
