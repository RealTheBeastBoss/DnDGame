import pygame

FPS = 60
pygame.display.set_caption("D&D Game (Temp Game Title)")

class Game:
    WIDTH = 1280
    HEIGHT = 720
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)