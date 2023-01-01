from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def end_game():
  game_is_on = False

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.display_score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(end_game, 'w')

game_is_on = True

def end_game():
  game_is_on = False

TIME_DELAY = 0.1

while game_is_on:
  screen.update()
  time.sleep(TIME_DELAY)
  snake.move()

  # detect collision with food
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()
    scoreboard.display_score()
    TIME_DELAY *= 0.95

  # detect collision with wall
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    scoreboard.reset()
    snake.reset()
    TIME_DELAY = 0.1

  # detect collision with tail
  for segment in snake.segments[1:]:
    if snake.head.distance(segment.position()) < 10:
      scoreboard.reset()
      snake.reset()
      TIME_DELAY = 0.1

screen.exitonclick()