import pygame
pygame.init()

WINDOW_SIZE = (700, 500)
FPS = 60
game = True
#BACKGROUND_IMAGE = "background.jpg"

window = pygame.display.set_mode(WINDOW_SIZE)
window.fill((123,123,123))
pygame.display.set_caption("PING PONG")
clock = pygame.time.Clock()
#background = pygame.transform.scale(pygame.image.load(BACKGROUND_IMAGE), WINDOW_SIZE)

class DefaultSprite(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, filename):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.filename = filename
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

while game:
    clock.tick(FPS)

    #window.blit(background, (0,0))

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    pygame.display.update()