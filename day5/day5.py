#!/usr/bin/env python3

import sys
from typing import List, Tuple, Dict


def get_inputs(file: str) -> List[Tuple[str, str]]:
    inputs: List[Tuple[str, str]] = []
    f = open(file, "r")
    for line in f:
        t1, t2 = line.rstrip().split(" -> ")
        inputs.append((t1, t2))
    return inputs


def stringToCoords(line: Tuple[str, str]) -> Tuple[int, int, int, int]:
    x1, y1 = [int(n) for n in line[0].split(',')]
    x2, y2 = [int(n) for n in line[1].split(',')]
    return x1, y1, x2, y2


def isStraightLine(n1: int, n2: int) -> bool:
    if (n1 == n2):
        return True
    else:
        return False


def getPoints(n1: int, n2: int) -> List[int]:
    n1, n2 = sorted((n1, n2))
    points: List[int] = [n for n in range(n1, n2+1)]
    return points


def getDiagonalPoints(x1: int, y1: int, x2: int, y2: int) -> List[Tuple[int, int]]:
    points: List[Tuple[int, int]] = []
    xpos = x1
    ypos = y1
    if x1 < x2: # Going Left to Right
        if y1 < y2: # Going down
            while ypos <= y2:
                points.append((xpos, ypos))
                xpos += 1
                ypos += 1
        if y1 > y2: # Going up
            while ypos >= y2:
                points.append((xpos, ypos))
                xpos += 1
                ypos -= 1
    if x1 > x2: # Going right to left
        if y1 < y2: # Going down
            while ypos <= y2:
                points.append((xpos, ypos))
                xpos -= 1
                ypos += 1
        if y1 > y2: # Going up
            while ypos >= y2:
                points.append((xpos, ypos))
                xpos -= 1
                ypos -= 1
    return points
                

def buildGrid(inputs: List[Tuple[str, str]], forTwo: bool) -> Dict[int, Dict[int, int]]:
    x1: int = 0
    y1: int = 0
    x2: int = 0
    y2: int = 0
    grid: Dict[int, Dict[int, int]] = {}
    for line in inputs:
        x1, y1, x2, y2 = stringToCoords(line)
        if isStraightLine(x1, x2): # Horizontal
            yPoints = getPoints(y1, y2)
            for point in yPoints:
                if x1 in grid:
                    if point in grid[x1]:
                        grid[x1][point] += 1
                    else:
                        grid[x1][point] = 1
                else:
                    grid[x1] = {point: 1}
        elif isStraightLine(y1, y2): # Vertical
            xPoints = getPoints(x1, x2)
            for point in xPoints:
                if point in grid:
                    if y1 in grid[point]:
                        grid[point][y1] += 1
                    else:
                        grid[point][y1] = 1
                else:
                    grid[point] = {y1: 1}
        elif forTwo == True: # Do diagonals for part2
            dPoints: List[Tuple[int, int]] = getDiagonalPoints(x1, y1, x2, y2)
            for location in dPoints:
                if location[0] in grid:
                    if location[1] in grid[location[0]]:
                        grid[location[0]][location[1]] += 1
                    else:
                        grid[location[0]][location[1]] = 1
                else:
                    grid[location[0]] = {location[1]: 1}
    return grid


def countDangerPoints(grid: Dict[int, Dict[int, int]]) -> int:
    count = 0
    for x in grid.keys():
        for y in grid[x].keys():
            if grid[x][y] > 1:
                count += 1
    return count


def part1(inputs: List[Tuple[str, str]]) -> None:
    grid = buildGrid(inputs, False)
    dangerPointCount = countDangerPoints(grid)
    print("Part 1: %s" % (dangerPointCount))


def part2(inputs: List[Tuple[str, str]]) -> None:
    grid = buildGrid(inputs, True)
    dangerPointCount = countDangerPoints(grid)
    print("Part 2: %s" % (dangerPointCount))


def main() -> None:
    filename = sys.argv[1]
    inputs: List[Tuple[str, str]] = get_inputs(filename)
    part1(inputs)
    part2(inputs)


if __name__ == "__main__":
    main()