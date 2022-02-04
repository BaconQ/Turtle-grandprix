from turtle import Turtle, Screen
import random
import string

screen = Screen()
screen.setup(width= 800, height=700)
user_bet = screen.textinput(prompt= "Place your bets (Blue/Red/Green/Yellow/Pink/Purple)", title="Welcom to the T1 grandprix: ")
user_bet = string.capwords(user_bet)

x= -230
y = -190
is_race_on = False
turtle = []
color = ["Blue", "Red", "Green", "Yellow", "Pink", "Purple"]


for i in range(6):
    turtle.append(Turtle(shape="turtle"))
    turtle[i].color(color[i])
    turtle[i].penup()
    y += 40
    turtle[i].setposition(x , y)

if user_bet:
    is_race_on = True

while is_race_on:

    for i in turtle:
        if i.xcor() > 380:
            is_race_on = False
            winner = i.pencolor()
            if user_bet == winner:
                print(f"Your bet on {user_bet} turtle was the winner")
            else:
                print(f"Your bet on {user_bet} turtle was the loser, {winner} won")

        random_speed = random.randint(0,10)
        i.forward(random_speed)
    
screen.exitonclick()