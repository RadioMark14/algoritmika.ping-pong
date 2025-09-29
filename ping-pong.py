from pygame import *
from time import time as timer

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong 2V2')
WHITE = (255, 255, 255)
window.fill(WHITE)

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
        ball.rect.x += speed_x
        ball.rect.y += speed_y

ball = Ball('ball.jpg', 300, 250, 3, 50, 50)

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOST!', True, (185, 0, 0))
lose2 = font1.render('PLAYER 2 LOST!', True, (180, 0, 0))

run = True
finish = False
clock = time.Clock()
speed_x = 3
speed_y = 3
score1 = 0
score2 = 0
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.fill(WHITE)
        player.update1()
        player.reset()
        player2.update2()
        player2.reset()
        ball.reset()
        ball.update()

       
        score_text = font1.render("Player 1: {score1}  |  Player 2: {score2}", True, (0, 0, 0))
        window.blit(score_text, (230, 20))

        
        if ball.rect.y <= 0 or ball.rect.y >= win_height - ball.rect.height:
            speed_y *= -1 

     
        if sprite.collide_rect(player, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1

        
        if ball.rect.x < 0:
            score2 += 1
            finish = True
            window.blit(lose1, (200, 200))

        
        if ball.rect.x > win_width:
            score1 += 1
            finish = True
            window.blit(lose2, (200, 200))

    else:
        
        display.update()
        time.delay(1500)

        finish = False
        speed_x = 3
        speed_y = 3

        player = Player('racket.jpg', 0, 235, 3, 50, 150)
        player2 = Player('racket.jpg', 650, 235, 3, 50, 150)
        ball = Ball('ball.jpg', 300, 250, 3, 50, 50)

    display.update()
    clock.tick(60)
