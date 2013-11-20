import pygame
from pprint import pprint

class Player(pygame.sprite.Sprite): 
   
    # Liikumine
    xchange = 0
    ychange = 0
 
    # Mitu korda saab parajasti hüpata
    jumps = 2
    
    #elud
    hp = 100
    
    #graafika
    sprite_row = 0
    sprite_column = 0
    scale = 3
    moveleft = False
    moveright = False
    jumping = False
    direction = "left"
    spritewidth = 60
    spriteheight = 100
    sheetedge = 7
    scaledwidth = spritewidth * scale
    scaledheight = spriteheight * scale
    scalededge = sheetedge * scale
    animframes = 4
    frame_count = 0
    def __init__(self,x,y,spritesheet): 
        pygame.sprite.Sprite.__init__(self) 
        
           
        self.right = pygame.transform.scale(pygame.image.load(spritesheet), (548*self.scale,1081*self.scale))
        self.left = pygame.transform.flip(self.right, True, False)
        self.rect = pygame.Rect(x, y, self.scaledwidth, self.scaledheight)
        self.rect.x = x
        self.rect.y = y
    
    #joonistame õige raami spritesheetist
    def draw(self, target_surface):
        self.update()
        if self.direction == "right":
            patch_rect = (self.sprite_column * self.scaledwidth + self.scalededge, self.sprite_row, self.scaledwidth, self.scaledheight)
            target_surface.blit(self.right, (self.rect.x, self.rect.y), patch_rect)
        else:
            patch_rect = (548*self.scale-self.scaledwidth-(self.sprite_column * self.scaledwidth + self.scalededge), self.sprite_row, self.scaledwidth, self.scaledheight)
            target_surface.blit(self.left, (self.rect.x, self.rect.y), patch_rect)            


    # uuendame tegelase asukohta
    def update(self): 
 
        self.scaledwidth = self.spritewidth * self.scale
        self.scaledheight = self.spriteheight * self.scale
        self.scalededge = self.sheetedge * self.scale
         
        # akna äärtest ei saa välja minna
        if self.rect.x <= 0:
            self.rect.x = 0

        if self.rect.x >= 1000-self.scaledwidth:
            self.rect.x = 1000-self.scaledwidth
    

        if self.moveleft:
            self.direction = "left"
            self.rect.x -= 5
            if self.rect.y == 319 or self.rect.y == 274:
                self.sprite_column = 0
                self.sprite_row = 280
                self.spriteheight = 77
                self.spritewidth = 68
                self.animframes = 6
                if self.rect.y == 550-92*3:
                    self.rect.y = 550-self.scaledheight
        elif self.moveright:
            self.direction = "right"
            self.rect.x += 5
            if self.rect.y == 319 or self.rect.y == 274:
                self.sprite_column = 0
                self.sprite_row = 280
                self.spriteheight = 77
                self.spritewidth = 68
                self.animframes = 6
                if self.rect.y == 550-92*3:
                    self.rect.y = 550-self.scaledheight

        else:

            self.sprite_column = 0
            self.spritewidth = 45
            self.spriteheight = 92
            self.sprite_row = 0
            self.sheetedge = 7
            self.animframes = 4
           
        if self.jumping:
            self.animframes = 0
            self.sprite_row = 172*3
            self.spriteheight = 92
            self.spritewidth = 48
            self.sprite_column = 6
            if self.rect.y >= 250 and self.ychange > 0:
                self.jumping = False
            
        # vertikaalne liikumine
        self.rect.y += self.ychange
        

        
        
        #animatsiooni kood
        if self.frame_count >= self.animframes*10-1:
            self.frame_count = 0
        else:
            self.frame_count += 1
        if not self.jumping:
            self.sprite_column = self.frame_count//10

        
    
        self.gravity()     
    # gravitatsioon hüppamise jaoks
    def gravity(self):
        self.ychange += .55
        # kontroll kas tegelane on maa peal või õhus
        if self.rect.y >= 550-self.scaledheight and self.ychange >= 0:
            self.ychange = 0
            self.rect.y = 550-self.scaledheight
            self.jumps = 2
 
    # hüppamine (tegin double jumpiga et oleks huvitavam)
    def jump(self):
        if self.jumps >= 1:
            self.ychange = -10
            self.jumping = True
            self.jumps -= 1
    
    def dist(self, other):
        return abs(self.rect.x-other.rect.x)
    
    # kaks erinevat lööki, kiire ja lühikese ulatusega ning aeglane ja pika ulatusega        
    def fast(self, other):
        if self.dist(other) <= 100:
            other.hp -= 10
        print(other.hp)
        self.anim_frame_count = 5
    def slow(self, other):
        if self.dist(other) <= 150:
            other.hp -= 20
        print(other.hp)
 
pygame.init() 
window=[1000,600] 
screen=pygame.display.set_mode(window) 
pygame.display.set_caption("Kaklus") 
all_sprites = pygame.sprite.Group()

    
frame0 = pygame.image.load("frame_000.gif").convert()
frame1 = pygame.image.load("frame_001.gif").convert()
frame2 = pygame.image.load("frame_002.gif").convert()
frame3 = pygame.image.load("frame_003.gif").convert()
frame4 = pygame.image.load("frame_004.gif").convert()
frame5 = pygame.image.load("frame_005.gif").convert()
frame6 = pygame.image.load("frame_006.gif").convert()
frame7 = pygame.image.load("frame_007.gif").convert()
   
# loon 2 tegelast kasutades Player klassi
player1 = Player(500,285,"surge2.png")


all_sprites.add(player1)

player2 = Player(100,285,"black2.png")

all_sprites.add(player2)

done = False
clock = pygame.time.Clock() 

frame = 0
background = frame0

# main loop
while not done: 
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1.moveleft = True
                player1.moveright = False
            if event.key == pygame.K_RIGHT:
                player1.moveright = True
                player1.moveleft = False
            if event.key == pygame.K_UP:
                player1.jump()
            if event.key == pygame.K_l:
                player1.fast(player2)
                 
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT: 
                player1.moveleft = False
            if event.key == pygame.K_RIGHT: 
                player1.moveright = False
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player2.moveleft = True
                player2.moveright = False
            if event.key == pygame.K_d:
                player2.moveright = True
                player2.moveleft = False
            if event.key == pygame.K_w:
                player2.jump()
                 
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_a: 
                player2.moveleft = False
            if event.key == pygame.K_d: 
                player2.moveright = False
                
 


    
    if frame == 48:
        frame = 0
    else:
        frame += 1
    
    if frame == 0:
        background = frame0
    elif frame == 6:
        background = frame1
    elif frame == 12:
        background = frame2
    elif frame == 18:
        background = frame3
    elif frame == 24:
        background = frame4
    elif frame == 30:
        background = frame5
    elif frame == 36:
        background = frame6
    elif frame == 42:
        background = frame7


    screen.blit(background, (0,0))
    pprint(vars(player1))
    for sprite in all_sprites:
        sprite.draw(screen)

    pygame.display.flip() 
    clock.tick(120) 

pygame.quit ()
