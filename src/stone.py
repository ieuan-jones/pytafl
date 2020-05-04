import pygame
import resources as R

from constants import *

class Stone:
    def __init__(self,side,pos,variant=NORMAL):
        if side == ATTACKER:
            colour = (0,128,255)
        if side == DEFENDER:
            colour = (255,255,255)
        if variant == KING:
            colour = (0,255,0)
        
        self.image = pygame.Surface((34,34),65536)
        pygame.draw.ellipse(self.image,colour,(0,0,34,34))
        
        self.rect = pygame.Rect(pos,(34,34))
        
        self.variant = variant
    
    def tick(self):
        pass
    
    def blit(self,screen):
        screen.blit(self.image,self.rect.topleft)
    
    
    def getPos(self):
        return [self.rect.left/34,self.rect.top/34]
    
    def setPos(self,pos):
        self.rect.topleft = pos
    
    def getVariant(self):
        return self.variant