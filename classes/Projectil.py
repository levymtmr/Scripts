import pygame

class Projectil(pygame.sprite.Sprite):
	def __init__(self,posy,posx,rota,personagem):
		pygame.sprite.Sprite.__init__(self)
		self.imagemProjectil = pygame.image.load(rota)
		self.rect = self.imagemProjectil.get_rect()
		self.velocidadeDisparo = 8

		self.rect.top = posx
		self.rect.left = posy

		self.disparoPersonagem = personagem

	def trajetoria(self):
		if self.disparoPersonagem == True:
			self.rect.top = self.rect.top - self.velocidadeDisparo
		else:
			self.rect.top = self.rect.top + self.velocidadeDisparo


	def desenhar(self,superficie):
		superficie.blit(self.imagemProjectil,self.rect)