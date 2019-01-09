import random


class Fighter_Idiot:
    def __init__(self, name, model_path):
        self.__name = name

    def loadPres(self, field, sign):
        self.__Field = field
        self.__sign = sign

    def getName(self):
        return self.__name

    def getSign(self):
        return self.__sign

    def loadStatus(self, status):
        self.status = status

    def makeStep(self):
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        if self.__Field[y][x] == " ":
            for i in range(0, 5):
                print(self.__Field[i])
            print('idiot')
            print(y, x)
            print(self.__Field[y][x])
            return (y, x)
        else:
            return self.makeStep()

