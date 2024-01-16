import pygame
import time
from random import randint
pygame.init()


back = (155, 0, 0)
mv = pygame.display.set_mode((500,500))
mv.fill(back)
clock = pygame.time.Clock()

class Area():
    def __init__(self, x=0, y=0, width =10, height =10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mv,self.fill_color,self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width =10, height =10,):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
    def draw(self):
        mv.blit(self.image, (self.rect.x, self.rect.y))

platform_x = 200
platform_y = 260

ball = Picture("ball.png", 160, 200, 50,50)
platform = Picture("platform.png", platform_x, platform_y, 100, 30)

monsters_x=5
monsters_y=5
count=9
monsters=[]

for j in range(3):
    y = monsters_y+(55*j)
    x = monsters_x+(28*j)
    for i in range(count):
        monster = Picture("enemy.png", x, y, 50, 50)
        monsters.append(monster)
        x = x + 55
    count = count - 1


game_over = False

ball_speed_x = 3
ball_speed_y = 3

while not game_over:
    ball.fill()
    platform.fill()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over = True
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and platform.rect.x>0:
        platform.rect.x -= 5
    if keys[pygame.K_RIGHT] and platform.rect.x<400:
        platform.rect.x += 5

    ball.rect.x+=ball_speed_x
    ball.rect.y+=ball_speed_y

    if ball.rect.x <= 0 or ball.rect.x >= 450:
        ball_speed_x = -ball_speed_x
    if ball.rect.y <= 0 or ball.rect.y >= 450:
        ball_speed_y = -ball_speed_y
    if ball.rect.colliderect(platform.rect):
        ball_speed_y=-ball_speed_y

    mv.fill(back)
    
    for m in monsters:
        m.draw()
    
        if m.rect.colliderect(ball.rect):
            monsters.remove(m)
            ball_speed_y=-ball_speed_y

    

    if not monsters:
        font1=pygame.font.Font(None, 45)
        text1 = font1.render("YOU WIN!!!", True,(0, 200, 0))
        mv.blit(text1,(200, 200))
        pygame.display.update()
        game_over = True

    ball.draw()
    platform.draw()

    if ball.rect.y > 350:
        font = pygame.font.Font(None, 45)
        text = font.render("YOU LOSE", True, (255,0,0))
        mv.blit(text,(200,200))
        pygame.display.update()
        game_over = True



    pygame.display.update()
    clock.tick(40)
