import pygame
import sys

# Pygame Initialization
pygame.init()

# Screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Paddle properties
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
PADDLE_SPEED = 8

# Ball properties
BALL_SIZE = 20
BALL_SPEED = 5

class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH / 2 - PADDLE_WIDTH / 2, SCREEN_HEIGHT - PADDLE_HEIGHT - 20, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED

    def move_left(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.x = 0

    def move_right(self):
        self.rect.x += self.speed
        if self.rect.x > SCREEN_WIDTH - PADDLE_WIDTH:
            self.rect.x = SCREEN_WIDTH - PADDLE_WIDTH

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED
        self.speed_y = -BALL_SPEED

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH - BALL_SIZE:
            self.speed_x *= -1
        if self.rect.y < 0:
            self.speed_y *= -1

def draw_text(text, font_size, x, y):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))

def main():
    clock = pygame.time.Clock()
    paddle = Paddle()
    ball = Ball()
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move_left()
        if keys[pygame.K_RIGHT]:
            paddle.move_right()

        ball.move()

        if ball.rect.colliderect(paddle.rect):
            ball.speed_y *= -1
            score += 1
        if ball.rect.y > SCREEN_HEIGHT:
            break

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, paddle.rect)
        pygame.draw.ellipse(screen, WHITE, ball.rect)
        draw_text(f"Score: {score}", 32, 10, 10)
        pygame.draw.line(screen, WHITE, (0, SCREEN_HEIGHT - PADDLE_HEIGHT - 40), (SCREEN_WIDTH, SCREEN_HEIGHT - PADDLE_HEIGHT - 40))

        pygame.display.flip()
        clock.tick(60)

    screen.fill(BLACK)
    draw_text("Game Over!", 64, SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 - 32)
    draw_text(f"Final Score: {score}", 32, SCREEN_WIDTH / 2 - 75, SCREEN_HEIGHT / 2 + 32)
    pygame.display.flip()
    pygame.time.wait(2000)

if __name__ == "__main__":
    main()