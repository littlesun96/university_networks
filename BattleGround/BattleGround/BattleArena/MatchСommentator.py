import numpy
from beautifultable import BeautifulTable

from BattleArena.Structs import SessionScore


class MatchCommentator:
    def __init__(self, commentPartys):
        self.commentPartys = commentPartys

    def loadNewParty(self, FighterList, Field):
        self.FighterList = FighterList
        self.Field = Field

    def showPartyNum(self, num):
        if self.commentPartys:
            print("\nParty № %i" % num)

    def showPartyStep(self, step):
        if self.commentPartys:
            print("\nStep: %i" % step)
            Map = BeautifulTable()
            for i in range(len(self.Field)):
                Map.append_row(self.Field[i])
            print(Map)

    def showResults(self, PatryList):
        PlayersDict = self.__calcResults(PatryList)
        for playerName in PlayersDict.keys():
            Scores = PlayersDict[playerName]
            print("Player: %s\n"
                  "Score: %s\n"
                  "Wins: %s\n"
                  "Draws: %s\n"
                  "Loses: %s\n" %
                  (playerName, Scores.score, Scores.wins, Scores.draws, Scores.loses))

    def __calcResults(self, PatryList):
        PlayersDict = {PatryList[0].player1: SessionScore(),
                       PatryList[0].player2: SessionScore()}
        for party in PatryList:
            for playerName in PlayersDict.keys():
                if party.winner is None:
                    PlayersDict[playerName].addDraw()
                else:
                    if playerName == party.winner:
                        PlayersDict[playerName].addWin(party.step,)
                    else:
                        PlayersDict[playerName].addLose(party.step)
        return PlayersDict
