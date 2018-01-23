#!/usr/bin/env python3
import argparse
import datetime

import sys


def main() -> None:
    """"
    Main routine
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", help="year for which we want to get the dates of the given weekday",
                        default=datetime.datetime.now().year, type=int)
    parser.add_argument("--weekday", help="weekday we want to print the dates for (e.g., 'Monday')",
                        required=True)
    args = parser.parse_args()

    weekdays = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }

    assert isinstance(args.year, int)

    assert isinstance(args.weekday, str)
    if args.weekday not in weekdays:
        print("Invalid weekday: {}".format(args.weekday), file=sys.stderr)
        return

    weekday = weekdays[args.weekday]

    first = datetime.date(year=args.year, month=1, day=1)
    last=datetime.date(year=args.year, month=12, day=31)

    day=first
    while day <= last:
        if day.weekday() == weekday:
            print(day.strftime("%Y-%m-%d"))

        day += datetime.timedelta(days=1)

if __name__ == "__main__":
    main()
