from turtle import *

class Player(Turtle):
  
  def __init__(self):
    super().__init__()
    self.shape("turtle")
    self.color("black")
    self.penup()
    self.setheading(90)
    self.goto(0, -280)
    #To increase the speed after each cycle
    self.i = 1
    self.score = 0
  
  def move_fd(self):
    self.fd(5)
  
  def move_bd(self):
    self.setheading(270)
    self.fd(5)
    
  def move_rt(self):
    self.setheading(0)
    self.fd(5)
    
  def move_lt(self):
    self.setheading(180)
    self.fd(5)
    
  def default(self):
    self.setheading(90)
    
  def check_game(self, Cars):
    self.can_play = 1
    for car in Cars.all_cars:
      if self.distance(car) < 18:
        self.can_play = 0
    
    if self.can_play == 1:
      return True
    else:
      return False

  def refresh(self):
    if self.ycor() > 300:
      self.score += 10
      self.i = self.i * (3 / 4)
      self.goto(0,-280)
      return self.i
    return self.i
    