import pygame

# load images
hashtagImg = pygame.image.load("images/#.png")
atImg = pygame.image.load("images/at.png")
dotImg = pygame.image.load("images/dot.png")
exclaimImg = pygame.image.load("images/exclaim.png")
questionImg = pygame.image.load("images/questionMark.png")
leftMoveImg = pygame.image.load("images/leftMove.png")
rightMoveImg = pygame.image.load("images/rightMove.png")
iImg = pygame.image.load("images/i.png")
startImg = pygame.image.load("images/start.png")
nullImg = pygame.image.load("images/null.png")  # not used in dict down below i guess


def renderImg(image, x, y):
    gameDisplay.blit(image, (x, y))


# colors
white = (255, 255, 255)
black = (0, 0, 0)

# run on startup
pygame.init()

windowsizeX = 700
windowsizeY = 400

gameDisplay = pygame.display.set_mode((windowsizeX, windowsizeY))
pygame.display.set_caption("Cavernous")

clock = pygame.time.Clock()

# render startscreen

# x,y = middle of window - half of image's size
renderImg(startImg, int(windowsizeX / 2 - 50), int(windowsizeY / 2 - 20))

blink = 1  # 1 = on, -1 = off


def startSelectBlink(blink):
    if blink == 1:
        rightImg = rightMoveImg
        leftImg = leftMoveImg
    else:
        rightImg = nullImg
        leftImg = nullImg
    # x = middle of window - half of images size, then move to left 100
    renderImg(leftImg, int(windowsizeX / 2 - 25 - 100), int(windowsizeY / 2 - 25))
    # x = middle of window - half of images size, then move to right 100
    renderImg(rightImg, int(windowsizeX / 2 - 25 + 100), int(windowsizeY / 2 - 25))


# pygame.display.update()

pygame.time.set_timer(pygame.USEREVENT + 1, 1000)

crashed = False
# startscreen game loop
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            exit()

        if event.type == pygame.USEREVENT + 1:
            blink *= -1

        elif event.type == pygame.KEYDOWN:
            crashed = True

    startSelectBlink(blink)

    pygame.display.update()  # only update parts of thing
    clock.tick(60)  # 60 tps

print("yes")
# here down to the end of the for loop: render map on game start
theMap = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "i", ".", "i", ".", "i", ".", "i", ".", "i", ">"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ">"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ">"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ">"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
]

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

mapStartX = 50
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


# main game loop
crashed = False
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moveUp()
            if event.key == pygame.K_a:
                moveLeft()
            if event.key == pygame.K_s:
                moveDown()
            if event.key == pygame.K_d:
                moveRight()

        # print(event)

    # renderImg(dotImg,50,50)

    # pygame.display.update() #only update parts of thing
    clock.tick(60)  # 60 tps
