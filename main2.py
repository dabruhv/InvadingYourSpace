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
timer = 0
shoot = False


class Alien:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = True
        self.direction = 1
    def draw(self):
        pygame.draw.rect(screen,(250,250,250),(self.xpos,self.ypos,40,40))
    def move(self,time):
        if time % 300 == 0:
            self.ypos += 50
            self.direction *= -1
            return 0
        
        if time%100==0:
            self.xpos+=50*self.direction
        
        return time
    
class Bullet:
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = False
    
    def move(self,xpos,ypos):
        if self.isAlive == True:
            self.ypos-=5
        if self.ypos<0:
            self.isAlive = False
            self.xpos = xpos
            self.ypos = ypos
    def draw(self):
        pygame.draw.rect(screen,(250,250,250),(self.xpos, self.ypos,3,20))
        
bullet = Bullet(xpos+28,ypos)
        
armada = []
for i in range(4):
    for j in range(9):
        armada.append(Alien(j*80+30, i*80+50))


while not gameover:
    clock.tick(60)
    timer += 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
    
    
    #Input Section--------------------------------
        if event.type == pygame.KEYDOWN:
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
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                shoot = False
        
    
    #physics--------------------------------------------------------
                
    for i in range (len(armada)):
        armada[i].move(timer)
        
        
    if shoot == True:
        bullet.Alive = True
    
    if bullet.isAlive == True:
        bullet.move(xpos+28,ypos)
    
    else:
        bullet.xpos = xpos +28
        bullet.ypos = ypos
    
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
        
    bullet.draw()#left off here slide 17
    
    pygame.draw.rect(screen,(0,255,0), (xpos,ypos,60,20))
    pygame.draw.rect(screen,(0,255,0), (xpos+5,ypos-5,50,25))
    pygame.draw.rect(screen,(0,255,0), (xpos+25,ypos-15,10,30))
    
    pygame.display.flip()

#end loop########################################################################
    
pygame.quit()
