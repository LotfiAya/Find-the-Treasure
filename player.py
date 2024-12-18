import pygame 

#creer une class qui va representer notre joueur 
class Player(pygame.sprite.Sprite) : 

    def __init__(self) : 
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 20 
        self.velocity = 50 
        self.image = pygame.image.load("player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (64,64))
        self.rect= self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 300

    def move_left(self):
        self.rect.x -= self.velocity
    
    def move_right(self):
        self.rect.x += self.velocity

    def move_up(self):
        self.rect.y -= self.velocity
    
    def move_down(self):
        self.rect.y += self.velocity