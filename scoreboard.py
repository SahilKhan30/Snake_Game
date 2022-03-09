import turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file="high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.show_leaderboard()

    def show_leaderboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}\tHigh Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file="high_score.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.show_leaderboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_leaderboard()
