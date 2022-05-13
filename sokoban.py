"""
Name: Harlean
Description: ACII implementation of the game Sokoban. A game in which the player (P) fills holes (o) with crates (#).
"""

class Sokoban:
  def __init__(self, board):
    self.__board = board
    self.__board_list = list()
    self.__board_list.append(self.__board)
    self.__steps = 0 #for steps method
  
  def __str__(self):
  """Returns a string representation of the board."""
    current_board = self.__board_list[-1]
    string_board = list()
    for board in range (len(current_board)):
      for i in range(len(current_board[board])):
        if i == len(current_board[board]) - 1 and board == len(current_board) - 1:
          string_board.append(current_board[board][i])
        elif i == len(current_board[board]) - 1:
          string_board.append(current_board[board][i])
          string_board.append('\n')
        else:
          string_board.append(current_board[board][i])
          string_board.append(' ')
    
    return ''.join(value for value in string_board)

  def find_player(self):
  ""Returns a tuple containing the row and column of the player"""
    current_board = self.__board_list[-1]
    for i in range(len(current_board)):
      for column in range(len(current_board[i])):
        if 'P' == current_board[i][column]:
          return (i, column)

  def restart(self):
  """Reverts the game to its initial state."""
    while len(self.__board_list) > 1:
      self.__board_list.pop()
    self.__steps = 0
      
  def complete(self):
  ""Returns True if the game is complete and False otherwise. A game is complete if all holes on the board have been filled."""
    current_board = self.__board_list[-1]
    for row in range(len(current_board)):
      if 'o' in current_board[row]:
        return False
    return True
  
  def get_steps(self):
  """Returns number of moves currently made."""
    return self.__steps
  
  def undo(self):
  """Undoes the most recent move as if it never happened."""
   if len(self.__board_list) > 1 and self.__steps > 0:
      self.__board_list.pop()
      self.__steps -= 1

  def move(self, direction):
  """Moves the player if they can move. Updates crates if pushed by the player, and holes if crates are pushed into them."""
    if direction == 'w':
      self.up_move(direction)
    elif direction == 'a':
      self.left_move(direction)
    elif direction == 'd':
      self.right_move(direction)
    elif direction == 's':
      self.down_move(direction)
  
  def up_move(self, direction):
  """Computes an upwards move done by the player with 'w' being used to move player up."""
    row, column = self.find_player()
    current_board = list(list(i) for i in self.__board_list[-1])
    #checking if it can make a move upwards - don't have to worry about indexing as each time a move is made, it is reset to a non-negative number!
    if current_board[row - 1][column] == ' ':
      current_board[row - 1][column] = 'P'
      current_board[row][column] = ' '
      self.__board_list.append(current_board)
      self.__steps += 1
    elif current_board[row - 1][column] == '#' and current_board[row - 2][column] == ' ':
      current_board[row - 1][column] = 'P'
      current_board[row - 2][column] = '#'
      current_board[row][column] = ' '
      self.__board_list.append(current_board)
      self.__steps += 1
    elif current_board[row - 1][column] == '#' and current_board[row - 2][column] == 'o':
      current_board[row - 1][column] = 'P'
      current_board[row - 2][column] = ' '
      current_board[row][column] = ' '
      self.__board_list.append(current_board)
      self.__steps += 1
  
  def left_move(self, direction):
  """Computes a left move done by player, done with 'a'."""
    row, column = self.find_player()
    current_board = list(list(i) for i in self.__board_list[-1])
    #check if can make a move to the left - so now column is decremented
    if current_board[row][column - 1] == ' ':
      current_board[row][column - 1] = 'P'
      current_board[row][column] = ' '
      self.__board_list.append(current_board)
      self.__steps += 1
    elif current_board[row][column - 1] == '#' and current_board[row][column - 2] == ' ':
      current_board[row][column - 1] = 'P'
      current_board[row][column - 2] = '#'
      current_board[row][column] = ' '
      self.__board_list.append(current_board)
      self.__steps += 1
    elif current_board[row][column - 1] == '#' and current_board[row][column - 2] == 'o':
      current_board[row][column - 1] = 'P'
      current_board[row][column - 2] = ' '
      current_board[row][column] = ' '
      self.__board_list.append(current_board)
      self.__steps += 1
  
#right and down moves have cases where it can't go over the index on the right or bottom (i.e. gets an IndexError), so use modulus

  def max_column(self, current_board):
  """Returns the width of the board."""
    for i in range(len(current_board)):
      for column in range(len(current_board[i])):
        if 'P' == current_board[i][column]:
          return len(current_board[i]) #gives one more than the max column
  
  def right_move(self, direction):
  """Computes a right move, done with 'd'."""
    row, column = self.find_player()
    current_board = list(list(i) for i in self.__board_list[-1])
    #check if can make a move to the right - now column is incremented
    max_column = self.max_column(current_board)
    if current_board[row][(column + 1) % max_column] == ' ':
      current_board[row][(column + 1) % max_column] = 'P'
      current_board[row][column] = ' '
      self.__board_list.append(current_board)
      self.__steps += 1
    elif current_board[row][(column + 1) % max_column] == '#' and current_board[row][(column + 2) % max_column] == ' ':
      current_board[row][(column + 1) % max_column] = 'P'
      current_board[row][(column + 2) % max_column] = '#'
      current_board[row][column] = ' '
      self.__board_list.append(current_board)
      self.__steps += 1
    elif current_board[row][(column + 1) % max_column] == '#' and current_board[row][(column + 2) % max_column] == 'o':
      current_board[row][(column + 1) % max_column] = 'P'
      current_board[row][(column + 2) % max_column] = ' '
      current_board[row][column] = ' '
      self.__board_list.append(current_board)
      self.__steps += 1
      
  
  def down_move(self, direction):
  """Computes a downwards move, done with 's'."""
    row, column = self.find_player()
    current_board = list(list(i) for i in self.__board_list[-1])
    #check if can make a move downwards - so row is now incremented
    max_row = len(current_board) #one more than max row
    if current_board[(row + 1) % max_row][column] == ' ':
      current_board[(row + 1) % max_row][column] = 'P'
      current_board[row][column] = ' '
      self.__board_list.append(current_board)
      self.__steps += 1
    elif current_board[(row + 1) % max_row][column] == '#' and current_board[(row + 2) % max_row][column] == ' ':
      current_board[(row + 1) % max_row][column] = 'P'
      current_board[(row + 2) % max_row][column] = '#'
      current_board[row][column] = ' '
      self.__board_list.append(current_board)
      self.__steps += 1
    elif current_board[(row + 1) % max_row][column] == '#' and current_board[(row + 2) % max_row][column] == 'o':
      current_board[(row + 1) % max_row][column] = 'P'
      current_board[(row + 2) % max_row][column] = ' '
      current_board[row][column] = ' '
      self.__board_list.append(current_board)
      self.__steps += 1
    

def main(board):
    game = Sokoban(board)
    message = 'Press w/a/s/d to move, r to restart, or u to undo'
    print(message)
    while not game.complete():
        print(game)
        move = input('Move: ').lower()
        while move not in ('w', 'a', 's', 'd', 'r', 'u'):
            print('Invalid move.', message)
            move = input('Move: ').lower()
        if move == 'r':
            game.restart()
        elif move == 'u':
            game.undo()
        else:
            game.move(move)
    print(game)
    print(f'Game won in {game.get_steps()} steps!')

test_board = [
    [' ', ' ', '*', '*', '*', '*', ' ', '*'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    [' ', ' ', ' ', '#', ' ', ' ', ' ', '*'],
    [' ', '*', '*', '*', '*', ' ', 'o', '*'],
    [' ', 'o', ' ', ' ', ' ', ' ', ' ', '*'],
    [' ', ' ', ' ', ' ', 'P', ' ', '#', ' '],
    [' ', ' ', '*', '*', '*', '*', ' ', ' ']
]
main(test_board)


