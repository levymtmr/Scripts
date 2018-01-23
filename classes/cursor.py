import pygame

class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/cursor.png")
    
    def draw(self,screen,position):
        screen.blit(self.image,(position))