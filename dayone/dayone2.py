#!/usr/bin/env python3
import sys

letters_as_numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


# TODO
def sum_of_calibration_values(filename: str):
    with open(filename, "r") as f:
        lines = f.read().split("\n")
        pass


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: %s <filename>" % sys.argv[0])
        sys.exit(1)
    filename = sys.argv[1].rstrip()
    sum_of_calibration_values(filename)


if __name__ == "__main__":
    main()
