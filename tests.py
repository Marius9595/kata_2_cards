from __future__ import annotations

import unittest
from enum import Enum

"""
KATA CARDS

CONTEXT:
    There are two players and they play with cards with the following rank:
         1 > 2 > 3 > 4 > 5 > 7 > 8 > 9 > J > Q > K

BEHAVIOUR:

    # one by one card is dealed to each player, when the second one
    has 2 cards, is ok the dealing

    # The first card compites with other first card and the same logic for the
    second one

    # The biggest card gives to player a point in each duel

    # It can be happen a Tie if the same value card is dueled

    # The score is result of sum of the two duels

    # The player with the higgest score is the winner and the other losser
"""
class Result(Enum):
    WON = 1
    LOST = 2
    TIED = 3

class Card:

    RANKING_VALUES = {
        '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8,
        '9': 9, 'J': 10, 'Q': 11, 'K': 12
    }

    def __init__(self, value: str):
        self.value = self.RANKING_VALUES[value]

    def compites_with(self, card) -> Result:

        if self.value < card.value:
            return Result.LOST
        elif self.value > card.value:
            return Result.WON

        return Result.TIED

class CardShould(unittest.TestCase):
    def test_(self):
        self.assertTrue(True)

    def test_compare_card_values(self):

        #TODO: comparar todas las combinaciones

        card_1 = Card('1')
        card_2 = Card('J')

        self.assertEqual(card_1.compites_with(card_2), Result.LOST)
        self.assertEqual(card_2.compites_with(card_1), Result.WON)
        self.assertEqual(card_2.compites_with(card_2), Result.TIED)












if __name__ == '__main__':
    unittest.main()
