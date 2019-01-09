class WinCheker:
    def __init__(self):
        self.SIGNS_IN_LINE_FOR_WIN = 4

    def checkWin(self, BattleField, sign):
        hasWinner = False
        winRes = sign * 4
        hasWinner = hasWinner or self.__winVertOrHor(BattleField, winRes)
        hasWinner = hasWinner or self.__winDiag(BattleField, winRes)
        return hasWinner

    def __winVertOrHor(self, BattleField, winRes):
        for i in range(2):
            for j in range(5):
                verLine = ""
                horLine = ""
                for k in range(self.SIGNS_IN_LINE_FOR_WIN):
                    verLine += BattleField[i + k][j]
                    horLine += BattleField[j][i + k]
                if winRes == verLine or winRes == horLine:
                    return True
        return False

    def __winDiag(self, BattleField, winRes):
        availableVariants = len(BattleField) - self.SIGNS_IN_LINE_FOR_WIN + 1
        for i in range(availableVariants):
            for j in range(availableVariants):
                mainDiag = ""
                fakeDiag = ""
                for k in range(self.SIGNS_IN_LINE_FOR_WIN):
                    mainDiag += BattleField[i + k][j + k]
                    fakeDiag += BattleField[(len(BattleField) - 1) - (i + k)][j + k]
                if winRes == mainDiag or winRes == fakeDiag:
                    return True
        return False