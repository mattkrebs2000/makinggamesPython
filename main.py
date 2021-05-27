import os
import sys, pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
Black = (0,0,0)

BALL_WIDTH, BALL_HEIGHT = 55, 55
FPS = 60

speed = [1,1]
blue = 0 , 0, 255
barpositionbegin = 200
barwidth = 100
barheight = 40
barbegins = 600
barends = barpositionbegin + barwidth
# newheight = height + 10
VEL = 5




ballImage = pygame.image.load(os.path.join('Assets', 'ball.png'))
ball = pygame.transform.rotate(pygame.transform.scale(ballImage, (BALL_WIDTH, BALL_HEIGHT)), 90)
ballrect = ball.get_rect()

bar = pygame.Surface((100,200)) 
pygame.draw.rect(bar,(0,255,255),(20,20,40,40))


def draw_window():
    WIN.fill(Black)
    WIN.blit(ball, ballrect)
    WIN.blit(bar,(200,400)) 
    pygame.display.update()
    


pygame.display.set_caption("First Game!")

def main():
    clock = pygame.time.Clock()
    
    run = True
    
  
    
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

        
        
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


   




# def bar_handle_movement(keys_pressed, barpositionbegin, VEL, width, barwidth):
#     count = bluebar.x
#     if keys_pressed[pygame.K_SPACE]: 
        
#         print(count)
        
        
        
    
    
    
    
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
  
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()


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
    
    
#     keys_pressed = pygame.key.get_pressed()

    
#     bar_handle_movement(keys_pressed, barpositionbegin, VEL, width, barwidth)
        
    
    
   
    
#     screen.blit(ball, ballrect)
  
#     pygame.display.flip()









