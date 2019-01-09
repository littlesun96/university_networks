from BattleArena.Structs import PartyStruct
from BattleArena.MatchСommentator import MatchCommentator
from BattleArena.WinChecker import WinCheker
from Fighters.Fighter_Human import Fighter_Human


class BattleArena:
    def __init__(self, Fighter1, Fighter2, commentParties=False):
        self.Fighters = [Fighter1, Fighter2]
        for fighter in self.Fighters:
            if type(fighter) == type(Fighter_Human("Check")):
                commentParties = True
        self.WinChekerExmpl = WinCheker()
        self.YourComenatator = MatchCommentator(commentParties)

    def playBattles(self, num, fieldSize=5):
        PatryList = []
        for partyNum in range(1, num + 1):
            self.__prepareForBattle(fieldSize)
            self.YourComenatator.showPartyNum(partyNum)
            PatryList.append(self.__playSingleBattle(fieldSize))
            self.Fighters.reverse()
        self.YourComenatator.showResults(PatryList)

    def __prepareForBattle(self, fieldSize):
        fighterSigns = ["x", "0"]
        self.BattleField = []
        for i in range(fieldSize):
            self.BattleField.append([' '] * fieldSize)
        for i, sign in enumerate(fighterSigns):
            self.Fighters[i].loadPres(self.BattleField, sign)
        self.YourComenatator.loadNewParty(self.Fighters, self.BattleField)

    def __playSingleBattle(self, fieldSize):
        hasWinner = False
        player = 1
        step = 0
        while step < fieldSize ** 2 and not hasWinner:
            step += 1
            player = (player + 1) % 2
            hasWinner = self.__makeStep(player)
            self.YourComenatator.showPartyStep(step)
        if hasWinner:
            winnerName = self.Fighters[player].getName()
            self.Fighters[player].loadStatus(1)
            player = (player + 1) % 2
            self.Fighters[player].loadStatus(-1)
        else:
            winnerName = None
            self.Fighters[player].loadStatus(0)
            player = (player + 1) % 2
            self.Fighters[player].loadStatus(0)
        return PartyStruct(player1=self.Fighters[0].getName(), player2=self.Fighters[1].getName(),
                           winner=winnerName, field=self.BattleField.copy(), step=step)

    def __makeStep(self, fighterNum):
        cords = self.Fighters[fighterNum].makeStep()
        sign = self.Fighters[fighterNum].getSign()
        self.BattleField[cords[0]][cords[1]] = sign
        return self.WinChekerExmpl.checkWin(self.BattleField, sign)



