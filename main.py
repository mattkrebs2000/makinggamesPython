import os
import sys, pygame
from random import randint

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
Black = (0,0,0)
speed = [1,1]

BALL_WIDTH, BALL_HEIGHT = 55, 55
FPS = 60
blue = 0 , 0, 255

ballImage = pygame.image.load(os.path.join('Assets', 'ball.png'))
ball = pygame.transform.scale(ballImage, (BALL_WIDTH, BALL_HEIGHT))

RECTANGLE = pygame.Surface((100,50))
bar = pygame.Surface((200,50)) 
pygame.draw.rect(bar,blue,(0,0,200,50))
pygame.draw.rect(RECTANGLE, blue, (0,0,95,50))


def draw_window(ballPosition, barPosition):
    WIN.fill(Black)
    WIN.blit(ball, (ballPosition.x, ballPosition.y))
    WIN.blit(bar, (barPosition.x, HEIGHT - 50)) 
    WIN.blit(RECTANGLE, (100,50)) 
    WIN.blit(RECTANGLE, (200,50))
    WIN.blit(RECTANGLE, (300,50))
    
    
    
    pygame.display.update()
    
def moveBall(ballPosition):
    ballPosition.x += speed[0]
    ballPosition.y += speed[1]
    
    if ballPosition.left < 0 or ballPosition.right > WIDTH:
        speed[0] = -speed[0]
    if ballPosition.top < 0 or ballPosition.bottom > HEIGHT:
        speed[1] = -speed[1]
    
    
def moveBar(barPosition):
    pygame.event.pump()  # Allow pygame to handle internal actions.
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        barPosition.x -= 5

    if key[pygame.K_RIGHT]:
        barPosition.x += 5
        
        
    
pygame.display.set_caption("First Game!")

def main():
    
    ballPosition = pygame.Rect(100,300,50,50)
    barPosition = pygame.Rect(500,300,200,50)
    
    clock = pygame.time.Clock()
    
    run = True
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        
        moveBar(barPosition)
        
        moveBall(ballPosition)
        
        draw_window(ballPosition, barPosition)
        
    pygame.quit()



if  __name__ == "__main__":
    main()

# import os
# import sys, pygame

# pygame.init()
# from pygame import K_RETURN, K_a


# size = width, height = 820, 640
# speed = [1,1]
# black = 0, 0, 0
# blue = 0 , 0, 255
# BALL_WIDTH, BALL_HEIGHT = 55, 55
# barpositionbegin = 200
# barwidth = 100
# barheight = 40
# barbegins = 600
# barends = barpositionbegin + barwidth
# newheight = height + 10
# VEL = 5


   




# # def bar_handle_movement(keys_pressed, barpositionbegin, VEL, width, barwidth):
# #     count = bluebar.x
# #     if keys_pressed[pygame.K_SPACE]: 
        
# #         print(count)
        
        
        
    
    
    
    
#     # if keys_pressed[pygame.K_SPACE]:  # LEFT
#     #     newvar -= VEL
#     #     print(newvar)
#     # if keys_pressed[pygame.K_a]:  # RIGHT
#     #     newvar += VEL
#     #     print(newvar)
    





# screen = pygame.display.set_mode(size)



# ballImage = pygame.image.load(
#     os.path.join('Assets', 'ball.png'))
# ball = pygame.transform.rotate(pygame.transform.scale(
#     ballImage, (BALL_WIDTH, BALL_HEIGHT)), 90)


# ballrect = ball.get_rect()

    
# bluebar = pygame.draw.rect(screen,blue,(barpositionbegin, barbegins, barwidth, barheight))


# while 1:
  
#     # for event in pygame.event.get():
#     #     if event.type == pygame.QUIT: sys.exit()


#     ballrect = ballrect.move(speed)
#     ballposition = ballrect.left
    
#     if barpositionbegin < ballposition < barends:
#         floor = newheight - barheight
#     else: 
#         floor = newheight
    
    
#     if ballrect.left < 0 or ballrect.right > width:
#         speed[0] = -speed[0]
#     if ballrect.top < 0 or ballrect.bottom > floor:
#         speed[1] = -speed[1]
        
#     # ballposition = ballrect.left
    
        
    
    
    
#     # print(bluebar.x)
#     # bluebar.x +=1
#     # print(bluebar.x)
    
    
#     # keys_pressed = pygame.key.get_pressed()
    
#     # bar_handle_movement(keys_pressed, barpositionbegin, VEL, width, barwidth)
        
    
    
   
    
#     screen.blit(ball, ballrect)
#     pygame.display.flip()









