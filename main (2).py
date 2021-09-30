import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 800))
rect(screen, (192, 192, 192 ), (0, 800, 400, 400))
rect(screen, (192,192, 192), (0, 0, 400, 270))
ellipse(screen, (0,0,0), (0,0,200,100))
ellipse(screen, (150,150,150), (100,50,300,100))
polygon(screen, (40,50, 0), [(0,100), (30,75),(120,75),(150,100)])
circle(screen, (192, 192, 192), (350, 400), 25)
circle(screen, (0, 0, 0), (335, 400), 5)
circle(screen, (0, 0, 0), (350, 400), 5)
circle(screen, (255, 255,255), (350, 50), 25)
ellipse(screen, (191,191,191), (320,410,30,90))
ellipse(screen, (191,191,191), (310,405,30,90))
ellipse(screen, (191,191,191), (330,410,30,90))
ellipse(screen, (191,191,191), (340,410,30,90))
ellipse(screen, (191,191,191), (350,410,30,90))
rect(screen, (184, 134, 60), (0,100,150,250))
rect(screen, (200, 134, 60), (15,300,30,30))
rect(screen, (200, 134, 60), (60,300,30,30))
rect(screen, (255, 134, 60), (105,300,30,30))
rect(screen, (150, 150, 150), (0,200,180,30))
rect(screen, (150, 150, 80), (10,120,20,60))
rect(screen, (150, 150, 80), (40,120,20,60))
rect(screen, (150, 150, 80), (70,120,20,60))
rect(screen, (150, 150, 80), (100,120,20,60))
rect(screen, (150, 150, 150), (20,170,10,60))
rect(screen, (150, 150, 150), (0,170,10,40))
rect(screen, (150, 150, 150), (40,170,10,40))
rect(screen, (150, 150, 150), (60,170,10,40))
rect(screen, (150, 150, 150), (80,170,10,40))
rect(screen, (150, 150, 150), (100,170,10,40))
rect(screen, (150, 150, 150), (120,170,10,40))
rect(screen, (150, 150, 150), (140,170,10,40))
rect(screen, (150, 150, 150), (160,170,10,40))
rect(screen, (150, 150, 150), (0,160,180,10))
rect(screen, (150, 150, 150), (10,30,20,60))
rect(screen, (150, 150, 150), (60,30,10,50))
circle(screen, (192, 192, 192), (150, 400), 25)
circle(screen, (0, 0, 0), (135, 400), 5)
circle(screen, (0, 0, 0), (150, 400), 5)
ellipse(screen, (191,191,191), (110,405,30,90))
ellipse(screen, (191,191,191), (130,410,30,90))
ellipse(screen, (191,191,191), (140,410,30,90))
ellipse(screen, (191,191,191), (150,410,30,90))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()