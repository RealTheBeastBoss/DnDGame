from game import *
import sys

def draw_window():  # This is where the game is run
    WINDOW.fill((69, 69, 69))

if __name__ == '__main__':
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        # Game Event Handler:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw_window()
        pygame.display.update()