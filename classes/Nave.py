import pygame
from classes.projectil import Projectil
from classes.invasor import Invasor

class Nave(pygame.sprite.Sprite):
	def __init__(self,altura,largura):
		pygame.sprite.Sprite.__init__(self)

		self.imagemNave1 = pygame.image.load('img/ship1.png')
		self.imagemNave2 = pygame.image.load('img/ship2.png')
		self.imagemNave3 = pygame.image.load('img/ship3.png')
		self.imagemNave4 = pygame.image.load('img/ship4.png')

		self.imagemExplosao = pygame.image.load('img/explosion1.png')
		
		self.listaImagens = [self.imagemNave1,self.imagemNave2,self.imagemNave3,self.imagemNave4]
		self.posImagem = 0

		self.imagemPlayer = self.listaImagens[self.posImagem]
		self.rect = self.imagemPlayer.get_rect()

		self.rect.centerx = largura/2
		self.rect.centery = altura-30

		self.listaDisparo = []
		self.vida = True
		self.vivo = True

		self.tempoTroca = 1
		self.velocidade = 20

		self.somDisparo = pygame.mixer.Sound('music/shoot.wav')
		self.somExplosao = pygame.mixer.Sound('music/death.wav')


	def __movimento(self):
		if self.vida == True:
			if self.rect.left <= 0:
				self.rect.left = 0
			elif self.rect.right > 1000:
				self.rect.right = 1000
			elif self.rect.top >= 600:
				self.rect.top = 300

	def movimentoDireita(self):
		self.rect.left += self.velocidade
		self.__movimento()

	def movimentoEsquerda(self):
		self.rect.left -= self.velocidade
		self.__movimento()

	def up(self):
		self.rect.top -= self.velocidade
		self.__movimento

	def down(self):
		self.rect.top += self.velocidade
		self.__movimento

	def disparar(self,x,y):
		meuProjectil = Projectil(x,y,"img/tiro1.png",True)
		self.listaDisparo.append(meuProjectil)
		self.somDisparo.play()

	def destruido(self):
		self.somExplosao.play()
		self.vida = False
		self.velocidade = 0
		self.imagemPlayer = self.imagemExplosao		

	def comportamento(self,tempo):
		self.posImagem +=1
		self.tempoTroca +=1
		if self.posImagem > len(self.listaImagens)-1:
			self.posImagem = 0

	def desenhar(self,superficie):
		if self.vida == True:
			self.imagemPlayer = self.listaImagens[self.posImagem]
			superficie.blit(self.imagemPlayer,self.rect)
		if self.vida == False:
			superficie.blit(self.imagemPlayer,self.rect)
