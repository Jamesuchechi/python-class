import pygame
import random
import sys

# Initialize
pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Enemies")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
RED = (255, 0, 0)

# Player
player_size = 30
player = pygame.Rect(WIDTH//2 - player_size//2, HEIGHT - 60, player_size, player_size)
player_speed = 5

# Enemies
enemy_size = 30
enemies = []
spawn_delay = 25
frame_count = 0

# Score
score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(WHITE)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= player_speed
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += player_speed

    # Spawn enemies
    frame_count += 1
    if frame_count >= spawn_delay:
        frame_count = 0
        x_pos = random.randint(0, WIDTH - enemy_size)
        speed = random.randint(3, 7)
        enemies.append({"rect": pygame.Rect(x_pos, 0, enemy_size, enemy_size), "speed": speed})

    # Move enemies
    for enemy in enemies[:]:
        enemy["rect"].y += enemy["speed"]
        if enemy["rect"].top > HEIGHT:
            enemies.remove(enemy)
            score += 1
        if enemy["rect"].colliderect(player):
            game_over_text = font.render("GAME OVER", True, BLACK)
            screen.blit(game_over_text, (WIDTH//2 - 80, HEIGHT//2))
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False

    # Draw player
    pygame.draw.rect(screen, BLUE, player)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy["rect"])

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
