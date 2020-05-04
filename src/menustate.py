import pygame
import sys

from state import State
from gui import Button

class MenuState(State):
    def __init__(self):
        pass
    
    def handleEvents(self):
        for i in self.events:
            if i.type == pygame.QUIT:
                sys.exit()
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    sys.exit()
    
    def tick(self):
        pass
    
    def blit(self,screen):
        screen.fill((0,0,0))
    
    def setEvents(self,events):
        self.events = events