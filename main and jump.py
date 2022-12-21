import pygame
#initialize the game always in the beginning
pygame.init()

#display settings
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("Game 1.0")

#char specs
screenwidth=500
x=50
y=450
width=40
height=60
velocity=5
isjump=False
jumpdist=10
run=True

while run:
    pygame.time.delay(50)
    #check for events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    #rectangle player specs and port to "win" display
    pygame.draw.rect(win,(0, 255, 0), (x,y,width,height))
    #keys mod
    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>velocity:
        x-=velocity
    if keys[pygame.K_RIGHT] and x<screenwidth-width-velocity:
        x+=velocity
    if not isjump:
        if keys[pygame.K_UP] and y>velocity:
            y-=velocity
        if keys[pygame.K_DOWN] and y<screenwidth-height-velocity:
            y+=velocity
        #jump function
        if keys[pygame.K_SPACE]:
            isjump=True
    else:
        if jumpdist>=-10:
            neg=1
            if jumpdist<0:
                neg=-1
            y-= (jumpdist ** 2) * 0.5 * neg
            jumpdist-=1
        else:
            isjump=False
            jumpdist=10


    win.fill((0,0,0))
    #rectangle player specs and port to "win" display
    pygame.draw.rect(win,(255, 0, 0), (x,y,width,height))
    # update with new code
    pygame.display.update()
pygame.quit()