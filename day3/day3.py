#!/usr/bin/env python3

import sys
from typing import List, Tuple


def get_inputs(file: str) -> List[List[str]]:
    inputs: list[list[str]] = []
    f = open(file, "r")
    for line in f:
        inputs.append(list(line.rstrip()))
    return inputs


def sumRow(row: List[str]) -> int:
    count = 0
    for b in row:
        count += int(b)
    return count


def getBitRows(inputs: List[List[str]]) -> List[List[str]]:
    return [[row[i] for row in inputs] for i in range(len(inputs[0]))]


def getRates(inputs: List[List[str]]) -> Tuple[int, int]:
    bitRows = getBitRows(inputs)
    gammaBin = ''
    epsilonBin = ''
    for row in bitRows:
        if sumRow(row) > int(len(row)/2):
            gammaBin += '1'
            epsilonBin += '0'
        else:
            gammaBin += '0'
            epsilonBin += '1'
    return int(gammaBin, 2), int(epsilonBin, 2)


def part1(inputs: List[List[str]]) -> None:
    (gammaRate, epsilonRate) = getRates(inputs)
    result: int = gammaRate * epsilonRate
    print("Part 1: %s" % result)


def removeUncommon(inputs: List[List[str]], selector: str, index: int) -> List[List[str]]:
    newInput: List[List[str]] = []
    for input in inputs:
        if input[index] == selector:
            newInput += [input]
    return newInput


def getOxyRating(inputs: List[List[str]]) -> int:
    index: int = 0
    while len(inputs) > 1:
        rows: List[List[str]] = getBitRows(inputs)
        row: List[str] = rows[index]
        sum: int = sumRow(row)
        if (sum == (len(row) - sum)):
            selector: str = '1'
        elif sum > (len(row) - sum):
            selector: str = '1'
        else:
            selector: str = '0'
        inputs = removeUncommon(inputs, selector, index)
        index += 1
    return int(''.join(inputs[0]), 2)


def getScrubRating(inputs: List[List[str]]) -> int:
    index: int = 0
    while len(inputs) > 1:
        rows: List[List[str]] = getBitRows(inputs)
        row: List[str] = rows[index]
        sum: int = sumRow(row)
        if (sum == (len(row) - sum)):
            selector: str = '0'
        elif sum > (len(row) - sum):
            selector: str = '0'
        else:
            selector: str = '1'
        inputs = removeUncommon(inputs, selector, index)
        index += 1
    return int(''.join(inputs[0]), 2)


def part2(inputs: List[List[str]]) -> None:
    oxyRating: int = getOxyRating(inputs)
    scrubRating: int = getScrubRating(inputs)
    result: int = oxyRating * scrubRating
    print("Part 2: %s" % result)


def main() -> None:
    filename = sys.argv[1]
    inputs: List[list[str]] = get_inputs(filename)
    part1(inputs)
    part2(inputs)


if __name__ == "__main__":
    main()