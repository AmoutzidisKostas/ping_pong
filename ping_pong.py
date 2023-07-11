from pygame import * 

#window settings
back = (200,255,255)
win_width = 500
win_height = 600
window = display.set_mode((win_height,win_width))
window.fill((200,255,255))



clock = time.Clock()
FPS = 60
game = True

#file names
player_image = 'player.png'
ball_image = 'ball.png'

#classes 
class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80 :
            self.rect.y += self.speed

    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80 :
            self.rect.y += self.speed
''' 
class Ball(GameSprite):
    def ball_update(self):
        if self.direction == "left":
            self.rect.x -= self.speed
        if self.direction == "right":
            self.rect.x += self.speed
'''
player1 = Player(player_image,30,200,50,150,4)
player2 = Player(player_image,520,200,50,150,4)
#ball = Ball(ball_image,200,200,50,50,4)



while game:

    window.fill(back)

    player1.reset()
    player1.update1()
    player2.reset()
    player2.update2()

    for e in event.get():
        if e.type == QUIT:
            game = False
    

    display.update()
    clock.tick(FPS)
