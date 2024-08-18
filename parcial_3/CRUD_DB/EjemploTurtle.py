import turtle

screen = turtle.Screen()
screen.bgcolor("black") 

estrella = turtle.Turtle()
estrella.shape("turtle")
estrella.color("yellow") 
estrella.speed(3)

for _ in range(5):
    estrella.forward(150) 
    estrella.right(144)    

estrella.hideturtle()

screen.exitonclick()
