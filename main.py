import pygame

# colors
white = (255, 255, 255)
black = (0, 0, 0)

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


# load text
pygame.font.init()
comicSansFont = pygame.font.Font(
    "fonts/COMIC.TTF", 15
)  # font size 15, maybe make variable?


def putTextHere(text, x, y):  # put text somewhere; specify x and y for topleft corner
    text = comicSansFont.render(text, True, white, black)
    textRect = text.get_rect()
    textRect.topleft = (x, y)
    gameDisplay.blit(text, textRect)
    pygame.display.update()

def printText(text):  # put text under the map.
    text = comicSansFont.render(text, True, white, black)
    textRect = text.get_rect()
    textRect.topleft = (400,0)
    gameDisplay.blit(text, textRect)
    pygame.display.update()

# run on startup
pygame.init()

windowsizeX = 700  # set pyGame window size vars
windowsizeY = 800  # ^

gameDisplay = pygame.display.set_mode(  # set pyGame window size
    (windowsizeX, windowsizeY)
)
pygame.display.set_caption("Cavernous")  # set pyGame caption (topleft)

clock = pygame.time.Clock()

# render startscreen

# x,y = middle of window - half of image's size
renderImg(startImg, int(windowsizeX / 2 - 50), int(windowsizeY / 2 - 20))

blink = 1  # 1 = on, -1 = off


def startSelectBlink(blink):  # startscreen arrow blink effect
    if blink == 1:  # show the arrows
        rightImg = rightMoveImg
        leftImg = leftMoveImg
    else:  # , show nothing
        rightImg = nullImg
        leftImg = nullImg
    # x = middle of window - half of images size, then move to left 100
    renderImg(leftImg, int(windowsizeX / 2 - 25 - 100), int(windowsizeY / 2 - 25))
    # x = middle of window - half of images size, then move to right 100
    renderImg(rightImg, int(windowsizeX / 2 - 25 + 100), int(windowsizeY / 2 - 25))


# pygame.display.update()

pygame.time.set_timer(
    pygame.USEREVENT + 1, 1000
)  # set a timer event to go off every 1000 ms (1 second)

crashed = False
# startscreen game loop
while not crashed:

    startSelectBlink(blink)  # every tick, check if you need to turn arrows off/on

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            exit()

        if event.type == pygame.USEREVENT + 1:  # every second
            blink *= -1  # , change sign of blink var. helps the startSelectBlink() func

        elif event.type == pygame.KEYDOWN:  # if any key pressed,
            gameDisplay.fill(black)
            crashed = True  # exit this game loop and go to the next one

    pygame.display.update()  # update whole screen
    clock.tick(60)  # 60 tps

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

renderTileX = 50
renderTileY = 50
for i in theMap:
    for j in i:
        for k in range(len(imagesDict)):
            renderImg(
                imagesDict[j], renderTileX, renderTileY
            )  # render correct image from theMap at x,y
        renderTileX += 50  # move over by 50
    renderTileY += 50  # go down by 50 and
    renderTileX = 50  # start again from left
pygame.display.update()

# player shenanigans
Apos = [1, 1]  # set starting position of player
renderImg(atImg, 50 + Apos[0] * 50, 50 + Apos[1] * 50)  # starting render of player
pygame.display.update()


def renderA(xOrY, direction):
    xChanged = 0
    yChanged = 0
    if xOrY == 0:
        xChanged = 1  # we're changing the xPos
    else:
        yChanged = 1  # we're changing the yPos
        # theMap[x][y] is [y][x] because nested arrays are hard
    if theMap[Apos[1] + yChanged * direction][Apos[0] + xChanged * direction] == ".":
        renderImg(dotImg, 50 + Apos[0] * 50, 50 + Apos[1] * 50)  # "cover up" original @
        Apos[xOrY] += direction  # change Apos
        renderImg(atImg, 50 + Apos[0] * 50, 50 + Apos[1] * 50)  # render new @
        pygame.display.update()


def moveUp():
    renderA(1, -1)


def moveLeft():
    renderA(0, -1)


def moveDown():
    renderA(1, 1)


def moveRight():
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

    clock.tick(60)  # 60 tps
