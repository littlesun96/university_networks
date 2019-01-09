class PartyStruct:
    def __init__(self, player1, player2, winner, field, step):
        self.field = field
        self.player1 = player1
        self.player2 = player2
        self.winner = winner
        self.step = step

class SessionScore:
    def __init__(self):
        self.wins = 0
        self.loses = 0
        self.draws = 0
        self.score = 0

    def addDraw(self):
        self.draws += 1

    def addWin(self, step):
        WIN_VAL = 1.5
        stepEval = 1 - (step - 7) / 36
        self.score += WIN_VAL * stepEval
        self.wins += 1

    def addLose(self, step):
        LOSE_VAL = -2
        stepEval = 1 - (step - 7) / 36
        self.score += LOSE_VAL * stepEval
        self.loses += 1

