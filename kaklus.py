import pygame

class Player(pygame.sprite.Sprite): 
   
    # Liikumise kiirus
    xchange = 0
    ychange = 0
 
    # Mitu korda saab parajasti hüpata
    jumps = 2
    
    #elud
    hp = 100
 
    def __init__(self, x, y): 
        pygame.sprite.Sprite.__init__(self) 
           
        # tegelase kujutise loomine
        self.image = pygame.Surface([15, 15]) 
        self.image.fill([255,255,255])
   
        # asukoha määramine
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
       
    # Leiame kus tegelane parajasti on
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
    
    # kaks erinevat lööki, kiire ja lühikese ulatusega ning aeglane ja pika ulatusega        
    def fast(self):
        0
    def slow(self):
        0
 
pygame.init() 
window=[800,600] 
screen=pygame.display.set_mode(window) 
pygame.display.set_caption("Kaklus") 
all_sprites = pygame.sprite.Group()
   
# loon 2 tegelast kasutades Player klassi ning määran nende asukohad
player1 = Player(20, 15)
player1.rect.x = 500
player1.rect.y = 485
all_sprites.add(player1)

player2 = Player(20, 15)
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
   
    all_sprites.draw(screen)

    pygame.display.flip() 
    clock.tick(60) 

pygame.quit ()
