import pygame
import random
import time
pygame.init()
print("красный")
print("зеленый")
print("синий")
sa = input("какой цвет выбераете: ")

ex = random.randint(1, 1000)
time.sleep(0.2)
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("cubs")

x = 50
y = 430
width = 20
height = 20
speed = 20

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x < 480 - width:
        x += speed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        y += speed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= speed
    if sa == "красный":
        pygame.draw.rect(win, (200,0,0), (x, y, width, height))
    if sa =="зеленый":
        pygame.draw.rect(win, (0,200,0), (x, y, width, height))
    if sa =="синий":
        pygame.draw.rect(win, (0,0,200), (x, y, width, height))
    pygame.display.update()
