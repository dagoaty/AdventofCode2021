#!/usr/bin/env python3

import sys
from typing import List, Tuple, Dict

def get_inputs(file: str) -> Tuple[Dict[Tuple[int, int], str], List[str]]:
    inputs: Dict[Tuple[int, int], str] = {}
    insts: List[str] = []
    f = open(file, "r")
    instrFlag: bool = False
    for line in f:
        if line.rstrip() == '':
            instrFlag = True
            continue
        if instrFlag == False:
            (x, y) = line.rstrip().split(',')
            inputs[(int(x), int(y))] = '#'
        else:
            insts.append(line.rstrip().split()[2])
    return (inputs, insts)


def foldVertical(inputs: Dict[Tuple[int, int], str], foldAt: int) -> Dict[Tuple[int, int], str]:
    for coord in list(inputs.keys()):
        if coord[0] > foldAt:
            mirrorX: int = foldAt - (coord[0]-foldAt)
            inputs[(mirrorX, coord[1])] = inputs[coord]
            inputs.pop(coord)
    return inputs


def foldHorizontal(inputs: Dict[Tuple[int, int], str], foldAt: int) -> Dict[Tuple[int, int], str]:
    for coord in list(inputs.keys()):
        if coord[1] > foldAt:
            mirrorY: int = foldAt - (coord[1]-foldAt)
            inputs[(coord[0], mirrorY)] = inputs[coord]
            inputs.pop(coord)
    return inputs


def transparaPrint(inputs: Dict[Tuple[int, int], str]):
    bigX: int = 0
    bigY: int = 0
    for coords in list(inputs.keys()):
        if coords[0] > bigX:
            bigX = coords[0]
        if coords[1] > bigY:
            bigY = coords[1]
    for y in range(bigY+1):
        for x in range(bigX+1):
            print(inputs.get((x,y), ' '), end='')
        print()
    print()


def part1(inputs: Dict[Tuple[int, int], str], insts: List[str]) -> None:
    (type, at) = insts[0].split('=')
    if type == 'x':
        inputs = foldVertical(inputs, int(at))
    elif type == 'y':
        inputs = foldHorizontal(inputs, int(at))
    print("Part 1: %s" % len(inputs))


def part2(inputs: Dict[Tuple[int, int], str], insts: List[str]) -> None:
    for inst in insts:
        (type, at) = inst.split('=')
        if type == 'x':
            inputs = foldVertical(inputs, int(at))
        elif type == 'y':
            inputs = foldHorizontal(inputs, int(at))
    print("Part 2\n======")
    transparaPrint(inputs)


def main() -> None:
    filename: str = sys.argv[1]
    (inputs, instructions) = get_inputs(filename)
    part1(inputs, instructions)
    part2(inputs, instructions)


if __name__ == "__main__":
    main()