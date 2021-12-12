#!/usr/bin/env python3

import sys
from typing import List, Dict, Tuple
from collections import defaultdict, Counter

def get_inputs(file: str) -> List[Tuple[str, str]]:
    inputs: List[Tuple[str, str]] = []
    f = open(file, "r")
    for line in f:
        (source, target) = line.rstrip().split('-')[:2]
        inputs.append((source, target))
    return inputs


def buildCaveMap(inputs: List[Tuple[str, str]]) -> Dict[str, List[str]]:
    caveMap: Dict[str, List[str]] = defaultdict(list)
    for route in inputs:
        (source, destination) = route
        caveMap[source].append(destination)
        caveMap[destination].append(source)
    return caveMap


def maxedVisits(cave: str, path: List[str], max: int) -> bool:
    maxFlag: bool = False
    visitCount = Counter(path)
    if visitCount[cave] >= max:
        maxFlag = True
    return maxFlag


def canVisit(cave: str, pathfinder: List[str], revisit: str) -> bool:
    visitFlag = False
    path = pathfinder[:]
    if revisit in path:
        path.remove(revisit)
    if cave.isupper():
        visitFlag = True
    elif cave.islower() and cave not in path:
        visitFlag = True
    return visitFlag


def findRoutes(caveMap: Dict[str, List[str]], smallCave: str ='') -> List[List[str]]:
    routes: List[List[str]] = []
    pathfinder: List[List[str]] = [['start']]
    while len(pathfinder) > 0:
        currentPath = pathfinder.pop()
        for nextCave in caveMap[currentPath[-1]]:
            if nextCave == 'start':
                next
            elif nextCave == 'end':
                routes.append(currentPath + [nextCave])
            elif canVisit(nextCave, currentPath, smallCave):
                pathfinder.append(currentPath + [nextCave])
    return routes


def getSmalls(caveMap: Dict[str, List[str]]) -> List[str]:
    smalls: List[str] = [c for c in caveMap.keys() if c.islower()]
    smalls.remove('start')
    smalls.remove('end')
    return smalls


def part1(inputs: List[Tuple[str, str]]) -> None:
    caveMap: Dict[str, List[str]] = buildCaveMap(inputs)
    routes = findRoutes(caveMap)
    print("Part 1: %s" % len(routes))


def part2(inputs: List[Tuple[str, str]]) -> None:
    routes: List[List[str]] = []
    caveMap: Dict[str, List[str]] = buildCaveMap(inputs)
    smalls: List[str] = getSmalls(caveMap)
    for small in smalls:
        routes += findRoutes(caveMap, small)
    uniqueRoutes = set(tuple(route) for route in routes)
    print("Part 2: %s" % len(uniqueRoutes))


def main() -> None:
    filename: str = sys.argv[1]
    inputs: List[Tuple[str, str]] = get_inputs(filename)
    part1(inputs)
    part2(inputs)


if __name__ == "__main__":
    main()