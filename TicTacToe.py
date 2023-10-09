from constants import *
from elements.board import Board
import sys

class TicTacToe:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.gameOver = False

        self.board = Board((0, 0), WIDTH)
        self.initBoard()

    def initBoard(self):
        squareSize = WIDTH//3

        for colIndex,col in enumerate(self.board.squares):
            for rowIndex,_ in enumerate(col):
                x = colIndex * squareSize
                y = rowIndex * squareSize
                
                self.board.squares[colIndex][rowIndex] = (
                    Board((x, y), squareSize, 0.6, 'gray')
                )

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameOver = True

    def update(self):
        self.events()
        self.screen.fill('gray12')

        self.board.update(self.screen)

        pygame.display.flip()
        self.dt = self.clock.tick(FPS)

    def run(self):
        while not self.gameOver:
            self.update()

        pygame.quit()
        sys.exit()


def main():
    game = TicTacToe()
    game.run()


if __name__ == '__main__':
    main()