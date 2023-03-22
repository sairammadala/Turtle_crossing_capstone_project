from turtle import *
from random import *

colors = ["red", "green", "blue", "yellow", "purple", "black", "orange"]

class Car:
  
  def __init__(self):
    self.all_cars = []
    self.l = 0

  def create_car(self):
    self.random_occurance = randint(1,6)
    if self.random_occurance == 1:
      self.y = randint(-280, 280)
      new_car = Turtle()
      new_car.shape("square")
      new_car.shapesize(stretch_wid=1, stretch_len=1.5)
      new_car.color(choice(colors))
      new_car.penup()
      new_car.setheading(180)
      new_car.goto(320,self.y)
      self.all_cars.append(new_car)
    
  def move(self):
    for car in self.all_cars:
      car.fd(5)
