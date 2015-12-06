import pygame,Projectil
from random import randint

class Invasor(pygame.sprite.Sprite):
	def __init__(self,posx,posy,distancia):
		pygame.sprite.Sprite.__init__(self)


		self.imagem1 = pygame.image.load('img/inimigo1.gif')
		self.imagem2 = pygame.image.load('img/inimigo2.gif')
		self.imagem3 = pygame.image.load('img/inimigo3.gif')
		self.imagem4 = pygame.image.load('img/inimigo4.gif')
		self.imagem5 = pygame.image.load('img/inimigo5.gif')
		self.imagem6 = pygame.image.load('img/inimigo6.gif')
		self.imagem7 = pygame.image.load('img/inimigo7.gif')
		self.imagem8 = pygame.image.load('img/inimigo8.gif')
		self.imagem9 = pygame.image.load('img/inimigo9.gif')
		self.imagem10 = pygame.image.load('img/inimigo10.gif')
		self.imagem11 = pygame.image.load('img/inimigo11.gif')
		self.imagem12 = pygame.image.load('img/inimigo12.gif')
		self.imagem13 = pygame.image.load('img/inimigo13.gif')
		self.imagem14 = pygame.image.load('img/inimigo14.gif')
		
		self.listaImagens = [self.imagem1,
							 self.imagem2,
							 self.imagem3,
							 self.imagem4,
							 self.imagem5,
							 self.imagem6,
							 self.imagem7,
							 self.imagem8,
							 self.imagem9,
							 self.imagem10,
							 self.imagem11,
							 self.imagem12,
							 self.imagem13,
							 self.imagem14]
		self.posImagem = 0

		self.imagemInvasor = self.listaImagens[self.posImagem]
		self.rect = self.imagemInvasor.get_rect()

		
		self.velocidade = 3
		self.listaDisparo = []
		self.rect.top = posy
		self.rect.left = posx

		self.rangeDisparo = 5
		self.tempoTroca = 1

		self.direita = True
		self.contador = 0
		self.maxDescida = self.rect.top + 40

		self.limiteDireita = posx+ distancia
		self.limiteEsquerda = posy-distancia 

		self.conquista = False 

	def desenhar(self,superficie):
		self.imagemInvasor = self.listaImagens[self.posImagem]
		superficie.blit(self.imagemInvasor,self.rect)


	def comportamento(self,tempo):
		if self.conquista == False:
			self.__movimento()

			self.__ataque()
			self.posImagem +=1
			self.tempoTroca +=1

			if self.posImagem > len(self.listaImagens)-1:
				self.posImagem = 0

	def __ataque(self):
		if (randint(0,100)<self.rangeDisparo):
			self.__disparo()

	def __disparo(self):
		x,y = self.rect.center
		meuProjectil = Projectil.Projectil(x-16,y,'img/bala1.png',False)
		self.listaDisparo.append(meuProjectil)

	def __movimento(self):
		if self.contador < 3:
			self.__movimentoLateral()
		else:
			self.__descida()

	def __descida(self):
		if self.maxDescida == self.rect.top:
			self.contador = 0
			self.maxDescida = self.rect.top + 40
		else:
			self.rect.top +=1

	def __movimentoLateral(self):
		if self.direita == True:
			self.rect.left = self.rect.left + self.velocidade
			if self.rect.left > self.limiteDireita:
				self.direita = False
				self.contador += 1
		else:
			self.rect.left = self.rect.left - self.velocidade
			if self.rect.left < self.limiteEsquerda:
				self.direita = True