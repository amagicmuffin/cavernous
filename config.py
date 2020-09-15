import pygame

# config variables
windowsizeX = 700
windowsizeY = 400

theMap = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "i", ".", "i", ".", "i", ".", "i", ".", "i", ">"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ">"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ">"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ">"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
]


# config images
hashtagImg = pygame.image.load("images/#.png")
atImg = pygame.image.load("images/at.png")
dotImg = pygame.image.load("images/dot.png")
exclaimImg = pygame.image.load("images/exclaim.png")
questionImg = pygame.image.load("images/questionMark.png")
leftMoveImg = pygame.image.load("images/leftMove.png")
rightMoveImg = pygame.image.load("images/rightMove.png")
iImg = pygame.image.load("images/i.png")


def renderImg(image, x, y):
    gameDisplay.blit(image, (x, y))


imagesDict = {
    "#": hashtagImg,
    "@": atImg,
    ".": dotImg,
    "!": exclaimImg,
    "?": questionImg,
    "<": leftMoveImg,
    ">": rightMoveImg,
    "i": iImg,
}

# colors
white = (255, 255, 255)
black = (0, 0, 0)

# stuff to display on init
pygame.init()

gameDisplay = pygame.display.set_mode((windowsizeX, windowsizeY))
pygame.display.set_caption("Cavernous")

clock = pygame.time.Clock()

mapStartX = 50  # this renders the map somehow
mapStartY = 50
for i in theMap:
    for j in i:
        for k in range(len(imagesDict)):
            renderImg(imagesDict[j], mapStartX, mapStartY)
        mapStartX += 50
    mapStartY += 50
    mapStartX = 50
pygame.display.update()

# player shenanigans
Apos = [1, 1]
renderImg(atImg, 50 + Apos[0] * 50, 50 + Apos[1] * 50)  # starting render
pygame.display.update()


def renderA(xOrY, direction):
    # print(theMap[Apos[0]][Apos[1]])
    xChanged = 0
    yChanged = 0
    if xOrY == 0:
        xChanged = 1
    else:
        yChanged = 1
        # theMap[x][y] is [y][x] because nested arrays are hard
    if theMap[Apos[1] + yChanged * direction][Apos[0] + xChanged * direction] == ".":
        renderImg(dotImg, 50 + Apos[0] * 50, 50 + Apos[1] * 50)
        Apos[xOrY] += direction
        renderImg(atImg, 50 + Apos[0] * 50, 50 + Apos[1] * 50)
        pygame.display.update()


def moveUp():
    renderA(1, -1)


def moveLeft():
    renderA(0, -1)


def moveDown():
    renderA(1, 1)


def moveRight():
    # Apos[0] += 1
    renderA(0, 1)

