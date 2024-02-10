from game import *

def draw_text(text, font, colour, location, boxed = False, center = True):  # Draws text centered on a location
    text_surface = font.render(text, True, colour)
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()
    if boxed:
        box_rect = pygame.rect.Rect((location[0] - (text_width/2)) - 10, (location[1] - (text_height/2)) - 8, text_width + 20, text_height + 20)
        pygame.draw.rect(WINDOW, RED, box_rect, 5, 5)
    if center:
        WINDOW.blit(text_surface, (location[0] - (text_width/2), location[1] - (text_height/2)))
    else:
        WINDOW.blit(text_surface, location)

def draw_text_input(location = (960, 330), max_length = 300):  # Creates Text Input Visuals
    text_surface = BUTTON_FONT.render(Game.USER_TEXT, True, RED)
    if text_surface.get_width() >= max_length:
        Game.CAN_INPUT_TEXT = False
    else:
        Game.CAN_INPUT_TEXT = True
    input_rect_width = max(text_surface.get_width() + 10, 200)
    input_rect = pygame.Rect(location[0] - (input_rect_width / 2), location[1], input_rect_width, 60)
    pygame.draw.rect(WINDOW, RED, input_rect, 5, 5)
    WINDOW.blit(text_surface, ((input_rect.x + (input_rect.width / 2)) - (text_surface.get_width() / 2), (input_rect.y + (input_rect.height / 2)) -
    text_surface.get_height() / 2))