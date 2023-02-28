import pygame

pygame.init()
pygame.display.set_caption("space invaders")
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
gameover = False

#player variables-----------------------
xpos = 400
ypos = 750
moveLeft = False
moveRight = False


class Alien:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = True
    def draw(self):
        pygame.draw.rect(screen,(250,250,250),(self.xpos,self.ypos,40,40))
        
armada = []
for i in range(2):
    for j in range(4):
        armada.append(Alien(j*60+50, i*50+50))


while not gameover:
    clock.tick(60)
    
    #Input Section----------------------------------------------------
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
            
        if event.type == pygame.KEYDOWN:import pygame

pygame.init()
pygame.display.set_caption("space invaders")
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
gameover = False

#player variables-----------------------
xpos = 400
ypos = 750
moveLeft = False
moveRight = False


class Alien:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = True
    def draw(self):
        pygame.draw.rect(screen,(250,250,250),(self.xpos,self.ypos,40,40))
        
armada = []
for i in range(2):
    for j in range(4):
        armada.append(Alien(j*60+50, i*50+50))


while not gameover:
    clock.tick(60)
    
    #Input Section--------------------------------
            if event.key == pygame.K_LEFT:
                moveLeft = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveLeft = False
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveRight = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moveRight = False
        
    
    #physics--------------------------------------------------------
    
    if moveLeft == True:
        vx =-3
    elif moveRight == True:
        vx = 3
    else:
        vx = 0
        
    xpos+=vx
    
    
    #RENDER------------------------------------------------------------------
    
    screen.fill((0,0,0))
    
    for i in range (len(armada)):
        armada[i].draw()
    
    pygame.draw.rect(screen,(0,255,0), (xpos,ypos,60,20))
    pygame.draw.rect(screen,(0,255,0), (xpos+5,ypos-5,50,25))
    pygame.draw.rect(screen,(0,255,0), (xpos+25,ypos-15,10,30))
    
    pygame.display.flip()

#end loop########################################################################
    
pygame.quit()
