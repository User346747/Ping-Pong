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

class DefaultSprite():

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


class Ball(DefaultSprite):

    def __init__(self, x, y, width, height, filename, speed):
        super().__init__(x, y, width, height, filename)
        self.speed = speed
        self.rotate = 60
    
    def move(self):

        if self.rotate == 60:
            self.rect.x += self.speed
            self.rect.y += self.speed
        elif self.rotate == 240:
            self.rect.x -= self.speed
            self.rect.y -= self.speed

        if self.rect.y >= WINDOW_SIZE[1]:
            self.rotate = 240

        if self.rect.y <= 0:
            self.rotate = 60

ball = Ball(0, 0, 50, 50, "ball.jpg", 1)

while game:
    clock.tick(FPS)

    ball.update()

    keys = pygame.key.get_pressed()
    ball.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    pygame.display.update()