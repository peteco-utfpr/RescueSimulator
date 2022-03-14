import pygame, time, math, sys, os
from pygame.locals import *
import boxItens

## Classe que define cada triangulo da malha
class Triangle:
    def __init__(self, ref, side, angle, typeT, screen, ide):
        """
        @param ref: Posicao X,Y onde se ira comecar a desenhar
        @param side: Tamanho dos dois lados iguais do triangulo isoceles
        @param angle: Angulo de abertura dos dois lados iguais (em radianos)
        @param typeT: Tipe do triangulo: 0 Se a base fica em baixo, ou 1 se ela fica em cima
        @param screen: Screen do pygame
        @param ide: Posicao x,y para identificacao
        """
        self.ref = ref
        self.side = side
        self.screen = screen
        self.ide = ide
        self.height = side*math.cos(angle)
        self.base = 2 * (math.sqrt(side**2 - ( self.height**2)))
        self.typeT = typeT
        ## Define os 3 pontos do triangulo
        self.p1 = ref
        if typeT == 0:
            self.p2 = (int(ref[0] + self.base/2), int(ref[1] + self.height))
            self.p3 = (int(ref[0] - self.base/2), int(ref[1] + self.height))
        else:
            self.p2 = (int(ref[0] + self.base/2), int(ref[1] - self.height))
            self.p3 = (int(ref[0] - self.base/2), int(ref[1] - self.height))
            

        ## Define o que pode ter dentro do Triangulo. Quando for True, significa que o objeto esta 'dentro' dele, na posicao
        self.color = False
        self.itemInside = False
        self.agent = False
        self.goal = False

        ## Variaveis usadas para definir se um objeto é acionavel
        self.actionable = False
        self.stateAction = False

    ## Retorna o ponto 2
    def getP2(self):
        return self.p2

    ## Seta se o agente esta dentro ou nao
    def setAgent(self, agentIn):
        self.agent = agentIn

    ## Seta se o objetivo esta dentro ou nao
    def setGoal(self, goalIn):
        self.goal = goalIn

    ## Retorna a altura do triangulo
    def getHeight(self):
        return self.height

    ## Mostra o trinagulo na tela
    def show(self):
        ## De acordo com o que tem dentro, irá mudar a cor
        if self.agent == True:
            pygame.draw.polygon(self.screen,(0,255,0),(self.p1,self.p2,self.p3))
        elif self.color != False:
            pygame.draw.polygon(self.screen,self.color,(self.p1,self.p2,self.p3))
        elif self.goal == True:
            pygame.draw.polygon(self.screen,(240,230,140),(self.p1,self.p2,self.p3))
        else:
            pygame.draw.polygon(self.screen,(255,255,255),(self.p1,self.p2,self.p3))
        ## Desenha o contorno preto
        pygame.draw.polygon(self.screen,(0,0,0),(self.p1,self.p2,self.p3), 1)
            

    ## Verifica se foi clicado dentro dele
    def checkClick(self, posMouse):
        ## Verifica se o tipo do triangulo é 0
        if self.typeT == 0:
            ## Verifica se clicou fora 
            if posMouse[0] < self.ref[0] - self.base/2 or posMouse[0] > self.ref[0] + self.base/2:
                return False
            elif posMouse[1] < self.ref[1] or posMouse[1] > self.ref[1] + self.height:
                return False
            else:
                if posMouse[1] < self.ref[1] + (2*self.height/self.base)*(abs(posMouse[0]-self.ref[0])):
                    return False
                else:
                    ## Se for clicado dentro, pinta ele de preto
                    pygame.draw.polygon(self.screen,(0,0,0),(self.p1,self.p2,self.p3))
                    ## Abre a caixa que mostra a opções de itens que podem estar dentro dele
                    self.openOptions()
                    return self
        ## Verifica se o tipo do triangulo é 1   
        elif self.typeT == 1:
            ## Verifica se clicou fora 
            if posMouse[0] < self.ref[0] - self.base/2 or posMouse[0] > self.ref[0] + self.base/2:
                return False
            elif posMouse[1] > self.ref[1] or posMouse[1] < self.ref[1] - self.height:
                return False
            else:
                if posMouse[1] > self.ref[1] - (2*self.height/self.base)*(abs(posMouse[0]-self.ref[0])):
                    return False
                else:
                    ## Se for clicado dentro, pinta ele de preto
                    pygame.draw.polygon(self.screen,(0,0,0),(self.p1,self.p2,self.p3))
                    ## Abre a caixa que mostra a opções de itens que podem estar dentro dele
                    self.openOptions()
                    return self 
        return False

    ## Metodo que abre as opções de itens
    def openOptions(self):
        self.selectItens = boxItens.BoxItens(self.screen)
        self.selectItens.show()
     
    ## Verifica se foi clicado em algum desses itens
    ## E define isso nos itens
    def checkClickItens(self, posMouse):
        self.itemInside = self.selectItens.checkClickIten(posMouse)
        if self.itemInside == "Robô":
            self.agent = True
            return self
        elif self.itemInside == "Objetivo":
            self.goal = True
            return self
        self.updateColor()
        return False
    
    ## Metodo que atualiza a cor do bloco de acordo com o item
    def updateColor(self):
        if self.itemInside == "Parede":
            self.color = (139,69,19)
        elif self.itemInside == "Cone":
            self.color = (255,69,0)
        elif self.itemInside == "Caixa":
            self.color = (205,133,63)
        elif self.itemInside == "Lâmpada":
            self.color = (0,0,0)
            self.actionable = True
        elif self.itemInside == "Robô":
            self.agent = True
        elif self.itemInside == "Objetivo":
            self.goal = True
        else:
            self.color = False


    ## Método que define as ações dos objetos acionáveis
    def doAction(self, action):
        ## No momento, só tem a lampada. Então a unica ação dela é ligar ou desligar
        if self.itemInside == "Lâmpada":
            if self.stateAction == False:
                self.color = (255,255,0)
                self.stateAction = True
            else:
                self.color = (0,0,0)
                self.stateAction = False
            self.show()
        ## Para adicionar mais elementos, coloque no aqui





