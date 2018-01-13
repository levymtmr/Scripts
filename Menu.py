import pygame,sys 
from pygame.locals import *
from Game import SpaceInvader

class MenuGame:
    def __init__(self):
        self.pygameinit = pygame.init()
        self.screen = pygame.display.set_mode((1000,600))
        self.font = pygame.font.SysFont("font/space.ttf",30)
        self.bg_image = pygame.image.load('img/bg_menu.gif')
        
    def press_start(self):
        self.opcao1 = self.font.render("Press Enter",0,(250,0,0))
        self.screen.blit(self.bg_image,(0,0))
        self.screen.blit(self.opcao1,(450,100))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == QUIT: 
    				    pygame.quit()
				        sys.exit()
                     if event.key == K_BACKSPACE:
                        SpaceInvader()

            pygame.display.update()

    def carregar(self):
        pass 

    def options(self):
        pass 

jogo = MenuGame()
jogo.press_start()