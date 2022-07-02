from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.01


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1


    def return_ball(self):
        self.x_move *= -1
        self.move_speed *= .01

    def reset_ball(self):
        self.hideturtle()
        self.move_speed = 0.01
        self.home()
        self.return_ball()
        self.showturtle()


