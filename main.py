from button import Button
from character import Character
from weapon import *
import sys

PLAYER = Character(None, None, None, None, None, 0, 0, 0,
                   0, 0, 0, None, None, [], None, None, None, 1)

def draw_window(): # This is where the screen is rendered and the game is calculated
    if starting_game(): # Starts the Game and Adds Player Name
        pass
    elif adding_race(): # Chooses the Player's Race and Choices therein
        pass
    elif adding_class(): # Chooses the Player's Class and Choices therein
        pass
    # Quit Button:
    quit_button = Button("Quit", 480, 900)
    if quit_button.check_click():
        pygame.quit()
        sys.exit()

def starting_game():
    if Game.CURRENT_STATE == ScreenState.START: # Start Menu
        WINDOW.fill(GREEN)
        draw_text("D&D Game", BIG_FONT, RED, (960, 150))
        game_button = Button("New Game", 960, 300)
        if game_button.check_click():
            Game.CURRENT_STATE = ScreenState.PLAYER_FIRST_NAME
        return True
    elif Game.CURRENT_STATE == ScreenState.PLAYER_FIRST_NAME: # Get the Player's First Name
        WINDOW.fill(GREEN)
        draw_text("Enter your Character's First Name:", MEDIUM_FONT, RED, (960, 200))
        draw_text_input((960, 300), 200)
        if Game.USER_TEXT != "":
            next_button = Button("Next", 960, 420)
            if next_button.check_click() or Game.ENTER_PRESSED:
                Game.CURRENT_STATE = ScreenState.PLAYER_LAST_NAME
                PLAYER.firstName = Game.USER_TEXT
                Game.USER_TEXT = ""
        return True
    elif Game.CURRENT_STATE == ScreenState.PLAYER_LAST_NAME: # Get the Player's Last Name
        WINDOW.fill(GREEN)
        draw_text("Enter your Character's Last Name:", MEDIUM_FONT, RED, (960, 200))
        draw_text_input((960, 300), 200)
        if Game.USER_TEXT != "":
            next_button = Button("Next", 960, 420)
            if next_button.check_click() or Game.ENTER_PRESSED:
                PLAYER.lastName = Game.USER_TEXT
                Game.USER_TEXT = ""
                Game.CURRENT_STATE = ScreenState.SELECT_RACE
        return True

def adding_race():
    if Game.CURRENT_STATE == ScreenState.SELECT_RACE: # Selects the Player Character's Race
        WINDOW.fill(GREEN)
        draw_text("Select " + PLAYER.firstName + " " + PLAYER.lastName + "'s Race:", MEDIUM_FONT, RED, (960, 200))
        dragonborn_button = Button("Dragonborn", 480, 300)
        if dragonborn_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_DRAGONBORN
        hill_dwarf_button = Button("Hill Dwarf", 960, 300)
        if hill_dwarf_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_HILL_DWARF
        mountain_dwarf_button = Button("Mountain Dwarf", 1440, 300)
        if mountain_dwarf_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_MOUNTAIN_DWARF
        high_elf_button = Button("High Elf", 480, 420)
        if high_elf_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_HIGH_ELF
        wood_elf_button = Button("Wood Elf", 960, 420)
        if wood_elf_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_WOOD_ELF
        half_elf_button = Button("Half-Elf", 1440, 420)
        if half_elf_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_HALF_ELF
        half_orc_button = Button("Half-Orc", 480, 540)
        if half_orc_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_HALF_ORC
        lightfoot_halfling_button = Button("Lightfoot Halfling", 960, 540)
        if lightfoot_halfling_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_LIGHTFOOT_HALFLING
        stout_halfling_button = Button("Stout Halfling", 1440, 540)
        if stout_halfling_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_STOUT_HALFLING
        human_button = Button("Human", 480, 660)
        if human_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_HUMAN
        variant_human_button = Button("Variant Human", 960, 660)
        if variant_human_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_VARIANT_HUMAN
        rock_gnome_button = Button("Rock Gnome", 1440, 660)
        if rock_gnome_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_ROCK_GNOME
        tiefling_button = Button("Tiefling", 960, 780)
        if tiefling_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_TIEFLING
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_DRAGONBORN: # Creates a Dragonborn Character
        WINDOW.fill(GREEN)
        draw_text("Select your Dragon Type:", MEDIUM_FONT, RED, (960, 200))
        blue_button = Button("Blue", 480, 420)
        if blue_button.check_click():
            Game.SELECTED_TYPE = DragonType.BLUE
        black_button = Button("Black", 960, 420)
        if black_button.check_click():
            Game.SELECTED_TYPE = DragonType.BLACK
        brass_button = Button("Brass", 1440, 420)
        if brass_button.check_click():
            Game.SELECTED_TYPE = DragonType.BRASS
        bronze_button = Button("Bronze", 480, 540)
        if bronze_button.check_click():
            Game.SELECTED_TYPE = DragonType.BRONZE
        copper_button = Button("Copper", 960, 540)
        if copper_button.check_click():
            Game.SELECTED_TYPE = DragonType.COPPER
        gold_button = Button("Gold", 1440, 540)
        if gold_button.check_click():
            Game.SELECTED_TYPE = DragonType.GOLD
        green_button = Button("Green", 480, 660)
        if green_button.check_click():
            Game.SELECTED_TYPE = DragonType.GREEN
        red_button = Button("Red", 960, 660)
        if red_button.check_click():
            Game.SELECTED_TYPE = DragonType.RED
        silver_button = Button("Silver", 1440, 660)
        if silver_button.check_click():
            Game.SELECTED_TYPE = DragonType.SILVER
        white_button = Button("White", 960, 780)
        if white_button.check_click():
            Game.SELECTED_TYPE = DragonType.WHITE
        if Game.SELECTED_TYPE is not None:
            next_button = Button("Confirm", 960, 900)
            if next_button.check_click(): # Finalise the Dragonborn
                PLAYER.race = Race.DRAGONBORN
                PLAYER.dragonType = Game.SELECTED_TYPE
                Game.SELECTED_TYPE = None
                PLAYER.speed = 30
                PLAYER.size = Size.MEDIUM
                PLAYER.resistance.append(DRAGONTYPE_TO_DAMAGE[PLAYER.dragonType])
                PLAYER.strength += 2
                PLAYER.charisma += 1
                PLAYER.languages.append(Language.COMMON)
                PLAYER.languages.append(Language.DRACONIC)
                Game.CURRENT_STATE = ScreenState.SELECT_CLASS
            match Game.SELECTED_TYPE:
                case DragonType.BLUE:
                    draw_text("Blue Dragon: Breathes a line of Lightning", BUTTON_FONT, RED, (960, 300))
                case DragonType.BLACK:
                    draw_text("Black Dragon: Breathes a line of Acid", BUTTON_FONT, RED, (960, 300))
                case DragonType.BRASS:
                    draw_text("Brass Dragon: Breathes a line of Fire", BUTTON_FONT, RED, (960, 300))
                case DragonType.BRONZE:
                    draw_text("Bronze Dragon: Breathes a line of Lightning", BUTTON_FONT, RED, (960, 300))
                case DragonType.COPPER:
                    draw_text("Copper Dragon: Breathes a line of Acid", BUTTON_FONT, RED, (960, 300))
                case DragonType.GOLD:
                    draw_text("Gold Dragon: Breathes a cone of Fire", BUTTON_FONT, RED, (960, 300))
                case DragonType.GREEN:
                    draw_text("Green Dragon: Breathes a cone of Poison", BUTTON_FONT, RED, (960, 300))
                case DragonType.RED:
                    draw_text("Red Dragon: Breathes a cone of Fire", BUTTON_FONT, RED, (960, 300))
                case DragonType.SILVER:
                    draw_text("Silver Dragon: Breathes a cone of Frost", BUTTON_FONT, RED, (960, 300))
                case DragonType.WHITE:
                    draw_text("White Dragon: Breathes a cone of Frost", BUTTON_FONT, RED, (960, 300))
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_HILL_DWARF: # Creates the Hill Dwarf Player:
        WINDOW.fill(GREEN)
        draw_text("Choose a Tool Proficiency:", MEDIUM_FONT, RED, (960, 200))
        brewer_button = Button("Brewer's Supplies", 960, 300)
        if brewer_button.check_click():
            PLAYER.proficiencies.append(Tool.BREWERSUPPLIES)
            PLAYER.constitution += 2
            PLAYER.size = Size.MEDIUM
            PLAYER.speed = 25
            PLAYER.senses.append(Sense.DARKVISION60)
            PLAYER.resistance.append(Damage.POISON)
            PLAYER.languages.append(Language.COMMON)
            PLAYER.languages.append(Language.DWARVISH)
            PLAYER.proficiencies.append(Battleaxe)
            PLAYER.proficiencies.append(Handaxe)
            PLAYER.proficiencies.append(LightHammer)
            PLAYER.proficiencies.append(Warhammer)
            PLAYER.wisdom += 1
            Game.CURRENT_STATE = ScreenState.SELECT_CLASS
        mason_button = Button("Mason's Tools", 960, 420)
        if mason_button.check_click():
            PLAYER.proficiencies.append(Tool.MASONTOOLS)
            PLAYER.constitution += 2
            PLAYER.size = Size.MEDIUM
            PLAYER.speed = 25
            PLAYER.senses.append(Sense.DARKVISION60)
            PLAYER.resistance.append(Damage.POISON)
            PLAYER.languages.append(Language.COMMON)
            PLAYER.languages.append(Language.DWARVISH)
            PLAYER.proficiencies.append(Battleaxe)
            PLAYER.proficiencies.append(Handaxe)
            PLAYER.proficiencies.append(LightHammer)
            PLAYER.proficiencies.append(Warhammer)
            PLAYER.wisdom += 1
            Game.CURRENT_STATE = ScreenState.SELECT_CLASS
        smith_button = Button("Smith's Tools", 960, 540)
        if smith_button.check_click():
            PLAYER.proficiencies.append(Tool.SMITHTOOLS)
            PLAYER.constitution += 2
            PLAYER.size = Size.MEDIUM
            PLAYER.speed = 25
            PLAYER.senses.append(Sense.DARKVISION60)
            PLAYER.resistance.append(Damage.POISON)
            PLAYER.languages.append(Language.COMMON)
            PLAYER.languages.append(Language.DWARVISH)
            PLAYER.proficiencies.append(Battleaxe)
            PLAYER.proficiencies.append(Handaxe)
            PLAYER.proficiencies.append(LightHammer)
            PLAYER.proficiencies.append(Warhammer)
            PLAYER.wisdom += 1
            Game.CURRENT_STATE = ScreenState.SELECT_CLASS
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_MOUNTAIN_DWARF: # Creates a Mountain Dwarf Player:
        WINDOW.fill(GREEN)
        draw_text("Choose a Tool Proficiency:", MEDIUM_FONT, RED, (960, 200))
        brewer_button = Button("Brewer's Supplies", 960, 300)
        if brewer_button.check_click():
            PLAYER.proficiencies.append(Tool.BREWERSUPPLIES)
            PLAYER.constitution += 2
            PLAYER.size = Size.MEDIUM
            PLAYER.speed = 25
            PLAYER.senses.append(Sense.DARKVISION60)
            PLAYER.resistance.append(Damage.POISON)
            PLAYER.languages.append(Language.COMMON)
            PLAYER.languages.append(Language.DWARVISH)
            PLAYER.proficiencies.append(Battleaxe)
            PLAYER.proficiencies.append(Handaxe)
            PLAYER.proficiencies.append(LightHammer)
            PLAYER.proficiencies.append(Warhammer)
            PLAYER.strength += 2
            PLAYER.proficiencies.append(ArmourType.LIGHT)
            PLAYER.proficiencies.append(ArmourType.MEDIUM)
            Game.CURRENT_STATE = ScreenState.SELECT_CLASS
        mason_button = Button("Mason's Tools", 960, 420)
        if mason_button.check_click():
            PLAYER.proficiencies.append(Tool.MASONTOOLS)
            PLAYER.constitution += 2
            PLAYER.size = Size.MEDIUM
            PLAYER.speed = 25
            PLAYER.senses.append(Sense.DARKVISION60)
            PLAYER.resistance.append(Damage.POISON)
            PLAYER.languages.append(Language.COMMON)
            PLAYER.languages.append(Language.DWARVISH)
            PLAYER.proficiencies.append(Battleaxe)
            PLAYER.proficiencies.append(Handaxe)
            PLAYER.proficiencies.append(LightHammer)
            PLAYER.proficiencies.append(Warhammer)
            PLAYER.strength += 2
            PLAYER.proficiencies.append(ArmourType.LIGHT)
            PLAYER.proficiencies.append(ArmourType.MEDIUM)
            Game.CURRENT_STATE = ScreenState.SELECT_CLASS
        smith_button = Button("Smith's Tools", 960, 540)
        if smith_button.check_click():
            PLAYER.proficiencies.append(Tool.SMITHTOOLS)
            PLAYER.constitution += 2
            PLAYER.size = Size.MEDIUM
            PLAYER.speed = 25
            PLAYER.senses.append(Sense.DARKVISION60)
            PLAYER.resistance.append(Damage.POISON)
            PLAYER.languages.append(Language.COMMON)
            PLAYER.languages.append(Language.DWARVISH)
            PLAYER.proficiencies.append(Battleaxe)
            PLAYER.proficiencies.append(Handaxe)
            PLAYER.proficiencies.append(LightHammer)
            PLAYER.proficiencies.append(Warhammer)
            PLAYER.strength += 2
            PLAYER.proficiencies.append(ArmourType.LIGHT)
            PLAYER.proficiencies.append(ArmourType.MEDIUM)
            Game.CURRENT_STATE = ScreenState.SELECT_CLASS
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_HIGH_ELF: # Creates a High Elf Player:
        
        return True

def adding_class():
    return True

def draw_text(text, font, colour, location, center = True):  # Draws text centered on a location
    text_surface = font.render(text, True, colour)
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()
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

if __name__ == '__main__':
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        # Game Event Handler:
        Game.LEFT_MOUSE_RELEASED = False
        Game.ENTER_PRESSED = False
        Game.CAN_INPUT_TEXT = False
        key_to_add = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # X Button
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                Game.LEFT_MOUSE_RELEASED = True
            elif event.type == BUTTON_COOLDOWN_EVENT:
                Game.BUTTONS_ENABLED = True
            elif event.type == pygame.KEYDOWN:
                if event.key in ALLOWED_KEYS:
                    if event.key == pygame.K_BACKSPACE:
                        Game.USER_TEXT = Game.USER_TEXT[:-1]
                    elif event.key == pygame.K_RETURN:
                        Game.ENTER_PRESSED = True
                    else:
                        key_to_add = event.unicode
        # Game Code:
        draw_window()
        if key_to_add is not None and Game.CAN_INPUT_TEXT:
            Game.USER_TEXT += key_to_add
        pygame.display.flip()