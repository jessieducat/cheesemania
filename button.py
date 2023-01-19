import pygame


class button():
    def __init__(self, colour, hover_colour, pos, width, height, text=''):
        self.colour = colour
        self.hover_colour = hover_colour
        self.x = pos[0]
        self.y = pos[1]
        self.width = width
        self.height = height
        self.text = text
        self.rect = self.text.get_rect(center=(self.x, self.y))
        self.text_rect = self.text.get_rect(center=(self.x, self.y))
