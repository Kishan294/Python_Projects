from turtle import Turtle, Screen, color
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle = ["Kajal", "Adesh", "Kishan", "Naman", "Bhavesh", "Sushi"]

turtle_y = -100    
all_turtles = []

for i in range(6):
    turtle_name = Turtle("turtle")
    turtle_name.color(colors[i])
    turtle_name.penup()
    turtle_name.goto(x = -230, y = turtle_y)
    turtle_y += 30
    all_turtles.append(turtle_name)


if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()