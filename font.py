#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

background_image = 'image/sushiplate.jpg'
background = pygame.image.load(background_image).convert()
# 以下两种方法都可以，第一种需要把字体文件复制到代码文件目录下
font = pygame.font.Font("simsun.ttc", 40)
# font = pygame.font.SysFont("simsunnsimsun", 40)

text_surface = font.render("你好", True, (0, 0, 255))

x = 0
y = (480 - text_surface.get_height())/2


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background, (0, 0))

    x -= 1
    if x < -text_surface.get_width():
        x = 640 - text_surface.get_width()

    screen.blit(text_surface, (x, y))

    pygame.display.update()
