import pygame 
from pygame import *
from time import time as timer

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong 2V2')
RED = (0, 255, 0)
window.fill(RED)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

player = Player('racket.jpg', 0, 235, 3, 50, 150)
player2 = Player('racket.jpg', 650, 235, 3, 50, 150)

class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(80, 620)
            lost = lost + 1

#ball = Ball('ball.jpg', 50, 250, 3, 10, 10)

run = True
finish = False
clock = time.Clock()
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.fill(RED)
        player.update1()
        player.reset()
        player2.update2()
        player2.reset()
        #ball.reset()
        #ball.update()

    display.update()
    clock.tick(60)