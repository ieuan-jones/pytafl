import pygame
import sys

class State:
    def __init__(self):
        self.events = []
    
    def handleEvents(self):
        for i in self.events:
            if i.type == pygame.QUIT:
                sys.exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.key == pygame.K_ESCAPE:
                    sys.exit()
    
    def tick(self):
        pass
    
    def blit(self,screen):
        screen.fill((0,0,0))
    
    def setEvents(self,events):
        self.events = events