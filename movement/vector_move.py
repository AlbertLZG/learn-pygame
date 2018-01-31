#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit
from vector import Vec2d

background_image = '../image/sushiplate.jpg'
sprite_image = '../image/fugu.png'

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image).convert()
sprite = pygame.image.load(sprite_image)

clock = pygame.time.Clock()

position = Vec2d(100, 100)
heading = Vec2d((0, 0))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, position)

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed/1000

    # 在参数前面加*意味着把列表或元组展开
    destination = Vec2d(*pygame.mouse.get_pos()) - Vec2d(*sprite.get_size())/2
    # 计算当鱼儿当前位置到鼠标位置的向量
    vector_to_mouse = Vec2d.__sub__(destination, position)

    vector_to_mouse.normalized()

    # heading可以看做是鱼的速度，鱼的速度大小、方向不断改变
    heading = heading * 0.99 + (vector_to_mouse * 0.1)
    position += heading * time_passed_seconds

    pygame.display.update()
