from turtle import Turtle
import math
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_turtle(self):
        self.forward(MOVE_DISTANCE)
        print(self.pos())

    def collided_with_car(self,cars:list):
        #min kode er alt inni """ """, virket som metoden for kollisjonsdeteksjon virket i følge kordinatene som
        #printes ut, når det enten er kollisjon på sidene eller over/under siden på bilen. Problemet var at
        #det så ikke riktig ut 'visuelt' sett! Dvs så ut som en kollisjon ble detektert selv med en stor "gap"
        #på skjermen mellom bil og turtle
        """for car in cars:

            #means the turtle is in either left/right side right next to the car its gonna hit.
            if abs(car.xcor() - self.xcor()) < 30:
                if car.distance(self) < math.sqrt(30**2 + 20**2) and car.distance(self) > math.sqrt(30**2):
                    #end game, also print it maybe, and lastly start from level 1/quit
                    print(f"Woah! You collided with either left/right side of the car\n")
                    print(f"Turtle pos x,y: {self.xcor()},{self.ycor()}\n")
                    print(f"Car you hit pos x,y,index: {car.xcor()},{car.ycor()},{cars.index(car)}\n")
                    return True

            #means its gonna crash from underside or upperside of car,
            # also end game, print it, and ofc start at level 1/quit
            if abs(car.ycor() - self.ycor()) < 20:
                if car.distance(self) < math.sqrt(30**2 + 20**2) and car.distance(self) > math.sqrt(20**2):
                    print(f"Woah! You collided with either upper/under side of the car")
                    print(f"Turtle pos x,y: {self.xcor()},{self.ycor()}\n")
                    print(f"Car you hit pos x,y,index: {car.xcor()},{car.ycor()},{cars.index(car)}\n")
                    return True"""
        for car in cars:
            if car.distance(self) < 20:
                return True

    def hitGoal(self):
        if self.ycor() >= FINISH_LINE_Y:
            #self.goto(STARTING_POSITION)
            return True


