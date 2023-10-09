import pygame
from constants import *

class Board:
    def __init__(self, pos: tuple, size: int | float, paddingRatio=0.25, lineColor='white'):
        self.size = size
        self.padding = size/3 * paddingRatio
        self.pos = pygame.Vector2(*pos)
        self.lineColor = lineColor

        self.squares = [
            ['x', ' ', ' '],
            [' ', 'o', ' '],
            [' ', ' ', ' '],
        ]

        self.font = pygame.font.Font(None, 70)

    def drawLines(self, screen):
        # Draw horizontal lines
        for i in range(2):
            x1 = self.pos.x + self.padding
            x2 = self.pos.x + self.size - self.padding

            y = self.pos.y + self.size/3 + i * self.size/3
            
            pygame.draw.line(screen, self.lineColor, (x1, y), (x2, y), 2)

        # Draw vertical lines
        for i in range(2):
            y1 = self.pos.y + self.padding
            y2 = self.pos.y + self.size - self.padding

            x = self.pos.x + self.size/3 + i * self.size/3

            pygame.draw.line(screen, self.lineColor, (x, y1), (x, y2), 2)

    def drawSquare(self, screen, value, colIndex, rowIndex):
        color = 'red' if value == 'x' else 'blue'
        surf = self.font.render(value, True, color)

        x = self.pos.x + colIndex * self.size/3 + self.size/3/2
        y = self.pos.y + rowIndex * self.size/3 + self.size/3/2

        surfRect = surf.get_rect(center=(x, y))

        screen.blit(surf, surfRect)

    def drawSquares(self, screen):
        for colIndex,col in enumerate(self.squares):
            for rowIndex,cell in enumerate(col):
                if isinstance(cell, type(self)):
                    cell.update(screen)
                
                else:
                    self.drawSquare(
                        screen, cell, colIndex, rowIndex
                    )

    def draw(self, screen):
        self.drawLines(screen)
        self.drawSquares(screen)

    def update(self, screen):
        self.draw(screen)
