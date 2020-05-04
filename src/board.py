import pygame
from stone import Stone
from constants import *

ALLOW_HIGHLIGHTS = False

class Board:
    def __init__(self):
        self.attack = []
        self.defense = []
        
        self.highlighted = []
    
    def blit(self,screen):
        for i in range(0,19):
            for j in range(0,19):
                pygame.draw.rect(screen,(160+((i+j)%2)*64,128+((i+j)%2)*64,0),(i*34,j*34,34,34))
                if [i,j] in self.highlighted and ALLOW_HIGHLIGHTS:
                    pygame.draw.rect(screen,(255,0,128),(i*34,j*34,34,34))
                if i < 2 or i > 16:
                    if j < 2 or j > 16:
                        if (i+j)%2 == 0: 
                            pygame.draw.rect(screen,(160,154,128),(i*34,j*34,34,34))
                        else:
                            pygame.draw.rect(screen,(224,218,179),(i*34,j*34,34,34))
        
        
        pygame.draw.rect(screen,(255,64,0),(0,0,34,34))
        pygame.draw.rect(screen,(255,64,0),(612,0,34,34))
        pygame.draw.rect(screen,(255,64,0),(0,612,34,34))
        pygame.draw.rect(screen,(255,64,0),(612,612,34,34))
        pygame.draw.rect(screen,(255,64,0),(306,306,34,34))
        
        for i in self.attack:
            i.blit(screen)
        for i in self.defense:
            i.blit(screen)
    
    def addStone(self,side,pos,variant=NORMAL):
        stone = Stone(side,(pos[0]*34,pos[1]*34),variant)
        
        if side == ATTACKER:
            self.attack.append(stone)
        if side == DEFENDER:
            self.defense.append(stone)
    
    
    def getStone(self,side,pos):
        if side == ATTACKER:
            stones = self.attack
        if side == DEFENDER:
            stones = self.defense
        
        for i in stones:
            if i.getPos() == pos:
                return i
    
    def removeStone(self,side,stone):
        if side == ATTACKER:
            self.attack.remove(stone)
        if side == DEFENDER:
            self.defense.remove(stone)
    
    def unhighlight(self):
        self.highlighted = []
    
    def highlightSquare(self,pos):
        self.highlighted.append(pos)
