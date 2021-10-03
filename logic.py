import pygame
import os

class Logic:
    def __init__(self):
        self.isRunning = True
        self.gameMode = 0 # 0 - Menus | 1 - Game | 2 - Level editor
    def InitGame(self, Game):      
        monitorInfo = pygame.display.Info()
        startScreenWidth = monitorInfo.current_w
        startScreenHeight = monitorInfo.current_h
        screenWidthArray =  [0, 640, 1366, 1600, 1920, 1920, 2560, 2560, 3840, 9999]
        objectsWidthArray = [25, 40, 60, 70, 80, 100, 100, 150]
        screenHeightArray = [0, 480, 768, 900, 1080, 1200, 1440, 1600, 2160, 9999]
        objectsHeightArray = [20, 30, 40, 50, 50, 70, 70, 100]
        fontSizeArray = [16, 20, 24, 28, 32, 36, 40, 44]
        bestWidthIndex = 0
        bestHeightIndex = 0

        # Determining the best object sizes, depending on the screen size

        for i in range(1, 10, 1):
            if (startScreenWidth > screenWidthArray[i - 1] and startScreenWidth <= screenWidthArray[i]):
                bestWidthIndex = i - 1
                break
        for i in range(1, 10, 1):
            if (startScreenHeight > screenHeightArray[i - 1] and startScreenHeight <= screenHeightArray[i]):
                bestHeightIndex = i - 1

                # Determining best font size

                Game.GameScreen.fontSize = fontSizeArray[i - 1]
                Game.GameScreen.font = pygame.font.Font("gamefont.ttf", Game.GameScreen.fontSize)
                break
        Game.setScreenInfo(objectsWidthArray[bestWidthIndex], objectsHeightArray[bestHeightIndex], startScreenWidth, startScreenHeight)

        # Determining Main Menu sizes, then load and start the main loop

        Game.GameObjects.mainMenu = Game.GameObjects.MainMenuPosition(Game.getScreenInfo().screenWidth, Game.getScreenInfo().screenHeight)
        Game.GameObjects.levelSelect = Game.GameObjects.LevelSelectMenu(Game.getScreenInfo().screenWidth, Game.getScreenInfo().screenHeight)
        Game.GameLogic.LoadMainMenu(Game, Game.GameObjects.mainMenu)
        Game.GameLogic.MainLoop(Game)

    def LoadMainMenu(self, Game, Menu):
        Game.GameObjects.buttonList.clear()
        Game.backGroundColor = (51, 51, 255)
        Game.GameObjects.buttonList.append(Game.GameObjects.Button((18, 196, 196), Menu.menuButtonSizeX, Menu.menuButtonSizeY, Menu.menuPositionX, Menu.menuPositionY, Game.GameLogic.LoadLevels, "Select level", Game))
        Game.GameObjects.buttonList.append(Game.GameObjects.Button((18, 196, 196), Menu.menuButtonSizeX, Menu.menuButtonSizeY, Menu.menuPositionX, Menu.menuPositionY + Menu.menuButtonDistance + Menu.menuButtonSizeY, Game.GameLogic.LoadEditor, "Level editor", Game))
        Game.GameObjects.buttonList.append(Game.GameObjects.Button((18, 196, 196), Menu.menuButtonSizeX, Menu.menuButtonSizeY, Menu.menuPositionX, Menu.menuPositionY +  2 * Menu.menuButtonDistance + 2 * Menu.menuButtonSizeY, Game.GameLogic.ExitGame, "Exit game", Game))

    def MainLoop(self, Game):
        while Game.GameLogic.isRunning == True:
            Game.GameLogic.HandleEvents(Game)
            Game.GameScreen.DrawFrame(Game)
    def HandleEvents(self, Game):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                Game.GameLogic.isRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                MousePosition = pygame.mouse.get_pos()
                for i in range(len(Game.GameObjects.buttonList)):
                    if (MousePosition[0] >= Game.GameObjects.buttonList[i].positionX and MousePosition[0] <= Game.GameObjects.buttonList[i].positionX + Game.GameObjects.buttonList[i].sizeX and MousePosition[1] >= Game.GameObjects.buttonList[i].positionY and MousePosition[1] <= Game.GameObjects.buttonList[i].positionY + Game.GameObjects.buttonList[i].sizeY):
                        Game.GameObjects.buttonList[i].eventOnClick(Game)
                        break
    def LoadLevels(self, Game):
        Game.GameScreen.FadeIn(Game)
        Game.GameObjects.buttonList.clear()
        Game.GameObjects.buttonList.append(Game.GameObjects.Button((18, 196, 196), Game.GameObjects.levelSelect.controlButtonSizeX, Game.GameObjects.levelSelect.controlButtonSizeY, Game.GameObjects.levelSelect.prevButtonPositionX, Game.GameObjects.levelSelect.prevButtonPositionY, Game.GameLogic.LoadLevelsPrev, "Previous Page", Game))
        Game.GameObjects.buttonList.append(Game.GameObjects.Button((18, 196, 196), Game.GameObjects.levelSelect.controlButtonSizeX, Game.GameObjects.levelSelect.controlButtonSizeY, Game.GameObjects.levelSelect.nextButtonPositionX, Game.GameObjects.levelSelect.nextButtonPositionY, Game.GameLogic.LoadLevelsNext, "Next Page", Game))

        for file in os.listdir(os.path.join(os.path.dirname(__file__), "levels")):
            if file.endswith(".txt"):
                Game.GameObjects.levelList.append(file)
                f = open(os.path.join(os.path.dirname(__file__), "levels", file))
                Game.GameObjects.levelNameList.append(f.readline().strip())
                f.close()
        
        Game.GameLogic.LoadLevelsCurrentIndex(Game)    
        Game.GameScreen.FadeOut(Game)

    def LoadLevelsNext(self, Game):
        Game.GameObjects.levelSelectPage = Game.GameObjects.levelSelectPage + 1
        if (Game.GameObjects.levelSelectPage * 6 > len(Game.GameObjects.levelList)):
            Game.GameObjects.levelSelectPage = Game.GameObjects.levelSelectPage - 1
        Game.GameLogic.LoadLevelsCurrentIndex(Game)
    def LoadLevelsPrev(self, Game):
        Game.GameObjects.levelSelectPage = Game.GameObjects.levelSelectPage - 1
        if (Game.GameObjects.levelSelectPage < 0):
            Game.GameObjects.levelSelectPage = 0
        Game.GameLogic.LoadLevelsCurrentIndex(Game)

    def LoadEditor(self, Game):
        print("Meow")
    def LoadLevelsCurrentIndex(self, Game):
        while(len(Game.GameObjects.buttonList) != 2):
            Game.GameObjects.buttonList.pop()
        for i in range(6 * Game.GameObjects.levelSelectPage, 6 * Game.GameObjects.levelSelectPage + 6, 1):
            if i == len(Game.GameObjects.levelList):
                break
            Game.GameObjects.buttonList.append(Game.GameObjects.Button((240, 247, 139), Game.GameObjects.levelSelect.levelButtonSizeX, Game.GameObjects.levelSelect.levelButtonSizeY, Game.GameObjects.levelSelect.levelButtonPositionX, Game.GameObjects.levelSelect.levelButtonPositionY + (i % 6) * Game.GameObjects.levelSelect.levelButtonDistance, Game.GameLogic.LoadEditor, Game.GameObjects.levelNameList[i], Game))

    def ExitGame(self, Game):
        self.isRunning = False