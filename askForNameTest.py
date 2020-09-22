import pygame

# imported string below

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


def putTextCenter(text, x, y):  # put text somewhere; specify x and y for topleft corner
    text = comicSansFont.render(text, True, white, black)
    textRect = text.get_rect()
    textRect.center = (x, y)
    gameDisplay.blit(text, textRect)
    pygame.display.update()


def printText(text):  # put text under the map.
    text = comicSansFont.render(text, True, white, black)
    textRect = text.get_rect()
    textRect.topleft = (400, 0)
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

name = ""


def updateName(text):
    global name
    gameDisplay.fill(black)
    name += text
    putTextCenter(name, windowsizeX / 2, windowsizeY / 2)


import string

crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            exit()

        elif event.type == pygame.KEYDOWN:  # if any key pressed,
            if pygame.key.name(event.key).lower() in string.ascii_lowercase:
                updateName(pygame.key.name(event.key).lower())
            if pygame.key.name(event.key).lower() == "return":
                crashed = True
                exit()
    clock.tick(60)
    pygame.display.update()
