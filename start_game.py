from war_card_game import GenerateCardDeck, PlayCards
from constants import RANKS, SUITS


def transfer_cards(total_cards, loser, winner):
    """
    The player with not enough cards loses the game.
    The other player gets all of this player's remaining cards.
    """

    winner.add_cards(total_cards)
    winner.add_cards(loser.cards)
    for _ in range(len(loser.cards)):
        loser.cards.pop()
    print("{} gets {}'s remaining cards".format(winner.name, loser.name))


def cards_not_equal(player, total_cards):

    # The player that picked the highest open card, gets both the cards
    print(
        "The highest card belongs to {}, {} gets the cards".format(
            player.name, player.name
        )
    )
    player.add_cards(total_cards)


def cards_equal(player1, player2, total_cards):
    """
    In war, both players place next three cards faced down and then
    another card faced up. The owner of the higher face-up card wins the war
    and adds all the cards on the table to the bottom of their deck.
    If the face up card is again equal then the battle repeats.
    """

    war_begin = True

    while war_begin:
        print("----Both players have equal card, so the war begins----")
        print("Each player places three cards faced down\n")
        print("-------------------------------------------")

        # Player 1 picks three cards faced down
        player1_face_down_cards = player1.war_cards()

        # To check if player 1 has returned any face down cards
        if len(player1_face_down_cards) == 0:
            transfer_cards(total_cards, player1, player2)
            # Player 1 has no sufficient cards, loses the game
            game_over = True
            break
        else:
            total_cards.extend(player1_face_down_cards)

        # Player 2 picks three cards faced down
        player2_face_down_cards = player2.war_cards()

        # To check if player 2 has returned any face down cards
        if len(player2_face_down_cards) == 0:
            transfer_cards(total_cards, player2, player1)
            # Player 2 has no sufficient cards, loses the game
            game_over = True
            break
        else:
            total_cards.extend(player2_face_down_cards)

        print("\nNow each player picks one card and places it faced up\n")
        # Both the players each pick an open card to determine who won the war
        player1_open_card = player1.draw_card()
        player2_open_card = player2.draw_card()
        total_cards.append(player1_open_card)
        total_cards.append(player2_open_card)

        # Player 1 picked the highest card
        if RANKS.index(player1_open_card[1]) > RANKS.index(player2_open_card[1]):
            cards_not_equal(player1, total_cards)
            war_begin = False

        # Player 2 picked the highest card
        elif RANKS.index(player1_open_card[1]) < RANKS.index(player2_open_card[1]):
            cards_not_equal(player2, total_cards)
            war_begin = False


def play_game(card_deck):
    """
    The card deck is divided evenly among the two players.
    At every round, each player reveals the top card of their deck.
    The player with the highest card, gets both the cards.
    If cards are of equal value, then there is a war.
    Player that gets all 52 cards wins the game.
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
            cards_equal(player1, player2, total_cards)

        print("\nScores after round {}:".format(game_round))
        print("{} scores {}".format(player1.name, len(player1.cards)))
        print("{} scores {}".format(player2.name, len(player2.cards)))
        print("***********************************************************")

        # Game ends when either one of the players has no cards
        if len(player1.cards) == 0 or len(player2.cards) == 0:
            game_over = True
        game_round += 1

    print("Game Ends")

    # The player that has all 52 cards becomes the winner
    if len(player1.cards) == 52:
        print("\n------{} has won the game!!!------\n".format(player1.name))
        return "player 1"

    else:
        print("\n------{} has won the game!!!------\n".format(player2.name))
        return "player 2"


if __name__ == "__main__":
    cards_generate = GenerateCardDeck()
    card_deck = cards_generate.shuffle_cards()
    play_game(card_deck)
