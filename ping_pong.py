from pygame import *
'''Required classes'''

#parent class for sprites
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #e.g. 55,55 - parameters
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

#game scene:
back = (200, 255, 255) #background color (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

#flags responsible for game state
game = True
finish = False
clock = time.Clock()
FPS = 60

#creating ball and paddles   
racket1 = Player('player.png', 30, 200, 4, 50, 150) 
racket2 = Player('player.png', 520, 200, 4, 50, 150)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)

#ball speed
speed_x = 3
speed_y = 3

font.init()
font1 = font.Font(None,35)
lose1 = font1.render('PLAYER 1 LOSES!', True, (180, 0 , 0))
lose2 = font1.render('PLAYER 2 LOSES!', True,(180, 0 , 0))



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_2()
        racket2.update_1()

        racket1.reset()
        racket2.reset()
        ball.reset()

        #ball movement
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        #racket collide
        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1


        #ground collide
        if ball.rect.y > win_height -50 or ball.rect.y < 0:
            speed_y *= -1



        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200.200))
        if ball.rect.x > 600:
            finish = True
            window.blit(lose2, (200,200))
        

    display.update()
    clock.tick(FPS)



