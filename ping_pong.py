from pygame import *



#window settings
back = (200,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_height,win_width))
window.fill(back)

clock = time.Clock()
FPS = 60
game = True



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    

    display.update 
    clock.tick(FPS)
