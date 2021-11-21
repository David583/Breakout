import tkinter
import pygame
import os
from tkinter.filedialog import asksaveasfile
from tkinter import colorchooser
from tkinter import messagebox

from pygame import time

class Logic:
    def __init__(self, Game):
        self.isRunning = True
        self.gameMode = 0 # 0 - Menus | 1 - Game | 2 - Level editor
        self.editOrPlay = 0   
        self.editOrPlayArray = [] # 0 - Load level for play | 1 - Load level for editing
        self.editTile = 0
        self.root = tkinter.Tk()
        self.root.withdraw()
    def InitGame(self, Game):      
        monitorInfo = pygame.display.Info()
        startScreenWidth = monitorInfo.current_w
        startScreenHeight = monitorInfo.current_h
        screenHeightArray = [0, 480, 768, 900, 1080, 1200, 1440, 1600, 2160, 9999]
        fontSizeArray = [16, 20, 24, 28, 32, 36, 40, 44]

        # Determining the best object sizes, depending on the screen size

        for i in range(1, 10, 1):
            if (startScreenHeight > screenHeightArray[i - 1] and startScreenHeight <= screenHeightArray[i]):

                # Determining best font size

                Game.GameScreen.fontSize = fontSizeArray[i - 1]
                Game.GameScreen.font = pygame.font.Font("gamefont.ttf", Game.GameScreen.fontSize)
                break
        
        # Determining Main Menu sizes, then load and start the main loop

        Game.GameScreen.screenInfo = Game.GameScreen.ScreenInfo(Game, startScreenWidth, startScreenHeight)
        Game.GameObjects.mainMenu = Game.GameObjects.MainMenuPosition(Game.GameScreen.screenInfo.screenWidth, Game.GameScreen.screenInfo.screenHeight)
        Game.GameObjects.levelSelect = Game.GameObjects.LevelSelectMenu(Game.GameScreen.screenInfo.screenWidth, Game.GameScreen.screenInfo.screenHeight)
        Game.GameLogic.LoadMainMenu(Game, Game.GameObjects.mainMenu)
        Game.GameObjects.builderLayout = Game.GameObjects.BuilderLayout(Game)
        Game.GameLogic.editOrPlayArray = [Game.GameLogic.LoadGame, Game.GameLogic.LoadEditor]
        Game.GameLogic.MainLoop(Game)
    def LoadMainMenu(self, Game, Menu):
        if Game.firstStart == 1:
            Game.GameScreen.FadeIn(Game)
        Game.GameObjects.buttonList.clear()
        Game.backGroundColor = (51, 51, 255)
        Game.GameScreen.tileBackgroundColors[0] = Game.backGroundColor
        Game.GameObjects.buttonList.append(Game.GameObjects.Button((18, 196, 196), Menu.menuButtonSizeX, Menu.menuButtonSizeY, Menu.menuPositionX, Menu.menuPositionY, Game.GameLogic.LoadLevels, "Select level", 0, Game))
        Game.GameObjects.buttonList.append(Game.GameObjects.Button((18, 196, 196), Menu.menuButtonSizeX, Menu.menuButtonSizeY, Menu.menuPositionX, Menu.menuPositionY + Menu.menuButtonDistance + Menu.menuButtonSizeY, Game.GameLogic.LoadLevels, "Level editor", 1, Game))
        Game.GameObjects.buttonList.append(Game.GameObjects.Button((18, 196, 196), Menu.menuButtonSizeX, Menu.menuButtonSizeY, Menu.menuPositionX, Menu.menuPositionY +  2 * Menu.menuButtonDistance + 2 * Menu.menuButtonSizeY, Game.GameLogic.ExitGame, "Exit game", "", Game))
        Game.GameLogic.gameMode = 0
        Game.firstStart = 1
        Game.GameScreen.FadeOut(Game)
    def MainLoop(self, Game):
        while Game.GameLogic.isRunning == True:
            Game.GameLogic.HandleEvents(Game)
            Game.GameScreen.DrawFrame(Game)
    def HandleEvents(self, Game):
        alreadyUsed = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                Game.GameLogic.LoadMainMenu(Game, Game.GameObjects.mainMenu)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                MousePosition = pygame.mouse.get_pos()
                for i in range(len(Game.GameObjects.buttonList)):
                    if (MousePosition[0] >= Game.GameObjects.buttonList[i].positionX and MousePosition[0] <= Game.GameObjects.buttonList[i].positionX + Game.GameObjects.buttonList[i].sizeX and MousePosition[1] >= Game.GameObjects.buttonList[i].positionY and MousePosition[1] <= Game.GameObjects.buttonList[i].positionY + Game.GameObjects.buttonList[i].sizeY):
                        Game.GameObjects.buttonList[i].eventOnClick(Game, Game.GameObjects.buttonList[i].extraData)
                        alreadyUsed = True
                        break
                if alreadyUsed == False and Game.GameLogic.gameMode == 2 and MousePosition[0] <= 10 * Game.GameScreen.screenInfo.objectWidth and MousePosition[1] <= 12 * Game.GameScreen.screenInfo.objectHeight:
                    Game.GameObjects.level[int(MousePosition[1] / Game.GameScreen.screenInfo.objectHeight) + 1][int(MousePosition[0] / Game.GameScreen.screenInfo.objectWidth) + 1] = Game.GameLogic.editTile
            if Game.GameLogic.gameMode == 1:
                MousePosition = pygame.mouse.get_pos()
                cursorPercentage = (MousePosition[0] * 100 / Game.GameScreen.screenInfo.screenWidth) / 100
                Game.GameObjects.levelData.playerPositionX = int(Game.GameObjects.levelData.avaliablePlayerSpace * cursorPercentage)
    def LoadLevels(self, Game, secondparam):
        Game.GameLogic.editOrPlay = secondparam
        Game.GameScreen.FadeIn(Game)
        Game.GameObjects.levelList.clear()
        Game.GameObjects.buttonList.clear()
        Game.GameObjects.buttonList.append(Game.GameObjects.Button((18, 196, 196), Game.GameObjects.levelSelect.controlButtonSizeX, Game.GameObjects.levelSelect.controlButtonSizeY, Game.GameObjects.levelSelect.prevButtonPositionX, Game.GameObjects.levelSelect.prevButtonPositionY, Game.GameLogic.LoadLevelsPrev, "Previous Page", "", Game))
        Game.GameObjects.buttonList.append(Game.GameObjects.Button((18, 196, 196), Game.GameObjects.levelSelect.controlButtonSizeX, Game.GameObjects.levelSelect.controlButtonSizeY, Game.GameObjects.levelSelect.nextButtonPositionX, Game.GameObjects.levelSelect.nextButtonPositionY, Game.GameLogic.LoadLevelsNext, "Next Page", "", Game))

        for file in os.listdir(os.path.join(os.path.dirname(__file__), "levels")):
            if file.endswith(".txt"):
                Game.GameObjects.levelList.append(file[:-4])
        
        Game.GameLogic.LoadLevelsCurrentIndex(Game)    
        Game.GameScreen.FadeOut(Game)
    def LoadLevelsNext(self, Game, secondparam):
        Game.GameObjects.levelSelectPage = Game.GameObjects.levelSelectPage + 1
        if (Game.GameObjects.levelSelectPage * 6 > len(Game.GameObjects.levelList)):
            Game.GameObjects.levelSelectPage = Game.GameObjects.levelSelectPage - 1
        Game.GameLogic.LoadLevelsCurrentIndex(Game)
    def LoadLevelsPrev(self, Game, secondparam):
        Game.GameObjects.levelSelectPage = Game.GameObjects.levelSelectPage - 1
        if (Game.GameObjects.levelSelectPage < 0):
            Game.GameObjects.levelSelectPage = 0
        Game.GameLogic.LoadLevelsCurrentIndex(Game)
    def LoadLevelsCurrentIndex(self, Game):
        while(len(Game.GameObjects.buttonList) != 2):
            Game.GameObjects.buttonList.pop()
        for i in range(6 * Game.GameObjects.levelSelectPage, 6 * Game.GameObjects.levelSelectPage + 6, 1):
            if i == len(Game.GameObjects.levelList):
                break
            Game.GameObjects.buttonList.append(Game.GameObjects.Button((240, 247, 139), Game.GameObjects.levelSelect.levelButtonSizeX, Game.GameObjects.levelSelect.levelButtonSizeY, Game.GameObjects.levelSelect.levelButtonPositionX, Game.GameObjects.levelSelect.levelButtonPositionY + (i % 6) * Game.GameObjects.levelSelect.levelButtonDistance, Game.GameLogic.editOrPlayArray[Game.GameLogic.editOrPlay], Game.GameObjects.levelList[i], Game.GameObjects.levelList[i], Game))
        if(Game.GameLogic.editOrPlay == 1):
            Game.GameObjects.buttonList.append(Game.GameObjects.Button((51, 237, 31), Game.GameObjects.levelSelect.controlButtonSizeX, Game.GameObjects.levelSelect.controlButtonSizeY, Game.GameScreen.screenInfo.screenWidth / 2 - Game.GameObjects.levelSelect.controlButtonSizeX / 2, Game.GameObjects.levelSelect.nextButtonPositionY, Game.GameLogic.LoadEditor, "New", "", Game))
    def LoadEditor(self, Game, secondparam):
        Game.GameScreen.FadeIn(Game)
        Game.GameObjects.buttonList.clear()
        Game.GameLogic.LoadLevel(Game, secondparam)
        bgcolor = Game.backGroundColor
        Game.GameObjects.buttonList.append(Game.GameObjects.Button((51, 237, 31), Game.GameScreen.screenInfo.objectWidth, Game.GameScreen.screenInfo.objectHeight, Game.GameObjects.builderLayout.saveButtonPositionX, Game.GameObjects.builderLayout.saveButtonPositionY, Game.GameLogic.SaveLevel, "Save", "",  Game))
        Game.GameObjects.buttonList.append(Game.GameObjects.Button((237, 21, 31), Game.GameScreen.screenInfo.objectWidth, Game.GameScreen.screenInfo.objectHeight, Game.GameObjects.builderLayout.exitButtonPositionX, Game.GameObjects.builderLayout.exitButtonPositionY, Game.GameLogic.LoadMainMenu, "Exit", Game.GameObjects.mainMenu,  Game))
        Game.GameObjects.buttonList.append(Game.GameObjects.Button(Game.playerColor, Game.GameScreen.screenInfo.objectWidth, Game.GameScreen.screenInfo.objectHeight, Game.GameObjects.builderLayout.colorStartFieldX, Game.GameObjects.builderLayout.colorStartFieldY, Game.GameLogic.SelectColor, "", 2, Game))
        Game.GameObjects.buttonList.append(Game.GameObjects.Button(Game.ballColor, Game.GameScreen.screenInfo.objectWidth, Game.GameScreen.screenInfo.objectHeight, Game.GameObjects.builderLayout.colorStartFieldX, Game.GameObjects.builderLayout.colorStartFieldY + Game.GameScreen.screenInfo.objectHeight, Game.GameLogic.SelectColor, "", 3, Game))
        Game.GameObjects.buttonList.append(Game.GameObjects.Button(bgcolor, Game.GameScreen.screenInfo.objectWidth, Game.GameScreen.screenInfo.objectHeight, Game.GameObjects.builderLayout.colorStartFieldX, Game.GameObjects.builderLayout.colorStartFieldY + 2 * Game.GameScreen.screenInfo.objectHeight, Game.GameLogic.SelectColor, "", 4, Game))
        for i in range(3):
            for j in range(4):
                Game.GameObjects.buttonList.append(Game.GameObjects.Button(Game.GameScreen.tileBackgroundColors[4 * i + j], Game.GameScreen.screenInfo.objectWidth, Game.GameScreen.screenInfo.objectHeight, Game.GameObjects.builderLayout.blocksStartX + j * Game.GameScreen.screenInfo.objectWidth, (Game.GameObjects.levelSizeY + 1) * Game.GameScreen.screenInfo.objectHeight + Game.GameScreen.screenInfo.objectHeight * i, Game.GameLogic.SetTile, "", 4 * i + j, Game))
        Game.backGroundColor = (51, 51, 255)
        Game.GameLogic.gameMode = 2
        Game.GameScreen.FadeOut(Game)   
    def SetTile(self, Game, secondparam):
        Game.GameLogic.editTile = secondparam
    def SelectColor(self, Game, secondParam):
        textList = ["Válaszd ki a játékos színét!", "Válaszd ki a labda színét!", "Válaszd ki a háttér színét!"]
        usedIndex = secondParam - 2
        color = colorchooser.askcolor(title = textList[usedIndex])
        if color[0] is not None:
            Game.GameObjects.buttonList[secondParam].backgroundColor = (int(color[0][0]), int(color[0][1]), int(color[0][2]))
    def LoadLevel(self, Game, secondparam):
        for i in range(Game.GameObjects.levelSizeY + 1):
            for j in range(Game.GameObjects.levelSizeX + 2):
                if (i == 0):
                    Game.GameObjects.level[i][j] = 3
                else:
                    Game.GameObjects.level[i][j] = 0
        if secondparam != "":
            for i in range(len(Game.GameObjects.levelList)):
                if (Game.GameObjects.levelList[i] == secondparam):
                    f = open(os.path.join(os.path.dirname(__file__), "levels", Game.GameObjects.levelList[i] + ".txt"))
                    Game.playerColor = tuple(map(int, f.readline().strip().split(',')))
                    Game.ballColor = tuple(map(int, f.readline().strip().split(',')))
                    Game.backGroundColor = tuple(map(int, f.readline().strip().split(',')))
                    for x in range(12):
                        row = f.readline().strip().split(' ')
                        for y in range(10):
                            Game.GameObjects.level[x + 1][y + 1] = int(row[y])
                    break           
    def SaveLevel(self, Game, secondparam):
        file = [('Text Document', '*.txt')]
        fileAsk = asksaveasfile(filetypes = file, defaultextension = file, initialdir = os.path.join(os.path.dirname(__file__), "levels"))
        f = open(fileAsk.name, "w")
        f.write(str(Game.GameObjects.buttonList[2].backgroundColor[0]) + "," + str(Game.GameObjects.buttonList[2].backgroundColor[1]) + "," + str(Game.GameObjects.buttonList[2].backgroundColor[2]) + "\n")
        f.write(str(Game.GameObjects.buttonList[3].backgroundColor[0]) + "," + str(Game.GameObjects.buttonList[3].backgroundColor[1]) + "," + str(Game.GameObjects.buttonList[3].backgroundColor[2]) + "\n")
        f.write(str(Game.GameObjects.buttonList[4].backgroundColor[0]) + "," + str(Game.GameObjects.buttonList[4].backgroundColor[1]) + "," + str(Game.GameObjects.buttonList[4].backgroundColor[2]) + "\n")
        for x in range(12):
            for y in range(10):
                f.write(str(Game.GameObjects.level[x + 1][y + 1]) + " ")
            f.write("\n")
        f.close()
    def LoadGame(self, Game, secondparam):
        Game.GameScreen.FadeIn(Game)
        Game.GameObjects.buttonList.clear()
        Game.GameObjects.levelData = Game.GameObjects.LevelStart(Game)
        Game.GameLogic.LoadLevel(Game, secondparam)
        for y in range(1, Game.GameObjects.levelSizeY, 1):
            for x in range(1, Game.GameObjects.levelSizeX, 1):
                if (Game.GameObjects.level[y][x] != 0 and Game.GameObjects.level[y][x] != 3):
                    Game.GameObjects.levelData.numberOfTiles = Game.GameObjects.levelData.numberOfTiles + 1
        Game.GameScreen.tileBackgroundColors[0] = Game.backGroundColor
        Game.GameLogic.gameMode = 1
        Game.GameScreen.FadeOut(Game)
        Game.GameObjects.levelData.ballDirectionY = 4
    def MoveBall(self, Game):
        Game.GameObjects.levelData.ballPositionX = Game.GameObjects.levelData.ballPositionX + Game.GameObjects.levelData.ballDirectionX
        Game.GameObjects.levelData.ballPositionY = Game.GameObjects.levelData.ballPositionY + Game.GameObjects.levelData.ballDirectionY
        # Check for player collision
        if (Game.GameObjects.levelData.ballPositionY + Game.GameObjects.levelData.ballSize / 2 > Game.GameObjects.levelData.playerPositionY):
            if (Game.GameObjects.levelData.ballPositionX >= Game.GameObjects.levelData.playerPositionX - 10 and Game.GameObjects.levelData.playerPositionX + Game.GameScreen.screenInfo.objectWidth + 10 >= Game.GameObjects.levelData.ballPositionX):
                Game.GameObjects.levelData.ballDirectionY = Game.GameObjects.levelData.ballDirectionY * -1
                Game.GameObjects.levelData.ballCheckTileY = Game.GameObjects.levelData.ballCheckTileY + (-2 * Game.GameObjects.levelData.ballCheckTileY)
                collisionPointSize = Game.GameObjects.levelData.ballPositionX - Game.GameObjects.levelData.playerPositionX
                collisionPointPerc = int(collisionPointSize * 100 / Game.GameScreen.screenInfo.objectWidth)
                Game.GameObjects.levelData.ballDirectionX = round(8 * collisionPointPerc / 100, 2) - 4
                if (Game.GameObjects.levelData.ballDirectionX < 0):
                    Game.GameObjects.levelData.ballCheckTileX = -1
                else:
                    Game.GameObjects.levelData.ballCheckTileX = 1
            else:
                Game.GameLogic.gameMode = 0
                messagebox.showinfo(title = "Bruh!", message = "Ezt próbáld újra!")
                Game.GameLogic.LoadMainMenu(Game, Game.GameObjects.mainMenu)

        ballArrayX = int(Game.GameObjects.levelData.ballPositionX / Game.GameScreen.screenInfo.objectWidth) + 1
        ballArrayY = int(Game.GameObjects.levelData.ballPositionY / Game.GameScreen.screenInfo.objectHeight) + 1
        ballInTileX = Game.GameObjects.levelData.ballPositionX % Game.GameScreen.screenInfo.objectWidth
        ballInTileY = Game.GameObjects.levelData.ballPositionY % Game.GameScreen.screenInfo.objectHeight
        # Check up or down
        if (ballArrayY + Game.GameObjects.levelData.ballCheckTileY < 13 and Game.GameObjects.level[ballArrayY + Game.GameObjects.levelData.ballCheckTileY][ballArrayX] != 0 and ballInTileY >= Game.GameObjects.levelData.ballTileArrayY[2 * (Game.GameObjects.levelData.ballCheckTileY + 1)] and ballInTileY <= Game.GameObjects.levelData.ballTileArrayY[2 * (Game.GameObjects.levelData.ballCheckTileY + 1) + 1]):
            Game.GameLogic.Collision(Game, ballArrayY + Game.GameObjects.levelData.ballCheckTileY, ballArrayX)
            Game.GameObjects.levelData.ballDirectionY = Game.GameObjects.levelData.ballDirectionY * -1
            Game.GameObjects.levelData.ballCheckTileY = Game.GameObjects.levelData.ballCheckTileY + (-2 * Game.GameObjects.levelData.ballCheckTileY)
        # Check left or right
        if (ballArrayY + Game.GameObjects.levelData.ballCheckTileY < 12 and Game.GameObjects.level[ballArrayY][ballArrayX + Game.GameObjects.levelData.ballCheckTileX] != 0 and ballInTileX >= Game.GameObjects.levelData.ballTileArrayX[2 * (Game.GameObjects.levelData.ballCheckTileX + 1)] and ballInTileX <= Game.GameObjects.levelData.ballTileArrayX[2 * (Game.GameObjects.levelData.ballCheckTileX + 1) + 1]):
            Game.GameLogic.Collision(Game, ballArrayY, ballArrayX + Game.GameObjects.levelData.ballCheckTileX)
            Game.GameObjects.levelData.ballDirectionX = Game.GameObjects.levelData.ballDirectionX * -1
            Game.GameObjects.levelData.ballCheckTileX = Game.GameObjects.levelData.ballCheckTileX + (-2 * Game.GameObjects.levelData.ballCheckTileX)
        # Check sides
        if (Game.GameObjects.levelData.ballPositionX < int(Game.GameObjects.levelData.ballSize / 2)):  
            Game.GameObjects.levelData.ballDirectionX = Game.GameObjects.levelData.ballDirectionX * -1
            Game.GameObjects.levelData.ballPositionX = int(Game.GameObjects.levelData.ballSize / 2)
            Game.GameObjects.levelData.ballCheckTileX = Game.GameObjects.levelData.ballCheckTileY + (-2 * Game.GameObjects.levelData.ballCheckTileY)
        if(Game.GameObjects.levelData.ballPositionX > Game.GameScreen.screenInfo.screenWidth - Game.GameScreen.screenInfo.extraSpaceX - int(Game.GameObjects.levelData.ballSize / 2)):
            Game.GameObjects.levelData.ballDirectionX = Game.GameObjects.levelData.ballDirectionX * -1
            Game.GameObjects.levelData.ballPositionX = Game.GameScreen.screenInfo.screenWidth - Game.GameScreen.screenInfo.extraSpaceX - int(Game.GameObjects.levelData.ballSize / 2)
            Game.GameObjects.levelData.ballCheckTileX = Game.GameObjects.levelData.ballCheckTileY + (-2 * Game.GameObjects.levelData.ballCheckTileY)
    def Collision(self, Game, Y, X):
        if (Game.GameObjects.level[Y][X] != 3):
            if (Game.GameObjects.level[Y][X] == 2):
                Game.GameObjects.level[Y][X] = 1
            else:
                Game.GameObjects.level[Y][X] = 0
                Game.GameObjects.levelData.numberOfTiles = Game.GameObjects.levelData.numberOfTiles - 1
                if (Game.GameObjects.levelData.numberOfTiles == 0):
                    Game.GameLogic.gameMode = 0
                    messagebox.showinfo(title = "Gratula!", message = "Kivitted ezt a pályát!")
                    Game.GameLogic.LoadMainMenu(Game, Game.GameObjects.mainMenu)
    def ExitGame(self, Game, secondparam):
        self.isRunning = False