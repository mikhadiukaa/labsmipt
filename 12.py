from random import randint
import turtle


number_of_turtles = 10
time_of_sim=100
steps_of_time_number = 10000000000


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(randint(0,100000000000000000)
    unit.goto(randint(-200, 200), randint(-200, 200))


for i in range(steps_of_time_number):
    for unit in pool:
        x = unit.speed
        unit.forward(x*(time_of_sim/steps_of_time_number))
        unit.left(randint(-360,0))
