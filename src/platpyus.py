# Platpyus
# Copyright 2018 Jacob Wharton. All Rights Reserved.

import pygame

from const import *
import artist
import collision
import controller
import entity
import image
import player
import vector

#-----------#
# collision #
#-----------#

def bboxInit(obj, w, h):
    obj.bbox = collision.BoxCollider(obj, w, h)

#--------#
# entity #
#--------#

def addStepFunction(obj, func):
    obj.fxns_step.append(func)
def addDrawFunction(obj, func):
    obj.fxns_draw.append(func)

#----------------#
# global objects #
#----------------#

game = controller.Controller()
draw = artist.Artist(WINDOW_W, WINDOW_H)
pc = player.init()
































