from tkinter import *

def init(data):
    data.nR = data.height//data.cellSize
    data.nC = data.width//data.cellSize
    data.xMargin = (data.width - ((data.nC)*data.cellSize))/2
    data.yMargin = (data.height - ((data.nR)*data.cellSize))/2


class Board(object):
    def __init__(self, board):
        self.board = board
        self.length = len(board)
        self.cellSize = 30

    def drawBoard(self, canvas, data):
        board = self.board
        for i in range(self.length):
            for j in range(self.length):
                if (i < self.length) and (j < self.length):
                    if board[i][j] == 0:
                    #open cells that pacman can travel through
                        canvas.create_rectangle(j * self.cellSize, i * self.cellSize,
                                                (j + 1) * self.cellSize, (i + 1) * self.cellSize,
                                                fill = "white")
                    else:
                    #walls
                        canvas.create_rectangle(i * self.cellSize, j * self.cellSize,
                                                (i + 1) * self.cellSize, (j + 1) * self.cellSize,
                                                fill = "blue")