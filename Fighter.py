import numpy as np


class Fighter:
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
        emp = False
        x = 0
        y = 0
        while not emp:
            x = np.random.random_integers(5) - 1
            y = np.random.random_integers(5) - 1
            if self.__field[x, y] == '-':
                emp = True
        return np.array([x, y])
