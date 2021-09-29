import pygame

class Logic:
    def __init__(self):
        self.isRunning = True
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
        Game.GameLogic.LoadMainMenu(Game, Game.GameObjects.mainMenu)
        Game.GameLogic.MainLoop(Game)

    def LoadMainMenu(self, Game, Menu):
        Game.GameObjects.buttonList.clear()
        Game.backGroundColor = (51, 51, 255)
        Game.GameObjects.buttonList.append(Game.GameObjects.Button(Menu.menuButtonSizeX, Menu.menuButtonSizeY, Menu.menuPositionX, Menu.menuPositionY, Game.GameLogic.LoadLevels, "Select level", "", Game))
        Game.GameObjects.buttonList.append(Game.GameObjects.Button(Menu.menuButtonSizeX, Menu.menuButtonSizeY, Menu.menuPositionX, Menu.menuPositionY + Menu.menuButtonDistance + Menu.menuButtonSizeY, Game.GameLogic.LoadEditor, "Level editor", "", Game))
        Game.GameObjects.buttonList.append(Game.GameObjects.Button(Menu.menuButtonSizeX, Menu.menuButtonSizeY, Menu.menuPositionX, Menu.menuPositionY +  2 * Menu.menuButtonDistance + 2 * Menu.menuButtonSizeY, Game.GameLogic.ExitGame, "Exit game", "", Game))

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
    def LoadLevels(self, Game):
        Game.GameScreen.FadeIn(Game)
    def LoadEditor(self, Game):
        print("Meow")
    def ExitGame(self, Game):
        self.isRunning = False