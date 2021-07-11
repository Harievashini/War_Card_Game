# War Card Game
import random
from constants import RANKS, SUITS


class GenerateCardDeck:
    """
    Generates deck of cards using ranks and suits.
    Deck of cards are shuffled to produce a randomized set
    """

    def __init__(self):
        self.deck = []
        for rank in RANKS:
            for suit in SUITS:
                self.deck.append((suit, rank))

    def shuffle_cards(self):
        random.shuffle(self.deck)
        return self.deck


class PlayCards:
    """
    Stores the player name and card details.
    Performs operations such as adding cards to the player's deck
    and removing cards from the player's deck
    """

    def __init__(self, cards):
        self.name = input("Enter your name: ")
        self.cards = cards

    def draw_card(self):
        # Each player picks the top card in their deck
        open_card = self.cards.pop(0)
        print("The open card is {} {} \n".format(open_card[1], open_card[0]))
        return open_card

    def add_cards(self, total_cards):
        # New cards are placed at the end of the player's deck
        self.cards.extend(total_cards)

    # To draw three cards from a player's deck and place them faced down
    def war_cards(self):
        closed_card = []

        # Checks if player has enough cards for the war
        if len(self.cards) <= 3:
            print("{} does not have enough cards".format(self.name))

        else:
            for _ in range(3):
                closed_card.append(self.cards.pop())
        return closed_card
