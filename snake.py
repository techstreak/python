import pygame
import time
import random

pygame.init()

# Set up the display
width, height = 440, 660
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake parameters
snake_block = 10
snake_speed = 15

# Snake function to draw the snake on the screen
def our_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, green, [x, y, snake_block, snake_block])

# Main game loop
def game_loop():
    game_over = False

    snake_list = []  # List to keep track of snake's body parts
    snake_length = 1  # Initial length of the snake

    snake_x, snake_y = width // 2, height // 2  # Initial position of the snake
    snake_change_x, snake_change_y = 0, 0  # Initial movement of the snake

    food_x, food_y = round(random.randrange(0, width - snake_block) / 10.0) * 10.0, round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_change_x = -snake_block
                    snake_change_y = 0
                elif event.key == pygame.K_RIGHT:
                    snake_change_x = snake_block
                    snake_change_y = 0
                elif event.key == pygame.K_UP:
                    snake_change_y = -snake_block
                    snake_change_x = 0
                elif event.key == pygame.K_DOWN:
                    snake_change_y = snake_block
                    snake_change_x = 0

        snake_x += snake_change_x
        snake_y += snake_change_y

        # Check if the snake hits the screen boundary
        if snake_x >= width or snake_x < 0 or snake_y >= height or snake_y < 0:
            game_over = True

        screen.fill(white)  # Clear the screen with white color
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])  # Draw the food on the screen
        snake_head = [snake_x, snake_y]  # Create a new head for the snake
        snake_list.append(snake_head)  # Add the head to the snake's body

        # If the snake length is greater than the allowed length, remove the last part of the body
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if the snake collides with itself (end the game if it does)
        for x, y in snake_list[:-1]:
            if x == snake_x and y == snake_y:
                game_over = True

        our_snake(snake_list)  # Draw the snake on the screen
        pygame.display.update()  # Update the display

        # Check if the snake eats the food
        if snake_x == food_x and snake_y == food_y:
            food_x, food_y = round(random.randrange(0, width - snake_block) / 10.0) * 10.0, round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)  # Set the frame rate for the game

    pygame.quit()
    quit()

game_loop()
