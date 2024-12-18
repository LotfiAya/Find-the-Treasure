import pygame
from pygame.constants import QUIT , KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN, KEYUP
from player import Player
from game import Game 
from math import sqrt , pow 
import time 


pygame.init()

#la police et les messages à afficher 
font=pygame.font.SysFont("freestylescript",40,False,False)
font2=pygame.font.SysFont('elephant', 50, False, False)
msg=font.render("start",True,(0,0,0),None)
msg1=font.render("go on!",True,(0,0,0),None)
msg2=font.render("go back!",True,(0,0,0),None)
msg3=font.render("you find it",True,(0,0,0),None)
msg4 = font.render("Please, respect the rules ",True,(0,0,0),None)
msg_lf = font.render("Life index :",True,(0,0,0),None)
perc = font.render(" %",True,(0,0,0),None)
lost = font2.render("RUN OUT ", True,(255,97,3),None)
win=font2.render("FIND IT ", True,(255,97,3),None)

# la fenetre
pygame.display.set_caption(" Nightmare house ! ")
screen = pygame.display.set_mode((600,650))

# les fct utilisées 
def cal_distance (a , b , c, d ):
        distance=sqrt(pow((a-b),2)+pow((c-d),2))
        return distance
        
def aff_msg(D1, D2):
    
    if D2>D1 :
        screen.blit(msg2,(180,110))
        #game.sound.play('go_back')
        pygame.display.flip()
    elif D2==0:
        screen.blit(msg3,(180,110))
        s1.fill((0, 0, 0, 128))
        #screen.blit(s1, (10, 270))
       
    elif D2<D1 and UP>2 :
        screen.blit(msg1,(180,110))

   
# importation des images       
opening=pygame.image.load("OP1.png").convert()
opening= pygame.transform.scale(opening, (600,650))
background = pygame.image.load('bag.png').convert()
background = pygame.transform.scale(background, (600,650))
story = pygame.image.load("History.png").convert()
rules = pygame.image.load("Rules.png").convert()
heart_1 = pygame.image.load("energy.png").convert_alpha()
s = pygame.Surface((300,100), pygame.SRCALPHA)
s1 = pygame.Surface((400,450), pygame.SRCALPHA)


# liste de life indexe 
heart = [heart_1, heart_1, heart_1, heart_1, heart_1]
z=[180,220,260,300,340]

# importation des class 
game = Game()

# les variables 
a = game.player.rect
b = game.box.rect
life_index = 100 
DOWN = 0
UP = 0
count = 0
count0 = 0 
COUNT = 5
CLOCK = pygame.time.Clock()

# callcule de la distance entre le joueur et la boite 
D1 = cal_distance(a.x , b.x , a.y , b.y)

run = True 

while run : 
    
    #print( "down",DOWN)
    #generation de fenetre d'acceuille 
    if DOWN==0:
        #pygame.display.flip()
        screen.blit(opening,(0,0))
        #game.sound.play('openning')
        pygame.display.flip()
    
    

    #notre jeu commence 
    for event in pygame.event.get():
        
        X= game.player.rect.x
        Y=game.player.rect.y
        
        #fermeture du jeu 
        if event.type == QUIT:
            run = False
            pygame.quit()
        
        if event.type == KEYUP :
            UP += 1 
        
        #if UP < 2 :
            #game.sound.play('intro')
            #pygame.display.flip()

        #if UP < 3 : 
            #screen.blit(msg, (100,70))

        if event.type == KEYDOWN : 
            
            DOWN+=1
            print( "down",DOWN)

            

            if DOWN == 1 :
                screen.blit(story, (0,0))
                #game.sound.play('openning')
                pygame.display.flip()

            if DOWN == 2 : 
                screen.blit(rules, (0,0))
                #game.sound.play('openning')
                pygame.display.flip()

                
            if DOWN > 2 :  

                screen.blit(background, (0,0))
                #screen.blit(game.player.image, game.player.rect)
                s.fill((87,99,98,128))                         
                screen.blit(s, (150,50))
                s1.fill((255, 127, 30, 128))
                #screen.blit(s1, (10, 270))    

                if UP == 2  : 
                    screen.blit(msg, (180,110))

                

                #mouvement de joueur 
                if event.key == K_RIGHT and game.player.rect.x <= 480 and UP > 2 :
                    game.player.move_right()
                    game.sound.play('step')
                if event.key == K_LEFT and game.player.rect.x >= 60 and UP > 2:
                    game.player.move_left()
                    game.sound.play('step')
                if event.key == K_UP and game.player.rect.y>= 350 and UP > 2:
                    game.player.move_up()
                    game.sound.play('step')
                if event.key == K_DOWN and game.player.rect.y<= 500 and UP > 2:
                    game.player.move_down()
                    game.sound.play('step')
                if event.key != KEYDOWN and  event.key != K_RIGHT and event.key != K_LEFT and event.key != K_UP and  event.key != K_DOWN and  event.key != KEYUP and UP > 2 : 
                    screen.blit(msg4 , (80, 2))
            
                print("x :", game.player.rect)
            
                #calcule du nouvel distance et affiche des messsages 
                D2= cal_distance(a.x , b.x , a.y , b.y)
                aff_msg(D1, D2)
                D1 = D2

                

                #life indexe 
                if game.player.rect.x != X or game.player.rect.y != Y :
                    count += 1 
                    print("Count : " , count)
            
                if count == 5:
                    life_index -= 20
                    COUNT -=1 # nombre de count 
                    count = 0 
                    count0+=1
                    print(life_index)
                    heart.remove(heart[COUNT])
                    z.remove(z[COUNT])
                    
                    #if life_index == 0 :

                        #run = False
                
                elif count==0 and count0==0:
                    life_index=100
            
                l_i = font.render(str(life_index),1,(0,0,0))
            
                #affiche des msg et image en relation avec life indexe 
                screen.blit(msg_lf, (180,55))
                screen.blit(l_i, (300,55))
                screen.blit(perc, (340,55))
            
                for i in range (0,len(heart)):
                    screen.blit(heart[i],(z[i],90))
            
               
                #screen.blit(background, (0,0))
                screen.blit(game.player.image, game.player.rect)
                
                if life_index == 0 : 
                    screen.blit(lost,(180,250))
                    run = False 
                if D2==0 :
                    screen.blit(win, (180,250))
                    run = False 
                    #if screen.blit(lost,(200,280)):
                       #Game()
                       #break

                
                #if D2 == 0 : 
                    #run = False 
                #if  a.x == game.box.rect.x and a.y == game.box.rect.y : 
                    #s1.fill((0, 0, 0, 128))
                    #screen.blit(s1, (10, 270))
                    #run = False 

                #if  D2 ==0 :
                    #if event.key == KEYDOWN or event.key == K_RIGHT or event.key == K_LEFT or event.key == K_UP or  event.key == K_DOWN and  event.key == KEYUP : 
                        
                        #a.x = b.x
                        #a.y = b.y  
                        #screen.blit(game.player.image, (a.x, a.y))
                    
                """
                    s1.fill((0, 0, 0, 128))
                    screen.blit(s1, (10, 270))  
                   
                    
                    time.sleep(3)
                    run = False
                    """

                #screen.blit(game.box.image, game.box.rect)
                pygame.display.update()
                

        

          
        

   
