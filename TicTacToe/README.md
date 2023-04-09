# Tic-Tac-Toe Game

This is a simple tic-tac-toe game built in Python. The game allows two players, one human and one computer, to take turns marking spaces on a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.
## How to Play

1. The game begins with an empty 3x3 grid.
2. The human player is assigned the mark 'X', and the computer is assigned the mark 'O'.
3. The human player takes the first turn by selecting a position on the board to mark with an 'X'.
4. The computer then takes its turn by selecting a random empty position on the board to mark with an 'O'.
5. Steps 3-4 are repeated until one player has three marks in a row or all positions on the board have been filled.
6. If a player has three marks in a row, that player wins the game.
7. If all positions on the board are filled and neither player has three marks in a row, the game ends in a tie.

## Code Overview

The code starts by initializing the game board, current player, winner, and game running status. It then defines several functions to print the game board, take player input, and check for a win or tie.

The game runs in a loop, with each iteration printing the game board, taking player input, and checking for a win or tie. If the game is still running after the human player's turn, the computer takes its turn by selecting a random empty position on the board. The game continues until one player wins or the game ends in a tie.
