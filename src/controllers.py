import pygame,sys
from stone import Stone
from constants import *
import resources as R

class Controller:
    def tick(self):
        pass
    
    def blit(self,screen):
        pass
    
    def handleEvents(self):
        pass
    
    def setEvents(self,events):
        self.events = events


class HumanTaflController(Controller):
    def __init__(self,GS,side):
        self.GS = GS
        
        self.pieces = []
        self.legalMoves = []
        self.selected = None
        
        self.side = side
        
        self.placing = False
    
    def tick(self):
        pass
    
    def blit(self,screen):
        if self.selected:
            pygame.draw.ellipse(screen,(0,0,0),(self.selected[0]*34,self.selected[1]*34,34,34),2)
    
    def handleEvents(self):
        for i in self.events:
            if i.type == pygame.QUIT:
                self.GS.save()
                sys.exit()
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    self.GS.save()
                    sys.exit()
                if i.key == pygame.K_SPACE:
                    self.selected = None
                    self.GS.endTurn()
                if i.key == pygame.K_LCTRL:
                    self.placing = True
                if i.key == pygame.K_l:
                    self.GS.load()
                if i.key == pygame.K_s:
                    self.GS.save()
            if i.type == pygame.KEYUP:
                if i.key == pygame.K_LCTRL:
                    self.placing = False
            if i.type == pygame.MOUSEBUTTONDOWN:
                pos = [i.pos[0]/34,i.pos[1]/34]
                stone = self.GS.getBoard().getStone(self.side,pos)
                if self.selected:
                    if not stone:
                        if pos in self.legalMoves:
                            if i.button == 1:
                                self.selected[2].setPos((pos[0]*34,pos[1]*34))
                                self.checkNewState(self.selected[2])
                                self.selected = None
                                self.GS.endTurn()
                                continue
                    if self.selected[2] == stone:
                        if i.button == 3:
                            self.GS.getBoard().removeStone(self.side,self.selected[2])
                            self.selected = None
                            self.GS.getBoard().unhighlight()
                            continue
                if stone:
                    if self.selected:
                        if stone == self.selected[2]:
                            self.selected = None
                            self.GS.getBoard().unhighlight()
                        else:
                            self.selected = [pos[0],pos[1],stone]
                            self.highlightSelected()
                    else:
                        self.selected = [pos[0],pos[1],stone]
                        self.highlightSelected()
                if not stone and self.placing:
                    self.GS.getBoard().addStone(self.side,pos)
    
    
    def highlightSelected(self):
        self.GS.getBoard().unhighlight()
        self.legalMoves = []
        
        pos = self.selected[2].getPos()
        
        for i in range(pos[0]-1,-1,-1): #-1 else 0 isn't included
            if not self.checkLegalSquare([i,pos[1]]):
                break
        for i in range(pos[0]+1,19):
            if not self.checkLegalSquare([i,pos[1]]):
                break
        for i in range(pos[1]-1,-1,-1):
            if not self.checkLegalSquare([pos[0],i]):
                break
        for i in range(pos[1]+1,19):
            if not self.checkLegalSquare([pos[0],i]):
                break
    
    def checkLegalSquare(self,pos):
        attackPiece = self.GS.getBoard().getStone(ATTACKER,pos)
        defencePiece = self.GS.getBoard().getStone(DEFENDER,pos)
        if attackPiece or defencePiece:
            return False
        else:
            self.legalMoves.append(pos)
            self.GS.getBoard().highlightSquare(pos)
            return True
    
    def checkNewState(self, movedStone):
        newStonePos = movedStone.getPos()
        otherSide = 1-self.side
        if newStonePos[0] > 1:
            if self.GS.getBoard().getStone(self.side,[newStonePos[0]-2,newStonePos[1]]):
                testStone = self.GS.getBoard().getStone(otherSide,[newStonePos[0]-1,newStonePos[1]])
                if testStone:
                    if testStone.getVariant() == NORMAL:
                        self.GS.getBoard().removeStone(otherSide,testStone)
        if newStonePos[0] < 17:
            if self.GS.getBoard().getStone(self.side,[newStonePos[0]+2,newStonePos[1]]):
                testStone = self.GS.getBoard().getStone(otherSide,[newStonePos[0]+1,newStonePos[1]])
                if testStone:
                    if testStone.getVariant() == NORMAL:
                        self.GS.getBoard().removeStone(otherSide,testStone)
        if newStonePos[1] > 1:
            if self.GS.getBoard().getStone(self.side,[newStonePos[0],newStonePos[1]-2]):
                testStone = self.GS.getBoard().getStone(otherSide,[newStonePos[0],newStonePos[1]-1])
                if testStone:
                    if testStone.getVariant() == NORMAL:
                        self.GS.getBoard().removeStone(otherSide,testStone)
        if newStonePos[1] < 17:
            if self.GS.getBoard().getStone(self.side,[newStonePos[0],newStonePos[1]+2]):
                testStone = self.GS.getBoard().getStone(otherSide,[newStonePos[0],newStonePos[1]+1])
                if testStone:
                    if testStone.getVariant() == NORMAL:
                        self.GS.getBoard().removeStone(otherSide,testStone)
    
    def populateStones(self):
        if self.side == ATTACKER:
            self.GS.getBoard().addStone(ATTACKER,(2,0))
            self.GS.getBoard().addStone(ATTACKER,(5,0))
            self.GS.getBoard().addStone(ATTACKER,(13,0))
            self.GS.getBoard().addStone(ATTACKER,(16,0))
            self.GS.getBoard().addStone(ATTACKER,(0,2))
            self.GS.getBoard().addStone(ATTACKER,(5,2))
            self.GS.getBoard().addStone(ATTACKER,(18,2))
            self.GS.getBoard().addStone(ATTACKER,(13,2))
            self.GS.getBoard().addStone(ATTACKER,(7,3))
            self.GS.getBoard().addStone(ATTACKER,(9,3))
            self.GS.getBoard().addStone(ATTACKER,(11,3))
            self.GS.getBoard().addStone(ATTACKER,(6,4))
            self.GS.getBoard().addStone(ATTACKER,(12,4))
            self.GS.getBoard().addStone(ATTACKER,(0,5))
            self.GS.getBoard().addStone(ATTACKER,(2,5))
            self.GS.getBoard().addStone(ATTACKER,(5,5))
            self.GS.getBoard().addStone(ATTACKER,(13,5))
            self.GS.getBoard().addStone(ATTACKER,(16,5))
            self.GS.getBoard().addStone(ATTACKER,(18,5))
            self.GS.getBoard().addStone(ATTACKER,(4,6))
            self.GS.getBoard().addStone(ATTACKER,(14,6))
            self.GS.getBoard().addStone(ATTACKER,(3,7))
            self.GS.getBoard().addStone(ATTACKER,(15,7))
            self.GS.getBoard().addStone(ATTACKER,(3,9))
            self.GS.getBoard().addStone(ATTACKER,(15,9))
            self.GS.getBoard().addStone(ATTACKER,(3,11))
            self.GS.getBoard().addStone(ATTACKER,(15,11))
            self.GS.getBoard().addStone(ATTACKER,(4,12))
            self.GS.getBoard().addStone(ATTACKER,(14,12))
            self.GS.getBoard().addStone(ATTACKER,(0,13))
            self.GS.getBoard().addStone(ATTACKER,(2,13))
            self.GS.getBoard().addStone(ATTACKER,(5,13))
            self.GS.getBoard().addStone(ATTACKER,(13,13))
            self.GS.getBoard().addStone(ATTACKER,(16,13))
            self.GS.getBoard().addStone(ATTACKER,(18,13))
            self.GS.getBoard().addStone(ATTACKER,(6,14))
            self.GS.getBoard().addStone(ATTACKER,(12,14))
            self.GS.getBoard().addStone(ATTACKER,(7,15))
            self.GS.getBoard().addStone(ATTACKER,(9,15))
            self.GS.getBoard().addStone(ATTACKER,(11,15))
            self.GS.getBoard().addStone(ATTACKER,(0,16))
            self.GS.getBoard().addStone(ATTACKER,(18,16))
            self.GS.getBoard().addStone(ATTACKER,(5,16))
            self.GS.getBoard().addStone(ATTACKER,(13,16))
            self.GS.getBoard().addStone(ATTACKER,(2,18))
            self.GS.getBoard().addStone(ATTACKER,(5,18))
            self.GS.getBoard().addStone(ATTACKER,(13,18))
            self.GS.getBoard().addStone(ATTACKER,(16,18))
        if self.side == DEFENDER:
            self.GS.getBoard().addStone(DEFENDER,(8,4))
            self.GS.getBoard().addStone(DEFENDER,(10,4))
            self.GS.getBoard().addStone(DEFENDER,(9,6))
            self.GS.getBoard().addStone(DEFENDER,(8,7))
            self.GS.getBoard().addStone(DEFENDER,(10,7))
            self.GS.getBoard().addStone(DEFENDER,(4,8))
            self.GS.getBoard().addStone(DEFENDER,(7,8))
            self.GS.getBoard().addStone(DEFENDER,(9,8))
            self.GS.getBoard().addStone(DEFENDER,(11,8))
            self.GS.getBoard().addStone(DEFENDER,(14,8))
            self.GS.getBoard().addStone(DEFENDER,(6,9))
            self.GS.getBoard().addStone(DEFENDER,(8,9))
            self.GS.getBoard().addStone(DEFENDER,(10,9))
            self.GS.getBoard().addStone(DEFENDER,(12,9))
            self.GS.getBoard().addStone(DEFENDER,(4,10))
            self.GS.getBoard().addStone(DEFENDER,(7,10))
            self.GS.getBoard().addStone(DEFENDER,(9,10))
            self.GS.getBoard().addStone(DEFENDER,(11,10))
            self.GS.getBoard().addStone(DEFENDER,(14,10))
            self.GS.getBoard().addStone(DEFENDER,(8,11))
            self.GS.getBoard().addStone(DEFENDER,(10,11))
            self.GS.getBoard().addStone(DEFENDER,(9,12))
            self.GS.getBoard().addStone(DEFENDER,(8,14))
            self.GS.getBoard().addStone(DEFENDER,(10,14))
            
            self.GS.getBoard().addStone(DEFENDER,(9,9),KING) #Add king
