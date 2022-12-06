""" COP 3502c -- Project 4: Sudoku
---> GROUP 102 <---
Created by: Harper Fuchs, Blake Wood, Devin Wylde, and Maddy Wirbel
Due Date: December 6th, 2022 """

from cell import Cell
from color import ColorClass
import pygame, sys

class Board:
  def __init__(self, width):
    """Constructor for the Board class.
    Screen is a window from PyGame.
    Difficulty is a variable that can be easy, medium, hard"""
    self.width = width
    self.height = width
    self.boxes = self.initialize_board_array()

  def initialize_board_array(self):
    # used in place of board.draw()
    boxes = []
    for a in range(self.width):
        boxes.append([])
        for b in range(self.height):
            boxes[a].append(Cell(-1, a, b))

    return boxes

  def iterate_by_box(self, position):
    """Used to allow the tab key to iterate through a 3x3 box,
    also used in the sudoku generator"""
    if position[0] % 3 == 2 and position[1] % 3 == 2:
        position[1] += 1
        position[0] -= 2
        if position[1] == 9:
            position[1] = 0
            position[0] += 3
    else:
        if position[1] % 3 == 2:
            position[1] -= 2
            position[0] += 1
        else:
            position[1] += 1
    return position, (position[0] % 3 == 2 and position[1] % 3 == 2)

  def sketch(self, value, indexes, screen):
    """Sets the skecthed value at the current selected cell equal to user
    entered value. It will be displayed at the top left corner of the cell
    using the draw() function."""
    sketch_val = Cell(value, indexes[0], indexes[1])
    if sketch_val.can_edit == True:
      sketch_val.is_perm = False
      sketch_val.draw(screen)

  def update_cell(self, value, indexes, screen):
    """ This function is called when the user presses the enter button
    ---> Transforms the value within the cell to permanent
    ---> Writes the value within cell permanently"""
    current_value = Cell(value, indexes[0], indexes[1])
    if current_value.is_perm == False:
      current_value.is_perm = True
      current_value.draw(screen)
    
  def reset_to_original(self):
    """ This function (when selected by the user) iterates through each cell in 
    the sudoku and determines whether or not the cell is able to be edited
    ---> If the cell is able to be edited or has been sketched in, the cell is cleared
    ---> Call with button"""
    for row in self.boxes:
      for tile in row:
          if tile.can_edit:
              tile.value = -1
              tile.is_perm = False
    
  def is_full(self):
    """ This function iterates through each cell in the board array and determines whether or not the cell is empty
    ---> If the cell is empty in the array (or value == -1) returns False
    ---> If cell is else, returns True"""
    for row in self.boxes:
      for col in row:
        for value in col:
          if value == -1 and value.is_perm == False:
            return False

    return True

  def check_filled(self):
    """ This function (similar to is_full) iterates through each cell in the 
    board array
    ---> If value is -1, function returns the (row, col) of cell
    ---> Else function is exited with return"""

    for row in self.boxes:
        for tile in row:
            if tile.value == -1 or (not tile.is_perm):
              # returns false if the cell is empty or contains only a sketch
                return False

    return True

  def check_win(self, initial):
    """ This function determines whether or not the user successfully completed the sudoku puzzle
    ---> Requires parameter of the original board """
    for row in range(0, len(initial)):
      for col in range(0, len(initial[row])):
        if initial[row][col] != self.boxes[row][col].value:
          return False

    return True

