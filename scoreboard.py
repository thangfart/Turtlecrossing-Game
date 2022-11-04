FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-235,270)
        self.levelNr = 1
        self.updateLevelNr()

    def updateLevelNr(self):
        self.write(f"Level:{self.levelNr}",align="center",font=FONT)

    def incLevel(self):
        self.levelNr += 1
        self.clear()
        self.updateLevelNr()

    def printGamesOver(self):
        self.goto(0,0)
        self.write(f"Games over!, you made it to level:{self.levelNr}",align="center",font=FONT)
