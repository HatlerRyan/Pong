from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f'{self.l_score}', True ,ALIGNMENT, FONT)
        self.goto(100,200)
        self.write(f'{self.r_score}', True, ALIGNMENT, FONT)

    def l_goal(self):
        self.l_score += 1

    def r_goal(self):
        self.r_score += 1

