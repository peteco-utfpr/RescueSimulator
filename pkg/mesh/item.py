import pygame, time, math, sys, os
from pygame.locals import *
from pygame import font
class Item:
    def __init__(self, text, img, size, pos, screen, action = False):
        """
        @param text: Nome do objeto
        @param img: Imagem do objeto (com a sua extensão)
        @param size: Tamanho da imagem
        @param pos: Posicao em que a imagem deve ficar
        @param screen: Screen do pygame
        @param action: Define a ação que aquele objeto pode fazer
        """
        self.image = pygame.image.load(os.path.join("pkg", "mesh", "images", img)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (size[0], size[1]))
        self.text = text
        self.pos = pos
        self.size = size
        self.screen = screen
    

    ## Metodo para mostrar o item 
    def show(self):
        ## Mostra a imagem
        self.screen.blit(self.image, (self.pos[0], self.pos[1] + 40))
        ## Mostra a escrita
        pygame.font.init() 
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        textsurface = myfont.render(self.text, False, (0, 0, 0))
        self.screen.blit(textsurface,(self.pos[0],self.pos[1]))

    ## Metodo que verifica se foi clicado no item
    def checkClick(self, posMouse):
        if posMouse[0] < self.pos[0] or posMouse[0]> self.pos[0]+self.size[0] or posMouse[1] < self.pos[1] or posMouse[1]> self.pos[1]+self.size[1]+40:
            return False
        else:
            ## Se sim, retorna o tipo tele
            return self.text
            
