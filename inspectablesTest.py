# figuring out how inspectables might work
# in main, make a function like text('') to put text under the map
# from there, i should be able to implement this inspectables thing.

from time import sleep

class inspectable:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def interact(self):
        print(self.desc)


class npc(inspectable):
    def __init__(self, name, desc, dialouge):
        super().__init__(name, desc)
        self.dialouge = dialouge
    def interact(self):
        print(self.desc)  # what they say
        sleep(0.5)
        print('\n')
        print(self.dialouge)  # what you say

hashtagImg = inspectable("#", "A wall")
atImg = inspectable("@", "Yourself. How did you get to see this?")
dotImg = inspectable(".", "You're looking at the floor lmao")
exclaimImg = 4
questionImg = 5
leftMoveImg = 6
rightMoveImg = 7
iImg = 8
startImg = 9
aImg =  npc("A","Hey there!","Hey to you too!")
inspectablesDict = {
    "#": hashtagImg,
    "@": atImg,
    ".": dotImg,
    "!": exclaimImg,
    "?": questionImg,
    "<": leftMoveImg,
    ">": rightMoveImg,
    "i": iImg,
    "A": aImg
}


# print(imagesDict["#"])
# inspectablesDict["#"].interact()
inspectablesDict["A"].interact()