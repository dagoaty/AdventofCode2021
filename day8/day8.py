#!/usr/bin/env python3

import sys
from typing import List

def get_inputs(file: str) -> List[List[List[str]]]:
    inputs: List[List[List[str]]] = []
    f = open(file, "r")
    for line in f:
        count = 0
        lineList: List[List[str]] = []
        for side in line.rstrip().split(' | '):
            lineList.append(side.split())
            count += 1
        inputs.append(lineList)
    return inputs


def countSingles(signals: List[int]) -> int:
    count: int = 0
    for line in signals:
        outputVals: List[int] = line[1]
        for val in outputVals:
            if len(val) in (2, 3, 4, 7):
                count += 1
    return count


def findOne(wires: List[str]) -> str:
    answer: str = ''
    for wire in wires:
        if len(wire) == 2:
            answer = ''.join(sorted(wire))
    return answer


def findFour(wires: List[str]) -> str:
    answer: str = ''
    for wire in wires:
        if len(wire) == 4:
            answer = ''.join(sorted(wire))
    return answer


def findSix(wires: List[str], nine, zero) -> str:
    answer: str = ''
    for wire in wires:
        if len(wire) == 6:
            reject = False
            if sorted(wire) == sorted(nine):
                reject = True
            if sorted(wire) == sorted(zero):
                reject = True
            if reject == False:
                answer = ''.join(sorted(wire))
                break
    return answer


def findSeven(wires: List[str]) -> str:
    answer: str = ''
    for wire in wires:
        if len(wire) == 3:
            answer = ''.join(sorted(wire))
    return answer


def findEight(wires: List[str]) -> str:
    answer: str = ''
    for wire in wires:
        if len(wire) == 7:
            answer = ''.join(sorted(wire))
    return answer


def findNine(wires: List[str], four: str) -> str:
    answer: str = ''
    for wire in wires:
        if len(wire) == 6:
            reject = False
            for c in four:
                if c not in wire:
                    reject = True
            if reject == False:
                answer = ''.join(sorted(wire))
                break
    return answer


def findZero(wires: List[str], seven: str, nine: str) -> str:
    answer: str = ''
    for wire in wires:
        if len(wire) == 6:
            reject = False
            for c in seven:
                if c not in wire:
                    reject = True
            if sorted(wire) == sorted(nine):
                reject = True
            if reject == False:
                answer = ''.join(sorted(wire))
                break
    return answer


def findThree(wires: List[str], seven: str) -> str:
    answer: str = ''
    for wire in wires:
        if len(wire) == 5:
            reject = False
            for c in seven:
                if c not in wire:
                    reject = True
            if reject == False:
                answer = ''.join(sorted(wire))
                break
    return answer


def findFive(wires: List[str], seven: str, nine: str) -> str:
    answer: str = ''
    partFive: str = ''
    for c in nine:
        if c not in seven:
            partFive += c
    for wire in wires:
        if len(wire) == 5:
            reject = False
            for c in partFive:
                if c not in wire:
                    reject = True
            if reject == False:
                answer = ''.join(sorted(wire))
                break
    return answer


def findTwo(wires: List[str], seven: str, nine: str) -> str:
    answer: str = ''
    for wire in wires:
        if len(wire) == 5:
            reject = False
            if sorted(wire) == sorted(seven):
                reject = True
            if sorted(wire) == sorted(nine):
                reject = True
            if reject == False:
                answer = ''.join(sorted(wire))
                break
    return answer


def processLine(display: List[List[int]]) -> int:
    number: int = 0
    one = findOne(display[0])
    four = findFour(display[0])
    seven = findSeven(display[0])
    eight = findEight(display[0])
    nine = findNine(display[0], four)
    zero = findZero(display[0], seven, nine)
    six = findSix(display[0], nine, zero)
    three = findThree(display[0], seven)
    five = findFive(display[0], seven, nine)
    two = findTwo(display[0], three, five)
    #print("Zero: %s\nOne: %s\nTwo: %s\nThree: %s\nFour: %s\nFive: %s\nSix: %s\nSeven: %s\nEight: %s\nNine: %s" % (zero, one, two, three, four, five, six, seven, eight, nine))
    number = ''
    for n in display[1]:
        sortn = ''.join(sorted(n))
        if sortn == one:
            number += '1'
        elif sortn == two:
            number += '2'
        elif sortn == three:
            number += '3'
        elif sortn == four:
            number += '4'
        elif sortn == five:
            number += '5'
        elif sortn == six:
            number += '6'
        elif sortn == seven:
            number += '7'
        elif sortn == eight:
            number += '8'
        elif sortn == nine:
            number += '9'
        elif sortn == zero:
            number += '0'
    return int(number)


def part1(inputs: List[int]) -> None:
    singleCount = countSingles(inputs)
    print("Part 1: %s" % singleCount)


def part2(inputs: List[int]) -> None:
    total = 0
    for display in inputs:
        total += processLine(display)
    print("Part 2: %s" % total)


def main() -> None:
    filename = sys.argv[1]
    inputs: List[int] = get_inputs(filename)
    part1(inputs)
    part2(inputs)


if __name__ == "__main__":
    main()