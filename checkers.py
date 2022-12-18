import pygame
import numpy as np
import sys
import random

GRID_SIZE = 10


class Tura:
    def __init__(self, grid_size, player):
        self.grid = np.zeros((grid_size-1, grid_size-1))
        self.player = player
        self.scores = (0, 0)

    def next(self, i, j):
        self.grid[i][j] = self.player
        self.checkCaptures()
        (x, y) = self.checkGroups()
        # print(f'{x}, {y}')
        self.checkGroupLib(x)
        self.checkGroupLib(y)
        print(self.scores)
        self.player *= -1

    def pas(self):
        self.player *= -1
        

    def checkGroupLib(self, playerGroups):
        dictG = {}
        for x in playerGroups:
            liberties = 0
            for y in x:
                liberties += self.checkPointLibGroup(y[0], y[1])
            if (liberties not in dictG.keys()):
                dictG[liberties] = [x]
            else:
                dictG[liberties] += [x]
        if 0 in dictG.keys():
            for i in dictG[0]:
                for j in i:
                    if self.grid[j[0]][j[1]] == -1:
                        self.scores = (self.scores[0] + 1, self.scores[1])
                    else:
                        self.scores = (self.scores[0], self.scores[1] + 1)
                    self.grid[j[0]][j[1]] *= 0

    def checkPointLib(self, i, j):
        liberties = 0
        if i > 0 and (self.grid[i-1][j] != -1 * self.grid[i][j] or self.grid[i-1][j] == 0):
            liberties += 1
        if j > 0 and (self.grid[i][j-1] != -1 * self.grid[i][j] or self.grid[i][j-1] == 0):
            liberties += 1
        if i+1 < len(self.grid) and (self.grid[i+1][j] != -1 * self.grid[i][j] or self.grid[i+1][j] == 0):
            liberties += 1
        if j+1 < len(self.grid) and (self.grid[i][j+1] != -1 * self.grid[i][j] or self.grid[i][j+1] == 0):
            liberties += 1
        return liberties

    def checkPointLibGroup(self, i, j):
        liberties = 0
        if i > 0 and (self.grid[i-1][j] == 0):
            liberties += 1
        if j > 0 and (self.grid[i][j-1] == 0):
            liberties += 1
        if i+1 < len(self.grid) and (self.grid[i+1][j] == 0):
            liberties += 1
        if j+1 < len(self.grid) and (self.grid[i][j+1] == 0):
            liberties += 1
        return liberties

    def checkCaptures(self):
        dictP = {}
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                liberties = self.checkPointLib(i, j)
                if (liberties not in dictP.keys()):
                    dictP[liberties] = [(i, j)]
                else:
                    dictP[liberties] += [(i, j)]
        if 0 in dictP.keys():
            for (i, j) in dictP[0]:
                if self.grid[i][j] == -1:
                    self.scores = (self.scores[0] + 1, self.scores[1])
                else:
                    self.scores = (self.scores[0], self.scores[1] + 1)
                self.grid[i][j] *= 0

    def checkGroups(self):
        player1Positions = []
        player2Positions = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 1:
                    player1Positions.append((i, j))
                if self.grid[i][j] == -1:
                    player2Positions.append((i, j))
        player1Groups = []
        player2Groups = []
        player1VisitedPositions = []
        player2VisitedPositions = []
        for x in player1Positions:
            group = []
            OK = True
            if x not in player1VisitedPositions:
                group.append(x)
                player1VisitedPositions.append(x)
                while OK == True and player1VisitedPositions != player1Positions:
                    for x in group:
                        OK = False
                        for y in player1Positions:
                            if y in player1VisitedPositions:
                                continue
                            if x == y:
                                continue
                            if x[0] == y[0] and (x[1] == y[1] + 1 or x[1] == y[1] - 1):
                                OK = True
                                group.append(y)
                                player1VisitedPositions.append(y)
                                break
                            if x[1] == y[1] and (x[0] == y[0] + 1 or x[0] == y[0] - 1):
                                OK = True
                                group.append(y)
                                player1VisitedPositions.append(y)
                                break
                if group != []:
                    player1Groups.append(group)

        for x in player2Positions:
            group = []
            OK = True
            if x not in player2VisitedPositions:
                group.append(x)
                player2VisitedPositions.append(x)
                while OK == True and player2VisitedPositions != player2Positions:
                    for x in group:
                        OK = False
                        for y in player2Positions:
                            if y in player2VisitedPositions:
                                continue
                            if x == y:
                                continue
                            if x[0] == y[0] and (x[1] == y[1] + 1 or x[1] == y[1] - 1):
                                OK = True
                                group.append(y)
                                player2VisitedPositions.append(y)
                                break
                            if x[1] == y[1] and (x[0] == y[0] + 1 or x[0] == y[0] - 1):
                                OK = True
                                group.append(y)
                                player2VisitedPositions.append(y)
                                break
                if group != []:
                    player2Groups.append(group)
        return (player1Groups, player2Groups)


WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('GO GAME - A')
GREY = (128, 128, 128)

FPS = 60
tura = Tura(GRID_SIZE, 1)

def checkPointLibGb(grid, i, j):
    liberties = 0
    if i > 0 and (grid[i-1][j] != -1 * tura.player or grid[i-1][j] == 0):
        liberties += 1
    if j > 0 and (grid[i][j-1] != -1 * tura.player or grid[i][j-1] == 0):
        liberties += 1
    if i+1 < len(grid) and (grid[i+1][j] != -1 * tura.player or grid[i+1][j] == 0):
        liberties += 1
    if j+1 < len(grid) and (grid[i][j+1] != -1 * tura.player or grid[i][j+1] == 0):
        liberties += 1
    return liberties


def checkMove(tura: Tura, i, j):
    if i == 0 or j == 0 or i == GRID_SIZE or j == GRID_SIZE or tura.grid[i-1][j-1] != 0 or checkPointLibGb(tura.grid, i-1, j-1) == 0:
        # print('NO')
        return False
    else:
        # print('YES')
        return True


def drawGrid(i: int, tura: Tura):
    blockSize = WIDTH // (i)
    width = WIDTH - WIDTH % i
    start = WIDTH % i
    var = 0
    for x in range(start//2, width, blockSize):
        var = 0
        for y in range(start//2, width, blockSize):
            if var > i:
                break
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(WIN, (200, 200, 200), rect, 1)
            var += 1
    for x in range(len(tura.grid)):
        for y in range(len(tura.grid[x])):
            if tura.grid[x][y] != 0:
                color = ()
                if tura.grid[x][y] == 1:
                    color = (0, 0, 0)
                else:
                    color = (255, 255, 255)
                pygame.draw.circle(
                    WIN, color, ((x+1)*blockSize, (y+1)*blockSize), blockSize/2.5)

                # print()


def draw_window():
    WIN.fill(GREY)
    drawGrid(GRID_SIZE, tura)
    pygame.display.update()


def getPosition():
    (x, y) = pygame.mouse.get_pos()
    blockSize = WIDTH / GRID_SIZE
    i = 0
    j = 0
    var = 0
    while var + blockSize < x:
        i += 1
        var += blockSize
    var = 0
    while var + blockSize < y:
        j += 1
        var += blockSize
    if checkMove(tura, i, j):
        tura.next(i-1, j-1)
        if (sys.argv[1] == 'computer'):
            computerMove()
    
    # print()
    
def computerMove():
    i = random.randint(0, GRID_SIZE)
    j = random.randint(0, GRID_SIZE)
    while checkMove(tura, i, j) == False:
        i = random.randint(0, GRID_SIZE)
        j = random.randint(0, GRID_SIZE)
    tura.next(i-1, j-1)
        


clock = pygame.time.Clock()

if (sys.argv[1] == 'computer'):
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed = pygame.mouse.get_pressed()
                # print(mouse_pressed)
                if mouse_pressed == (True, False, False):
                    getPosition()
                elif mouse_pressed == (False, False, True):
                    tura.pas()
                    computerMove()
        draw_window()

    pygame.quit()
    
elif (sys.argv[1] == 'human'):
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed = pygame.mouse.get_pressed()
                # print(mouse_pressed)
                if mouse_pressed == (True, False, False):
                    getPosition()
                elif mouse_pressed == (False, False, True):
                    tura.pas()
        draw_window()

    pygame.quit()
