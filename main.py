#!/usr/bin/env python3

"""
Tic-Tac-Toe Game in Python
"""

import sys

def display_board(board):
  """
  Displays the game board.

  Args:
    board (list): The game board.
  """
  for row in board:
    print(' '.join(row))

def get_user_input(board):
  """
  Gets the user's input.

  Args:
    board (list): The game board.

  Returns:
    int: The user's move.
  """
  while True:
    print('Enter your move (1-9): ')
    move = input()
    move = int(move)
    if move > 0 and move < 10 and board[move-1] == ' ':
      return move

def make_move(board, player, move):
  """
  Makes a move on the game board.

  Args:
    board (list): The game board.
    player (str): The player's symbol.
    move (int): The player's move.
  """
  board[move-1] = player

def check_winner(board):
  """
  Checks if there is a winner.

  Args:
    board (list): The game board.

  Returns:
    str: The winner's symbol, or None if there is no winner.
  """
  for row in range(3):
    if board[row][0] == board[row][1] == board[row][2] != ' ':
      return board[row][0]
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] != ' ':
      return board[0][col]
  if board[0][0] == board[1][1] == board[2][2] != ' ':
    return board[0][0]
  if board[0][2] == board[1][1] == board[2][0] != ' ':
    return board[0][2]
  return None

def game_over(board):
  """
  Checks if the game is over.

  Args:
    board (list): The game board.

  Returns:
    bool: True if the game is over, False otherwise.
  """
  winner = check_winner(board)
  if winner is not None:
    return True
  for row in board:
    if ' ' in row:
      return False
  return True

def main():
  """
  The main function.
  """
  board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
  player = 'X'
  turn = 0
  while not game_over(board):
    if turn % 2 == 0:
      player = 'X'
    else:
      player = 'O'
    print('Player {}'.format(player))
    display_board(board)
    move = get_user_input(board)
    make_move(board, player, move)
    turn += 1
  winner = check_winner(board)
  if winner == 'X':
    print("test)
    print('Player X won!')
  elif winner == 'O':
    print('Player O won!')
  else:
    print('Tie!')

if __name__ == '__main__':
  main()
