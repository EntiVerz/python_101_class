import sys
import pygame
from pygame.locals import *
import random 
import time

Snake_block_size = 30

class Snake:
    def __init__(self, parent_ui, length):
        self.length = length
        self.parent_ui = parent_ui
        self.snake_block = pygame.Surface((25,25))
        self.snake_block.fill((100,200,120))
        self.direction = 'down'
        self.x_position = [Snake_block_size] * length
        self.y_position = [Snake_block_size] * length

    def draw(self):
        for i in range(0, self.length):
            self.parent_ui.blit(self.snake_block, (self.x_position[i], self.y_position[i]))
        pygame.display.update()

    def increase_length(self):
        self.length = self.length + 1
        self.x_position.append(1)
        self.y_position.append(1)

    def decrease_length(self):
        self.length = self.length - 1
        self.x_position.pop(-1)
        self.y_position.pop(-1)

    def move_left(self):
        self.direction = 'left'
    def move_right(self):
        self.direction = 'right'
    def move_up(self):
        self.direction = 'up'
    def move_down(self):
        self.direction = 'down'

    def moving(self):
        for i in range(self.length-1, 0, -1):
            self.x_position[i] = self.x_position[i-1]
            self.y_position[i] = self.y_position[i-1]

        if self.direction == 'up':
            self.y_position[0] -= Snake_block_size
        if self.direction == 'down':
            self.y_position[0] += Snake_block_size
        if self.direction == 'left':
            self.x_position[0] -= Snake_block_size
        if self.direction == 'right':
            self.x_position[0] += Snake_block_size
        self.draw()

Food_block_size = 30

class Food:
    def __init__(self, parent_ui):
        self.parent_ui = parent_ui
        self.food_block = pygame.Surface((25,25))
        self.food_block.fill((250,60,60))
        self.x_position = Food_block_size * 5
        self.y_position = Food_block_size * 5 

    def draw(self):
        self.parent_ui.blit(self.food_block, (self.x_position, self.y_position))
        pygame.display.update()

    def move(self):
        self.x_position = random.randint(0,20) * Food_block_size
        self.y_position = random.randint(0,20) * Food_block_size

Enemy_block_size = 30
Enemy_moving = True

class Enemy:
    def __init__(self, parent_ui):
        self.parent_ui = parent_ui
        self.enemy_block = pygame.Surface((25,25))
        self.enemy_block.fill((0,0,0))
        self.x_position = Enemy_block_size * 0
        self.y_position = Enemy_block_size * random.randint(0,25)
    
    def draw(self):
        self.parent_ui.blit(self.enemy_block, (self.x_position, self.y_position))
        pygame.display.update
    
    def move(self):
        if Enemy_moving == True:
            self.x_position = self.x_position + 30

    def respawn(self):
        self.x_position = Enemy_block_size * 0
        self.y_position = Enemy_block_size * random.randint(0,25)

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((750, 750))
        self.surface.fill((255,255,255))
        self.snake = Snake(self.surface, 1)
        self.food = Food(self.surface)
        self.enemy = Enemy(self.surface)

    def play(self):
        self.enemy.draw()
        self.snake.draw()
        self.food.draw()
        self.snake.moving()
        self.enemy.move()

    def food_interact(self, snake_x, snake_y, food_x, food_y):
        if snake_x == food_x:
            if snake_y == food_y:
                return True
        else:return False

    def enemy_interact(self, snake_x, snake_y, enemy_x, enemy_y):
        if snake_x == enemy_x:
            if snake_y == enemy_y:
                return True
        else:return False

    def enemy_borders(self, enemy_x, enemy_y):
        if enemy_x > 750 or enemy_x < 0:
            return True
        if enemy_y > 750 or enemy_y < 0:
            return True

    def run(self):
        game_running = True

        while game_running:
            self.surface.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        game_running = False
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                elif event.type == QUIT:
                    game_running = False
            
            self.play()

            if self.enemy_borders(self.enemy.x_position, self.enemy.y_position):
                self.enemy.respawn()
            else:pass

            if self.food_interact(self.snake.x_position[0], self.snake.y_position[0], self.food.x_position, self.food.y_position) == True:
                self.food.move()
                self.snake.increase_length()
            else:pass

            if self.enemy_interact(self.snake.x_position[0], self.snake.y_position[0], self.enemy.x_position, self.enemy.y_position) == True:
                self.snake.decrease_length()
                self.enemy.respawn()
                print("pass")
            else:pass
            time.sleep(0.15)

if __name__ == "__main__":
    game = Game()
    game.run()