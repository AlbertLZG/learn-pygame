#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *

pygame.init()

my_event = pygame.event.Event(KEYDOWN, key=K_SPACE, mod=0, unicode=' ')
# my_event = pygame.event.Event(KEYDOWN,{"key":K_SPACE, "mod":0, "unicode":' '})
pygame.event.post(my_event)

###############
# 产生一个自定义的全新事件
CATONKEYBOARD = USEREVENT + 1
my_event = pygame.event.Event(CATONKEYBOARD, message="bad act!")
pygame.event.post(my_event)
# 获得这个事件
for event in pygame.event.get():
    if event.type == CATONKEYBOARD:
        print( event.message)
