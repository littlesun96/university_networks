from keras.models import load_model
import os
import numpy as np
import matplotlib.pyplot as plt


class Dataset:
    def __init__(self):
        self.X = np.empty((0, 25))
        self.Y = np.empty((0, 25))

    def addData(self, x, y):
        self.X = np.append(self.X, x, axis=0)
        self.Y = np.append(self.Y, y, axis=0)
        # print(y)
        # print(self.X.shape)
        # print(self.Y.size)


class Step:
    def __init__(self, field, qvalue, probs, y, x):
        self.field = field
        self.qvalue = qvalue
        self.probs = probs
        self.y = y
        self.x = x


class Game:
    def __init__(self):
        self.status = None
        self.steps = []

    def addStep(self, field, qvalue, probs, y, x):
        self.steps.append(Step(field, qvalue, probs, y, x))


class Net:

    def __init__(self, model_path):
        print(os.path.abspath(__file__))
        self.model_path = model_path
        self.model = load_model(self.model_path)
        self.game_list = []
        self.current_game = Game()
        self.dataset = Dataset()
        self.reward = [1, 0.9, 0.8, 0.6, 0.3]

    def endGame(self, status):
        print('END GAME')
        self.current_game.status = status
        self.game_list.append(self.current_game)
        self.current_game = Game()
        self.check_train()

    def addData(self):
        print('ADD DATA')
        for game in self.game_list:
            game.steps.reverse()
            # print(len(game.steps))
            # y = np.zeros(1, 25)
            if game.status == 0:
                for i in range(0, 2):
                    step = game.steps[i]
                    unique, counts = np.unique(game.steps[i].field, return_counts=True)
                    # print(unique)
                    # print(counts)
                    # print(game.steps[i].field)
                    label = np.zeros((1, 25))
                    label[0][step.y*4 + step.x] = self.reward[i + 3]
                    self.dataset.addData(step.field, label)
                continue

            for i in range(0, 5):
                if i > len(game.steps) - 1:
                    continue
                step = game.steps[i]
                unique, counts = np.unique(game.steps[i].field, return_counts=True)
                # print(unique)
                # print(counts)
                # print(game.steps[i].field)
                label = np.zeros((1, 25))
                if game.status == 1:
                    label[0][step.y * 5 + step.x] = self.reward[i]
                else:
                    label[0][step.y * 5 + step.x] = -self.reward[i]
                self.dataset.addData(step.field, label)

        self.game_list.clear()

    def check_train(self):
        print('CHECK TRAIN')
        if len(self.game_list) % 100 == 0:
            self.addData()
# ! TURN ON TRAINING
#             self.train(0)

    def makeStep(self, field, sign):
        # print('MAKE STEP')
        inp_field = self.convert(field, sign)
        # print(inp_field)
        res = self.model.predict(inp_field)
        # print(res)

        ind = np.argmax(res[1])
        # print(ind)
        x = ind % 5
        y = int(ind / 5)

        while field[y][x] != ' ':
            res[1][0][ind] = 0
            ind = np.argmax(res[1])
            x = ind % 5
            y = int(ind / 5)

        # print('coords - ', y, x)
        self.current_game.addStep(inp_field, res[0], res[1], y, x)
        return (y, x)

    def convert(self, field, sign):
        print('CONVERT')
        inp_field = np.zeros((1, 25))
        for y in range(0, 5):
            for x in range(0, 5):
                # print(y, ' ', x, ' ', field[y][x])
                if field[y][x] == sign:
                    inp_field[0][y * 5 + x] = 1
                elif field[y][x] != " ":
                    inp_field[0][y * 5 + x] = -1
        # print(inp_field)
        return inp_field

    def train(self, mode):
        print('TRAIN')
        history = self.model.fit(self.dataset.X, self.dataset.Y, batch_size=5, epochs=130, verbose=1)
        self.model.save(self.model_path + "trained.h5")







