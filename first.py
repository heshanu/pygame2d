#import pygame
#pygame.init()
#win = pygame.display.set_mode((500, 500))
#pygame.display.set_caption("First Game")

# This goes outside the while loop, near the top of the program
#walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
#walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
#bg = pygame.image.load('bg.jpg')
#char = pygame.image.load('standing.png')

#x = 50

#y = 50
#width = 64
#height = 64
#vel = 10
#isJump = False
#jumpCount = 10
#left = False
#right = False
#walkCount = 0


#def redrawGameWindow():
 #   global walkCount
  #  win.plit(bg, (0, 0))
   # pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    #pygame.display.update()

#run = True
#while True:
 #   pygame.time.delay(100)
  #  for event in pygame.event.get():
   #     if event.type == pygame.QUIT:
    #        run = False
    #keys = pygame.key.get_pressed()

    #if keys[pygame.K_LEFT and x > vel]:
     #   x -= vel
      #  left = True
       # right = False

    #elif keys[pygame.K_RIGHT] and x < 500-width-vel:
     #   x += vel
      #  left = False
       # right = True
    #else:
     #   right = False
       # left = False
      #  walkCount = 0

    #if not(isJump):
    #    if keys[pygame.K_SPACE]:
     #       isJump = True
      #      right = False
       #     left = False
        #    walkCount = 0
   # else:
    #   if jumpCount >= -10:
     #       neg = 1
     #       if jumpCount < 0:
      #          neg -= 1






    #redrawGameWindow()

    #win.fill((0, 0, 0))
    #pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    #pygame.display.update()

#pygame.quit()

import pygame

pygame.init()

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

x = 50
y = 400
width = 40
height = 60
vel = 5

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0


def redrawGameWindow():
    global walkCount

    win.blit(bg, (0, 0))
    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0

    pygame.display.update()


run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel
        left = False
        right = True

    else:
        left = False
        right = False
        walkCount = 0

    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    redrawGameWindow()

pygame.quit()
