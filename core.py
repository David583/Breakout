import pygame
import ctypes
import platform
from screen import *
from logic import *
from objects import *

if platform.system() == "Windows":
    ctypes.windll.user32.SetProcessDPIAware()

class Game():
    def __init__(self):
        pygame.init()
        self.fpsClock = pygame.time.Clock()
        self.backgroundColor = (0, 0, 0)
        self.playerColor = (255, 255, 255)
        self.ballColor = (127, 127, 127)
        self.GameScreen = Screen(self)
        self.GameLogic = Logic(self)
        self.GameObjects = Objects(self)
        self.GameLogic.InitGame(self)