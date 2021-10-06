import pygame
import random
import sys
from pygame.math import Vector2

pygame.init()


# Snake
class SNAKE:
    def __init__(self):
        # Initialise snake
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (120, 181, 122), block_rect)

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True


# Food
class FOOD:
    def __init__(self):
        self.randomize()

    def draw_food(self):
        x_pos = int(self.pos.x * cell_size)
        y_pos = int(self.pos.y * cell_size)
        food_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        screen.blit(food_icon, food_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


# Game update
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.food = FOOD()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.snake.draw_snake()
        self.food.draw_food()

    def check_collision(self):
        if self.food.pos == self.snake.body[0]:
            # Change position of fruit
            self.food.randomize()
            # Add extra block to snake body
            self.snake.add_block()

    def check_fail(self):
        # Check if snake hits walls or itself
        if self.snake.body[0].x < 0 or self.snake.body[0].x >= cell_number or self.snake.body[0].y < 0 or self.snake.body[0].y >= cell_number:
            game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                game_over()


def game_over():
    pygame.quit()
    sys.exit()


cell_size = 40
cell_number = 20

# Display
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
screen.fill((175, 215, 70))

# Running clock
clock = pygame.time.Clock()

# Caption and icon
pygame.display.set_caption("Snake")
snake_icon = pygame.image.load('Graphics/snake.png')
pygame.display.set_icon(snake_icon)

# Food icon
food_icon = pygame.image.load('Graphics/watermelon.png').convert_alpha()

# Background

# Background sound

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 120)

main_game = MAIN()

# Game loop
running = True
while running:

    screen.fill((175, 215, 70))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)

    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
