from tkinter import *
import random
from board import *

def inBoard(x, y, d, data):
    r = d/2
    return (0 < x < (data.width - r)) and (0 < y < (data.height - r))

class Monster(object):
    all_monsters = []
    
    def __init__(self, data, color):
        self.color = color
        self.x, self.y = data.x, data.y
        self.d = data.speedX #diameter of monster
    
    @staticmethod
    def draw(canvas):
        for monster in Monster.all_monsters:
            canvas.create_oval(monster.x, monster.y, monster.x + monster.d,
                                monster.y + monster.d, fill = monster.color)
    
    @staticmethod
    def move(data, direction):
    #moves monster
        if data.gameOver: return

        for monster in Monster.all_monsters:
            temp = monster.x, monster.y
            if direction == 'up':
                monster.y -= data.speedY
            elif direction == 'down':
                monster.y += data.speedY
            elif direction == 'left':
                monster.x -= data.speedX
            elif direction == 'right':
                monster.x += data.speedX
            if not inBoard(monster.x, monster.y, monster.d, data):
            #if the monster is no longer in the board, undo the move
                monster.x, monster.y = temp[0], temp[1]
    
    @staticmethod
    def collideWithWalls(data):
        for i in range(len(data.board)):
            for j in range(len(data.board[0])):
                pass

############################################################################
# Basic animation frame work from 112 website
# https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html
############################################################################
def init(data):
# load data.xyz as appropriate
    board = [[0, 0, 0, 0],
             [0, 1, 0, 1],
             [0, 1, 0, 1],
             [0, 0, 0, 0]]
    data.board = Board(board)
    data.gameOver = False
    data.timer = 0
    data.x = random.randint(1, data.width - 1)
    data.y = random.randint(1, data.height - 1)
    data.speedX, data.speedY = 30, 30 #moves by width and height of each cell
    data.counter = 0
    data.direction = random.choice(['up', 'down', 'left', 'right'])

def mousePressed(event, data):
# use event.x and event.y
    pass

def keyPressed(event, data):
# use event.char and event.keysym
    pass

def timerFired(data):
    if data.timer == 0:
        Monster.all_monsters.append(Monster(data, "red"))

    data.timer += 100 #tracks number of milliseconds (1000 milliseconds = 1 sec)
    data.counter += 100
    if (data.timer % 100) == 0:
        if (data.counter % 500) == 0:
            data.direction = random.choice(['up', 'down', 'left', 'right'])
        Monster.move(data, data.direction)

def redrawAll(canvas, data):
# draw in canvas
    data.board.drawBoard(canvas, data)
    Monster.draw(canvas)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(400, 200)