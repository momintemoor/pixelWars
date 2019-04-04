import pygame
import math

pygame.init()
pygame.display.set_caption("Pixel Wars")
widthS = 600
heightS = 480
screen = pygame.display.set_mode((widthS, heightS))
image = pygame.Surface((16, 16))
image.fill((0, 0, 0))
image.set_colorkey((0, 0, 0))
pygame.draw.circle(image, pygame.Color('grey'), (4, 4), 4)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, angle):
        super(Bullet, self).__init__()
        self.image = pygame.transform.rotate(image, angle)
        self.rect = self.image.get_rect(center=position)
        self.position = pygame.math.Vector2(position)
        self.velocity = pygame.math.Vector2(4, 0).rotate(angle)  # adjust the speed of bullets

    def update(self):
        self.position += self.velocity  # add velocity to bullet
        self.rect.center = self.position

class Player(pygame.sprite.Sprite):
    def __init__(self, surface, width, height, size):
        super(Player, self).__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.surface = surface
        self.height = height
        self.width = width
        self.size = size
        self.x = (0 + (self.width/10))
        self.y = self.height - self.size
        self.rect = self.image.get_rect(center=(self.x + 20, self.y + 20))
        self.health = 100
        self.points = 0

    def keyPress(self, key):
        if key == pygame.K_a:
            self.x -= 10
            self.rect = self.image.get_rect(center=(self.x + 20, self.y + 20))
        elif key == pygame.K_d:
            self.x += 10
            self.rect = self.image.get_rect(center=(self.x + 20, self.y + 20))
        elif key == pygame.K_w:
            self.y -= 10
            self.rect = self.image.get_rect(center=(self.x + 20, self.y + 20))
        elif key == pygame.K_s:
            self.y += 10
            self.rect = self.image.get_rect(center=(self.x + 20, self.y + 20))

    def draw(self, color):
        pygame.draw.rect(self.surface, pygame.Color(color), [self.x, self.y, self.size, self.size])

def main():

    clock = pygame.time.Clock()
    n = 0
    n += 1
    player = Player(screen, widthS, heightS, 50)
    player2 = Player(screen, 5000, 250, 50)
    angle = 0
    bullet_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    if n == 1:
        player_group.add(player2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bullet_group.add(Bullet(player.rect.center, angle))
            if event.type == pygame.KEYDOWN:
                player.keyPress(event.key)

        bullet_group.update()
        x, y = pygame.math.Vector2(pygame.mouse.get_pos()) - player.rect.center  # get the cursor position
        angle = math.degrees(math.atan2(y, x))

        screen.fill(pygame.Color('black'))
        player.draw('red')
        player2.draw('red')
        player_group.draw(screen)
        bullet_group.draw(screen)

        if pygame.sprite.spritecollide(player2, bullet_group, True):
            player2.health -= 10
            player.points += 1
            player2.points -= 1
            #if player2.health <= 0:
                #player2.kill()
                #player2.draw('black')
                #player2.health = 0
            #print(player2.health)
            print("Your Points: " + str(player.points))
            print("Enemy Points: " + str(player2.points))

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
    pygame.quit()
