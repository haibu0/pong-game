from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        self.goto(0, 150)

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def game_over(self, winner):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER,{winner} wins ", align="center", font=("Courier", 20, "normal"))

    def allocate_point(self, player):

        if player == 'player_l':
            self.l_score += 1
            self.update()
            self.goto(0, 0)
            self.write(f"BLUE POINT ", align="center", font=("Courier", 20, "normal"))
        elif player == 'player_r':
            self.r_score += 1
            self.update()
            self.goto(0, 0)
            self.write(f"RED POINT ", align="center", font=("Courier", 20, "normal"))
        else:
            print("point allocation input error")
