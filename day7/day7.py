#!/usr/bin/env python3

import sys
from typing import List, Dict

def get_inputs(file: str) -> List[int]:
    inputs: List[int] = []
    f = open(file, "r")
    for line in f:
        inputs = ([int(n) for n in line.rstrip().split(',')])
    return inputs


def fuelCalc(curPos: int, destPos: int) -> int:
    return abs(curPos - destPos)


def thirstyFuelCalc(curPos: int, destPos: int) -> int:
    distance = abs(curPos - destPos)
    return int(((distance**2)+distance)/2)


def getLimit(inputs: List[int]) -> int:
    return sorted(inputs)[-1]


def part1(inputs: List[int]) -> None:
    limit: int = getLimit(inputs)
    fuelNeeded: Dict[int, int] = {}
    for destPos in range(limit):
        fuelNeeded[destPos] = sum([fuelCalc(n, destPos) for n in inputs])
    leastFuelDest: int = min(fuelNeeded, key=lambda k: fuelNeeded.get(k, 0))
    print("Part 1: %s requires %s" % (leastFuelDest, fuelNeeded[leastFuelDest]))


def part2(inputs: List[int]) -> None:
    limit: int = getLimit(inputs)
    fuelNeeded: Dict[int, int] = {}
    for destPos in range(limit):
        fuelNeeded[destPos] = sum([thirstyFuelCalc(n, destPos) for n in inputs])
    leastFuelDest: int = min(fuelNeeded, key=lambda k: fuelNeeded.get(k, 0))
    print("Part 2: %s requires %s" % (leastFuelDest, fuelNeeded[leastFuelDest]))


def main() -> None:
    filename = sys.argv[1]
    inputs: List[int] = get_inputs(filename)
    part1(inputs)
    part2(inputs)


if __name__ == "__main__":
    main()