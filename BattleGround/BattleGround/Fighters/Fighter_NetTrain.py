import random
from Fighters.NetTrain import Net

class Fighter_NetTrain:
    def __init__(self, name, model_path):
        self.__name = name
        self.__model = Net(model_path)

    def loadPres(self, field, sign):
        self.__Field = field
        self.__sign = sign

    def getName(self):
        return self.__name

    def getSign(self):
        return self.__sign

    def loadStatus(self, status):
        self.__model.endGame(status)

    def makeStep(self):
        for i in range(0, 5):
            print(self.__Field[i])
        print('net')
        (y, x) = self.__model.makeStep(self.__Field, self.__sign)
        print(y, x)
        print(self.__Field[y][x])
        return (y, x)

