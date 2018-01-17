import pygame,sys
from pygame.locals import*
from random import randint
from classes.Nave import Nave
from classes.Invasor import Invasor as Inimigo
# from classes.Menu import MenuGame 

largura = 1000
altura = 600
listaInimigos = []


def pararTudo():
	for inimigo in listaInimigos:
		for disparo in inimigo.listaDisparo:
			inimigo.listaDisparo.remove(disparo)
		inimigo.conquista = True

def carregarInimigos():
	inimigo = Inimigo(400,200,100)
	listaInimigos.append(inimigo)

	inimigo = Inimigo(300,80,100)
	listaInimigos.append(inimigo)

	inimigo = Inimigo(100,150,100)
	listaInimigos.append(inimigo)

	inimigo = Inimigo(600,50,100)
	listaInimigos.append(inimigo)

	inimigo = Inimigo(500,100,100)
	listaInimigos.append(inimigo)

def movimentoTeclado():
	if emJogo == True:
		if event.type == pygame.KEYDOWN:
			if event.key == K_LEFT:
				jogador.movimentoEsquerda()
			elif event.key == K_RIGHT:
				jogador.movimentoDireita()
			elif event.key == K_UP:
				jogador.up()
			elif event.key == K_DOWN:
				jogador.down()
			elif event.key == K_s:
				x,y = jogador.rect.center
				jogador.disparar(x-15,y)
				jogador.disparar(x+15,y)

def SpaceInvader():
	pygame.init()
	screen = pygame.display.set_mode((largura,altura))
	pygame.display.set_caption("Space Invader")
	imagemFundo = pygame.image.load('img/bacgroundSky.png')
	cloud = pygame.image.load('img/cloud3.png')


	pygame.mixer.music.load('music/undertale.wav')
	pygame.mixer.music.play()

	minhaFonte = pygame.font.SysFont("Arial",30)
	texto = minhaFonte.render("SE FUDEU ;D",0,(120,100,100))

	jogador = Nave(altura,largura)
	carregarInimigos()

	relogio = pygame.time.Clock()

	emJogo = True
	while True:
		
		relogio.tick(30)
		
		tempo = pygame.time.get_ticks()/1000
		

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == K_s:
					x,y = jogador.rect.center
					jogador.disparar(x-15,y)
					jogador.disparar(x+15,y)

		if emJogo == True:
			if event.type == pygame.KEYDOWN:
				if event.key == K_LEFT:
					jogador.movimentoEsquerda()
				elif event.key == K_RIGHT:
					jogador.movimentoDireita()
				elif event.key == K_UP:
					jogador.up()
				elif event.key == K_DOWN:
					jogador.down()

			

		
		screen.blit(imagemFundo,(0,0))
		screen.blit(cloud,(50,100))
		screen.blit(cloud,(300,200))
		jogador.desenhar(screen)
		jogador.comportamento(screen)
		
		

		if len(jogador.listaDisparo)>0:
			for x in jogador.listaDisparo:
				x.desenhar(screen)
				x.trajetoria()

				if x.rect.top<100:
					jogador.listaDisparo.remove(x)
				else:
					for inimigo in listaInimigos:
						if x.rect.colliderect(inimigo.rect):
							listaInimigos.remove(inimigo)
							jogador.listaDisparo.remove(x)


		if len(listaInimigos)>0:
			for inimigo in listaInimigos:
				inimigo.comportamento(tempo)
				inimigo.desenhar(screen)

				if inimigo.rect.colliderect(jogador.rect):
					jogador.destruido()
					emJogo = False
					pararTudo()

				if len(inimigo.listaDisparo)>0:
					for x in inimigo.listaDisparo:
						x.desenhar(screen)
						x.trajetoria()

						if x.rect.colliderect(jogador.rect):
							jogador.destruido()
							emJogo = False
							pararTudo()

						if x.rect.top>900:
							inimigo.listaDisparo.remove(x)
						else:
							for disparo in jogador.listaDisparo:
								if x.rect.colliderect(disparo.rect):
									jogador.listaDisparo.remove(disparo)
									inimigo.listaDisparo.remove(x)

		

		if emJogo == False:
			pygame.mixer.music.fadeout(3000)
			screen.blit(texto,(300,300))



		pygame.display.update()




