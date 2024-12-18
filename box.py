import pygame 
import random

class Box : 

    def __init__(self) : 
        super().__init__()
        self.image = pygame.image.load("santa-claus.png").convert_alpha()
        self.rect= self.image.get_rect()
        self.rect.x = random.randrange(80,480,50)
        self.rect.y = random.randrange(350,500,50)
    
#print(pygame.font.get_fonts())