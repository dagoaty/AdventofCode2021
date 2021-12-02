#!/usr/bin/env python3

import sys
from typing import List, Tuple


def get_inputs(file: str) -> List[str]:
    inputs: list[str] = []
    f = open(file, "r")
    for line in f:
        inputs.append(str(line.rstrip()))
    return inputs


def findSimplePosition(inputs: List[str]) -> Tuple[int, int]:
    hPos: int = 0
    depth: int = 0
    for input in inputs:
        (instruction, size) = input.split()
        size = int(size)
        if instruction == "forward":
            hPos += size
        elif instruction == "up":
            depth -= size
        elif instruction == "down":
            depth += size
    return (hPos, depth)


def findPositionWithAim(inputs: List[str]) -> Tuple[int, int]:
    hPos: int = 0
    depth: int = 0
    aim: int = 0
    for input in inputs:
        (instruction, size) = input.split()
        size = int(size)
        if instruction == "forward":
            hPos += size
            depth += size * aim
        elif instruction == "up":
            aim -= size
        elif instruction == "down":
            aim += size
    return (hPos, depth)


def part1(inputs: List[str]) -> None:
    (hPos, depth)  = findSimplePosition(inputs)
    sumPos: int = hPos * depth
    print("Part 1: %s" % sumPos)


def part2(inputs: List[str]) -> None:
    (hPos, depth)  = findPositionWithAim(inputs)
    sumPos: int = hPos * depth
    print("Part 2: %s" % sumPos)


def main() -> None:
    filename = sys.argv[1]
    inputs: List[str] = get_inputs(filename)
    part1(inputs)
    part2(inputs)


if __name__ == "__main__":
    main()