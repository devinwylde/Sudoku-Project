""" COP 3502c -- Project 4: Sudoku
---> GROUP 102 <---
Created by: Harper Fuchs, Blake Wood, Devin Wylde, and Maddy Wirbel
Due Date: December 6th, 2022 """

import pygame
from color import ColorClass

class Cell:
    def __init__(self, value, row, col):
      # constructor for the Cell class
      self.value = value
      # value - int containing number in cell
      self.loc = [row, col]
      # loc - index in board list
      # can_edit - boolean that sets whether or not user can edit cell (starts as False)
      self.is_invalid = False

      self.is_perm = True
      self.can_edit = False
      # is_invalid - boolean that sets whether edited tile is invalid, AKA wrong answer (starts         as False)
      self.square_size = 70 # 630 / 9
      self.rect = pygame.Rect((col//3)*10+col*50+64, (row//3)*10+row*50+78, 48, 48)

    def set_cell_value(self, value):
      # setter for this cell's value
      self.value = value

    def set_sketched_value(self, value):
      # setter for this cell's sketched value
      self.sketch_value = value
      
    def draw(self, screen, font, mouse, is_selected):
        """ Draws this cell, along with the value inside it.
        If the cell has a nonzero value, that value is displayed.
        Otherwise, no value is displayed in the cell.
        The cell is outlined red if it is currently selected."""
        # None is the default font, 32 is the font size (change if needed)

        if is_selected:
            pygame.draw.rect(screen, (247, 158, 199), (self.rect.x - 2, self.rect.y - 2, self.rect.width + 4, self.rect.height + 4))
        
        if self.rect.collidepoint(mouse.x, mouse.y):
            pygame.draw.rect(screen, (237, 212, 240), self.rect, border_radius=1)
        elif self.can_edit:
            pygame.draw.rect(screen, (255, 255, 255), self.rect, border_radius=1)
        else:
            pygame.draw.rect(screen, (240, 232, 240), self.rect, border_radius=1)
        # makes cells different colors if they can be edited or not
        if self.value != -1:
            text = font[self.value - 1]
            cell_rect = pygame.Rect(self.rect.centerx - font[self.value - 1].get_rect().centerx, self.rect.centery - font[self.value - 1].get_rect().centery, font[self.value - 1].get_rect().width, font[self.value - 1].get_rect().height)
            screen.blit(text, cell_rect)

        
    @property
    def is_editable(self):
        return self.can_edit and not self.is_perm
        


# rect - pygame rectangle for drawing to screen
