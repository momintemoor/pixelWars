import unittest
import theGame
import pygame

class UnitTesting(unittest.TestCase):
    def tests(self):
        widthS = 600
        heightS = 480
        screen = pygame.display.set_mode((widthS, heightS))
        player = theGame.Player(screen, widthS, heightS, 50)  # player position (60, 430)
        player.keyPress(pygame.K_a)  # player position (50, 430) moved left 1
        self.assertTrue(player.x == 50)
        player.keyPress(pygame.K_d)  # player position (60, 430) moved right 1
        self.assertTrue(player.x == 60)
        player.keyPress(pygame.K_w)  # player position (60, 420) moved up 1
        self.assertTrue(player.y == 420)
        player.keyPress(pygame.K_s)
        player.keyPress(pygame.K_s)  # player position (60, 440) moved down 2
        self.assertTrue(player.y == 440)

        player.keyPress(pygame.K_e)  # random inputs that do not affect movement
        player.keyPress(pygame.K_LEFT)
        self.assertTrue(player.x == 60)
        self.assertTrue(player.y == 440)

if __name__ == '__main__':
    unittest.main()
