# code credit: https://www.geeksforgeeks.org/turtle-race-game-using-python-turtle/

from record_game_data import record_game_data

import random
from turtle import Turtle, Screen

Race = False

s = Screen()
s.setup(width=500, height=400)
bet = s.textinput(title="Make your Bet", prompt="Which turtle will win? Enter a color: ")
X = -230
Y = -100
colors = ["red", "orange", "yellow", "blue", "violet"]

turtles = []
for i in range(0, 5):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=X, y=Y + 50 * i)
    turtles.append(t)

if bet:
    Race = True

while Race:
    for turtle in turtles:
        if turtle.xcor() >= 230:  
            Race = False
            winning = turtle.pencolor()

            if winning == bet:
                print(f"You have won the bet on {winning} turtle! The {winning} is the winner")
            else:
                print(f"You lose! {winning} turtle is the winner")

        record_game_data(bet, winning)

        distance = random.randint(0, 10)
        turtle.forward(distance)

s.exitonclick()
