import pygame

class Sound : 
    

    def __init__(self):
        self.sounds = {
            'step' : pygame.mixer.Sound("footstep.wav"),
            #'intro' : pygame.mixer.Sound("intro.wav")
            }


    def play(self,name) : 
        self.sounds[name].play()
