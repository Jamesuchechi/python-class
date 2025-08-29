import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
FPS = 60

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the ball
ball_x, ball_y = WIDTH / 2, HEIGHT / 2
ball_speed_x, ball_speed_y = 5, 5

# Set up the paddle
paddle_x, paddle_y = WIDTH / 2 - PADDLE_WIDTH / 2, HEIGHT - PADDLE_HEIGHT - 20

# Set up the score
score = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 8
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - PADDLE_WIDTH:
        paddle_x += 10

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce the ball off the edges
    if ball_x < BALL_RADIUS or ball_x > WIDTH - BALL_RADIUS:
        ball_speed_x *= -1
    if ball_y < BALL_RADIUS:
        ball_speed_y *= -1

    # Check for collision with the paddle
    if (ball_y + BALL_RADIUS > paddle_y and
            ball_x > paddle_x and ball_x < paddle_x + PADDLE_WIDTH):
        ball_speed_y *= -1
        score += 1

    # Check for game over
    if ball_y > HEIGHT:
        break

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), BALL_RADIUS)
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(FPS)

# Game over screen
screen.fill(BLACK)
text = font.render("Game Over!", True, WHITE)
screen.blit(text, (WIDTH / 2 - 75, HEIGHT / 2 - 18))
text = font.render(f"Final Score: {score}", True, WHITE)
screen.blit(text, (WIDTH / 2 - 90, HEIGHT / 2 + 18))
pygame.display.flip()
pygame.time.wait(2000)