import math
from random import choice
from random import randint as rnd
import pygame

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
g = 2


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):

        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):

        self.vy = (self.vy - g) * 0.99
        self.vx = 0.98 * self.vx
        self.x += self.vx
        self.y -= self.vy - g / 2
        if self.x > 800 - self.r:
            self.vx = -self.vx * 0.8
            self.x = 800
        if self.x < self.r:
            self.vx = -self.vx * 0.8
            self.x = 0
        if self.y > 500:
            self.vy = - self.vy * 0.8
            self.y = 500

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):

        return( int((obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= (obj.r + self.r) ** 2))

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self):
        self.f2_on = 1

    def fire2_end(self, event):

        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5

        self.an = -math.atan2((event.pos[1] - 450), (event.pos[0] - 40))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)

        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):

        if event:
            self.an = -math.atan2((event.pos[1] - 450), (event.pos[0] - 40))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        delta = 40 + self.f2_power
        pygame.draw.polygon(self.screen, GREY,((40, 450), (40 + delta * math.cos(self.an), 450 - delta * math.sin(self.an)),(40 + delta * math.cos(self.an) - 10 * math.sin(self.an),450 - delta * math.sin(self.an) - 10 * math.cos(self.an)),(40 - 10 * math.sin(self.an),450 - 10 * math.cos(self.an))))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:


    def __init__(self):

        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(2, 50)
        self.vx = rnd(-10, 10)
        self.vy = rnd(-10, 10)
        self.color = RED
        self.points = 0
        self.live = 1

    def move(self):
        self.x += self.vx
        self.y -= self.vy
        if self.x > 800 - self.r:
            self.vx = -self.vx
            self.x = 800 - self.r
        if self.x < self.r:
            self.vx = -self.vx
            self.x = self.r
        if self.y > 500:
            self.vy = - self.vy
            self.y = 500
        if self.y < self.r:
            self.vy = - self.vy
            self.y = self.r

    def hit(self, points = 1):
        self.points += points

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
targets = [Target(),Target(),Target()]
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()

    for obj in targets:
        obj.draw()
    for b in balls:

        if b.vx ** 2 + b.vy ** 2 > 3 or b.y < 485 + b.r :
            b.draw()

    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:

        b.move()

        for obj in targets:
            if b.hittest(obj) and obj.live == True:
                obj.live = 0
                obj.hit()
                obj.__init__()

    for obj in targets:
        obj.move()

    gun.power_up()
pygame.quit()