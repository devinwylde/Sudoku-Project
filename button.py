""" COP 3502c -- Project 4: Sudoku
---> GROUP 102 <---
Created by: Harper Fuchs, Blake Wood, Devin Wylde, and Maddy Wirbel
Due Date: December 6th, 2022 """

import pygame
from color import ColorClass

class Button:
    def __init__(self, color, rect, shadow_length, overlay):
      # creates an instance of Button
        self.color = color
        self.rect = rect
        self.shadow_length = shadow_length
        self.shadow_rect = pygame.Rect(self.rect.x, self.rect.y + shadow_length, self.rect.width, self.rect.height)
        self.overlay = overlay
        self.Color = ColorClass()

    def draw(self, screen, button_clicked):
      # draws the buttons  
      if button_clicked:
            pygame.draw.rect(screen, self.Color.Darken(self.color), self.shadow_rect, border_radius=8)
            screen.blit(self.overlay, (self.rect.centerx - self.overlay.get_width()/2, self.rect.centery + self.shadow_length/2 - self.overlay.get_height()/2))
      else:
            pygame.draw.rect(screen, self.Color.Dark_Gray, self.shadow_rect, border_radius=8)
            pygame.draw.rect(screen, self.color, self.rect, border_radius=8)
            screen.blit(self.overlay, (self.rect.centerx - self.overlay.get_width()/2, self.rect.centery - self.overlay.get_height()/2))