#!/usr/bin/env python3
import sys


def sum_of_calibration_values(filename: str) -> int:
    numbers = []
    letters = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    try:
        with open(filename, "r") as f:
            lines = f.read().split("\n")
            for line in lines:
                digs = []
                for i, j in enumerate(line):
                    if j.isdigit():
                        digs.append(j)
                    for x, y in enumerate(letters):
                        if line[i:].startswith(y):
                            digs.append(str(x + 1))
                numbers.append(int(digs[0] + digs[-1]))
    except:
        sys.exit(f"File <%s> not found" % filename)
    return sum(numbers)


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(f"Usage: %s <filename>" % sys.argv[0])
    filename = sys.argv[1].rstrip()
    print(sum_of_calibration_values(filename))


if __name__ == "__main__":
    main()
