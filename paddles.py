from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, cor):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.shapesize(1, 5)
        self.color("white")
        self.goto(cor)
        self.setheading(90)
        self.showturtle()

    def move_paddle_up(self):
        self.forward(20)

    def move_paddle_down(self):
        self.backward(20)
