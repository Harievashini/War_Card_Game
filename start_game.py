from war_card_game import GenerateCardDeck, PlayCards
from constants import RANKS, SUITS


def play_game(card_deck):
    """
    The card deck is divided evenly among the two players.
    """

    print("\nWelcome to War Card Game\n")

    player1_deck = []
    player2_deck = []

    # To split the cards one by one similar to standard card game.
    # Player 1 gets the first card then Player 2 and so on
    for card in range(0, len(card_deck), 2):
        player1_deck.append(card_deck[card])
        player2_deck.append(card_deck[card + 1])

    # Creating players
    print("PLAYER 1")
    player1 = PlayCards(player1_deck)
    print("PLAYER 2")
    player2 = PlayCards(player2_deck)


if __name__ == "__main__":
    cards_generate = GenerateCardDeck()
    card_deck = cards_generate.shuffle_cards()
    play_game(card_deck)
