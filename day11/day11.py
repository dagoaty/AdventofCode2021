#!/usr/bin/env python3

import sys
from typing import List, Tuple

def get_inputs(file: str) -> List[List[int]]:
    inputs: List[List[int]] = []
    f = open(file, "r")
    for line in f:
        inputs.append([int(c) for c in line.rstrip()])
    return inputs


def incrementOctos(inputs: List[List[int]]) -> List[List[int]]:
    return [[octo+1 for octo in line] for line in inputs]


def findCharged(inputs: List[List[int]], flashed: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    charged: List[Tuple[int, int]] = []
    yPos = 0
    for y in inputs:
        xPos = 0
        while xPos < len(y):
            if inputs[yPos][xPos] > 9 and (xPos, yPos) not in flashed:
                charged.append((xPos, yPos))
            xPos += 1
        yPos += 1        
    return charged


def incrementNeighbours(inputs: List[List[int]], flasher: Tuple[int, int]) -> None:
    (xPos, yPos) = flasher
    octoGroup: List[Tuple[int, int]] = [(x,y) for x in range(xPos-1, xPos+2) for y in range(yPos-1, yPos+2)]
    octoGroup.remove(flasher)
    for octo in octoGroup:
        if 0 <= octo[1] < len(inputs) and 0 <= octo[0] < len(inputs[0]):
            inputs[octo[1]][octo[0]] += 1


def processCharged(inputs: List[List[int]], flashed: List[Tuple[int, int]], charged: List[Tuple[int, int]]) -> None:
    while len(charged) > 0:
        flashOcto = charged.pop()
        if flashOcto not in flashed:
            incrementNeighbours(inputs, flashOcto)
            flashed.append(flashOcto)
        charged.extend(findCharged(inputs, flashed))


def resetFlashed(inputs: List[List[int]], flashed: List[Tuple[int, int]]) -> None:
    while len(flashed) > 0:
        (x, y) = flashed.pop()
        inputs[y][x] = 0


def getFlashCount(inputs: List[List[int]], steps: int) -> int:
    flashCount: int = 0
    while steps > 0:
        charged: List[Tuple[int, int]] = []
        flashed: List[Tuple[int, int]] = []
        inputs = incrementOctos(inputs)
        charged.extend(findCharged(inputs, flashed))
        processCharged(inputs, flashed, charged)
        flashCount += len(flashed)
        resetFlashed(inputs, flashed)
        steps -= 1
    return flashCount
    

def findSyncStep(inputs: List[List[int]]) -> int:
    steps: int = 0
    allFlashed: bool = False
    while allFlashed is False:
        charged: List[Tuple[int, int]] = []
        flashed: List[Tuple[int, int]] = []
        inputs = incrementOctos(inputs)
        charged.extend(findCharged(inputs, flashed))
        processCharged(inputs, flashed, charged)
        if len(flashed) == 100:
            allFlashed = True
        resetFlashed(inputs, flashed)
        steps += 1
    return steps


def part1(inputs: List[List[int]]) -> None:
    steps: int = 100
    flashCount = getFlashCount(inputs, steps)
    print("Part 1: %s" % flashCount)


def part2(inputs: List[List[int]]) -> None:
    steps = findSyncStep(inputs)
    print("Part 2: %s" % steps)


def main() -> None:
    filename: str = sys.argv[1]
    inputs: List[List[int]] = get_inputs(filename)
    part1(inputs)
    part2(inputs)


if __name__ == "__main__":
    main()