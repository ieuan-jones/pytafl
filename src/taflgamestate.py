import pygame
import time
import os
from state import State
from controllers import HumanTaflController
from board import Board
import resources as R
from constants import *

class TaflGameState(State):
    def __init__(self):
        self.board = Board()
        self.controllers = [HumanTaflController(self,ATTACKER),HumanTaflController(self,DEFENDER)]
        
        self.currentSide = 0
        
        for i in self.controllers:
            i.populateStones()
        
        self.replaying = False
        self.totalEvents = []
        
        self.timer = 0
    
    def handleEvents(self):
        self.controllers[self.currentSide].handleEvents()
    
    def tick(self):
        self.timer += 1
        
        self.controllers[self.currentSide].tick()
        
        if self.replaying:
            if self.timer%20 == 0:
                if self.replayLine < self.replayLength-1:
                    self.controllers[self.currentSide].setEvents([self.replayEvents[self.replayLine]])
                    self.replayLine += 1
                else:
                    self.replaying = False
            else:
                self.controllers[self.currentSide].setEvents([])
    
    def blit(self,screen):
        screen.fill((0,0,0))
        
        self.board.blit(screen)
        
        pygame.draw.rect(screen,(self.currentSide%2*255,128+self.currentSide%2*127,255),(0,646,646,10))
        self.controllers[self.currentSide].blit(screen)
    
    
    def endTurn(self):
        self.currentSide = 1-self.currentSide
        self.board.unhighlight()
    
    
    def setEvents(self,events):
        for i in events:
            if i.type == pygame.KEYDOWN:
                if i.key not in [pygame.K_ESCAPE,pygame.K_l,pygame.K_s]:
                    self.totalEvents.append(i)
            if i.type == pygame.KEYUP:
                self.totalEvents.append(i)
            if i.type == pygame.MOUSEBUTTONDOWN:
                self.totalEvents.append(i)
        self.controllers[self.currentSide].setEvents(events)
    
    def getBoard(self):
        return self.board
    
    
    def load(self):
        file = open(os.path.join("replays","1376511321.67.replay"),"r")
        contents = file.read()
        file.close()
        
        contents = contents.split("\n")
        self.replayEvents = []
        for i in contents:
            if i != "":
                line = i.split(",")
                if int(line[0]) == pygame.KEYDOWN:
                    key = int(line[1])
                    event = pygame.event.Event(int(line[0]),{"key" : key})
                if int(line[0]) == pygame.KEYUP:
                    key = int(line[1])
                    event = pygame.event.Event(int(line[0]),{"key" : key})
                if int(line[0]) == pygame.MOUSEBUTTONDOWN:
                    button = int(line[1])
                    x = int(line[2])
                    y = int(line[3])
                    event = pygame.event.Event(int(line[0]),{"button" : button, "pos" : [x,y]})
                
                self.replayEvents.append(event)
        
        self.replaying = True
        self.replayLength = len(contents)
        self.replayLine = 0
    
    
    def save(self):
        toSave = ""
        for i in self.totalEvents:
            if i.type == pygame.KEYDOWN:
                toSave += str(i.type)
                toSave += ","
                toSave += str(i.key)
            if i.type == pygame.KEYUP:
                toSave += str(i.type)
                toSave += ","
                toSave += str(i.key)
            if i.type == pygame.MOUSEBUTTONDOWN:
                toSave += str(i.type)
                toSave += ","
                toSave += str(i.button)
                toSave += ","
                toSave += str(i.pos[0])
                toSave += ","
                toSave += str(i.pos[1])
            toSave += "\n"
        
        file = open(os.path.join("replays",str(time.time())+".replay"),"w")
        file.write(toSave)
        file.close()