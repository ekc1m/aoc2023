#!/usr/bin/env python3
import sys


def sum_of_calibration_values(filename: str):
    with open(filename, "r") as f:
        lines = f.read().split("\n")
        first = None
        last = None
        numbers = []
        for i in lines:
            for j in i:
                if j.isdigit():
                    if first == None:
                        first = j
                        last = j
                    last = j
            if first != None and last != None:
                numbers.append(first + last)
            first = None
            last = None
        return sum(list(map(int, numbers)))


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: %s <filename>" % sys.argv[0])
        sys.exit(1)
    filename = sys.argv[1].rstrip()
    print(sum_of_calibration_values(filename))


if __name__ == "__main__":
    main()
