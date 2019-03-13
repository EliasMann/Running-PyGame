import pygame

pygame.init()
screen = pygame.display.set_mode((640, 640))
done = False

class Player(pygame.sprite.Sprite):
    def __init__(self,image,image2,x,y):s
        super().__init__()

        self.image = pygame.image.load('img1.png')
        self.image2 = pygame.image.load('img2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.jumping = False

	def jump(self):
        pass

class Platform(pygame.sprite.Sprite):
    def __init__(self,color,x,y,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y            
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()