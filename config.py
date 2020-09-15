import pygame

#config variables
windowsizeX = 700
windowsizeY = 400

theMap=[['#','#','#','#','#','#','#','#','#','#','#','#'],
        ['#','.','i','.','i','.','i','.','i','.','i','>'],
        ['#','.','.','.','.','.','.','.','.','.','.','>'],
        ['#','.','.','.','.','.','.','.','.','.','.','>'],
        ['#','.','.','.','.','.','.','.','.','.','.','>'],
        ['#','#','#','#','#','#','#','#','#','#','#','#']]




        

#config images
hashtagImg = pygame.image.load('pictures/#.png')
atImg = pygame.image.load('pictures/at.png')
dotImg = pygame.image.load('pictures/dot.png')
exclaimImg = pygame.image.load('pictures/exclaim.png')
questionImg = pygame.image.load('pictures/questionMark.png')
leftMoveImg = pygame.image.load('pictures/leftMove.png')
rightMoveImg = pygame.image.load('pictures/rightMove.png')
iImg = pygame.image.load('pictures/i.png')

def renderImg(image,x,y):
    gameDisplay.blit(image,(x,y))

#colors
white = (255,255,255)
black = (0,0,0)

#some pygame stuff
pygame.init()

gameDisplay = pygame.display.set_mode((windowsizeX,windowsizeY))
pygame.display.set_caption('Cavernous')

clock = pygame.time.Clock()

mapStartX = 50#render placeholder map, replace later
mapStartY = 50
for i in theMap:
    for j in i:
        renderImg(dotImg,mapStartX,mapStartY)
        mapStartX += 50
    mapStartY += 50
    mapStartX = 50
pygame.display.update()

#player shenanigans
APos = [1,1]
renderImg(atImg, 50+APos[0]*50, 50+APos[1]*50) #starting render
pygame.display.update()

def renderA(xOrY,direction):
    renderImg(dotImg, 50+APos[0]*50, 50+APos[1]*50)
    APos[xOrY] += direction
    renderImg(atImg, 50+APos[0]*50, 50+APos[1]*50)
    pygame.display.update()

def moveUp():
    renderA(1,-1)
def moveLeft():
    renderA(0,-1)
def moveDown():
    renderA(1,1)
def moveRight():
    #APos[0] += 1
    renderA(0,1)

