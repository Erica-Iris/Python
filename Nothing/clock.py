import sys, random, math, pygame
from pygame import *
from datetime import datetime, date, time


def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


def wrap_angle(angle):
    return angle % 360


pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("clock")
font = pygame.font.Font(None, 36)
ora