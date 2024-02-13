from utility import *

class Spell:
    def __init__(self, lvl, name, desc, school, use, cls = [], combat = True):
        self.name = name
        self.level = lvl
        self.school = school
        self.description = desc
        self.classes = cls
        self.combatOnly = combat
        self.useFunction = use

def acid_splash(player):
    print("Used Acid Splash!")
def animal_friendship(player):
    print("Used Animal Friendship!")
def bane(player):
    print("Used Bane!")
def bless(player):
    print("Used Bless!")
def chill_touch(player):
    print("Used Chill Touch!")
def cure_wounds(player):
    print("Used Cure Wounds!")
def dancing_lights(player):
    print("Used Dancing Lights!")
def fire_bolt(player):
    print("Used Fire Bolt!")
def guidance(player):
    print("Used Guidance!")
def guiding_bolt(player):
    print("Used Guiding Bolt!")
def healing_word(player):
    print("Used Healing Word!")
def inflict_wounds(player):
    print("Used Inflict Wounds!")
def longstrider(player):
    print("Used Longstrider!")
def poison_spray(player):
    print("Used Poison Spray!")
def ray_of_frost(player):
    print("Used Ray of Frost!")
def resistance(player):
    print("Used Resistance!")
def sacred_flame(player):
    print("Used Sacred Flame!")
def shocking_grasp(player):
    print("Used Shocking Grasp!")
def sleep(player):
    print("Used Sleep!")
def spare_the_dying(player):
    print("Used Spare the Dying!")
def thaumaturgy(player):
    print("Used Thaumaturgy!")
def thunderwave(player):
    print("Used Thunderwave!")
def true_strike(player):
    print("Used True Strike!")
def vicious_mockery(player):
    print("Used Vicious Mockery!")

# Spells:
ACID_SPLASH = Spell(0, "Acid Splash", ["You hurl a bubble of acid. Choose one or two creatures you can see within range.",
                    "If you choose two, they must be within 5 feet of each other. A target must succeed on a Dexterity saving throw or take 1d6 acid damage.",
                    "This spell’s damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6)."],
                    School.CONJURATION, acid_splash, [Class.SORCERER, Class.WIZARD])

ANIMAL_FRIENDSHIP = Spell(1, "Animal Friendship", ["This spell lets you convince a beast that you mean it no harm.",
                        "Choose a beast that you can see within range. It must see and hear you. If the beast's Intelligence is 4 or higher, the spell fails.",
                        "Otherwise, the beast must succeed on a Wisdom saving throw or be charmed by you for the spell's duration.",
                        "If you or one of your companions harms the target, the spell ends.",
                        "At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, you can affect one additional beast for each slot level above 1st."],
                        School.ENCHANTMENT, animal_friendship, [Class.BARD, Class.DRUID, Class.RANGER])

BANE = Spell(1, "Bane", ["Up to three creatures of your choice that you can see within range must make Charisma saving throws.",
            "Whenever a target that fails this saving throw makes an attack roll or a saving throw before the spell ends, the target must roll a d4 and",
            "subtract the number rolled from the attack roll or saving throw.",
            "At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each slot level above 1st."],
             School.ENCHANTMENT, bane, [Class.BARD, Class.CLERIC])

BLESS = Spell(1, "Bless", ["You bless up to three creatures of your choice within range.",
            "Whenever a target makes an attack roll or a saving throw before the spell ends, the target can roll a d4 and add the number rolled to the attack roll or saving throw.",
            "At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each slot level above 1st."],
              School.ENCHANTMENT, bless, [Class.CLERIC, Class.PALADIN])

CHILL_TOUCH = Spell(0, "Chill Touch", ["You create a ghostly, skeletal hand in the space of a creature within range.",
                    "Make a ranged spell attack against the creature to assail it with the chill of the grave.",
                    "On a hit, the target takes 1d8 necrotic damage, and it can't regain hit points until the start of your next turn.",
                    "Until then, the hand clings to the target. If you hit an undead target, it also has disadvantage on attack rolls against you until the end of your next turn.",
                    "This spell's damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8)."],
                    School.NECROMANCY, chill_touch, [Class.SORCERER, Class.WIZARD, Class.WARLOCK])

CURE_WOUNDS = Spell(1, "Cure Wounds", ["A creature you touch regains a number of hit points equal to 1d8 + your spellcasting ability modifier.",
                    "This spell has no effect on undead or constructs.",
                    "At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, the healing increases by 1d8 for each slot level above 1st."],
                    School.EVOCATION, cure_wounds, [Class.BARD, Class.CLERIC, Class.DRUID, Class.PALADIN, Class.RANGER])

DANCING_LIGHTS = Spell(0, "Dancing Lights", ["You create up to four torch-sized lights within range, making them appear as torches, lanterns, or glowing orbs that hover in the air for the duration.",
                        "You can also combine the four lights into one glowing vaguely humanoid form of Medium size. Whichever form you choose, each light sheds dim light in a 10-foot radius.",
                        "As a bonus action on your turn, you can move the lights up to 60 feet to a new spot within range.",
                        "A light must be within 20 feet of another light created by this spell, and a light winks out if it exceeds the spell's range"],
                        School.EVOCATION, dancing_lights, [Class.BARD, Class.WIZARD, Class.SORCERER])

FIRE_BOLT = Spell(0, "Fire Bolt", ["You hurl a mote of fire at a creature or object within range. Make a ranged spell attack against the target.",
                   "On a hit, the target takes 1d10 fire damage. A flammable object hit by this spell ignites if it isn't being worn or carried.",
                   "This spell's damage increases by 1d10 when you reach 5th level (2d10), 11th level (3d10), and 17th level (4d10)."],
                  School.EVOCATION, fire_bolt, [Class.SORCERER, Class.WIZARD])

GUIDANCE = Spell(0, "Guidance", ["You touch one willing creature. Once before the spell ends, the target can roll a d4 and add the number rolled to one ability check of its choice.",
                "It can roll the die before or after making the ability check. The spell then ends."], School.DIVINATION, guidance, [Class.CLERIC, Class.DRUID])

GUIDING_BOLT = Spell(1, "Guiding Bolt", ["A flash of light streaks toward a creature of your choice within range. Make a ranged spell attack against the target.",
                    "On a hit, the target takes 4d6 radiant damage, and the next attack roll made against this target before the end of your next turn has advantage, thanks to the mystical dim light glittering on the target until then.",
                    "At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d6 for each slot level above 1st."],
                     School.EVOCATION, guiding_bolt, [Class.CLERIC])

HEALING_WORD = Spell(1, "Healing Word", ["A creature of your choice that you can see within range regains hit points equal to 1d4 + your spellcasting ability modifier.",
                    "This spell has no effect on undead or constructs.",
                    "At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, the healing increases by 1d4 for each slot level above 1st."],
                     School.EVOCATION, healing_word, [Class.BARD, Class.CLERIC, Class.DRUID])

INFLICT_WOUNDS = Spell(1, "Inflict Wounds", ["Make a melee spell attack against a creature you can reach. On a hit, the target takes 3d10 necrotic damage.",
                    "At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d10 for each slot level above 1st."],
                       School.NECROMANCY, inflict_wounds, [Class.CLERIC])

LONGSTRIDER = Spell(1, "Longstrider", ["You touch a creature. The target’s speed increases by 10 feet until the spell ends.",
                    "At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each slot level above 1st."],
                    School.TRANSMUTATION, longstrider, [Class.BARD, Class.DRUID, Class.RANGER, Class.WIZARD])

POISON_SPRAY = Spell(0, "Poison Spray", ["You extend your hand toward a creature you can see within range and project a puff of noxious gas from your palm.",
                      "The creature must succeed on a Constitution saving throw or take 1d12 poison damage.",
                      "This spell's damage increases by 1d12 when you reach 5th level (2d12), 11th level (3d12), and 17th level (4d12)."],
                     School.CONJURATION, poison_spray, [Class.SORCERER, Class.DRUID, Class.WIZARD, Class.WARLOCK])

RAY_OF_FROST = Spell(0, "Ray of Frost", ["A frigid beam of blue-white light streaks toward a creature within range.",
                    "Make a ranged spell attack against the target. On a hit, it takes 1d8 cold damage, and its speed is reduced by 10 feet until the start of your next turn.",
                    "The spell's damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8)."],
                     School.EVOCATION, ray_of_frost, [Class.SORCERER, Class.WIZARD])

RESISTANCE = Spell(0, "Resistance", ["You touch one willing creature. Once before the spell ends, the target can roll a d4 and add the number rolled to one saving throw of its choice.",
                    "It can roll the die before or after making the saving throw. The spell then ends."], School.ABJURATION, resistance, [Class.CLERIC, Class.DRUID])

SACRED_FLAME = Spell(0, "Sacred Flame", ["Flame-like radiance descends on a creature that you can see within range. The target must succeed on a Dexterity saving throw or take 1d8 radiant damage.",
                    "The target gains no benefit from cover for this saving throw.",
                    "The spell's damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8)."], School.EVOCATION, sacred_flame,
                     [Class.CLERIC])

SHOCKING_GRASP = Spell(0, "Shocking Grasp", ["Lightning springs from your hand to deliver a shock to a creature you try to touch.",
                    "Make a melee spell attack against the target. You have advantage on the attack roll if the target is wearing armor made of metal.",
                    "On a hit, the target takes 1d8 lightning damage, and it can't take reactions until the start of its next turn.",
                    "The spell's damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8)."],
                    School.EVOCATION, shocking_grasp, [Class.SORCERER, Class.WIZARD])

SLEEP = Spell(1, "Sleep", ["This spell sends creatures into a magical slumber. Roll 5d8; the total is how many hit points of creatures this spell can affect.",
                "Creatures within 20 feet of a point you choose within range are affected in ascending order of their current hit points (ignoring unconscious creatures).",
                "Starting with the creature that has the lowest current hit points, each creature affected by this spell falls unconscious until the spell ends,",
                "the sleeper takes damage, or someone uses an action to shake or slap the sleeper awake.",
                "Subtract each creature’s hit points from the total before moving on to the creature with the next lowest hit points.",
                "A creature’s hit points must be equal to or less than the remaining total for that creature to be affected.Undead and creatures immune to being charmed aren’t affected by this spell.",
                "At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, roll an additional 2d8 for each slot level above 1st."],
              School.ENCHANTMENT, sleep, [Class.BARD, Class.SORCERER, Class.WIZARD])

SPARE_THE_DYING = Spell(0, "Spare the Dying", ["You touch a living creature that has 0 hit points. The creature becomes stable. This spell has no effect on undead or constructs."],
                        School.NECROMANCY, spare_the_dying, [Class.CLERIC])

THAUMATURGY = Spell(0, "Thaumaturgy", ["You manifest a minor wonder, a sign of supernatural power, within range. You create one of the following magical effects within range:",
                    "- Your voice booms up to three times as loud as normal for 1 minute.",
                    "- You cause flames to flicker, brighten, dim, or change color for 1 minute.",
                    "- You cause harmless tremors in the ground for 1 minute.",
                    "- You create an instantaneous sound that originates from a point of your choice within range, such as a rumble of thunder, the cry of a raven, or ominous whispers.",
                    "- You instantaneously cause an unlocked door or window to fly open or slam shut.",
                    "- You alter the appearance of your eyes for 1 minute.",
                    "If you cast this spell multiple times, you can have up to three of its 1-minute effects active at a time, and you can dismiss such an effect as an action."],
                    School.TRANSMUTATION, thaumaturgy, [Class.CLERIC])

THUNDERWAVE = Spell(1, "Thunderwave", ["A wave of thunderous force sweeps out from you. Each creature in a 15-foot cube originating from you must make a Constitution saving throw.",
                    "On a failed save, a creature takes 2d8 thunder damage and is pushed 10 feet away from you. On a successful save, the creature takes half as much damage and isn't pushed.",
                    "In addition, unsecured objects that are completely within the area of effect are automatically pushed 10 feet away from you by the spell's effect,",
                    "and the spell emits a thunderous boom audible out to 300 feet.",
                    "At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d8 for each slot level above 1st."],
                    School.EVOCATION, thunderwave, [Class.BARD, Class.DRUID, Class.SORCERER, Class.WIZARD])

TRUE_STRIKE = Spell(0, "True Strike", ["You point a finger at a target in range. Your magic grants you a brief insight into the target's defenses.",
                    "On your next turn, you gain advantage on your first attack roll against the target, provided that this spell hasn't ended."],
                    School.DIVINATION, true_strike, [Class.BARD, Class.SORCERER, Class.WARLOCK, Class.WIZARD])

VICIOUS_MOCKERY = Spell(0, "Vicious Mockery", ["You unleash a string of insults laced with subtle enchantments at a creature you can see within range.",
                        "If the target can hear you (though it need not understand you), it must succeed on a Wisdom saving throw or take 1d4 psychic damage",
                        "and have disadvantage on the next attack roll it makes before the end of its next turn.",
                        "This spell's damage increases by 1d4 when you reach 5th level (2d4), 11th level (3d4), and 17th level (4d4)."], School.ENCHANTMENT,
                        vicious_mockery, [Class.BARD])

ALL_SPELLS = [ACID_SPLASH, ANIMAL_FRIENDSHIP, BANE, BLESS, CHILL_TOUCH, CURE_WOUNDS, DANCING_LIGHTS, FIRE_BOLT, GUIDANCE, GUIDING_BOLT, HEALING_WORD, INFLICT_WOUNDS,
              LONGSTRIDER, POISON_SPRAY, RAY_OF_FROST, RESISTANCE, SACRED_FLAME, SHOCKING_GRASP, SLEEP, SPARE_THE_DYING, THAUMATURGY, THUNDERWAVE, TRUE_STRIKE, VICIOUS_MOCKERY]
