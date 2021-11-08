import pygame

class Objects:
    def __init__(self, Game):
        self.buttonList = []
        self.mainMenu = 0
        self.levelSelect = 0
        self.levelSelectPage = 0
        self.levelList = []
        self.builderLayout = 0
        self.levelSizeX = 10
        self.levelSizeY = 12
        self.level = [[0 for i in range(self.levelSizeX + 2)] for j in range(self.levelSizeY + 1)]
        self.ball

    class Button:
        def __init__(self, bgColor, sX, sY, pX, pY, e, t, d, Game):
            self.backgroundColor = bgColor
            self.sizeX = sX
            self.sizeY = sY
            self.positionX = pX
            self.positionY = pY
            self.eventOnClick = e
            self.textToDisplay = t
            self.extraData = d
            self.textToRender = Game.GameScreen.font.render(self.textToDisplay, 1, pygame.Color(0, 0, 0))
            self.textPositionX = int((self.sizeX - self.textToRender.get_width()) / 2 + self.positionX)
            self.textPositionY = int((self.sizeY - self.textToRender.get_height()) / 2 + self.positionY)

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
    
    class BuilderLayout:
        def __init__(self, Game):
            self.saveButtonPositionX = Game.GameScreen.screenInfo.extraSpaceX / 2
            self.saveButtonPositionY = (Game.GameObjects.levelSizeY + 5) * Game.GameScreen.screenInfo.objectHeight - 4 * Game.GameScreen.screenInfo.objectHeight
            self.exitButtonPositionX = Game.GameScreen.screenInfo.extraSpaceX / 2
            self.exitButtonPositionY = (Game.GameObjects.levelSizeY + 5) * Game.GameScreen.screenInfo.objectHeight - 2 * Game.GameScreen.screenInfo.objectHeight
            self.colorStartFieldX = Game.GameScreen.screenInfo.screenWidth - Game.GameScreen.screenInfo.extraSpaceX / 2 - Game.GameScreen.screenInfo.objectWidth
            self.colorStartFieldY = self.saveButtonPositionY
            self.blocksStartX = int(Game.GameScreen.screenInfo.screenWidth / 2) - 2 * Game.GameScreen.screenInfo.objectWidth
    
    class LevelStart:
        def __init__(self, Game):
            self.playerPositionX = Game.GameScreen.screenInfo.objectWidth * 4 + int(Game.GameScreen.screenInfo.objectWidth / 2)
            self.playerPositionY = Game.GameScreen.screenInfo.screenHeight - Game.GameScreen.screenInfo.objectHeight - Game.GameScreen.screenInfo.extraSpaceY
            self.ballPositionX = self.playerPositionX
            self.ballPositionY = self.Game.GameScreen.screenInfo.objectHeight * 10 + int(Game.GameScreen.screenInfo.objectWidth / 2)
            self.ballDirectionX = 0
            self.ballDirectionY = -0.01
            self.realBallPositionX = self.ballPositionX
            self.realBallPositionY = self.ballPositionY