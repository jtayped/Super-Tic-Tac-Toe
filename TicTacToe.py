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

        self.nextSquare = (1, 1)
        self.nextPlayer = 'x'

        self.history = [self.nextSquare]

    def initBoard(self):
        squareSize = WIDTH//3

        for colIndex,col in enumerate(self.board.squares):
            for rowIndex,_ in enumerate(col):
                x = colIndex * squareSize
                y = rowIndex * squareSize
                
                self.board.squares[colIndex][rowIndex] = (
                    Board((x, y), squareSize, 0.6, 1, 'black')
                )

    def drawNextSquare(self):
        x = WIDTH//3 * self.nextSquare[0]
        y = HEIGHT//3 * self.nextSquare[1]

        pygame.draw.rect(
            self.screen, 'red',
            (x, y, WIDTH//3+2, HEIGHT//3+2),
            4
        )

    def invertPlayer(self):
        if self.nextPlayer == 'x':
            self.nextPlayer = 'o'
        else:
            self.nextPlayer = 'x'
        
    def handleMove(self, x, y):
        # Calculate square index
        colIndex, rowIndex = int(x / (WIDTH / 3)), int(y / (HEIGHT / 3))

        # Check if in appropriate square
        if colIndex == self.nextSquare[0] and rowIndex == self.nextSquare[1]:
            board = self.board.squares[colIndex][rowIndex]

            if board.validMove(board.squares, x, y):
                newBoard, colIndex2, rowIndex2 = board.makeMove(board.squares, x, y, self.nextPlayer)
                board.squares = newBoard

                self.nextSquare = (colIndex2, rowIndex2)
                self.history.append(self.nextSquare)

                self.invertPlayer()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameOver = True
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handleMove(*event.pos)

    def update(self):
        self.events()
        self.screen.fill('white')

        self.board.update(self.screen)
        self.drawNextSquare()

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