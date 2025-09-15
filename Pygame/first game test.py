import pygame
import random

# Initialize
pygame.init()

# Screen
screen_width = 1200
screen_height = 650
gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SnakeX")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
dark_green = (0, 100, 0)
bright_yellow = (255, 255, 0)

# Background image
background_image = pygame.image.load("D:/python project 2025/Pygame/snake_background.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Font
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])

def plot_snake(win, color, snk_list, size):
    for x, y in snk_list:
        pygame.draw.circle(win, color, (x + size // 2, y + size // 2), size // 2)

#  food
snake_x = 45
snake_y = 55
snake_size = 20
velocity_x = 0
velocity_y = 0

food_x = random.randint(10, screen_width - 30)
food_y = random.randint(10, screen_height - 30)

score = 0
snk_list = []
snk_length = 1

fps = 70
clock = pygame.time.Clock()
exit_game = False
game_over = False

# Game loop
while not exit_game:
    if game_over:
        gamewindow.blit(background_image, (0, 0))
        text_screen("Game Over!", red, screen_width // 2 - 130, screen_height // 2 - 50)
        text_screen("Score: " + str(score * 10), red, screen_width // 2 - 130, screen_height // 2 - 100)
        text_screen("Enter to Restart", red, screen_width // 2 - 125, screen_height // 2 + 10)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Reset game
                    snake_x = 45
                    snake_y = 55
                    velocity_x = 0
                    velocity_y = 0
                    food_x = random.randint(10, screen_width - 30)
                    food_y = random.randint(10, screen_height - 30)
                    score = 0
                    snk_list = []
                    snk_length = 1
                    game_over = False

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    velocity_x = -10
                    velocity_y = 0
                elif event.key == pygame.K_RIGHT:
                    velocity_x = 10
                    velocity_y = 0
                elif event.key == pygame.K_UP:
                    velocity_y = -10
                    velocity_x = 0
                elif event.key == pygame.K_DOWN:
                    velocity_y = 10
                    velocity_x = 0

        snake_x += velocity_x
        snake_y += velocity_y

        head = [snake_x, snake_y]
        snk_list.append(head)
        if len(snk_list) > snk_length:
            del snk_list[0]

        #  food indicate
        if abs(snake_x - food_x) < 20 and abs(snake_y - food_y) < 20:
            score += 1
            snk_length += 1
            food_x = random.randint(10, screen_width - 30)
            food_y = random.randint(10, screen_height - 30)

        # Takrana with doli
        if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
            game_over = True

        # Draw everything
        gamewindow.blit(background_image, (0, 0))
        text_screen("Score: " + str(score * 10), red, 5, 5)
        pygame.draw.circle(gamewindow, bright_yellow, (food_x + snake_size // 2, food_y + snake_size // 2), snake_size // 2)
        plot_snake(gamewindow, dark_green, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

pygame.quit()
quit()
