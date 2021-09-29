import pygame

class Objects:
    def __init__(self, Game):
        self.buttonList = []
        self.mainMenu = 0
    class Button:
        def __init__(self, sX, sY, pX, pY, e, t, i, Game):
            self.sizeX = sX
            self.sizeY = sY
            self.positionX = pX
            self.positionY = pY
            self.eventOnClick = e
            self.textToDisplay = t
            self.imageToDisplay = i
            self.textToRender = Game.GameScreen.font.render(self.textToDisplay, 1, pygame.Color(0, 0, 0))
            self.textPositionX = self.positionX + (self.sizeX - self.textToRender.get_width()) / 2
            self.textPositionY = self.positionY + (self.sizeY - self.textToRender.get_height()) / 2 

    class MainMenuPosition:
        def __init__(self, screenW, screenH):
            self.screenWidth = screenW
            self.screenHeight = screenH
            self.menuSizeX = int(self.screenWidth / 2)
            self.menuSizeY = int(self.screenHeight * 0.3)
            self.menuPositionX = int(self.screenWidth / 4)
            self.menuPositionY = int(self.screenHeight * 0.3)
            self.menuButtonSizeX = self.menuSizeX
            self.menuButtonSizeY = int(self.menuSizeY * 0.3)
            self.menuButtonDistance = int(self.menuSizeY * 0.1)