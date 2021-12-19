import pygame
import pygame.draw
from random import randint

pygame.init()
font = pygame.font.SysFont('arial', 50)
FPS = 50
width = 1000
length = 500
min_ball_size = 50
max_ball_size = 150

# создание дисплея
screen = pygame.display.set_mode((width, length))
name = input('Your name: ')

# цвета текста и фона соответственно
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# создание шаров
class Balls(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        if randint(0, 1) == 0:
            self.image = pygame.image.load('ball1.png')
            self.coefficient_of_lack = 2
        else:
            self.image = pygame.image.load('ball2.png')
            self.coefficient_of_lack = 1
        # задает начальные координаты шаров и их скорости трансформирует картинки
        self.rect = self.image.get_rect()
        self.rect.x = randint(max_ball_size, width - max_ball_size)
        self.rect.y = randint(max_ball_size, length - max_ball_size)
        self.scal = randint(min_ball_size, max_ball_size)
        self.image = pygame.transform.scale(self.image, (self.scal, self.scal))
        self.v_x = randint(-3, 3)
        self.v_y = randint(-3, 3)

    # движение с отраженим от стен, стирание шаров
    def update(self):
        if self.rect.x + self.v_x <= 0 or self.rect.x + self.v_x >= width - self.scal:
            self.v_x = -self.v_x
        if self.rect.y + self.v_y <= 0 or self.rect.y + self.v_y >= length - self.scal:
            self.v_y = -self.v_y
        self.rect.x += self.v_x
        self.rect.y += self.v_y
        if (randint(1, 40) == 1):
            self.kill

    # определяет, попал ли пользователь по шару
    def check(self, coords):
        x_m = coords[0]
        y_m = coords[1]
        if x_m >= self.rect.x and x_m <= self.rect.x + self.scal:
            condition_x = True

        else:
            condition_x = False

        if self.rect.y <= y_m and self.rect.y + self.scal >= y_m:
            condition_y = True

        else:
            condition_y = False

        if condition_x and condition_y:
            return True

        else:
            return False


# выводит очки пользователя на экран
def score(Score):
    text = font.render(name + " you score is: " + str(Score), True, BLACK)
    screen.blit(text, (100, 100))
    #text = font.render("DGAP is proud for you: " , True, BLACK)
    #screen.blit(text, (250, 50))

clock = pygame.time.Clock()
finished = False
Score = 0
ball_class = Balls()
ball = pygame.sprite.Group()
ball.add(ball_class)
ball.update()
pygame.display.flip()

while not finished:
    # обновление экрана, изменение движения шаров и их удаление
    clock.tick(FPS)
    screen.fill(WHITE)
    score(Score)
    ball.update()
    ball.draw(screen)
    pygame.display.flip()
    # добавление шаров
    if randint(1, 60) == 1:
        ball_class = Balls()
        ball.add(ball_class)
    # проверка, попал ли пользователь по шару
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in ball:
                if i.check(event.pos):
                    if i.coefficient_of_lack == 2:
                        Score += 1
                    elif i.coefficient_of_lack == 1:
                        Score += 5
                    i.kill()



pygame.quit()
