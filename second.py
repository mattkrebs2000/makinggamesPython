import pygame
import sys
pygame.init()
sur_obj=pygame.display.set_mode((400,300))
pygame.display.set_caption("Rectangle")
sta_img=pygame.image.load("star.png")
sur_obj.blit(sta_img,(1,2))
while True:
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()