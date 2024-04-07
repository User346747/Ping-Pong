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
        self.speed_x = speed
        self.speed_y = speed
    
    def move(self):

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y >= WINDOW_SIZE[1]:
            self.speed_y *= -1

        if self.rect.y <= 0:
            self.speed_y *= -1


class Platform(DefaultSprite):

    def __init__(self, x, y, width, height, filename, id):
        super().__init__(x, y, width, height, filename)
        self.id = id
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 0 and self.id == 1:
            self.rect.y -= 3
        if keys[pygame.K_s] and self.rect.y < 450 and self.id == 1:
            self.rect.y += 3
        if keys[pygame.K_UP] and self.rect.y > 0 and self.id == 2:
            self.rect.y -= 3
        if keys[pygame.K_DOWN] and self.rect.y < 450 and self.id == 2:
            self.rect.y += 3

ball = Ball(250, 350, 50, 50, "ball.jpg", 1)
platform1 = Platform(50, 100, 10, 50, "platform.png", 1)
platform2 = Platform(650, 100, 10, 50, "platform.png", 2)
finish = False
txt = pygame.font.SysFont("Arial", 40)
text = txt.render("Game Over!", True, (255,255,255))

while game:
    clock.tick(FPS)

    window.fill((123,123,123))

    if not finish:
        platform1.move()
        platform1.update()
        platform2.move()
        platform2.update()

        if pygame.sprite.collide_rect(platform1, ball) or pygame.sprite.collide_rect(platform2, ball):
            ball.speed_x *= -1
    
        if ball.rect.x < 0 or ball.rect.x > WINDOW_SIZE[0]:
            finish = True
        
        ball.move()
        ball.update()
    else:
        window.blit(text, (250, 350))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    pygame.display.update()