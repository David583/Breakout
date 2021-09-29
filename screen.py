import pygame

class Screen:
    def __init__(self, Game):
        self.fontSize = 0
        self.mainCanvas = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    class ScreenInfo:
        def __init__(self):
            self.objectWidth = 0
            self.objecHeight = 0
            self.screenWidth = 0
            self.screenHeight = 0

    def FadeIn(self, Game):
        alpha = 0
        alphaCanvas = pygame.Surface((self.mainCanvas.get_width(), self.mainCanvas.get_height()))
        alphaCanvas.set_alpha(0)
        alphaCanvas.fill((0,0,0))
        while(alpha < 260):
            self.mainCanvas.blit(alphaCanvas, (0, 0))
            alphaCanvas.set_alpha(alpha)
            pygame.display.update()
            Game.fpsClock.tick(60)
            alpha = alpha + 7
        pygame.event.clear()
    def FadeOut(self):
        return
    def DrawText(self, text, posX, posY, Game):
        font = pygame.font.SysFont("Trebuchet MS", 30)
        SomeText = font.render(text, False, (0, 0, 0))
        Game.GameScreen.mainCanvas.blit(SomeText, (posX, posY))
    def DrawFrame(self, Game):
        Game.GameScreen.mainCanvas.fill(Game.backGroundColor)
        # Drawing buttons

        for i in range(len(Game.GameObjects.buttonList)):
            if (Game.GameObjects.buttonList[i].imageToDisplay == ""):
                pygame.draw.rect(Game.GameScreen.mainCanvas, (18, 196, 196), pygame.Rect(Game.GameObjects.buttonList[i].positionX, Game.GameObjects.buttonList[i].positionY, Game.GameObjects.buttonList[i].sizeX, Game.GameObjects.buttonList[i].sizeY))
                pygame.draw.rect(Game.GameScreen.mainCanvas, (0, 0, 0), pygame.Rect(Game.GameObjects.buttonList[i].positionX, Game.GameObjects.buttonList[i].positionY, Game.GameObjects.buttonList[i].sizeX, Game.GameObjects.buttonList[i].sizeY), 2)
                Game.GameScreen.DrawText(Game.GameObjects.buttonList[i].textToDisplay, Game.GameObjects.buttonList[i].textPositionX, Game.GameObjects.buttonList[i].textPositionY, Game)
        
        pygame.display.update()
        Game.fpsClock.tick(60)
        # print(str(int(Game.fpsClock.get_fps())))