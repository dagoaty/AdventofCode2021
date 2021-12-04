#!/usr/bin/env python3

import sys
from typing import List, Tuple, Set


def getCallLine(inputs: List[str]) -> List[int]:
    return [int(n) for n in inputs[0].split(',')]


def buildCards(inputs: List[str]) -> List[List[List[int]]]:
    cards: List[List[List[int]]] = [[]]
    card = 0
    for input in inputs[2:]:
        if input == '':
            cards.append([])
            card += 1
        else:
            cards[card].append([int(n) for n in input.split()])
    return cards


def cardToWinLines(card: List[List[int]]) -> List[List[int]]:
    for col in [[row[i] for row in card] for i in range(len(card))]:
        card.append(col)
    return card


def get_inputs(file: str) -> List[str]:
    inputs: list[str] = []
    f = open(file, "r")
    for line in f:
        inputs.append(line.rstrip())
    return inputs


def getNumPos(num: int, callLine: List[int]) -> int:
    pos: int = 0
    for call in callLine:
        if call == num:
            return pos
        pos += 1
    return pos


def getCardWinningPos(card: List[List[int]], callLine: List[int]) -> int:
    cardWinPos: int = len(callLine)
    for line in card:
        lineWinPos: int = 0
        for num in line:
            numPos = getNumPos(num, callLine)
            if numPos > lineWinPos:
                lineWinPos = numPos
        if lineWinPos < cardWinPos:
            cardWinPos = lineWinPos
    return cardWinPos


def getWinningCard(cards: List[List[List[int]]], callLine: List[int]) -> Tuple[int, int]:
    winCard: int = len(cards)
    cardNum: int = 0
    winPos: int = len(callLine)
    for card in cards:
        cardWinPos = getCardWinningPos(card, callLine)
        if cardWinPos < winPos:
            winCard = cardNum
            winPos = cardWinPos
        cardNum += 1
    return winCard, winPos


def getLosingCard(cards: List[List[List[int]]], callLine: List[int]) -> Tuple[int, int]:
    loseCard: int = len(cards)
    cardNum: int = 0
    winPos: int = 0
    for card in cards:
        cardWinPos = getCardWinningPos(card, callLine)
        if cardWinPos > winPos:
            loseCard = cardNum
            winPos = cardWinPos
        cardNum += 1
    return loseCard, winPos


def flattenCard(card: List[List[int]]) -> Set[int]:
    return set([num for line in card for num in line])


def sumUncalledNumbers(card: List[List[int]], callLine: List[int]) -> int:
    cardNums = flattenCard(card)
    unused: Set[int] = cardNums.difference(set(callLine))
    return sum(unused)


def parts(inputs: List[str]) -> None:
    callLine: List[int] = getCallLine(inputs)
    cards: List[List[List[int]]] = buildCards(inputs)
    cardsWinLines: List[List[List[int]]] = []
    for card in cards:
        cardsWinLines.append(cardToWinLines(card))
    winningCard, winningPos = getWinningCard(cards, callLine)
    winningNum = callLine[winningPos]
    sumUncalled = sumUncalledNumbers(cards[winningCard], callLine[:winningPos+1])
    print("Part 1: %s" % (sumUncalled * winningNum))

    # Part 2 starts here
    losingCard, losingPos = getLosingCard(cards, callLine)
    losingNum = callLine[losingPos]
    sumUncalled = sumUncalledNumbers(cards[losingCard], callLine[:losingPos+1])
    print("Part 2: %s" % (sumUncalled * losingNum))


def main() -> None:
    filename = sys.argv[1]
    inputs: List[str] = get_inputs(filename)
    parts(inputs)


if __name__ == "__main__":
    main()