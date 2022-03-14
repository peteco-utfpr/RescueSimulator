# -*- coding: cp1252 -*-
import pygame, time, math, sys
from pygame.locals import *


class View:
    """Desenha o ambiente (o que está representado no Model) em formato texto."""
    def __init__(self, model):
        self.model = model
        ##Define a posicao do agente
        self.posRob = None

        ## Desvio utilizado para dar espaco para colocar a numeracao no grid
        self.desv = 50

        ## Tamanho dos quadrados
        self.square_size = 50

        ##Inicia os módulos do PYGAME
        pygame.init() 

        ## Define a largura e a altura da tela
        self.largura = 900
        self.altura = 600
        ## Cria a tela, somando 300 na largura para colocar a parte de mostrar a saida
        #self.window = pygame.display.set_mode((self.largura + 300, self.altura)) ##Cria uma tela.. X e Y
        self.window = pygame.display.set_mode((self.largura, self.altura)) ##Cria uma tela.. X e Y

        pygame.display.set_caption("Robo Fun Simulator")##Nomeia a Janela
        self.tela = pygame.display.get_surface()##)
        self.cor_branca = (255, 255, 255)
        self.cor_preta = (0, 0, 0)
        self.cor_cinza = (128,128,128)
        self.window.fill(self.cor_branca)
        pygame.display.flip()
        pygame.display.update()
        
        ##Imagens utilizadas
        self.log = pygame.image.load('img/log.png').convert_alpha()
        self.log = pygame.transform.scale(self.log, (299, 550))


        ## Variavel para permitir construir a parte estatica do ambiente uma unica vez
        self.strutucteGenerate = False

        ## Variavel que guarda uma instancia do labirinto
        self.board = False

        """
        O funcionamento consiste em duas partes:
            1° -> Construcao do ambiente. O usuario clica no bloco define o que vai ter nele;
            2° -> Depois que o usuário apertar a tecla ENTER, comeca a execucao do programa.
        """
        #self.step = "build"
        self.step ="notbuild"

    ## Metodo que retorna a screen criada para o pygame
    def getScreen(self):
        return self.tela
    
    ## Metodo que seta o labirinto
    def setBoard(self, board):
        self.board = board
        
    ## Metodo usado para construir a parte estatica do ambiente
    def drawStructure(self):
        self.board.show()

    ## Metodo que retorna o step atual (build ou deliberate)
    def getStep(self):
        return self.step

    ## Metodo que desenha a estrutura do labirinto, e executa no step build
    def drawToBuild(self):
        ## Verifica se a parte estatisca ja foi desenhada, caso nao, constroi e nao precisa mais chamar
        if self.strutucteGenerate == False:
            self.drawStructure()
            self.strutucteGenerate = True

        redraw = True   
        for event in pygame.event.get():
            ## Verifica se foi apertada a tecla ENTER. Se caso sim, passa para a proxima etapa
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    self.step = "deliberate"
                if event.key==pygame.K_s:
                    self.board.save()
                    
            ## Verifica se foi clicado em um bloco 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                redraw = self.board.checkClick(pygame.mouse.get_pos())
                if redraw:
                    self.window.fill((255, 255, 255))
                    self.board.show()
                        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  
        pygame.display.update()

    ## Metodo para desenhar na tela, e usado durante o step deliberate     
    def draw(self):
        ## Limpa as mensagens do robo
        #self.tela.blit(self.log, (self.largura, 5))
        ## Apaga a posicao antiga do robo
        if self.posRob != None:
            self.board.listPlaces[self.posRob[0]][self.posRob[1]].setAgent(False)
            self.board.listPlaces[self.posRob[0]][self.posRob[1]].show()
            
        ## Desenha o robo na nova posicao, e mostra a mensagem do robo no lado
        self.board.listPlaces[self.model.agentPos[0]][self.model.agentPos[1]].setAgent(True)
        self.board.listPlaces[self.model.agentPos[0]][self.model.agentPos[1]].show()
        self.posRob = (self.model.agentPos[0], self.model.agentPos[1])

        ## Desenha a fala do robo na lateral
        #txt = "Estou em (x, y): " + str(self.model.agentPos[1]) + ", " + str(self.model.agentPos[0]) +  " Cambio..."
        #fonte=pygame.font.SysFont("Times New Roman", 20, False, False)           ##### usa a fonte padrão
        #txttela = fonte.render(txt, 0, (0,0,0))  ##### renderiza o texto na cor desejada
        #self.tela.blit(txttela,(self.largura+6, 170))

        ##Desenha o objetivo
        self.board.listPlaces[self.model.goalPos[0]][self.model.goalPos[1]].setGoal(True)
        self.board.listPlaces[self.model.goalPos[0]][self.model.goalPos[1]].show()

        ## Verifica se o robo chegou no lugar, e se sim, mostra uma mensagem diferente
        # if self.model.goalPos[0] == self.model.agentPos[0] and self.model.goalPos[1] == self.model.agentPos[1]:
            # self.tela.blit(self.log, (self.largura, 5))
           
            #txt = "UFA.... Finalmente cheguei!"
            #fonte=pygame.font.SysFont("Times New Roman", 20, False, False)           ##### usa a fonte padrão
            #txttela = fonte.render(txt, 0, (0,0,0))  ##### renderiza o texto na cor desejada
            #self.tela.blit(txttela,(self.largura+6, 170))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
       
        pygame.display.update()

