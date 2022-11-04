import random
from turtle import Turtle
from Exercises.day23_TurtleCrossing_capstone.player import Player
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
YMAX = 280
YMIN = -280
XMAX = 300
XMIN = -300


class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    #flag to control wether its ok to spawn a new car, its ok when a randomly generated int ranging from
    # 1 to 10 is equal to 1
    def roadIsClear(self):
        lucky_nr = random.randint(1,6)
        if lucky_nr == 1:
            return True

    #INITIALIZE A RAND CAR BASED ON SOME CONDITIONS
    def spawnCar(self):
        """
        Creates randomly generated car, based on some coniditons, it decides if the the cars given parameters are ok
        here; ycord and xcord, related to the last car in the list self.cars
        :return: None
        """
        if self.roadIsClear():
            rand_car = Turtle()
            rand_car.penup()
            rand_car.setheading(180)
            rand_car.shape("square")
            rand_car.shapesize(stretch_wid=1,stretch_len=2)
            chosen_color = random.choice(COLORS)
            rand_car.color(chosen_color)
            start_y = random.randint(YMIN,YMAX)
            start_x = XMAX
            print(f"Trying to create car with color/ycor: {chosen_color}/{start_y}\n")
            #check if this car´s y_pos i identical or very close to the previous car spawned
            #If True, this means the spawned cars ycor is way too close to the previuous one´s
            #therefor increment the randomly generated ycor by a little (at least +/- 40  pixels
            #check first if there is a car already
            #if not we it means were creating the first car, hence no need to take care for its ycor
            if len(self.cars) >= 1:
                prev_car = self.cars[-1]
                print(f"Last created car has index/ycor: {self.cars.index(prev_car)}/{prev_car.ycor()}\n")
                #delta_y = prev_car.ycor() - rand_car.ycor()
                #delta_x = prev_car.xcor() - rand_car.xcor()

                if self.needLowerYcord(prev_car.ycor(),start_y):
                    #start_y = start_y - abs(delta_y)
                    start_y = prev_car.ycor() - 40
                    print(f"Created cars ycor was BELOW last car but too close \nNew y is then: {start_y}")

                if self.needHigherYcord(prev_car.ycor(),start_y):
                    #start_y = start_y + abs(delta_y)
                    start_y = prev_car.ycor() + 40
                    print(f"Created cars ycor was OVER last car but too close \nNew y is then: {start_y}")

                #if self.needHigherXcord(prev_car,rand_car):
                    #start_x = 360
                    #print(f"Created cars xcord is too close the prev cars x \n")

            rand_car.goto(start_x,start_y)
            self.cars.append(rand_car)
            print(f"Actual car created with color/index/ycor: {chosen_color}/{self.cars.index(rand_car)}/{self.cars[-1].ycor()}\n")

    def moveCars(self):
        for car in self.cars:
            car.forward(self.car_speed)
        return

    #method checking if a new car´s y is over the prev car´s y, but its too close
    def needHigherYcord(self,prev_car_ycor,new_car_ycor):
        """
        Method checks wether the created cars ycord is too close the last one (checks if abs(delta_y) <40),
        also decides wether it is beneath or over the the prev car;here if the created car is over the prev car.
        :param prev_car: Turtle()
        :param new_car: Turtle()
        :return: Bool
        """
        delta_y = prev_car_ycor - new_car_ycor
        if delta_y <= 0 and abs(delta_y) < 40:
            return True

    #method checking if a new car´s y is under the prev car´s y, but its too close
    def needLowerYcord(self,prev_car_ycor,new_car_ycor):
        """
        Method checks wether the created cars ycord is too close the last one (checks if abs(delta_y) <40),
        also decides wether it is beneath or over the the prev car;here if the created car is beneath the prev car.
        :param prev_car: Turtle()
        :param new_car: Turtle()
        :return: Bool
        """
        delta_y = prev_car_ycor - new_car_ycor
        if delta_y > 0 and abs(delta_y) < 40:
            return True

    #Method making sure the car created wont be too close horizontally, PS: FOR NOW,NOT USED!
    def needHigherXcord(self,prev_car_xcor,new_car_xcor):
        """
        Calculates distance between prev and last created car, check if its less than 60, 60 as limit so that
        the turtle would be able to pass between them when its moving forward
        :param prev_car: Turtle()
        :param new_car: Turtle()
        :return: Bool
        """
        delta_x = prev_car_xcor - new_car_xcor
        if abs(delta_x) < 60:
            return True


    def lvlUp(self):
        self.car_speed += MOVE_INCREMENT
        return


