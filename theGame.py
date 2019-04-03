import pygame
import math

pygame.init()
pygame.display.set_caption("Pixel Wars")
screen = pygame.display.set_mode((600, 480))
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

def main():
    clock = pygame.time.Clock()
    player = pygame.Surface((60, 22), pygame.SRCALPHA)
    pygame.draw.rect(player, pygame.Color('red'), [0, 0, 32, 32])
    first_player = player
    player_cent = player.get_rect(center=(320, 240))
    angle = 0
    # Add bullets to this group.
    bullet_group = pygame.sprite.Group()
    moveX = 0
    moveY = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bullet_group.add(Bullet(player_cent.center, angle))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moveX -= 1
                if event.key == pygame.K_d:
                    moveX += 1
                if event.key == pygame.K_w:
                    moveY += 1
                if event.key == pygame.K_s:
                    moveY -= 1

        bullet_group.update()
        x, y = pygame.math.Vector2(pygame.mouse.get_pos()) - player_cent.center  # get the cursor position
        angle = math.degrees(math.atan2(y, x))


        screen.fill((0, 0, 0))
        pygame.draw.rect(first_player, pygame.Color('red'), [moveX, moveY, 32, 32])

        screen.fill(pygame.Color('black'))
        bullet_group.draw(screen)
        screen.blit(player, player_cent)
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
    pygame.quit()
