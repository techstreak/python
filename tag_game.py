import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up display
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pac-Man Game")

# Colors
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Pac-Man properties
pacman_radius = 20
pacman_x = screen_width // 2
pacman_y = screen_height // 2
pacman_speed = 5

# Enemy properties
enemy_radius = 15
enemy_x = random.randint(0, screen_width)
enemy_y = random.randint(0, screen_height)
enemy_speed = 5

# Coin properties
coin_radius = 10
coin_x = random.randint(0, screen_width)
coin_y = random.randint(0, screen_height)

# Scoring
score = 100
font = pygame.font.Font(None, 36)

def show_score():
    score_text = font.render(f"Score: {score}", True, yellow)
    screen.blit(score_text, (10, 10))

# End screen
def end_screen():
    screen.fill(black)
    end_text = font.render("Game Over", True, red)
    screen.blit(end_text, (120, 180))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move Pac-Man based on arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed

    # Wrap characters around the screen
    pacman_x = pacman_x % screen_width
    pacman_y = pacman_y % screen_height
    enemy_x = enemy_x % screen_width
    enemy_y = enemy_y % screen_height
    coin_x = coin_x % screen_width
    coin_y = coin_y % screen_height

    # Move enemy towards Pac-Man
    if enemy_x < pacman_x:
        enemy_x += enemy_speed
    else:
        enemy_x -= enemy_speed

    if enemy_y < pacman_y:
        enemy_y += enemy_speed
    else:
        enemy_y -= enemy_speed

    # Check for collision with enemy
    distance_to_enemy = ((enemy_x - pacman_x)**2 + (enemy_y - pacman_y)**2)**0.5
    if distance_to_enemy < pacman_radius + enemy_radius:
        score -= 10  # Decrease score for collision

    # Check for collision with coin
    distance_to_coin = ((coin_x - pacman_x)**2 + (coin_y - pacman_y)**2)**0.5
    if distance_to_coin < pacman_radius + coin_radius:
        score += 100  # Increase score for collecting coin
        coin_x = random.randint(0, screen_width)
        coin_y = random.randint(0, screen_height)

    # Clear the screen
    screen.fill(black)

    # Draw characters
    pygame.draw.circle(screen, yellow, (pacman_x, pacman_y), pacman_radius)
    pygame.draw.circle(screen, red, (enemy_x, enemy_y), enemy_radius)
    pygame.draw.circle(screen, blue, (coin_x, coin_y), coin_radius)

    # Display score
    show_score()

    # Check for end condition
    if score < -1:
        end_screen()

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    pygame.time.Clock().tick(30)

# Quit pygame
pygame.quit()
sys.exit()
