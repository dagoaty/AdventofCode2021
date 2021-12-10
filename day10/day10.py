#!/usr/bin/env python3

import sys
from typing import List, Dict

def get_inputs(file: str) -> List[List[str]]:
    inputs: List[List[str]] = []
    f = open(file, "r")
    for line in f:
        inputs.append([c for c in line.rstrip()])
    return inputs


def isOpening(char: str) -> bool:
    opening: bool = False
    openChars: str = '([{<'
    if char in openChars:
        opening = True
    return opening


def isClosing(char: str) -> bool:
    closing: bool = False
    closeChars: str = ')]}>'
    if char in closeChars:
        closing = True
    return closing


def scoreFailed(char: str) -> int:
    score: int = 0
    if char == ')':
        score = 3
    elif char == ']':
        score = 57
    elif char == '}':
        score = 1197
    elif char == '>':
        score = 25137
    else:
        score = 0
    return score


def closesPrevious(char: str, prev: str) -> bool:
    ret: bool = True
    if char == ')' and prev != '(':
        ret = False
    elif char == ']' and prev != '[':
        ret = False
    elif char == '}' and prev != '{':
        ret = False
    elif char == '>' and prev != '<':
        ret = False
    return ret


def parseLine(line: List[str]) -> int:
    score: int = 0
    parsed: List[str] = []
    for char in line:
        if isOpening(char):
            parsed.append(char)
        elif isClosing(char) and closesPrevious(char, parsed[-1]):
            parsed.pop(-1)
        else:
            score = scoreFailed(char)
            break
    return score


def calculateInvScore(scores: Dict[int, int]) -> int:
    finalScore: int = 0
    for value in scores.keys():
        finalScore += value * scores[value]
    return finalScore


def close(c: str) -> str:
    close: str = ''
    if c == '(':
        close = ')'
    elif c == '[':
        close = ']'
    elif c == '{':
        close = '}'
    elif c == '<':
        close = '>'
    return close


def completeClose(chars: List[str]) -> List[str]:
    chars.reverse()
    newChars: List[str] = [close(c) for c in chars]
    return newChars


def completeLine(line: List[str]) -> List[str]:
    parsed: List[str] = []
    for char in line:
        if isOpening(char):
            parsed.append(char)
        elif isClosing(char) and closesPrevious(char, parsed[-1]):
            parsed.pop(-1)
        else:
            print("Invalid line: %s" % line)
            exit(1)
    closers: List[str] = completeClose(parsed)
    return closers


def calculateCloseScore(scores: List[str]) -> int:
    score: int = 0
    for c in scores:
        score *= 5
        if c == ')':
            score += 1
        elif c == ']':
            score += 2
        elif c == '}':
            score += 3
        elif c == '>':
            score += 4
    return score


def part1(inputs: List[List[str]]) -> None:
    scores: Dict[int, int] = {3: 0, 57: 0, 1197: 0, 25137: 0}
    for line in inputs:
        score = parseLine(line)
        if score > 0:
            scores[score] += 1
    finalScore: int = calculateInvScore(scores)
    print("Part 1: %s" % finalScore)


def part2(inputs: List[List[str]]) -> None:
    incompleteLines: List[List[str]] = []
    scores: List[List[str]] = []
    for line in inputs:
        if parseLine(line) == 0:
            incompleteLines.append(line)
    for line in incompleteLines:
        scores.append(completeLine(line))
    finalScores: List[int] = []
    for score in scores:
        finalScores.append(calculateCloseScore(score))
    midScorePos = int(len(finalScores)/2)
    print("Part 2: %s" % sorted(finalScores)[midScorePos])


def main() -> None:
    filename: str = sys.argv[1]
    inputs: List[List[str]] = get_inputs(filename)
    part1(inputs)
    part2(inputs)


if __name__ == "__main__":
    main()