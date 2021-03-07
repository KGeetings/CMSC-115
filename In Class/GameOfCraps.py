import random

gamesWon = 0
games = 5

for i in range(games):
    dice = random.randrange(1,7) + random.randrange(1,7)
    if dice == 7 or dice == 11:
        gamesWon += 1
    elif dice == 2 or dice == 3 or dice == 12:
        pass
    else:
        point = dice
        dice = random.randrange(1,7) + random.randrange(1,7)
        while dice != point and dice != 7:
            dice = random.randrange(1,7) + random.randrange(1,7)
        if dice == point:
            gamesWon += 1
            
print("You won", gamesWon, "out of", games, "games which is", gamesWon / games * 100, "%.")