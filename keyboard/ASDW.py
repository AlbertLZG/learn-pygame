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
sprite_pos = Vec2d(200, 150)
sprite_speed = 300

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pressed_keys = pygame.key.get_pressed()
    key_direction = Vec2d(0, 0)
    if pressed_keys[K_LEFT]:
        key_direction.x = -1
    elif pressed_keys[K_RIGHT]:
        key_direction.x = +1
    if pressed_keys[K_UP]:
        key_direction.y = -1
    elif pressed_keys[K_DOWN]:
        key_direction.y = +1
    key_direction.normalized()

    screen.blit(background, (0, 0))
    screen.blit(sprite, sprite_pos)

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed/1000
    sprite_pos += key_direction * sprite_speed * time_passed_seconds

    pygame.display.update()