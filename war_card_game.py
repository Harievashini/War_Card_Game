# War Card Game
import random

ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
suits = ["Club", "Diamond", "Heart", "Spade"]


class GenerateCardDeck:
    """
    Generates deck of cards using ranks and suits.
    Deck of cards are shuffled to produce a randomized set
    """

    def __init__(self):
        self.deck = []
        for rank in ranks:
            for suit in suits:
                self.deck.append((suit, rank))

    def shuffle_cards(self):
        random.shuffle(self.deck)
        return self.deck


if __name__ == "__main__":
    cards_generate = GenerateCardDeck()
    card_deck = cards_generate.shuffle_cards()
