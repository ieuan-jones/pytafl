import pygame
from taflgamestate import TaflGameState
from menustate import MenuState
import resources as R
from constants import *

pygame.init()

class Main:
    def __init__(self,surface):
        self.screen = surface
        self.states = {MENUSTATE : MenuState(),
                       TAFLGAMESTATE : TaflGameState()}
        self.currentState = TAFLGAMESTATE
    
    def handleEvents(self):
        pygame.event.pump()
        
        events = []
        
        for i in pygame.event.get():
            events.append(i)
        
        self.states[self.currentState].setEvents(events)
    
    def tick(self):
        self.states[self.currentState].tick()
        self.states[self.currentState].handleEvents()
    
    def blit(self):
        self.states[self.currentState].blit(self.screen)
        
        pygame.display.flip()
    
    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(30)
            self.handleEvents()
            self.tick()
            self.blit()

screen = pygame.display.set_mode((646,656),pygame.FULLSCREEN)
pygame.display.set_caption("Alea Evangelii")

M = Main(screen)
M.run()