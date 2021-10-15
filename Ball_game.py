import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((700, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
score=0
def new_ball():#функция рисует шары
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
t=randint(2,10)
for ball in range(1,t):
   new_ball()
pygame.display.update()
clock = pygame.time.Clock()
finished = False
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (event.x, event.y) = event.pos
            radius = ((event.x - x) ** 2 + (event.y - y) ** 2) ** 0.5
            if radius <= r:#выполняется, если игрок попал по мячу
                score+=1
                s=str(score)
                print(s, '+1, DGAP is proud for you')
                
            else:
                print('Try again, padawan!')#выполняется, если игрок промахнулся
    for i in range(2,t):
                  new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
