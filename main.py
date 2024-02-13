from button import Button
from weapon import *
from spell import *
from character import *
from dice import Dice
import random
import sys

PLAYER = Character(None, None, None, None, None, None, [], None, None, None, 1)

def draw_window(): # This is where the screen is rendered and the game is calculated
    if Game.CURRENT_DICE is not None:
        rolling_dice()
    elif starting_game(): # Starts the Game and Adds Player Name
        pass
    elif player_scores(): # Sets the Player's Scores
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
                Game.CURRENT_STATE = ScreenState.ABILITIES
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
            for spell in ALL_SPELLS:
                if Class.WIZARD in spell.classes and spell.level == 0:
                    Game.SELECTED_SET.append(spell)
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
        # TODO: Breath Weapon
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
                PLAYER.abilities[Ability.STRENGTH] += 2
                PLAYER.abilities[Ability.CHARISMA] += 1
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
        # TODO: Stone Cunning
        # TODO: Hit Point Increase
        WINDOW.fill(GREEN)
        draw_text("Choose a Tool Proficiency:", MEDIUM_FONT, RED, (960, 200))
        brewer_button = Button("Brewer's Supplies", 960, 300)
        if brewer_button.check_click():
            PLAYER.proficiencies.append(Tool.BREWERSUPPLIES)
            PLAYER.abilities[Ability.CONSTITUTION] += 2
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
            PLAYER.abilities[Ability.WISDOM] += 1
            Game.CURRENT_STATE = ScreenState.SELECT_CLASS
        mason_button = Button("Mason's Tools", 960, 420)
        if mason_button.check_click():
            PLAYER.proficiencies.append(Tool.MASONTOOLS)
            PLAYER.abilities[Ability.CONSTITUTION] += 2
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
            PLAYER.abilities[Ability.CONSTITUTION] += 1
            Game.CURRENT_STATE = ScreenState.SELECT_CLASS
        smith_button = Button("Smith's Tools", 960, 540)
        if smith_button.check_click():
            PLAYER.proficiencies.append(Tool.SMITHTOOLS)
            PLAYER.abilities[Ability.CONSTITUTION] += 2
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
            PLAYER.abilities[Ability.WISDOM] += 1
            Game.CURRENT_STATE = ScreenState.SELECT_CLASS
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_MOUNTAIN_DWARF: # Creates a Mountain Dwarf Player:
        WINDOW.fill(GREEN)
        draw_text("Choose a Tool Proficiency:", MEDIUM_FONT, RED, (960, 200))
        brewer_button = Button("Brewer's Supplies", 960, 300)
        if brewer_button.check_click():
            PLAYER.proficiencies.append(Tool.BREWERSUPPLIES)
            PLAYER.abilities[Ability.CONSTITUTION] += 2
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
            PLAYER.abilities[Ability.STRENGTH] += 2
            PLAYER.proficiencies.append(ArmourType.LIGHT)
            PLAYER.proficiencies.append(ArmourType.MEDIUM)
            Game.CURRENT_STATE = ScreenState.SELECT_CLASS
        mason_button = Button("Mason's Tools", 960, 420)
        if mason_button.check_click():
            PLAYER.proficiencies.append(Tool.MASONTOOLS)
            PLAYER.abilities[Ability.CONSTITUTION] += 2
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
            PLAYER.abilities[Ability.STRENGTH] += 2
            PLAYER.proficiencies.append(ArmourType.LIGHT)
            PLAYER.proficiencies.append(ArmourType.MEDIUM)
            Game.CURRENT_STATE = ScreenState.SELECT_CLASS
        smith_button = Button("Smith's Tools", 960, 540)
        if smith_button.check_click():
            PLAYER.proficiencies.append(Tool.SMITHTOOLS)
            PLAYER.abilities[Ability.CONSTITUTION] += 2
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
            PLAYER.abilities[Ability.STRENGTH] += 2
            PLAYER.proficiencies.append(ArmourType.LIGHT)
            PLAYER.proficiencies.append(ArmourType.MEDIUM)
            Game.CURRENT_STATE = ScreenState.SELECT_CLASS
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_HIGH_ELF: # Creates a High Elf Player:
        # TODO: Fey Ancestry
        # TODO: Trance
        WINDOW.fill(GREEN)
        if len(PLAYER.languages) == 0:
            draw_text("Select a Language:", MEDIUM_FONT, RED, (960, 200))
            draconic_button = Button("Draconic", 480, 300)
            if draconic_button.check_click():
                PLAYER.languages.append(Language.DRACONIC)
            dwarvish_button = Button("Dwarvish", 960, 300)
            if dwarvish_button.check_click():
                PLAYER.languages.append(Language.DWARVISH)
            gnomish_button = Button("Gnomish", 1440, 300)
            if gnomish_button.check_click():
                PLAYER.languages.append(Language.GNOMISH)
            undercommon_button = Button("Undercommon", 480, 420)
            if undercommon_button.check_click():
                PLAYER.languages.append(Language.UNDERCOMMON)
            orc_button = Button("Orc", 960, 420)
            if orc_button.check_click():
                PLAYER.languages.append(Language.ORC)
            halfling_button = Button("Halfling", 1440, 420)
            if halfling_button.check_click():
                PLAYER.languages.append(Language.HALFLING)
            infernal_button = Button("Infernal", 480, 540)
            if infernal_button.check_click():
                PLAYER.languages.append(Language.INFERNAL)
            druidic_button = Button("Druidic", 960, 540)
            if druidic_button.check_click():
                PLAYER.languages.append(Language.DRUIDIC)
            thieves_button = Button("Thieves' Cant", 1440, 540)
            if thieves_button.check_click():
                PLAYER.languages.append(Language.THIEVESCANT)
        else:
            draw_text("Select a Cantrip:", MEDIUM_FONT, RED, (960, 200))
            draw_text(Game.SELECTED_SET[Game.SELECTED_INDEX].name, SMALL_FONT, RED, (960, 290), True)
            draw_text("Spell Description:", BUTTON_FONT, RED, (960, 350))
            for x in range(len(Game.SELECTED_SET[Game.SELECTED_INDEX].description)):
                line = Game.SELECTED_SET[Game.SELECTED_INDEX].description[x]
                draw_text(line, TINY_FONT, RED, (960, 400 + (x * 40)))
            if Game.ENTER_PRESSED:
                PLAYER.abilities[Ability.DEXTERITY] += 2
                PLAYER.size = Size.MEDIUM
                PLAYER.senses.append(Sense.DARKVISION60)
                PLAYER.speed = 30
                PLAYER.skills.append(Skill.PERCEPTION)
                PLAYER.languages.append(Language.COMMON)
                PLAYER.languages.append(Language.ELVISH)
                PLAYER.abilities[Ability.INTELLIGENCE] += 1
                PLAYER.proficiencies.append(Longsword)
                PLAYER.proficiencies.append(Shortsword)
                PLAYER.proficiencies.append(Shortbow)
                PLAYER.proficiencies.append(Longbow)
                PLAYER.cantrips.append(Game.SELECTED_SET[Game.SELECTED_INDEX])
                PLAYER.spellAbility = Ability.INTELLIGENCE
                Game.SELECTED_SET.clear()
                Game.SELECTED_INDEX = 0
                Game.CURRENT_STATE = ScreenState.SELECT_CLASS
            elif Game.LEFT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == 0:
                    Game.SELECTED_INDEX = len(Game.SELECTED_SET) - 1
                else:
                    Game.SELECTED_INDEX -= 1
            elif Game.RIGHT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == len(Game.SELECTED_SET) - 1:
                    Game.SELECTED_INDEX = 0
                else:
                    Game.SELECTED_INDEX += 1
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_WOOD_ELF: # Creates the Wood Elf Player:
        # TODO: Mask of the Wild
        PLAYER.abilities[Ability.DEXTERITY] += 2
        PLAYER.size = Size.MEDIUM
        PLAYER.speed = 35
        PLAYER.senses.append(Sense.DARKVISION60)
        PLAYER.skills.append(Skill.PERCEPTION)
        PLAYER.languages.append(Language.COMMON)
        PLAYER.languages.append(Language.ELVISH)
        PLAYER.abilities[Ability.WISDOM] += 1
        PLAYER.proficiencies.append(Longsword)
        PLAYER.proficiencies.append(Shortsword)
        PLAYER.proficiencies.append(Shortbow)
        PLAYER.proficiencies.append(Longbow)
        Game.CURRENT_STATE = ScreenState.SELECT_CLASS
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_HALF_ELF: # Creates the Half Elf Player:
        WINDOW.fill(GREEN)
        if len(PLAYER.languages) == 0:
            draw_text("Select a Language:", MEDIUM_FONT, RED, (960, 200))
            draconic_button = Button("Draconic", 480, 300)
            if draconic_button.check_click():
                PLAYER.languages.append(Language.DRACONIC)
            dwarvish_button = Button("Dwarvish", 960, 300)
            if dwarvish_button.check_click():
                PLAYER.languages.append(Language.DWARVISH)
            gnomish_button = Button("Gnomish", 1440, 300)
            if gnomish_button.check_click():
                PLAYER.languages.append(Language.GNOMISH)
            undercommon_button = Button("Undercommon", 480, 420)
            if undercommon_button.check_click():
                PLAYER.languages.append(Language.UNDERCOMMON)
            orc_button = Button("Orc", 960, 420)
            if orc_button.check_click():
                PLAYER.languages.append(Language.ORC)
            halfling_button = Button("Halfling", 1440, 420)
            if halfling_button.check_click():
                PLAYER.languages.append(Language.HALFLING)
            infernal_button = Button("Infernal", 480, 540)
            if infernal_button.check_click():
                PLAYER.languages.append(Language.INFERNAL)
            druidic_button = Button("Druidic", 960, 540)
            if druidic_button.check_click():
                PLAYER.languages.append(Language.DRUIDIC)
            thieves_button = Button("Thieves' Cant", 1440, 540)
            if thieves_button.check_click():
                PLAYER.languages.append(Language.THIEVESCANT)
        elif len(PLAYER.skills) != 2:
            draw_text("Select two Skills to Learn:", MEDIUM_FONT, RED, (960, 200))
            draw_text(SKILL_NAME[Skill(Game.SELECTED_INDEX)], SMALL_FONT, RED, (960, 300), True)
            if len(PLAYER.skills) > 0:
                draw_text("Current Skills:", BUTTON_FONT, RED, (960, 390))
                for x in range(len(PLAYER.skills)):
                    draw_text(SKILL_NAME[PLAYER.skills[x]], BUTTON_FONT, RED, (960, 420 + (x * 20)))
            if Game.ENTER_PRESSED:
                if Skill(Game.SELECTED_INDEX) not in PLAYER.skills:
                    PLAYER.skills.append(Skill(Game.SELECTED_INDEX))
                    if len(PLAYER.skills) == 2:
                        Game.SELECTED_INDEX = 0
                        PLAYER.abilities[Ability.CHARISMA] += 2
            elif Game.LEFT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == 0:
                    Game.SELECTED_INDEX = len(Skill) - 1
                else:
                    Game.SELECTED_INDEX -= 1
            elif Game.RIGHT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == len(Skill) - 1:
                    Game.SELECTED_INDEX = 0
                else:
                    Game.SELECTED_INDEX += 1
        else:
            draw_text("Select two Abilities to Better Yourself in:", MEDIUM_FONT, RED, (960, 200))
            draw_text(ABILITY_NAME[Ability(Game.SELECTED_INDEX)], SMALL_FONT, RED, (960, 300), True)
            if Game.ENTER_PRESSED and PLAYER.abilities[Ability(Game.SELECTED_INDEX)] == 0:
                PLAYER.abilities[Ability(Game.SELECTED_INDEX)] += 1
                added_count = 0
                for ability in PLAYER.abilities.values():
                    if ability > 0:
                        added_count += 1
                if added_count == 3:
                    PLAYER.size = Size.MEDIUM
                    PLAYER.speed = 30
                    PLAYER.senses.append(Sense.DARKVISION60)
                    PLAYER.languages.append(Language.COMMON)
                    PLAYER.languages.append(Language.ELVISH)
                    Game.SELECTED_INDEX = 0
                    Game.CURRENT_STATE = ScreenState.SELECT_CLASS
            elif Game.LEFT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == 0:
                    Game.SELECTED_INDEX = len(Ability) - 1
                else:
                    Game.SELECTED_INDEX -= 1
            elif Game.RIGHT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == len(Ability) - 1:
                    Game.SELECTED_INDEX = 0
                else:
                    Game.SELECTED_INDEX += 1
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_HALF_ORC: # Creates the Half-Orc Player:
        # TODO: Relentless Endurance
        # TODO: Savage Attacks
        PLAYER.abilities[Ability.STRENGTH] += 2
        PLAYER.abilities[Ability.CONSTITUTION] += 1
        PLAYER.size = Size.MEDIUM
        PLAYER.speed = 30
        PLAYER.senses.append(Sense.DARKVISION60)
        PLAYER.skills.append(Skill.INTIMIDATION)
        PLAYER.languages.append(Language.COMMON)
        PLAYER.languages.append(Language.ORC)
        Game.CURRENT_STATE = ScreenState.SELECT_CLASS
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_LIGHTFOOT_HALFLING: # Creates the Lightfoot Halfling Player:
        # TODO: Lucky
        # TODO: Brave
        # TODO: Halfling Nimbleness
        # TODO: Naturally Stealthy
        PLAYER.abilities[Ability.DEXTERITY] += 2
        PLAYER.abilities[Ability.CHARISMA] += 1
        PLAYER.size = Size.SMALL
        PLAYER.speed = 25
        PLAYER.languages.append(Language.COMMON)
        PLAYER.languages.append(Language.HALFLING)
        Game.CURRENT_STATE = ScreenState.SELECT_CLASS
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_STOUT_HALFLING: # Creates the Stout Halfling Player:
        # TODO: Stout Resilience
        PLAYER.abilities[Ability.DEXTERITY] += 2
        PLAYER.abilities[Ability.CONSTITUTION] += 1
        PLAYER.size = Size.SMALL
        PLAYER.speed = 25
        PLAYER.languages.append(Language.COMMON)
        PLAYER.languages.append(Language.HALFLING)
        PLAYER.resistance.append(Damage.POISON)
        Game.CURRENT_STATE = ScreenState.SELECT_CLASS
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_HUMAN: # Creates the Human Player:
        WINDOW.fill(GREEN)
        if len(PLAYER.languages) == 0:
            draw_text("Select a Language:", MEDIUM_FONT, RED, (960, 200))
            draconic_button = Button("Draconic", 480, 300)
            if draconic_button.check_click():
                PLAYER.languages.append(Language.DRACONIC)
            dwarvish_button = Button("Dwarvish", 960, 300)
            if dwarvish_button.check_click():
                PLAYER.languages.append(Language.DWARVISH)
            gnomish_button = Button("Gnomish", 1440, 300)
            if gnomish_button.check_click():
                PLAYER.languages.append(Language.GNOMISH)
            undercommon_button = Button("Undercommon", 480, 420)
            if undercommon_button.check_click():
                PLAYER.languages.append(Language.UNDERCOMMON)
            orc_button = Button("Orc", 960, 420)
            if orc_button.check_click():
                PLAYER.languages.append(Language.ORC)
            halfling_button = Button("Halfling", 1440, 420)
            if halfling_button.check_click():
                PLAYER.languages.append(Language.HALFLING)
            infernal_button = Button("Infernal", 480, 540)
            if infernal_button.check_click():
                PLAYER.languages.append(Language.INFERNAL)
            druidic_button = Button("Druidic", 960, 540)
            if druidic_button.check_click():
                PLAYER.languages.append(Language.DRUIDIC)
            thieves_button = Button("Thieves' Cant", 1440, 540)
            if thieves_button.check_click():
                PLAYER.languages.append(Language.THIEVESCANT)
            elf_button = Button("Elvish", 960, 660)
            if elf_button.check_click():
                PLAYER.languages.append(Language.ELVISH)
        else:
            PLAYER.abilities[Ability.STRENGTH] += 1
            PLAYER.abilities[Ability.DEXTERITY] += 1
            PLAYER.abilities[Ability.CONSTITUTION] += 1
            PLAYER.abilities[Ability.INTELLIGENCE] += 1
            PLAYER.abilities[Ability.WISDOM] += 1
            PLAYER.abilities[Ability.CHARISMA] += 1
            PLAYER.size = Size.MEDIUM
            PLAYER.speed = 30
            PLAYER.languages.append(Language.COMMON)
            Game.CURRENT_STATE = ScreenState.SELECT_CLASS
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_VARIANT_HUMAN: # Creates the Variant Human Player:
        WINDOW.fill(GREEN)
        if len(PLAYER.languages) == 0:
            draw_text("Select a Language:", MEDIUM_FONT, RED, (960, 200))
            draconic_button = Button("Draconic", 480, 300)
            if draconic_button.check_click():
                PLAYER.languages.append(Language.DRACONIC)
            dwarvish_button = Button("Dwarvish", 960, 300)
            if dwarvish_button.check_click():
                PLAYER.languages.append(Language.DWARVISH)
            gnomish_button = Button("Gnomish", 1440, 300)
            if gnomish_button.check_click():
                PLAYER.languages.append(Language.GNOMISH)
            undercommon_button = Button("Undercommon", 480, 420)
            if undercommon_button.check_click():
                PLAYER.languages.append(Language.UNDERCOMMON)
            orc_button = Button("Orc", 960, 420)
            if orc_button.check_click():
                PLAYER.languages.append(Language.ORC)
            halfling_button = Button("Halfling", 1440, 420)
            if halfling_button.check_click():
                PLAYER.languages.append(Language.HALFLING)
            infernal_button = Button("Infernal", 480, 540)
            if infernal_button.check_click():
                PLAYER.languages.append(Language.INFERNAL)
            druidic_button = Button("Druidic", 960, 540)
            if druidic_button.check_click():
                PLAYER.languages.append(Language.DRUIDIC)
            thieves_button = Button("Thieves' Cant", 1440, 540)
            if thieves_button.check_click():
                PLAYER.languages.append(Language.THIEVESCANT)
            elf_button = Button("Elvish", 960, 660)
            if elf_button.check_click():
                PLAYER.languages.append(Language.ELVISH)
        elif len(PLAYER.skills) == 0:
            draw_text("Select a Skill to Learn:", MEDIUM_FONT, RED, (960, 200))
            draw_text(SKILL_NAME[Skill(Game.SELECTED_INDEX)], SMALL_FONT, RED, (960, 300), True)
            if Game.ENTER_PRESSED:
                PLAYER.skills.append(Skill(Game.SELECTED_INDEX))
                Game.SELECTED_INDEX = 0
            elif Game.LEFT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == 0:
                    Game.SELECTED_INDEX = len(Skill) - 1
                else:
                    Game.SELECTED_INDEX -= 1
            elif Game.RIGHT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == len(Skill) - 1:
                    Game.SELECTED_INDEX = 0
                else:
                    Game.SELECTED_INDEX += 1
        else:
            draw_text("Select two Abilities to Better Yourself in:", MEDIUM_FONT, RED, (960, 200))
            draw_text(ABILITY_NAME[Ability(Game.SELECTED_INDEX)], SMALL_FONT, RED, (960, 300), True)
            if Game.ENTER_PRESSED and PLAYER.abilities[Ability(Game.SELECTED_INDEX)] == 0:
                PLAYER.abilities[Ability(Game.SELECTED_INDEX)] += 1
                added_count = 0
                for ability in PLAYER.abilities.values():
                    if ability > 0:
                        added_count += 1
                if added_count == 2:
                    PLAYER.size = Size.MEDIUM
                    PLAYER.speed = 30
                    PLAYER.languages.append(Language.COMMON)
                    Game.CURRENT_STATE = ScreenState.SELECT_CLASS
            elif Game.LEFT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == 0:
                    Game.SELECTED_INDEX = len(Ability) - 1
                else:
                    Game.SELECTED_INDEX -= 1
            elif Game.RIGHT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == len(Ability) - 1:
                    Game.SELECTED_INDEX = 0
                else:
                    Game.SELECTED_INDEX += 1
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_ROCK_GNOME: # Creates the Rock Gnome Player:
        # TODO: Artificer's Lore
        # TODO: Tinker
        # TODO: Gnome Cunning
        PLAYER.abilities[Ability.INTELLIGENCE] += 2
        PLAYER.abilities[Ability.CONSTITUTION] += 1
        PLAYER.size = Size.SMALL
        PLAYER.speed = 25
        PLAYER.senses.append(Sense.DARKVISION60)
        PLAYER.languages.append(Language.COMMON)
        PLAYER.languages.append(Language.GNOMISH)
        Game.CURRENT_STATE = ScreenState.SELECT_CLASS
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_TIEFLING: # Creates the Tiefling Player:
        # TODO: Infernal Legacy
        PLAYER.abilities[Ability.INTELLIGENCE] += 1
        PLAYER.abilities[Ability.CHARISMA] += 2
        PLAYER.size = Size.MEDIUM
        PLAYER.speed = 30
        PLAYER.senses.append(Sense.DARKVISION60)
        PLAYER.resistance.append(Damage.FIRE)
        PLAYER.cantrips.append(THAUMATURGY)
        PLAYER.spellAbility = Ability.CHARISMA
        Game.CURRENT_STATE = ScreenState.SELECT_CLASS
        return True

def adding_class():
    if Game.CURRENT_STATE == ScreenState.SELECT_CLASS: # Makes the player choose a class:
        WINDOW.fill(GREEN)
        draw_text("Select Class", MEDIUM_FONT, RED, (960, 200))
        barbarian_button = Button("Barbarian", 480, 300)
        if barbarian_button.check_click():
            Game.SELECTED_SET = [Skill.ANIMAL_HANDLING, Skill.ATHLETICS, Skill.INTIMIDATION, Skill.NATURE, Skill.PERCEPTION, Skill.SURVIVAL]
            Game.CURRENT_STATE = ScreenState.CREATE_BARBARIAN
        bard_button = Button("Bard", 960, 300)
        if bard_button.check_click():
            for skill in list(Skill):
                Game.SELECTED_SET.append(skill)
            Game.CURRENT_STATE = ScreenState.CREATE_BARD
        cleric_button = Button("Cleric", 1440, 300)
        if cleric_button.check_click():
            Game.SELECTED_SET = [Skill.HISTORY, Skill.INSIGHT, Skill.MEDICINE, Skill.PERSUASION, Skill.RELIGION]
            Game.CURRENT_STATE = ScreenState.CREATE_CLERIC
        druid_button = Button("Druid", 480, 420)
        if druid_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_DRUID
        fighter_button = Button("Fighter", 960, 420)
        if fighter_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_FIGHTER
        monk_button = Button("Monk", 1440, 420)
        if monk_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_MONK
        paladin_button = Button("Paladin", 480, 540)
        if paladin_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_PALADIN
        ranger_button = Button("Ranger", 960, 540)
        if ranger_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_RANGER
        rogue_button = Button("Rogue", 1440, 540)
        if rogue_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_ROGUE
        sorcerer_button = Button("Sorcerer", 480, 660)
        if sorcerer_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_SORCERER
        warlock_button = Button("Warlock", 960, 660)
        if warlock_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_WARLOCK
        wizard_button = Button("Wizard", 1440, 660)
        if wizard_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_WIZARD
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_BARBARIAN: # Creates the Barbarian Player:
        WINDOW.fill(GREEN)
        # TODO: Barbarian Rage
        # TODO: Unarmoured Defence
        if len(Game.SELECTED_SET) != 4:
            draw_text("Choose Two Skills to Learn:", MEDIUM_FONT, RED, (960, 200))
            draw_text(SKILL_NAME[Game.SELECTED_SET[Game.SELECTED_INDEX]], BUTTON_FONT, RED, (960, 280), True)
            if len(PLAYER.skills) > 0:
                draw_text("Current Skills:", BUTTON_FONT, RED, (960, 390))
                for x in range(len(PLAYER.skills)):
                    draw_text(SKILL_NAME[PLAYER.skills[x]], BUTTON_FONT, RED, (960, 420 + (x * 20)))
            if Game.ENTER_PRESSED:
                if Game.SELECTED_SET[Game.SELECTED_INDEX] not in PLAYER.skills:
                    PLAYER.skills.append(Game.SELECTED_SET[Game.SELECTED_INDEX])
                    Game.SELECTED_SET.remove(Game.SELECTED_SET[Game.SELECTED_INDEX])
                    Game.SELECTED_INDEX = 0
            elif Game.LEFT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == 0:
                    Game.SELECTED_INDEX = len(Game.SELECTED_SET) - 1
                else:
                    Game.SELECTED_INDEX -= 1
            elif Game.RIGHT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == len(Game.SELECTED_SET) - 1:
                    Game.SELECTED_INDEX = 0
                else:
                    Game.SELECTED_INDEX += 1
        else:
            PLAYER.hitDice = (1, 12)
            PLAYER.maxHP = 12 + ABILITY_MODIFIER[PLAYER.abilities[Ability.CONSTITUTION]]
            PLAYER.hp = PLAYER.maxHP
            PLAYER.ragesLeft = 2
            PLAYER.rageDamage = 2
            PLAYER.proficiencies.append(ArmourType.LIGHT)
            PLAYER.proficiencies.append(ArmourType.MEDIUM)
            PLAYER.proficiencies.append(ArmourType.SHIELD)
            PLAYER.proficiencies.append(WeaponType.SIMPLE_MELEE)
            PLAYER.proficiencies.append(WeaponType.SIMPLE_RANGED)
            PLAYER.proficiencies.append(WeaponType.MARTIAL_MELEE)
            PLAYER.proficiencies.append(WeaponType.MARTIAL_RANGED)
            PLAYER.saves.append(Ability.STRENGTH)
            PLAYER.saves.append(Ability.CONSTITUTION)
            Game.SELECTED_SET.clear()
            Game.SELECTED_INDEX = 0
            Game.CURRENT_STATE = ScreenState.ABILITIES
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_BARD: # Creates the Bard Player:
        # TODO: Bardic Inspiration
        WINDOW.fill(GREEN)
        if Game.SELECTED_SET[Game.SELECTED_INDEX] in Skill:
            draw_text("Choose Three Skills to Learn:", MEDIUM_FONT, RED, (960, 200))
            draw_text(SKILL_NAME[Game.SELECTED_SET[Game.SELECTED_INDEX]], BUTTON_FONT, RED, (960, 280), True)
            if len(PLAYER.skills) > 0:
                draw_text("Current Skills:", BUTTON_FONT, RED, (960, 390))
                for x in range(len(PLAYER.skills)):
                    draw_text(SKILL_NAME[PLAYER.skills[x]], BUTTON_FONT, RED, (960, 420 + (x * 25)))
            if Game.ENTER_PRESSED:
                if Game.SELECTED_SET[Game.SELECTED_INDEX] not in PLAYER.skills:
                    PLAYER.skills.append(Game.SELECTED_SET[Game.SELECTED_INDEX])
                    Game.SELECTED_SET.remove(Game.SELECTED_SET[Game.SELECTED_INDEX])
                    Game.SELECTED_INDEX = 0
                    if len(Game.SELECTED_SET) == 15:
                        Game.SELECTED_SET.clear()
                        for spell in ALL_SPELLS:
                            if Class.BARD in spell.classes and spell.level == 0:
                                Game.SELECTED_SET.append(spell)
            elif Game.LEFT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == 0:
                    Game.SELECTED_INDEX = len(Game.SELECTED_SET) - 1
                else:
                    Game.SELECTED_INDEX -= 1
            elif Game.RIGHT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == len(Game.SELECTED_SET) - 1:
                    Game.SELECTED_INDEX = 0
                else:
                    Game.SELECTED_INDEX += 1
        elif Game.SELECTED_SET[Game.SELECTED_INDEX] in ALL_SPELLS and Game.SELECTED_SET[Game.SELECTED_INDEX].level == 0:
            draw_text("Select two Cantrips:", MEDIUM_FONT, RED, (960, 200))
            draw_text(Game.SELECTED_SET[Game.SELECTED_INDEX].name, SMALL_FONT, RED, (960, 290), True)
            draw_text("Spell Description:", BUTTON_FONT, RED, (960, 350))
            for x in range(len(Game.SELECTED_SET[Game.SELECTED_INDEX].description)):
                line = Game.SELECTED_SET[Game.SELECTED_INDEX].description[x]
                draw_text(line, TINY_FONT, RED, (960, 400 + (x * 40)))
            if Game.ENTER_PRESSED:
                if Game.SELECTED_SET[Game.SELECTED_INDEX] not in PLAYER.cantrips:
                    PLAYER.cantrips.append(Game.SELECTED_SET[Game.SELECTED_INDEX])
                    Game.SELECTED_SET.remove(Game.SELECTED_SET[Game.SELECTED_INDEX])
                    Game.SELECTED_INDEX = 0
                if len(Game.SELECTED_SET) == 1:
                    Game.SELECTED_SET.clear()
                    for spell in ALL_SPELLS:
                        if Class.BARD in spell.classes and spell.level == 1:
                            Game.SELECTED_SET.append(spell)
            elif Game.LEFT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == 0:
                    Game.SELECTED_INDEX = len(Game.SELECTED_SET) - 1
                else:
                    Game.SELECTED_INDEX -= 1
            elif Game.RIGHT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == len(Game.SELECTED_SET) - 1:
                    Game.SELECTED_INDEX = 0
                else:
                    Game.SELECTED_INDEX += 1
        elif Game.SELECTED_SET[Game.SELECTED_INDEX] in ALL_SPELLS and Game.SELECTED_SET[Game.SELECTED_INDEX].level == 1:
            draw_text("Select four Spells:", MEDIUM_FONT, RED, (960, 200))
            draw_text(Game.SELECTED_SET[Game.SELECTED_INDEX].name, SMALL_FONT, RED, (960, 290), True)
            draw_text("Spell Description:", BUTTON_FONT, RED, (960, 350))
            for x in range(len(Game.SELECTED_SET[Game.SELECTED_INDEX].description)):
                line = Game.SELECTED_SET[Game.SELECTED_INDEX].description[x]
                draw_text(line, TINY_FONT, RED, (960, 400 + (x * 40)))
            if Game.ENTER_PRESSED:
                if Game.SELECTED_SET[Game.SELECTED_INDEX] not in PLAYER.knownSpells:
                    PLAYER.knownSpells.append(Game.SELECTED_SET[Game.SELECTED_INDEX])
                    Game.SELECTED_SET.remove(Game.SELECTED_SET[Game.SELECTED_INDEX])
                    Game.SELECTED_INDEX = 0
                if len(Game.SELECTED_SET) == 3:
                    Game.SELECTED_SET = [None]
            elif Game.LEFT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == 0:
                    Game.SELECTED_INDEX = len(Game.SELECTED_SET) - 1
                else:
                    Game.SELECTED_INDEX -= 1
            elif Game.RIGHT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == len(Game.SELECTED_SET) - 1:
                    Game.SELECTED_INDEX = 0
                else:
                    Game.SELECTED_INDEX += 1
        else:
            PLAYER.hitDice = (1, 8)
            PLAYER.maxHP = 8 + ABILITY_MODIFIER[PLAYER.abilities[Ability.CONSTITUTION]]
            PLAYER.hp = PLAYER.maxHP
            PLAYER.proficiencies.append(ArmourType.LIGHT)
            PLAYER.proficiencies.append(WeaponType.SIMPLE_MELEE)
            PLAYER.proficiencies.append(WeaponType.SIMPLE_RANGED)
            PLAYER.proficiencies.append(HandCrossbow)
            PLAYER.proficiencies.append(Longsword)
            PLAYER.proficiencies.append(Rapier)
            PLAYER.proficiencies.append(Shortsword)
            PLAYER.saves.append(Ability.DEXTERITY)
            PLAYER.saves.append(Ability.CHARISMA)
            PLAYER.lvl1SlotsLeft = 2
            PLAYER.inspireDice = (1, 6)
            PLAYER.spellAbility = Ability.CHARISMA
            Game.SELECTED_SET.clear()
            Game.CURRENT_STATE = ScreenState.ABILITIES
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_CLERIC: # Creates the Cleric Player:
        WINDOW.fill(GREEN)
        if Game.SELECTED_SET[0] in Skill:
            draw_text("Select Two Skills:", MEDIUM_FONT, RED, (960, 100))
            draw_text(SKILL_NAME[Game.SELECTED_SET[Game.SELECTED_INDEX]], SMALL_FONT, RED, (960, 200), True)
            if Game.ENTER_PRESSED:
                if Game.SELECTED_SET[Game.SELECTED_INDEX] not in PLAYER.skills:
                    PLAYER.skills.append(Game.SELECTED_SET[Game.SELECTED_INDEX])
                    Game.SELECTED_SET.remove(Game.SELECTED_SET[Game.SELECTED_INDEX])
                    Game.SELECTED_INDEX = 0
                    if len(Game.SELECTED_SET) == 3:
                        Game.SELECTED_SET.clear()
                        for spell in ALL_SPELLS:
                            if Class.CLERIC in spell.classes and spell.level == 0:
                                Game.SELECTED_SET.append(spell)
            elif Game.LEFT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == 0:
                    Game.SELECTED_INDEX = len(Game.SELECTED_SET) - 1
                else:
                    Game.SELECTED_INDEX -= 1
            elif Game.RIGHT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == len(Game.SELECTED_SET) - 1:
                    Game.SELECTED_INDEX = 0
                else:
                    Game.SELECTED_INDEX += 1
        elif Game.SELECTED_SET[0] in ALL_SPELLS and Game.SELECTED_SET[0].level == 0:
            draw_text("Select Three Cantrips:", MEDIUM_FONT, RED, (960, 100))
            draw_text(Game.SELECTED_SET[Game.SELECTED_INDEX].name, SMALL_FONT, RED, (960, 200), True)
            draw_text("Spell Description:", BUTTON_FONT, RED, (960, 280))
            for x in range(len(Game.SELECTED_SET[Game.SELECTED_INDEX].description)):
                line = Game.SELECTED_SET[Game.SELECTED_INDEX].description[x]
                draw_text(line, TINY_FONT, RED, (960, 320 + (x * 40)))
            if Game.ENTER_PRESSED:
                if Game.SELECTED_SET[Game.SELECTED_INDEX] not in PLAYER.cantrips:
                    PLAYER.cantrips.append(Game.SELECTED_SET[Game.SELECTED_INDEX])
                    Game.SELECTED_SET.remove(Game.SELECTED_SET[Game.SELECTED_INDEX])
                    Game.SELECTED_INDEX = 0
                    if len(Game.SELECTED_SET) == 2:
                        Game.SELECTED_SET.clear()
                        for spell in ALL_SPELLS:
                            if Class.CLERIC in spell.classes and spell.level == 1:
                                Game.SELECTED_SET.append(spell)
            elif Game.LEFT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == 0:
                    Game.SELECTED_INDEX = len(Game.SELECTED_SET) - 1
                else:
                    Game.SELECTED_INDEX -= 1
            elif Game.RIGHT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == len(Game.SELECTED_SET) - 1:
                    Game.SELECTED_INDEX = 0
                else:
                    Game.SELECTED_INDEX += 1
        elif Game.SELECTED_SET[0] in ALL_SPELLS and Game.SELECTED_SET[0].level == 1:
            spell_count = max(1, 1 + ABILITY_MODIFIER[PLAYER.abilities[Ability.WISDOM]])
            draw_text("Select " + str(spell_count) + " Spell(s):", MEDIUM_FONT, RED, (960, 100))
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_DRUID: # Creates the Druid Player:
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_FIGHTER: # Creates the Fighter Player:
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_MONK: # Creates the Monk Player:
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_PALADIN: # Creates the Paladin Player:
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_RANGER: # Creates the Ranger Player:
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_ROGUE: # Creates the Rogue Player:
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_SORCERER: # Creates the Sorcerer Player:
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_WARLOCK: # Creates the Warlock Player:
        return True
    elif Game.CURRENT_STATE == ScreenState.CREATE_WIZARD: # Creates the Wizard Player:
        return True

def player_scores():
    if Game.CURRENT_STATE == ScreenState.ABILITIES: # Handles the Player's Abilities
        WINDOW.fill(GREEN)
        draw_text("Choose a Method of Getting Abilities:", MEDIUM_FONT, RED, (960, 200))
        point_button = Button("Point Buy", 960, 300)
        if point_button.check_click():
            Game.CURRENT_STATE = ScreenState.POINT_BUY
            for ability in list(Ability):
                PLAYER.abilities[ability] = 8
        roll_button = Button("Dice Roll", 960, 370)
        if roll_button.check_click():
            Game.CURRENT_STATE = ScreenState.POINT_ROLL
            Game.CURRENT_DICE = [Dice(6), Dice(6), Dice(6), Dice(6)]
        return True
    elif Game.CURRENT_STATE == ScreenState.POINT_BUY:
        WINDOW.fill(GREEN)
        draw_text("Buy Abilities", MEDIUM_FONT, RED, (960, 100))
        draw_text("Points Remaining: " + str(Game.POINTS_LEFT), SMALL_FONT, RED, (960, 270))
        draw_text(ABILITY_NAME[Ability(Game.SELECTED_INDEX)] + ": " + str(PLAYER.abilities[Ability(Game.SELECTED_INDEX)]), SMALL_FONT, RED, (960, 350), True)
        match PLAYER.abilities[Ability(Game.SELECTED_INDEX)]:
            case 8:
                nine_button = Button("Nine (-1 Point)", 960, 430)
                if nine_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 9
                    Game.POINTS_LEFT -= 1
                ten_button = Button("Ten (-2 Points)", 960, 495)
                if ten_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 10
                    Game.POINTS_LEFT -= 2
                eleven_button = Button("Eleven (-3 Points)", 960, 560)
                if eleven_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 11
                    Game.POINTS_LEFT -= 3
                twelve_button = Button("Twelve (-4 Points)", 960, 625)
                if twelve_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 12
                    Game.POINTS_LEFT -= 4
                thirteen_button = Button("Thirteen (-5 Points)", 960, 690)
                if thirteen_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 13
                    Game.POINTS_LEFT -= 5
                fourteen_button = Button("Fourteen (-7 Points)", 960, 755)
                if fourteen_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 14
                    Game.POINTS_LEFT -= 7
                fifteen_button = Button("Fifteen (-9 Points)", 960, 820)
                if fifteen_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 15
                    Game.POINTS_LEFT -= 9
            case 9:
                eight_button = Button("Eight (+1 Point)", 960, 430)
                if eight_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 8
                    Game.POINTS_LEFT += 1
                ten_button = Button("Ten (-1 Point)", 960, 495)
                if ten_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 10
                    Game.POINTS_LEFT -= 1
                eleven_button = Button("Eleven (-2 Points)", 960, 560)
                if eleven_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 11
                    Game.POINTS_LEFT -= 2
                twelve_button = Button("Twelve (-3 Points)", 960, 625)
                if twelve_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 12
                    Game.POINTS_LEFT -= 3
                thirteen_button = Button("Thirteen (-4 Points)", 960, 690)
                if thirteen_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 13
                    Game.POINTS_LEFT -= 4
                fourteen_button = Button("Fourteen (-6 Points)", 960, 755)
                if fourteen_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 14
                    Game.POINTS_LEFT -= 6
                fifteen_button = Button("Fifteen (-8 Points)", 960, 820)
                if fifteen_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 15
                    Game.POINTS_LEFT -= 8
            case 10:
                eight_button = Button("Eight (+2 Points)", 960, 430)
                if eight_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 8
                    Game.POINTS_LEFT += 2
                nine_button = Button("Nine (+1 Point)", 960, 495)
                if nine_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 9
                    Game.POINTS_LEFT += 1
                eleven_button = Button("Eleven (-1 Point)", 960, 560)
                if eleven_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 11
                    Game.POINTS_LEFT -= 1
                twelve_button = Button("Twelve (-2 Points)", 960, 625)
                if twelve_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 12
                    Game.POINTS_LEFT -= 2
                thirteen_button = Button("Thirteen (-3 Points)", 960, 690)
                if thirteen_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 13
                    Game.POINTS_LEFT -= 3
                fourteen_button = Button("Fourteen (-5 Points)", 960, 755)
                if fourteen_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 14
                    Game.POINTS_LEFT -= 5
                fifteen_button = Button("Fifteen (-7 Points)", 960, 820)
                if fifteen_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 15
                    Game.POINTS_LEFT -= 7
            case 11:
                eight_button = Button("Eight (+3 Points)", 960, 430)
                if eight_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 8
                    Game.POINTS_LEFT += 3
                nine_button = Button("Nine (+2 Points)", 960, 495)
                if nine_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 9
                    Game.POINTS_LEFT += 2
                ten_button = Button("Ten (+1 Point)", 960, 560)
                if ten_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 10
                    Game.POINTS_LEFT += 1
                twelve_button = Button("Twelve (-1 Point)", 960, 625)
                if twelve_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 12
                    Game.POINTS_LEFT -= 1
                thirteen_button = Button("Thirteen (-2 Points)", 960, 690)
                if thirteen_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 13
                    Game.POINTS_LEFT -= 2
                fourteen_button = Button("Fourteen (-4 Points)", 960, 755)
                if fourteen_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 14
                    Game.POINTS_LEFT -= 4
                fifteen_button = Button("Fifteen (-6 Points)", 960, 820)
                if fifteen_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 15
                    Game.POINTS_LEFT -= 6
            case 12:
                eight_button = Button("Eight (+4 Points)", 960, 430)
                if eight_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 8
                    Game.POINTS_LEFT += 4
                nine_button = Button("Nine (+3 Points)", 960, 495)
                if nine_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 9
                    Game.POINTS_LEFT += 3
                ten_button = Button("Ten (+2 Points)", 960, 560)
                if ten_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 10
                    Game.POINTS_LEFT += 2
                eleven_button = Button("Eleven (+1 Point)", 960, 625)
                if eleven_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 11
                    Game.POINTS_LEFT += 1
                thirteen_button = Button("Thirteen (-1 Point)", 960, 690)
                if thirteen_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 13
                    Game.POINTS_LEFT -= 1
                fourteen_button = Button("Fourteen (-3 Points)", 960, 755)
                if fourteen_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 14
                    Game.POINTS_LEFT -= 3
                fifteen_button = Button("Fifteen (-5 Points)", 960, 820)
                if fifteen_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 15
                    Game.POINTS_LEFT -= 5
            case 13:
                eight_button = Button("Eight (+5 Points)", 960, 430)
                if eight_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 8
                    Game.POINTS_LEFT += 5
                nine_button = Button("Nine (+4 Points)", 960, 495)
                if nine_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 9
                    Game.POINTS_LEFT += 4
                ten_button = Button("Ten (+3 Points)", 960, 560)
                if ten_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 10
                    Game.POINTS_LEFT += 3
                eleven_button = Button("Eleven (+2 Points)", 960, 625)
                if eleven_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 11
                    Game.POINTS_LEFT += 2
                twelve_button = Button("Twelve (+1 Point)", 960, 690)
                if twelve_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 12
                    Game.POINTS_LEFT += 1
                fourteen_button = Button("Fourteen (-2 Points)", 960, 755)
                if fourteen_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 14
                    Game.POINTS_LEFT -= 2
                fifteen_button = Button("Fifteen (-4 Points)", 960, 820)
                if fifteen_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 15
                    Game.POINTS_LEFT -= 4
            case 14:
                eight_button = Button("Eight (+7 Points)", 960, 430)
                if eight_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 8
                    Game.POINTS_LEFT += 7
                nine_button = Button("Nine (+6 Points)", 960, 495)
                if nine_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 9
                    Game.POINTS_LEFT += 6
                ten_button = Button("Ten (+5 Points)", 960, 560)
                if ten_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 10
                    Game.POINTS_LEFT += 5
                eleven_button = Button("Eleven (+4 Points)", 960, 625)
                if eleven_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 11
                    Game.POINTS_LEFT += 4
                twelve_button = Button("Twelve (+3 Points)", 960, 690)
                if twelve_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 12
                    Game.POINTS_LEFT += 3
                thirteen_button = Button("Thirteen (+2 Points)", 960, 755)
                if thirteen_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 13
                    Game.POINTS_LEFT += 2
                fifteen_button = Button("Fifteen (-2 Points)", 960, 820)
                if fifteen_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 15
                    Game.POINTS_LEFT -= 2
            case 15:
                eight_button = Button("Eight (+9 Points)", 960, 430)
                if eight_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 8
                    Game.POINTS_LEFT += 9
                nine_button = Button("Nine (+8 Points)", 960, 495)
                if nine_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 9
                    Game.POINTS_LEFT += 8
                ten_button = Button("Ten (+7 Points)", 960, 560)
                if ten_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 10
                    Game.POINTS_LEFT += 7
                eleven_button = Button("Eleven (+6 Points)", 960, 625)
                if eleven_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 11
                    Game.POINTS_LEFT += 6
                twelve_button = Button("Twelve (+5 Points)", 960, 690)
                if twelve_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 12
                    Game.POINTS_LEFT += 5
                thirteen_button = Button("Thirteen (+4 Points)", 960, 755)
                if thirteen_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 13
                    Game.POINTS_LEFT += 4
                fourteen_button = Button("Fourteen (+2 Points)", 960, 820)
                if fourteen_button.check_click():
                    PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = 14
                    Game.POINTS_LEFT += 2
        if Game.POINTS_LEFT == 0:
            next_button = Button("Next", 960, 1000)
            if next_button.check_click():
                Game.SELECTED_INDEX = 0
                Game.CURRENT_STATE = ScreenState.SELECT_RACE
        if Game.LEFT_ARROW_PRESSED:
            if Game.SELECTED_INDEX == 0:
                Game.SELECTED_INDEX = len(Ability) - 1
            else:
                Game.SELECTED_INDEX -= 1
        elif Game.RIGHT_ARROW_PRESSED:
            if Game.SELECTED_INDEX == len(Ability) - 1:
                Game.SELECTED_INDEX = 0
            else:
                Game.SELECTED_INDEX += 1
        return True
    elif Game.CURRENT_STATE == ScreenState.POINT_ROLL:
        WINDOW.fill(GREEN)
        draw_text("Point Rolling", MEDIUM_FONT, RED, (960, 100))
        if len(Game.ROLL_GROUPS) == 6:
            draw_text(ABILITY_NAME[Ability(Game.SELECTED_INDEX)] + ": " + str(PLAYER.abilities[Ability(Game.SELECTED_INDEX)]), SMALL_FONT, RED, (960, 200), True)
            if PLAYER.abilities[Ability(Game.SELECTED_INDEX)] == 0:
                for x in range(len(Game.ROLL_GROUPS)):
                    if x not in Game.DICE_RESULTS:
                        button = Button(str(Game.ROLL_GROUPS[x]), 960, 300 + (x * 65))
                        if button.check_click():
                            Game.DICE_RESULTS.append(x)
                            PLAYER.abilities[Ability(Game.SELECTED_INDEX)] = Game.ROLL_GROUPS[x]
                            break
            reset_button = Button("Reset", 960, 690)
            if reset_button.check_click():
                for ability in list(Ability):
                    PLAYER.abilities[ability] = 0
                    Game.DICE_RESULTS = []
            if len(Game.DICE_RESULTS) == 6:
                continue_button = Button("Continue", 960, 755)
                if continue_button.check_click():
                    Game.DICE_RESULTS = []
                    Game.ROLL_GROUPS = []
                    Game.SELECTED_INDEX = 0
                    Game.CURRENT_STATE = ScreenState.SELECT_RACE
            if Game.LEFT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == 0:
                    Game.SELECTED_INDEX = len(Ability) - 1
                else:
                    Game.SELECTED_INDEX -= 1
            elif Game.RIGHT_ARROW_PRESSED:
                if Game.SELECTED_INDEX == len(Ability) - 1:
                    Game.SELECTED_INDEX = 0
                else:
                    Game.SELECTED_INDEX += 1
        else:
            if len(Game.ROLL_GROUPS) > 0:
                draw_text("Scores:", SMALL_FONT, RED, (1800, 360))
                for x in range(len(Game.ROLL_GROUPS)):
                    draw_text(str(Game.ROLL_GROUPS[x]), BUTTON_FONT, RED, (1800, 400 + (x * 30)))
            draw_text("This Roll", SMALL_FONT, RED, (960, 300))
            for x in range(len(Game.DICE_RESULTS)):
                colour = GOLD
                if x == 3:
                    colour = RED
                draw_text(str(Game.DICE_RESULTS[x]), BUTTON_FONT, colour, (930 + (x * 20), 360))
            num = Game.DICE_RESULTS[0] + Game.DICE_RESULTS[1] + Game.DICE_RESULTS[2]
            draw_text(str(num), SMALL_FONT, RED, (960, 420))
            if len(Game.ROLL_GROUPS) == 5:
                next_button = Button("Assign the Scores", 960, 480)
                if next_button.check_click():
                    Game.ROLL_GROUPS.append(num)
                    Game.DICE_RESULTS = []
            else:
                next_button = Button("Next Roll", 960, 480)
                if next_button.check_click():
                    Game.ROLL_GROUPS.append(num)
                    Game.DICE_RESULTS = []
                    Game.CURRENT_DICE = [Dice(6), Dice(6), Dice(6), Dice(6)]
        return True

def rolling_dice():
    WINDOW.fill(GREEN)
    draw_text("Rolling Dice", MEDIUM_FONT, RED, (960, 100))
    start_pos = 0
    match len(Game.CURRENT_DICE):
        case 4:
            start_pos = 762
    for x in range(len(Game.CURRENT_DICE)):
        Game.CURRENT_DICE[x].draw(start_pos + (x * 104), 360)
    if len(Game.DICE_RESULTS) == 0:
        roll_button = Button("Roll the Dice", 960, 500)
        if roll_button.check_click():
            for dice in Game.CURRENT_DICE:
                dice.sideFacing = random.randint(1, dice.sides)
                Game.DICE_RESULTS.append(dice.sideFacing)
    else:
        next_button = Button("Continue", 960, 500)
        if next_button.check_click():
            Game.CURRENT_DICE = None
            Game.DICE_RESULTS.sort(reverse = True)

if __name__ == '__main__':
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        # Game Event Handler:
        Game.LEFT_MOUSE_RELEASED = False
        Game.ENTER_PRESSED = False
        Game.CAN_INPUT_TEXT = False
        Game.LEFT_ARROW_PRESSED = False
        Game.RIGHT_ARROW_PRESSED = False
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
                if event.key == pygame.K_LEFT:
                    Game.LEFT_ARROW_PRESSED = True
                if event.key == pygame.K_RIGHT:
                    Game.RIGHT_ARROW_PRESSED = True
                elif event.key in ALLOWED_KEYS:
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