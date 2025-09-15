import pygame
import random
pygame.init()

# Background music
# pygame.mixer.init()
# pygame.mixer.music.load("D:/python project 2025/Pygame/[No Copyright] 8 Bit Retro Game Music Loop(M4A_128K).mp3")
# pygame.mixer.music.play(-1)

# Game geometry
screen_width = 500
screen_height = 500
gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SnakeX")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
dark_green = (0, 100, 0)  # Snake
bright_yellow = (255, 255, 0)  # Food

# Background image
background_image = pygame.image.load("D:/python project 2025/Pygame/snake_background.jpg")
background_image = pygame.transform.scale(background_image, (500, 500))

# Snake starting
snake_x = 45
snake_y = 55
snake_size = 20
velocity_x = 0
velocity_y = 0

# Food position
food_x = random.randint(10, int(screen_width / 2))
food_y = random.randint(10, int(screen_height / 2))

# Score and snake body
score = 0
snk_list = []
snk_length = 1

# Game  speed (fps) control
exit_game = False
fps = 50
clock = pygame.time.Clock()

# Font setup
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])

def plot_snake(gamewindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.circle(gamewindow, color, (x + snake_size // 2, y + snake_size // 2), snake_size // 2)

# Game loop
while not exit_game:
    if exit_game:
        gamewindow.fill(white)
        text_screen("Game Over! Press Enter to continue", red, screen_height/2, screen_width/2)

        
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         exit_game = True
        #         if event.type == pygame.KEYDOWN:
        #             if event.type == pygame.K_RETURN
                    
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

    # Movement update
    snake_x += velocity_x
    snake_y += velocity_y

    # Snake head update
    head = [snake_x, snake_y]
    snk_list.append(head)
    if len(snk_list) > snk_length:
        del snk_list[0]

    # food
    if abs(snake_x - food_x) < 25 and abs(snake_y - food_y) < 25:
        score += 1
        snk_length += 1
        food_x = random.randint(10, screen_width - snake_size)
        food_y = random.randint(10, screen_height - snake_size)

    # SCORE
    gamewindow.blit(background_image, (0, 0))
    text_screen("Score: " + str(score * 10), red, 5, 5)

    # Draw food 
    pygame.draw.circle(gamewindow, bright_yellow, (food_x + snake_size // 2, food_y + snake_size // 2), snake_size // 2)

    # Draw snake
    plot_snake(gamewindow, dark_green, snk_list, snake_size)

# for Game over and Score visible after collson
    if snake_x  < 0 or snake_x > screen_width or snake_y < 0 or snake_y> screen_height:
        gamewindow.blit(background_image, (0,0))
        text_screen("Game Over! ",red,screen_width//2 - 110, screen_height//2 - 100)
        text_screen("Score: " + str(score * 10),red, screen_height//2 - 100, screen_width//2 - 30 )
        pygame.display.update()
        pygame.time.delay(3000)
        exit_game = True

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
