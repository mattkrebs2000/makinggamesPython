import pygame 
from pygame.locals import *
from sys import exit
from random import *

WIDTH, HEIGHT = 900, 500
ROW = WIDTH/100
TOTALBLOCKS = ROW * 3
WIDTHOFBLOCKS = WIDTH/ROW
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0,32)

def getHeightOfRow(start):
    if start < 10:
        return 0
    if start > 9 and start < 19:
        return 50
    if start > 18:
        return 100
    
def getWidthOfRow(start):
    return start % 9
    


class Rectangle:
    def __init__(self, pos, color, size):
        self.pos = pos
        self.color = color
        self.size = size
    def draw(self):
        pygame.draw.rect(screen, self.color, Rect(self.pos, self.size))


rectangles = []     

start = 0 

for start in range(int(TOTALBLOCKS)):
    Height = getHeightOfRow(start)
    WidthSpot = getWidthOfRow(start) * 100
    random_color = (randint(0,255), randint(0,255), randint(0,255))
    random_pos = (WidthSpot, Height)
    random_size = (WIDTHOFBLOCKS, 50)
    rectangles.append(Rectangle(random_pos, random_color, random_size))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.lock()
    for rectangle in rectangles:
    
        #screen out rectangles based on a condition 
        if rectangle.pos[0] > 500:
            rectangle.draw()
    screen.unlock()
    pygame.display.update()

