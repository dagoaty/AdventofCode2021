#!/usr/bin/env python3

import sys
from typing import List


def get_inputs(file: str) -> List[int]:
    inputs: list = []
    f = open(file, "r")
    for line in f:
        inputs.append(int(line.rstrip()))
    return inputs


def processReturns(inputs: List[int]) -> int:
    position: int = 1 # skip the first item
    depthCount: int = 0
    while position < len(inputs):
        if inputs[position] > inputs[position - 1]:
            depthCount += 1
        position += 1
    return depthCount


def addList(values: List[int]) -> int:
    total = 0
    for value in values:
        total += value
    return total


def slideWindows(inputs: List[int]) -> int:
    pos: int = 0
    count: int = 0
    while pos+4 <= len(inputs):
        sumA: int = addList(inputs[pos:pos+3])
        sumB: int = addList(inputs[pos+1:pos+4])
        if sumA < sumB:
            count += 1
        pos += 1
    return count


def part1(inputs: List[int]) -> None:
    depthCount: int = processReturns(inputs)
    print(depthCount)


def part2(inputs: List[int]) -> None:
    increaseCount: int = slideWindows(inputs)
    print(increaseCount)


def main() -> None:
    filename = sys.argv[1]
    inputs: List[int] = get_inputs(filename)
    part1(inputs)
    part2(inputs)


if __name__ == "__main__":
    main()