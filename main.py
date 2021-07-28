from turtle import Screen, Turtle
import random

is_race_on = False
colors = ["green", "orange", "indigo", "yellow", "red", "violet"]
y_positions = [-70, -40, -10, 20, 50, 80]

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Racing Game")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(-230, y_positions[index])

screen.exitonclick()
