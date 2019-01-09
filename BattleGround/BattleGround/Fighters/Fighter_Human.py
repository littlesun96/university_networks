import random


class Fighter_Human:
    def __init__(self, name):
        self.__name = name

    def loadPres(self, field, sign):
        self.__field = field
        self.__sign = sign

    def getName(self):
        return self.__name

    def getSign(self):
        return self.__sign

    def makeStep(self):
        [y, x] = list(map(int, input("\nYour play as %s. Please type row and colomn num: " % self.__sign).split(" ")))
        isxNormal = 0 <= x < len(self.__field)
        isyNormal = 0 <= y < len(self.__field)
        if isxNormal and isyNormal and self.__field[y][x] == " ":
            return (y, x)
        else:
            print("Don't try to cheat!!!")
            return self.makeStep()
