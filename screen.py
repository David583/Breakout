import pygame

class Screen:
    def __init__(self, Game):
        self.fontSize = 0
        self.font = pygame.font.Font("gamefont.ttf", self.fontSize)
        self.mainCanvas = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h), pygame.NOFRAME)
        self.alpha = 0
        self.alphaCanvas = pygame.Surface((self.mainCanvas.get_width(), self.mainCanvas.get_height()))
        self.alphaIncrement = 0
        self.screenInfo = 0
        self.tileBackgroundColors = [(51, 51, 255), (255, 255, 255), (127, 127, 127), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 127, 0), (120, 20,255), (38, 255, 251), (210, 60, 255)]
    class ScreenInfo:
        def __init__(self, Game, scrW, scrH):
            self.screenWidth = scrW
            self.screenHeight = scrH
            self.objectWidth = int(self.screenWidth / Game.GameObjects.levelSizeX)
            self.objectHeight = int(self.screenHeight / (Game.GameObjects.levelSizeY + 5))
            self.extraSpaceX = self.screenWidth - Game.GameObjects.levelSizeX * self.objectWidth
            self.extraSpaceY = self.screenHeight - (Game.GameObjects.levelSizeY + 5) * self.objectHeight 

    def FadeIn(self, Game):
        Game.GameScreen.alphaIncrement = 7
        while (Game.GameScreen.alpha < 260):
            Game.GameScreen.DrawFrame(Game)
        pygame.event.clear()
    def FadeOut(self, Game):
        Game.GameScreen.alphaIncrement = -7
        while (Game.GameScreen.alpha > 0):
            Game.GameScreen.DrawFrame(Game)
        Game.GameScreen.alphaIncrement = 0
        pygame.event.clear()
    def DrawText(self, text, posX, posY, Game):
        SomeText = self.font.render(text, False, (0, 0, 0))
        Game.GameScreen.mainCanvas.blit(SomeText, (posX, posY))
    def DrawFrame(self, Game):
        Game.GameScreen.mainCanvas.fill(Game.backGroundColor)
        # Drawing buttons

        for i in range(len(Game.GameObjects.buttonList)):
            pygame.draw.rect(Game.GameScreen.mainCanvas, Game.GameObjects.buttonList[i].backgroundColor, pygame.Rect(Game.GameObjects.buttonList[i].positionX, Game.GameObjects.buttonList[i].positionY, Game.GameObjects.buttonList[i].sizeX, Game.GameObjects.buttonList[i].sizeY))
            pygame.draw.rect(Game.GameScreen.mainCanvas, (0, 0, 0), pygame.Rect(Game.GameObjects.buttonList[i].positionX, Game.GameObjects.buttonList[i].positionY, Game.GameObjects.buttonList[i].sizeX, Game.GameObjects.buttonList[i].sizeY), 2)
            Game.GameScreen.DrawText(Game.GameObjects.buttonList[i].textToDisplay, Game.GameObjects.buttonList[i].textPositionX, Game.GameObjects.buttonList[i].textPositionY, Game)
        
        # Draw game board

        if Game.GameLogic.gameMode != 0:
            for i in range(1, Game.GameObjects.levelSizeY + 1, 1):
                for j in range(1, Game.GameObjects.levelSizeX + 1, 1):
                    pygame.draw.rect(Game.GameScreen.mainCanvas, Game.GameScreen.tileBackgroundColors[Game.GameObjects.level[i][j]], pygame.Rect((j - 1) * Game.GameScreen.screenInfo.objectWidth, (i - 1) * Game.GameScreen.screenInfo.objectHeight, Game.GameScreen.screenInfo.objectWidth, Game.GameScreen.screenInfo.objectHeight))
        if Game.GameLogic.gameMode == 1:
            pass

        # Handle alpha

        if Game.GameScreen.alphaIncrement != 0:
            Game.GameScreen.alphaCanvas.set_alpha(Game.GameScreen.alpha)
            Game.GameScreen.alphaCanvas.fill((0,0,0))
            self.mainCanvas.blit(Game.GameScreen.alphaCanvas, (0, 0))
            Game.GameScreen.alpha = Game.GameScreen.alpha + Game.GameScreen.alphaIncrement

        pygame.display.update()
        Game.fpsClock.tick(60)
        # print(str(int(Game.fpsClock.get_fps())))