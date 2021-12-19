from time import sleep

from ADB_server import ADB_server


class Bot:
    def __init__(self, port):
        self.ADB = ADB_server(port=port)

    def runBattleMode(self, mode=2):
        self.ADB.click(400, 630)
        sleep(0.5)
        if mode == 1:
            self.ADB.click(420, 400)
        else:
            self.ADB.click(420, 640)

    def runBattleGlobal(self):
        self.ADB.click(180, 630)

    def runBattleEvent(self):
        self.ADB.click(280, 720)

    def rewardLimit(self):
        self.ADB.click(276, 600)

    def getRewardChest(self, number):
        self.ADB.click(-25 + number * 120, 780)

    def openChest(self, number):
        self.ADB.click(-25 + number * 120, 780)
        sleep(0.5)
        self.ADB.click(276, 625)

    def returnHome(self):
        self.ADB.click(500, 920)
        sleep(0.5)
        self.ADB.click(220, 920)
        sleep(0.5)

    def goToClanChat(self):
        self.ADB.click(371, 911)

    def openCloseClanChat(self):
        self.ADB.click(490, 61)

    def requestCard(self):
        self.ADB.click(70, 805)

    def swipeRequestCard(self):
        self.ADB.swipe(250, 800, 250, 297)
        sleep(0.5)

    def goToEvents(self):
        self.ADB.click(520, 930)

    def goToDeck(self):
        self.ADB.click(168, 930)

    def goToShop(self):
        self.ADB.click(80, 930)

    def placingCard1X1(self, x, y):
        self.ADB.click(x, y)

    def placingCard2X2(self, x, y):
        self.ADB.click(x, y)

    def exitBatle2X2(self):
        self.ADB.click(74, 910)

    def closeChatBatle2X2(self):
        self.ADB.click(509, 30)

    def exitBatle1X1(self):
        self.ADB.click(270, 840)

    def selectCard(self, number):
        self.ADB.click(170 + number * 100, 850)

    def setEnglishLanguage(self):
        self.ADB.click(500, 100)
        sleep(0.5)
        self.ADB.click(325, 470)
        sleep(0.5)
        self.ADB.click(160, 570)
        sleep(0.5)
        self.ADB.click(275, 235)
        sleep(0.5)
        self.ADB.click(370, 590)

    def reboot(self):
        self.ADB.closeCR()
        sleep(2)
        self.ADB.openCR()

    def openCR(self):
        self.ADB.openCR()

    def closeCR(self):
        self.ADB.closeCR()

    def getScreen(self):
        return self.ADB.getScreen()
