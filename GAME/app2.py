import pygame
import random
import sys

# Initialize
pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 150, 255)

# Basket
basket_width, basket_height = 80, 20
basket = pygame.Rect(WIDTH // 2 - basket_width // 2, HEIGHT - 40, basket_width, basket_height)
basket_speed = 6

# Falling objects
object_width, object_height = 20, 20
falling_objects = []
object_speed = 4
spawn_delay = 30  # frames

# Score & lives
score = 0
lives = 3
font = pygame.font.Font(None, 36)

frame_count = 0
running = True

while running:
    screen.fill(WHITE)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Basket movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket.left > 0:
        basket.x -= basket_speed
    if keys[pygame.K_RIGHT] and basket.right < WIDTH:
        basket.x += basket_speed

    # Spawn new objects
    frame_count += 1
    if frame_count >= spawn_delay:
        frame_count = 0
        x_pos = random.randint(0, WIDTH - object_width)
        falling_objects.append(pygame.Rect(x_pos, 0, object_width, object_height))

    # Move objects
    for obj in falling_objects[:]:
        obj.y += object_speed
        if obj.colliderect(basket):
            score += 1
            falling_objects.remove(obj)
        elif obj.top > HEIGHT:
            lives -= 1
            falling_objects.remove(obj)

    # Draw basket
    pygame.draw.rect(screen, BLUE, basket)

    # Draw objects
    for obj in falling_objects:
        pygame.draw.rect(screen, RED, obj)

    # Draw score/lives
    score_text = font.render(f"Score: {score}", True, BLACK)
    lives_text = font.render(f"Lives: {lives}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (WIDTH - 120, 10))

    # Game over
    if lives <= 0:
        game_over_text = font.render("GAME OVER", True, BLACK)
        screen.blit(game_over_text, (WIDTH//2 - 80, HEIGHT//2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()
    clock.tick(60)
