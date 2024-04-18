import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Mayhem")

# Colors and settings
BLACK = (0, 0, 0) # background color 
WHITE = (255, 255, 255) # General color for sprites if images fail to load 
RED = (255, 0, 0)   # color for bullets 
BLUE = (0, 0, 255)  # Color for the obstacle

# FPS
clock = pygame.time.Clock()
fps = 60

# Load spaceship images or create simple shapes if images are not available
def load_image(path, size):
    try:
        image = pygame.image.load(path).convert_alpha()
        image = pygame.transform.scale(image, size)
    except:
        # Use a simple shape if the image can't be loaded
        image = pygame.Surface(size)
        image.fill(WHITE)
    return image

player_image = load_image('spaceship.png', (40, 40))

# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image, angle=0):
        super().__init__()
        self.original_image = image
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = angle
        self.velocity = [0, 0]
        self.speed = 0.2
        self.rotation_speed = 5

    def update(self, rotate_left, rotate_right, thrust):
        if rotate_left:
            self.angle += self.rotation_speed
        if rotate_right:
            self.angle -= self.rotation_speed
        if thrust:
            radians = math.radians(self.angle)
            self.velocity[0] += math.sin(radians) * self.speed
            self.velocity[1] -= math.cos(radians) * self.speed

        # Apply velocity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # Update image rotation
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.centery, self.angle)
        bullets.add(bullet)

# Define the Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = [math.sin(math.radians(angle)) * 10, -math.cos(math.radians(angle)) * 10]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if self.rect.y < 0 or self.rect.y > screen_height or self.rect.x < 0 or self.rect.x > screen_width:
            self.kill()

# Define the Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(x, y))

# Sprite groups
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
bullets = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

player1 = Player(100, screen_height // 2, player_image)
player2 = Player(screen_width - 100, screen_height // 2, player_image)
players.add(player1, player2)
all_sprites.add(player1, player2)

obstacle = Obstacle(screen_width // 2, screen_height // 2, 100, 50)
obstacles.add(obstacle)
all_sprites.add(obstacle)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player1.shoot()

    # Update
    keys = pygame.key.get_pressed()
    player1.update(keys[pygame.K_a], keys[pygame.K_d], keys[pygame.K_w])
    player2.update(keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP])
    bullets.update()

    # Check collisions
    for player in players:
        if pygame.sprite.spritecollide(player, obstacles, False):
            player.kill()  # Or handle it in another way

    for bullet in bullets:
        if pygame.sprite.spritecollide(bullet, obstacles, True):
            bullet.kill()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    bullets.draw(screen)

    # Update the display
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()
