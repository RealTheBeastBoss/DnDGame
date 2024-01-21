import pygame
import os
from enum import Enum

FPS = 60
WIDTH = 1920
HEIGHT = 1080
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("D&D Game (Temp Game Title)")
BUTTON_COOLDOWN_EVENT = pygame.USEREVENT + 1
pygame.font.init()

# Game Fonts:
TINY_FONT = pygame.font.Font(os.path.join("Fonts", "beastboss_font.ttf"), 20)
BUTTON_FONT = pygame.font.Font(os.path.join("Fonts", "beastboss_font.ttf"), 30)
MEDIUM_FONT = pygame.font.Font(os.path.join("Fonts", "beastboss_font.ttf"), 60)
BIG_FONT = pygame.font.Font(os.path.join("Fonts", "beastboss_font.ttf"), 90)

# Game Colours:
RED = (168, 15, 15)
GOLD = (218,165,32)
GREEN = (0,100,0)

# ScreenStates:
class ScreenState(Enum):
    START = 1
    PLAYER_FIRST_NAME = 2
    PLAYER_LAST_NAME = 3
    SELECT_RACE = 4
    CREATE_DRAGONBORN = 5
    CREATE_HILL_DWARF = 6
    CREATE_MOUNTAIN_DWARF = 7
    CREATE_HIGH_ELF = 8
    CREATE_WOOD_ELF = 9
    CREATE_HALF_ELF = 10
    CREATE_HALF_ORC = 11
    CREATE_LIGHTFOOT_HALFLING = 12
    CREATE_STOUT_HALFLING = 13
    CREATE_HUMAN = 14
    CREATE_VARIANT_HUMAN = 15
    CREATE_ROCK_GNOME = 16
    CREATE_TIEFLING = 17
    SELECT_CLASS = 18

class Game:
    CURRENT_STATE = ScreenState.START
    USER_TEXT = ""
    CAN_INPUT_TEXT = False
    SELECTED_TYPE = None
    # Events:
    BUTTONS_ENABLED = True
    ENTER_PRESSED = False
    LEFT_MOUSE_RELEASED = False

# Races:
class Race(Enum):
    DRAGONBORN = 1
    HILL_DWARF = 2
    MOUNTAIN_DWARF = 3
    HIGH_ELF = 4
    WOOD_ELF = 5
    HALF_ELF = 6
    HALF_ORC = 7
    LIGHTFOOT_HALFLING = 8
    STOUT_HALFLING = 9
    HUMAN = 10
    VARIANT_HUMAN = 11
    ROCK_GNOME = 12
    TIEFLING = 13

# Dragon Types:
class DragonType(Enum):
    BLUE = 1
    BLACK = 2
    BRASS = 3
    BRONZE = 4
    COPPER = 5
    GOLD = 6
    GREEN = 7
    RED = 8
    SILVER = 9
    WHITE = 10

# Damage Types:
class Damage(Enum):
    ACID = 1
    BLUDGEONING = 2
    COLD = 3
    FIRE = 4
    FORCE = 5
    LIGHTNING = 6
    NECROTIC = 7
    PIERCING = 8
    POISON = 9
    PSYCHIC = 10
    RADIANT = 11
    SLASHING = 12
    THUNDER = 13

DRAGONTYPE_TO_DAMAGE = {
    DragonType.BLUE: Damage.LIGHTNING,
    DragonType.BLACK: Damage.ACID,
    DragonType.BRASS: Damage.FIRE,
    DragonType.BRONZE: Damage.LIGHTNING,
    DragonType.COPPER: Damage.ACID,
    DragonType.GOLD: Damage.FIRE,
    DragonType.GREEN: Damage.POISON,
    DragonType.RED: Damage.FIRE,
    DragonType.SILVER: Damage.COLD,
    DragonType.WHITE: Damage.COLD
}

# Senses:
class Sense(Enum):
    BLINDSIGHT = 1
    DARKVISION60 = 2
    DARKVISION120 = 3
    TREMORSENSE = 4
    TRUESIGHT = 5

# Tools:
class Tool(Enum):
    BREWERSUPPLIES = 1
    MASONTOOLS = 2
    SMITHTOOLS = 3

# Languages:
class Language(Enum):
    COMMON = 1
    DRACONIC = 2
    DWARVISH = 3
    ELVISH = 4
    GNOMISH = 5
    UNDERCOMMON = 6
    ORC = 7
    HALFLING = 8
    INFERNAL = 9
    DRUIDIC = 10
    THEIVESCANT = 11

# Armour Types:
class ArmourType(Enum):
    LIGHT = 1
    MEDIUM = 2
    HEAVY = 3

# Weapon Properties:
class Properties(Enum):
    LIGHT = 1
    FINESSE = 2
    THROWN20_60 = 3
    TWOHANDED = 4
    THROWN30_120 = 5
    VERSATILE1_8 = 6
    AMMO80_320 = 7
    LOADING = 8
    AMMO30_120 = 9
    VERSATILE1_10 = 10
    HEAVY = 11
    REACH = 12
    AMMO25_100 = 13
    AMMO100_400 = 14
    AMMO150_600 = 15
    THROWN5_15 = 16

# Abilities:
class Ability(Enum):
    STRENGTH = 1
    DEXTERITY = 2
    CONSTITUTION = 3
    INTELLIGENCE = 4
    WISDOM = 5
    CHARISMA = 6

# Sizes:
class Size(Enum):
    TINY = 1
    SMALL = 2
    MEDIUM = 3
    LARGE = 4
    HUGE = 5
    GARGANTUAN = 6

ALLOWED_KEYS = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_a, pygame.K_b,
                pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n,
                pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z,
                pygame.K_BACKSLASH, pygame.K_BACKSPACE, pygame.K_COMMA, pygame.K_SPACE, pygame.K_RETURN, pygame.K_PERIOD]