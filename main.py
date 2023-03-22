from carmanager import *
from time import *
from playerbehaviour import *
from scoreboard import *

frame = Screen()
frame.setup(width=600, height=600)
frame.listen()

tracer(0)

car = Car()
player = Player()
score = Score()


#keyevents
frame.onkeypress(player.move_fd, "Up")
frame.onkeypress(player.move_bd, "Down")
frame.onkeypress(player.move_lt, "Left")
frame.onkeypress(player.move_rt, "Right")
frame.onkeyrelease(player.default, "Up")
frame.onkeyrelease(player.default, "Down")
frame.onkeyrelease(player.default, "Left")
frame.onkeyrelease(player.default, "Right")



game_on = True

while game_on:
  update()
  car.create_car()
  car.move()
  game_on = player.check_game(car)
  i = player.refresh()
  score.update_score(player.score)
  sleep(0.1*i)
  
game = Turtle()
game.hideturtle()
game.write("GAME OVER!!!", align = "center", font = ("arial", 24, "normal"))
  
frame.exitonclick()
  
  
  