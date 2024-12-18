import pygame 

from player import Player 
from box import Box 
from sounds import Sound 




#class qui represente notre jeu 
class Game : 
       

    def __init__(self):
        #generer notre joueur 
        self.player = Player()
        self.box = Box()
        self.sound = Sound()

    
    