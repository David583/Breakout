import pygame
import ctypes
from screen import *
from logic import *
from objects import *

ctypes.windll.user32.SetProcessDPIAware()

class Game():
    def __init__(self):
        pygame.init()
        self.fpsClock = pygame.time.Clock()
        self.backGroundColor = (0, 0, 0)
        self.GameScreen = Screen(self)
        self.GameLogic = Logic()
        self.GameObjects = Objects(self)
        self.GameLogic.InitGame(self)

    def getScreenInfo(self):
       return self.GameScreen.ScreenInfo
    def setScreenInfo(self, objW, objH, scrW, scrH):
        self.GameScreen.ScreenInfo.objectWidth = objW
        self.GameScreen.ScreenInfo.objecHeight = objH
        self.GameScreen.ScreenInfo.screenWidth = scrW
        self.GameScreen.ScreenInfo.screenHeight = scrH