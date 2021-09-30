import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
circle(screen,(255, 255, 0),(200,200),200)
circle(screen,(255, 0, 0),(100,150),35)
circle(screen,(255, 0, 0),(300,150),35)
circle(screen,(0, 0, 0),(100,150),10)
circle(screen,(0, 0, 0),(300,150),10)
rect(screen, (0,0,0,),(100,250,200,50))
polygon(screen, (0,0, 0), [(70,100), (50,75),(120,75),(200,180)])
polygon(screen, (0,0, 0), [(330,100), (350,75),(280,75),(200,180)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()