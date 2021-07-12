import unittest
from start_game import play_game
from start_game import cards_equal
from war_card_game import PlayCards
from war_card_game import GenerateCardDeck
from test_CardDeck import *
import random


class TestGenerateCardDeck(unittest.TestCase):
    def test_shuffle_cards(self):
        """
        Testing shuffle_cards function
        Creating a deck of cards and shuffling it.
        Checking if the generated card deck is shuffled correctly.
        """

        print("test_shuffle_cards")
        test_cards_generate = GenerateCardDeck()
        test_card_deck = test_cards_generate.shuffle_cards()

        # Testing the length of the ordered deck same as shuffled deck.
        self.assertEqual(
            len(deck_ordered),
            len(test_card_deck),
            "Card count in the decks are not equal",
        )

        # Testing if the elements within the deck are same.
        self.assertNotEqual(
            deck_ordered,
            test_card_deck,
            "Cards in the deck are same. Check shuffle_cards function",
        )


class TestPlayCards(unittest.TestCase):
    def test_draw_card(self):
        """
        Testing draw_card function
        Checking if the cards are drawn correctly from each player.
        """

        print("test_draw_card")

        deck3_temp = list(deck3)

        gamer = PlayCards(deck3_temp)

        open_card_deck = []
        for x in range(0, len(deck3_temp)):
            open_card_deck.append(gamer.draw_card())

        self.assertEqual(
            len(deck3),
            len(open_card_deck),
            "Card count in the decks are not equal",
        )

        self.assertEqual(
            deck3,
            open_card_deck,
            "Cards in the deck are not same. Check draw_cards function",
        )

    def test_add_cards(self):
        """
        Testing add_cards function
        Checking if the cards are added correctly to each player's card deck.
        """

        print("test_add_cards")

        add_card_deck = []
        gamer = PlayCards(add_card_deck)
        gamer.add_cards(deck3)

        self.assertEqual(
            len(deck3),
            len(add_card_deck),
            "Card count in the decks are not equal",
        )

        self.assertEqual(
            deck3,
            add_card_deck,
            "Cards in the deck are not same. Check add_cards function",
        )

    def test_war_cards(self):
        """
        Testing war_cards function
        if the deck has >3, checking war condition.
        """

        print("test_war_cards")
        deck3_temp = list(deck3)

        gamer = PlayCards(deck3_temp)
        war_card_deck = gamer.war_cards()
        self.assertEqual(
            len(war_card_deck),
            3,
            "Length of war cards is != 3",
        )

        consolidated_deck = list(deck3_temp)

        for x in range(len(war_card_deck) - 1, -1, -1):
            consolidated_deck.append(war_card_deck[x])

        self.assertEqual(
            len(deck3),
            len(consolidated_deck),
            "Card count in the decks are not equal",
        )

        self.assertEqual(
            deck3,
            consolidated_deck,
            "Cards in the deck are not same. Check war_cards function",
        )

        """
        Testing war_cards function
        if the deck has <= 3, checking war condition.
        """
        deck3_temp = deck3[:3]
        gamer1 = PlayCards(deck3_temp)
        war_card_deck1 = gamer1.war_cards()

        self.assertEqual(
            len(war_card_deck1),
            0,
            "Length of war cards is != 0",
        )


class TestPlayGame(unittest.TestCase):
    def test_play_game(self):
        """
        Testing play_game function
        """
        
        # Setting up deck1 so player 2 is the winner
        print("test_play_game")
        self.assertEqual(
            play_game(deck1),
            "player 2",
            "Should be player 2",
        )

        # Setting up deck2 so player 1 is the winner
        self.assertEqual(
            play_game(deck2),
            "player 1",
            "Should be player 2",
        )

    def test_cards_equal(self):
        """
        Testing cards_equal function
        Both players get the same 8 deck3 cards

        Assumption:
        Open face cards match then this test is implemented.
        Each player's deck contains 8 cards instead of 26.
        The total_cards variable has 4 dummy cards that also needs to be added to the winner's deck.
        """

        print("test_play_game")
        total_cards_deck = list(deck4)
        gamer1_deck = list(deck3)
        gamer1 = PlayCards(gamer1_deck)
        gamer2_deck = list(deck3)
        gamer2 = PlayCards(gamer2_deck)
        cards_equal(gamer1, gamer2, total_cards_deck)
        self.assertEqual(
            len(gamer1_deck),
            0,
            "Card count in the decks are not equal. Check cards_equal function",
        )
        self.assertEqual(
            ((len(deck3) * 2) + len(deck4)),
            len(gamer2_deck),
            "Card count in the decks are not equal. Check cards_equal function",
        )

        """
        Testing cards_equal function
        Both players get the same deck3[:5] cards
        """
        total_cards_deck = list(deck4)
        gamer1_deck = list(deck3[:5])
        gamer1 = PlayCards(gamer1_deck)
        gamer2_deck = list(deck3[:5])
        gamer2 = PlayCards(gamer2_deck)
        cards_equal(gamer1, gamer2, total_cards_deck)
        self.assertEqual(
            len(gamer1_deck),
            0,
            "Card count in the decks are not equal. Check cards_equal function",
        )
        self.assertEqual(
            ((len(deck3[:5]) * 2) + len(deck4)),
            len(gamer2_deck),
            "Card count in the decks are not equal. Check cards_equal function",
        )

        """
        Testing cards_equal function
        Both players get the same deck3[:3] cards
        """
        total_cards_deck = list(deck4)
        gamer1_deck = list(deck3[:3])
        gamer1 = PlayCards(gamer1_deck)
        gamer2_deck = list(deck3[:3])
        gamer2 = PlayCards(gamer2_deck)
        cards_equal(gamer1, gamer2, total_cards_deck)
        self.assertEqual(
            len(gamer1_deck),
            0,
            "Card count in the decks are not equal. Check cards_equal function",
        )
        self.assertEqual(
            ((len(deck3[:3]) * 2) + len(deck4)),
            len(gamer2_deck),
            "Card count in the decks are not equal. Check cards_equal function",
        )

        """
        Testing cards_equal function
        Gamer1 has 0 cards when he/she enters cards_equal function 
        """
        total_cards_deck = list(deck4)
        gamer1_deck = []
        gamer1 = PlayCards(gamer1_deck)
        gamer2_deck = list(deck3)
        gamer2 = PlayCards(gamer2_deck)
        cards_equal(gamer1, gamer2, total_cards_deck)
        self.assertEqual(
            len(gamer1_deck),
            0,
            "Card count in the decks are not equal. Check cards_equal function",
        )
        self.assertEqual(
            ((len(deck3)) + len(deck4)),
            len(gamer2_deck),
            "Card count in the decks are not equal. Check cards_equal function",
        )


if __name__ == "__main__":
    unittest.main()
