from game import *
import sys

def draw_window():  # This is where the screen is rendered and the game is calculated
    Game.WINDOW.fill((69, 69, 69))

if __name__ == '__main__':
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        # Game Event Handler:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # X Button
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:  # Resized Window - Maintains 16:9 Aspect Ratio
                width = event.size[0]
                height = round(width * 0.5625, 0)
                Game.WINDOW = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                Game.WIDTH = width
                Game.HEIGHT = height
        draw_window()
        pygame.display.update()