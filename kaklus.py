import pygame

class Player(pygame.sprite.Sprite): 
   
    # Liikumise kiirus
    xchange = 0
    ychange = 0
 
    # Mitu korda saab parajasti hüpata
    jumps = 2
    
    #elud
    hp = 100
    
    #graafika
    sprite_row = 0
    sprite_column = 0
    frame_count = 0
    
    def __init__(self,x,y): 
        pygame.sprite.Sprite.__init__(self) 
        
           
        self.image = pygame.image.load("sprites.gif")
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
    
    #joonistame õige raami spritesheetist
    def draw(self, target_surface):
        patch_rect = (self.sprite_column * 50+273, self.sprite_row*50, 50, 85)
        target_surface.blit(self.image, (self.rect.x, self.rect.y), patch_rect)

    # uuendame tegelase asukohta
    def update(self): 
 
        # horisontaalne liikumine
        self.rect.x += self.xchange
         
        # akna äärtest ei saa välja minna
        if self.rect.x <= 0 and self.xchange != 0:
            self.xchange = 0
            self.rect.x = 0

        if self.rect.x >= 785 and self.xchange != 0:
            self.xchange = 0
            self.rect.x = 785

 
        # vertikaalne liikumine
        self.rect.y += self.ychange
        
        
        # ajutine kood, kasutan 3 raami mingist suvalisest spritesheetist mis ma leidsin et anda tegelasele animatsioon
        if self.frame_count == 29:
            self.frame_count = 0
        else:
            self.frame_count += 1
        
        if self.frame_count <= 9:
            self.sprite_column = 0
        elif self.frame_count <= 19:
            self.sprite_column = 1
        else:
            self.sprite_column = 2
        
         
    # gravitatsioon hüppamise jaoks
    def gravity(self):
        self.ychange += .85
        # kontroll kas tegelane on maa peal või õhus
        if self.rect.y >= 500 and self.ychange >= 0:
            self.ychange = 0
            self.rect.y = 500
            self.jumps = 2
 
    # hüppamine (tegin double jumpiga et oleks huvitavam)
    def jump(self):
        if self.jumps >= 1:
            self.ychange = -10
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
window=[800,600] 
screen=pygame.display.set_mode(window) 
pygame.display.set_caption("Kaklus") 
all_sprites = pygame.sprite.Group()
   
# loon 2 tegelast kasutades Player klassi ning määran nende asukohad
player1 = Player(100,100)
player1.rect.x = 500
player1.rect.y = 485
all_sprites.add(player1)

player2 = Player(100,100)
player2.rect.x = 100
player2.rect.y = 485
all_sprites.add(player2)

done = False
clock = pygame.time.Clock() 




# main loop
while not done: 
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1.xchange -= 5
            if event.key == pygame.K_RIGHT:
                player1.xchange += 5
            if event.key == pygame.K_UP:
                player1.jump()
            if event.key == pygame.K_l:
                player1.fast(player2)
                 
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT: 
                player1.xchange += 5
            if event.key == pygame.K_RIGHT: 
                player1.xchange -= 5
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player2.xchange -= 5
            if event.key == pygame.K_d:
                player2.xchange += 5
            if event.key == pygame.K_w:
                player2.jump()
                 
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_a: 
                player2.xchange += 5
            if event.key == pygame.K_d: 
                player2.xchange -= 5
                
 

    player1.gravity()
    player1.update() 
    player2.gravity()
    player2.update()
      
    screen.fill([0,0,0])
   

   
    for sprite in all_sprites:
        sprite.draw(screen)

    pygame.display.flip() 
    clock.tick(60) 

pygame.quit ()
