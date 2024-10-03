from dataclasses import dataclass
from timestamp import TimeStamp, make_timestamp


@dataclass
class Date:
    year: int
    month: int
    day: int
    time: TimeStamp
