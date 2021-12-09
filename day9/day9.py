#!/usr/bin/env python3

import sys
from typing import List, Tuple

def get_inputs(file: str) -> List[List[int]]:
    inputs: List[List[int]] = []
    f = open(file, "r")
    for line in f:
        inputs.append([int(n) for n in line.rstrip()])
    return inputs


def isLowPoint(inputs: List[List[int]], hPos: int, wPos: int) -> bool:
    test: bool = True
    posVal: int = inputs[hPos][wPos]
    if hPos > 0:
        if inputs[hPos-1][wPos] <= posVal:
            test = False
    if hPos < len(inputs)-1:
        if inputs[hPos+1][wPos] <= posVal:
            test = False
    if wPos > 0:
        if inputs[hPos][wPos-1] <= posVal:
            test = False
    if wPos < len(inputs[hPos])-1:
        if inputs[hPos][wPos+1] <= posVal:
            test = False
    return test


def countLowSpots(inputs: List[List[int]]) -> int:
    count: int = 0
    height = len(inputs)
    for h in range(height):
        width = len(inputs[h])
        for w in range(width):
            if isLowPoint(inputs, h, w):
                count += inputs[h][w]+1
    return count


def countBasin(inputs: List[List[int]], pos: Tuple[int, int]) -> Tuple[List[List[int]], int]:
    size: int = 0
    checkPos: List[Tuple[int, int]] = [pos]
    while len(checkPos) > 0:
        (hPos, wPos) = checkPos.pop()
        if inputs[hPos][wPos] != 9:
            size += 1
            inputs[hPos][wPos] = 9
            if hPos > 0:
                if inputs[hPos-1][wPos] < 9:
                    checkPos.append((hPos-1, wPos))
            if hPos < len(inputs)-1:
                if inputs[hPos+1][wPos] < 9:
                    checkPos.append((hPos+1, wPos))
            if wPos > 0:
                if inputs[hPos][wPos-1] < 9:
                    checkPos.append((hPos, wPos-1))
            if wPos < len(inputs[hPos])-1:
                if inputs[hPos][wPos+1] < 9:
                    checkPos.append((hPos, wPos+1))
    return inputs, size


def countBasins(inputs: List[List[int]]) -> int:
    basins: List[int] = []
    for h in range(len(inputs)):
        for w in range(len(inputs[h])):
            inputs, newBasin = countBasin(inputs, (h, w))
            if newBasin > 0:
                basins.append(newBasin)
    basins = sorted(basins)
    return basins[-3] * basins[-2] * basins[-1]


def part1(inputs: List[List[int]]) -> None:
    count = countLowSpots(inputs)
    print("Part 1: %s" % count)


def part2(inputs: List[List[int]]) -> None:
    count = countBasins(inputs)
    print("Part 2: %s" % count)


def main() -> None:
    filename: str = sys.argv[1]
    inputs: List[List[int]] = get_inputs(filename)
    part1(inputs)
    part2(inputs)


if __name__ == "__main__":
    main()