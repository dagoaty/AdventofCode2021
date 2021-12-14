#!/usr/bin/env python3

import sys
from typing import Tuple, Dict
from collections import Counter, defaultdict

def get_inputs(file: str) -> Tuple[str, Dict[str, str]]:
    inputs: str = ''
    insts: Dict[str, str] = {}
    f = open(file, "r")
    instFlag: bool = False
    for line in f:
        if line.rstrip() == '':
            instFlag = True
            continue
        if instFlag == True:
            (i, r) = line.rstrip().split(' -> ')
            insts[i] = r
        else:
            inputs = line.rstrip()
    return (inputs, insts)


def polymerise(pairs: Dict[str, int], insts: Dict[str, str]) -> Dict[str, int]:
    newPairs: Dict[str, int] = defaultdict(int)
    for key in pairs.keys():
        a, c = key
        b = insts[key]
        newPairs[a+b] += pairs[key]
        newPairs[b+c] += pairs[key]
    return newPairs

def buildPairs(inputs: str) -> Dict[str, int]:
    pos = 0
    pairs: Dict[str, int] = defaultdict(int)
    while pos < len(inputs)-1:
        pairs[inputs[pos:pos+2]] += 1
        pos += 1
    return pairs


def countLetters(pairs: Dict[str, int]) -> Dict[str, int]:
    letters: Dict[str, int] = defaultdict(int)
    for key in pairs.keys():
        a, b = key
        letters[a] += pairs[key]
        letters[b] += pairs[key]
    return letters

def part1(inputs: str, insts: Dict[str, str]) -> None:
    i: int = 0
    pairs: Dict[str, int] = buildPairs(inputs)
    while i < 10:
        pairs = polymerise(pairs, insts)
        i += 1
    letters = countLetters(pairs)
    letters[inputs[0]] += 1
    letters[inputs[-1]] += 1
    counts = list(Counter(letters).values())
    counts.sort()
    answer = (counts[-1] - counts[0]) / 2
    print("Part 1: %s" % int(answer))


def part2(inputs: str, insts: Dict[str, str]) -> None:
    i: int = 0
    pairs: Dict[str, int] = buildPairs(inputs)
    while i < 40:
        pairs = polymerise(pairs, insts)
        i += 1
    letters = countLetters(pairs)
    letters[inputs[0]] += 1
    letters[inputs[-1]] += 1
    counts = list(Counter(letters).values())
    counts.sort()
    answer = (counts[-1] - counts[0]) / 2
    print("Part 2: %s" % int(answer))


def main() -> None:
    filename: str = sys.argv[1]
    (inputs, instructions) = get_inputs(filename)
    part1(inputs, instructions)
    part2(inputs, instructions)


if __name__ == "__main__":
    main()