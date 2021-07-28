from turtle import Screen, Turtle
import random

is_race_on = False
colors = ["green", "orange", "indigo", "yellow", "red", "violet"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Racing Game")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(-230, y_positions[index])
    all_turtles.append(new_turtle)

print(f"User input {user_bet}")
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
