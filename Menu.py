import pygame,sys 
from pygame.locals import *
from Game import SpaceInvader

class MenuGame:
    def __init__(self):
        self.pygameinit = pygame.init()
        self.screen = pygame.display.set_mode((1000,600))
        self.font = pygame.font.SysFont("font/space.ttf",30)
        self.bg_image = pygame.image.load('img/bg_menu.gif')
        

    def press_start(self, screen):
        self.opcao1 = self.font.render("Press Start",0,(250,0,0))
        self.screen.blit(self.bg_image,(0,0))
       
    
        self.mouse = pygame.mouse.get_pos()
        print(self.mouse)
        if self.mouse == (450,100):
            self.screen.blit(self.opcao1,(450,100))
        
    def carregar(self,screen):
        self.opcao2 = self.font.render("Carregar Jogo Salvo",0,(250,250,250))
        self.screen.blit(self.opcao2,(420,200))
        
    def options(self,screen):
        self.opcao3 = self.font.render("Options",0,(250,250,250))
        self.screen.blit(self.opcao3,(420,300)) 
        
    def main(self):
         while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                            sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_RETURN:
                            print("chamando")
                            SpaceInvader()

                self.press_start(self.screen)
                self.carregar(self.screen)
                self.options(self.screen)
                pygame.display.update()


jogo = MenuGame()
jogo.main()
