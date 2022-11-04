import time,math
from turtle import Screen
from Exercises.day23_TurtleCrossing_capstone.player import Player
from Exercises.day23_TurtleCrossing_capstone.car_manager import CarManager
from Exercises.day23_TurtleCrossing_capstone.scoreboard import Scoreboard

#CONFIG SCREEN
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#CONFIG PLAYER
me = Player()

#CONFIG CARMANAGER
carmng = CarManager()

#CONFIG SB
sb = Scoreboard()

#CONFIG KEY EVENTS
screen.listen()
screen.onkeypress(me.move_turtle,"Up")
#screen.onkeypress(me.move_turtle(),"Up")

game_is_on = True
ok_create_car_flag = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmng.spawnCar()
    carmng.moveCars()

    #check for collision
    if me.collided_with_car(carmng.cars):
        sb.printGamesOver()
        game_is_on = False

    #check for success, if so; go back to startpos, inc level, and car speed
    if me.hitGoal():
        me.goto((0, -280))
        sb.incLevel()
        carmng.lvlUp()

screen.exitonclick()
