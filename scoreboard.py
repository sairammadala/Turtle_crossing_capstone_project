from turtle import *

class Score(Turtle):
  
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.goto(0,260)

  def update_score(self, score):
    self.clear()
    self.write(f"SCORE: {score}", align="center", font=("arial", 24, "normal"))