import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()

    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
        elif player.is_finish_line():
            player.go_to_start()
            scoreboard.increase_level()
            car_manager.level_up()
screen.exitonclick()
