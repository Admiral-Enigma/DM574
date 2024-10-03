from dataclasses import dataclass

@dataclass
class TimeStamp:
  """Class for keeping track of a specific point in time"""
  hours: int
  minutes: int
  seconds: int


def make_timestamp(hours: int = 0, minutes: int = 0, seconds: int = 0) -> TimeStamp:
  """Makes a timestamp"""
  return TimeStamp(hours, minutes, seconds)

def valid(hours: int, minutes: int, seconds: int) -> bool:
  """Checks if input is a valid timestamp"""
  return hours >= 0 and hours <= 23 and minutes > 0 and minutes <= 59 and seconds >= 0 and seconds <= 59

def skip_second(t: TimeStamp) -> None:
  """Skips a second in t"""
  if (t.seconds + 1) % 60 == 0:
    # We need to increment minutes
    skip_minute(t)
  else:
    t.seconds += 1

def skip_minute(t: TimeStamp) -> None:
  """Skip minute"""
  if (t.minutes + 1) % 60 == 0:
    # We need to increment hours
    skip_hour(t)
  else:
    t.minutes += 1

def skip_hour(t: TimeStamp) -> None:
  """Skip hour"""
  if (t.hours + 1) % 24 == 0:
    # A day has passed
    t.hours = 0
  else:
    t.hours += 1

def skip(t1: TimeStamp, t2: TimeStamp) -> None:
  """Skips t1 with t2"""
  t1.hours = (t1.hours + t2.hours) % 24

  if (t1.minutes + t2.minutes) >= 60:
    skip_hour(t1)
  t1.minutes = (t1.minutes + t2.minutes) % 60

  if (t1.seconds + t2.seconds) >= 60:
    skip_minute(t1)
  t1.seconds = (t1.seconds + t2.seconds) % 60

def equals(t1: TimeStamp, t2: TimeStamp) -> None:
  """Returns true if t1 and t2 is equal"""
  return t1.hours == t2.hours and t1.minutes == t2.minutes and t1.seconds == t2.seconds

def copy (t: TimeStamp) -> TimeStamp:
  """Returns a new copy of a timestamp"""
  return TimeStamp(t.hours, t.minutes, t.seconds)

def to_string(t: TimeStamp) -> str:
  """Returns a timestamp as a string representation"""
  return f'{t.hours}:{t.minutes}:{t.seconds}'


if __name__ == "__main__":
  ts = make_timestamp()
  for i in range(24 * 60 * 60):
      skip_second(ts)
      print(to_string(ts))
  print("---------------------")
  ts1 = make_timestamp(20, 1, 0)
  print(to_string(ts1))
  ts2 = make_timestamp(5, 0, 0)
  print(to_string(ts2))

  skip(ts1, ts2)
  print(to_string(ts1))

  print("---------------------")
  ts1 = make_timestamp(0, 30, 59)
  print(to_string(ts1))
  ts2 = make_timestamp(0, 30, 59)
  print(to_string(ts2))
  skip(ts1, ts2)
  print(to_string(ts1))
