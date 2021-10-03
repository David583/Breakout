import pygame

class Objects:
    def __init__(self, Game):
        self.buttonList = []
        self.mainMenu = 0
        self.levelSelect = 0
        self.levelSelectPage = 0
        self.levelList = []
        self.levelNameList = []
    class Button:
        def __init__(self, bgColor, sX, sY, pX, pY, e, t, Game):
            self.backgroundColor = bgColor
            self.sizeX = sX
            self.sizeY = sY
            self.positionX = pX
            self.positionY = pY
            self.eventOnClick = e
            self.textToDisplay = t
            self.textToRender = Game.GameScreen.font.render(self.textToDisplay, 1, pygame.Color(0, 0, 0))
            self.textPositionX = self.positionX + (self.sizeX - self.textToRender.get_width()) / 2
            self.textPositionY = self.positionY + (self.sizeY - self.textToRender.get_height()) / 2 

    class MainMenuPosition:
        def __init__(self, screenWidth, screenHeight):
            self.menuSizeX = int(screenWidth / 2)
            self.menuSizeY = int(screenHeight * 0.3)
            self.menuPositionX = int(screenWidth / 4)
            self.menuPositionY = int(screenHeight * 0.3)
            self.menuButtonSizeX = self.menuSizeX
            self.menuButtonSizeY = int(self.menuSizeY * 0.3)
            self.menuButtonDistance = int(self.menuSizeY * 0.1)
    
    class LevelSelectMenu:
        def __init__(self, screenWidth, screenHeight):
            self.levelList = []
            self.pageIndex = 0
            self.prevButtonPositionX = int(screenWidth * 0.02)
            self.prevButtonPositionY = int(screenHeight * 0.92)
            self.nextButtonPositionX = int(screenWidth * 0.83)
            self.nextButtonPositionY = self.prevButtonPositionY
            self.controlButtonSizeX = int(screenWidth * 0.15)
            self.controlButtonSizeY = int(screenHeight * 0.06)
            self.levelButtonDistance = int(screenHeight * 0.15)
            self.levelButtonSizeX = int(screenWidth * 0.96)
            self.levelButtonSizeY = int(screenHeight * 0.11)
            self.levelButtonPositionX = int(screenWidth * 0.02)
            self.levelButtonPositionY = int(screenHeight * 0.02)