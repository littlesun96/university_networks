from BattleArena.BattleArena import BattleArena
from Fighters.Fighter_Idiot import Fighter_Idiot
from Fighters.Fighter_NetTrain import Fighter_NetTrain
from Fighters.Fighter_Human import Fighter_Human

FirstBot = Fighter_Idiot("Idiot", "")
FirstBot1 = Fighter_NetTrain("first", "D:\\Usacheva\\university\\neural_networks\\BattleGround\\BattleGround\\Fighters\\net\\first.h5")
SecondBot = Fighter_NetTrain("first2.h5", "D:\\Usacheva\\university\\neural_networks\\BattleGround\\BattleGround\\Fighters\\net\\first.h5")
BattleArenaExmpl = BattleArena(Fighter1=SecondBot, Fighter2=FirstBot)
BattleArenaExmpl.playBattles(num=500)

