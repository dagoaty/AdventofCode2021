#!/usr/bin/env python3

import sys
from typing import List, Dict

def get_inputs(file: str) -> List[int]:
    inputs: List[int] = []
    f = open(file, "r")
    for line in f:
        inputs = ([int(n) for n in line.rstrip().split(',')])
    return inputs


def runDay(fishByAge: Dict[int, int]) -> Dict[int, int]:
    newFishAges: Dict[int, int] = dict.fromkeys(range(7), 0)
    for age in fishByAge.keys():
        newFishAges[age-1] = fishByAge[age]
    newFishAges[8] = newFishAges[-1]
    newFishAges[6] += newFishAges[-1]
    newFishAges[-1] = 0
    return newFishAges


def ageFish(inputs: List[int], days: int) -> int:
    fishByAge: Dict[int, int] = dict.fromkeys(range(7), 0)
    for age in inputs:
        fishByAge[age] += 1
    while days > 0:
        fishByAge = runDay(fishByAge)
        days -= 1
    fishCount = 0
    for age in fishByAge.keys():
        fishCount += fishByAge[age]
    return fishCount


def part1(inputs: List[int]) -> None:
    days: int = 80
    fish = ageFish(inputs, days)
    print("Part 1: %s" % fish)


def part2(inputs: List[int]) -> None:
    days: int = 256
    fish = ageFish(inputs, days)
    print("Part 2: %s" % fish)


def main() -> None:
    filename = sys.argv[1]
    inputs: List[int] = get_inputs(filename)
    part1(inputs)
    part2(inputs)


if __name__ == "__main__":
    main()