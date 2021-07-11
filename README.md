# War Card Game

War is a card game played by two players using a standard 52 playing card deck. The objective of the game is that a player should win all of the 52 cards in the deck. In War, the cards are ranked Aces high and 2s low with suits being ignored. 

Randomized deck of cards is generated and divided between the two players 26 each. Each player reveals the top card of their deck at the same time. The player with the highest card takes both the cards and moves them to their deck. 

If the cards are of same value, then there is a war. Each player places the next three cards faced down and one card faced up. The player who owns the face-up card with higher value wins the war and adds all the cards on the table to the bottom of their deck. If again the face-up cards are equal then the battle repeats with each player placing three faced down cards and one face up card again. If a player lacks enough cards during the war then that player immediately loses the game, the other player gets this player’s cards and becomes the winner.

The game continues until either one of the players wins all the cards.

<h2><b> How to run? </b></h2>

python3 start_game.py

<h2><b> How to test? </b></h2>

test_CardDeck.py file contains sample decks which are used for testing.
<br>test.py file includes all test conditions.

Run <b> python3 test.py </b>
