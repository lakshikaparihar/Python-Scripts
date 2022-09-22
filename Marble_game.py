'''
Replay: who won the marble game?
A group of N players finished the marble game. Find out which player was the winner.
You are given the sequence of dice rolled during the game.

The game rules
At the start, each player from 1 to N has a bag with 10 marbles.
On the table there are 5 marble parking holes - numbered from 1-5. A parking hole can hold max 1 marble.

Starting with player 1, players roll the dice (after each other in ascending order i.e. player 1, 2, ... player 1, 2 ...).

IF dice value is 6: the player removes 1 marble from the player's bag.
IF dice value is 1,2,3,4, or 5: the player transfers 1 marble from the player's bag into the corresponding parking hole IF that corresponding parking hole is empty. OTHERWISE, the player transfers the marble from the corresponding parking hole into the player's bag.

The player wins, if the player's bag contains no marbles after the turn.
Marbles in the parking holes belong to no player.

'''

