import pygame

class Screen:
    def __init__(self, Game):
        self.fontSize = 0
        self.mainCanvas = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.alpha = 0
        self.alphaCanvas = pygame.Surface((self.mainCanvas.get_width(), self.mainCanvas.get_height()))
        self.alphaIncrement = 0
    class ScreenInfo:
        def __init__(self):
            self.objectWidth = 0
            self.objecHeight = 0
            self.screenWidth = 0
            self.screenHeight = 0

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
        font = pygame.font.SysFont("Trebuchet MS", 30)
        SomeText = font.render(text, False, (0, 0, 0))
        Game.GameScreen.mainCanvas.blit(SomeText, (posX, posY))
    def DrawFrame(self, Game):
        Game.GameScreen.mainCanvas.fill(Game.backGroundColor)
        # Drawing buttons

        for i in range(len(Game.GameObjects.buttonList)):
            pygame.draw.rect(Game.GameScreen.mainCanvas, Game.GameObjects.buttonList[i].backgroundColor, pygame.Rect(Game.GameObjects.buttonList[i].positionX, Game.GameObjects.buttonList[i].positionY, Game.GameObjects.buttonList[i].sizeX, Game.GameObjects.buttonList[i].sizeY))
            pygame.draw.rect(Game.GameScreen.mainCanvas, (0, 0, 0), pygame.Rect(Game.GameObjects.buttonList[i].positionX, Game.GameObjects.buttonList[i].positionY, Game.GameObjects.buttonList[i].sizeX, Game.GameObjects.buttonList[i].sizeY), 2)
            Game.GameScreen.DrawText(Game.GameObjects.buttonList[i].textToDisplay, Game.GameObjects.buttonList[i].textPositionX, Game.GameObjects.buttonList[i].textPositionY, Game)
        
        # Handle alpha

        if Game.GameScreen.alphaIncrement != 0:
            Game.GameScreen.alphaCanvas.set_alpha(Game.GameScreen.alpha)
            Game.GameScreen.alphaCanvas.fill((0,0,0))
            self.mainCanvas.blit(Game.GameScreen.alphaCanvas, (0, 0))
            Game.GameScreen.alpha = Game.GameScreen.alpha + Game.GameScreen.alphaIncrement

        pygame.display.update()
        Game.fpsClock.tick(60)
        # print(str(int(Game.fpsClock.get_fps())))