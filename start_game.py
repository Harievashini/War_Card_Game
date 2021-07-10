from war_card_game import GenerateCardDeck, PlayCards
from constants import RANKS, SUITS


def cards_not_equal(player, total_cards):

    # The player that picked the highest open card, gets both the cards
    print(
        "The highest card belongs to {}, {} gets the cards".format(
            player.name, player.name
        )
    )
    player.add_cards(total_cards)


def play_game(card_deck):
    """
    The card deck is divided evenly among the two players.
    At every round, each player reveals the top card of their deck.
    The player with the highest card, gets both the cards.
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
    game_round = 1
    print("\n \nRound 1")
    print("Each player receives 26 cards at the start")
    game_over = False

    while not game_over:
        total_cards = []  # cards on the table

        print("{} draws a card".format(player1.name))
        player1_open_card = player1.draw_card()
        print("{} draws a card".format(player2.name))
        player2_open_card = player2.draw_card()

        total_cards.append(player1_open_card)
        total_cards.append(player2_open_card)

        # Player 1 picked the highest card
        if RANKS.index(player1_open_card[1]) > RANKS.index(player2_open_card[1]):
            cards_not_equal(player1, total_cards)

        # Player 2 picked the highest card
        elif RANKS.index(player1_open_card[1]) < RANKS.index(player2_open_card[1]):
            cards_not_equal(player2, total_cards)

        # war begins when both the cards have same value
        else:
            pass

if __name__ == "__main__":
    cards_generate = GenerateCardDeck()
    card_deck = cards_generate.shuffle_cards()
    play_game(card_deck)
