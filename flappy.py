import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Game constants
GRAVITY = 0.25
BIRD_JUMP = -6.5
PIPE_GAP = 150
PIPE_FREQ = 1500 # milliseconds

# Load fonts
FONT = pygame.font.SysFont(None, 36)

# Bird class
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((34, 24))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center=(WIDTH // 4, HEIGHT // 2))
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += int(self.velocity)
        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity = 0

    def jump(self):
        self.velocity = BIRD_JUMP

# Pipe class
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, is_top):
        super().__init__()
        self.image = pygame.Surface((52, HEIGHT))
        self.image.fill((0, 255, 0))
        if is_top:
            self.rect = self.image.get_rect(midbottom=(x, y - PIPE_GAP // 2))
        else:
            self.rect = self.image.get_rect(midtop=(x, y + PIPE_GAP // 2))

    def update(self):
        self.rect.x -= 3
        if self.rect.right < 0:
            self.kill()

# Function to create pipe pair
def create_pipes(x):
    center_y = random.randint(PIPE_GAP, HEIGHT - PIPE_GAP)
    top_pipe = Pipe(x, center_y, True)
    bottom_pipe = Pipe(x, center_y, False)
    return top_pipe, bottom_pipe

# Game loop
bird = Bird()
all_sprites = pygame.sprite.Group(bird)
pipes = pygame.sprite.Group()
clock = pygame.time.Clock()
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, PIPE_FREQ)
score = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()
        if event.type == SPAWNPIPE:
            p_top, p_bottom = create_pipes(WIDTH + 10)
            pipes.add(p_top, p_bottom)
            all_sprites.add(p_top, p_bottom)

    all_sprites.update()

    # Check collisions
    if pygame.sprite.spritecollideany(bird, pipes) or bird.rect.bottom >= HEIGHT:
        running = False

    # Update score
    for pipe in pipes:
        if pipe.rect.centerx == bird.rect.centerx and pipe.rect.bottom > 0:
            score += 0.5

    SCREEN.fill((135, 206, 235))
    all_sprites.draw(SCREEN)
    score_surf = FONT.render(f"Score: {int(score)}", True, (0,0,0))
    SCREEN.blit(score_surf, (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
