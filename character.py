from lifeform import *
from game import *

class Character(Lifeform):
    def __init__(self, fname, lname, ac, max_hp, bonus, percept, lang, size, race, class_, lvl,
                 speed = 0, abilities = {Ability.STRENGTH: 0, Ability.CONSTITUTION: 0, Ability.DEXTERITY: 0, Ability.INTELLIGENCE: 0, Ability.WISDOM: 0, Ability.CHARISMA: 0},
                 senses = [], inv = [], prof = [], skills = [], saves = [], resist = [], vulnerable = [], immune = []):
        super().__init__(ac, max_hp, speed, bonus, percept, lang, size, abilities, senses, skills, saves, resist, vulnerable, immune)
        self.race = race
        self.class_ = class_
        self.inventory = inv
        self.proficiencies = prof
        self.abilities = abilities
        self.firstName = fname
        self.lastName = lname
        self.level = lvl
        self.deathS = 0
        self.deathF = 0
        self.twoFreeHands = True
        self.equippedArmour = None
        self.hitDice = None
        self.usingShield = False
        self.inspired = False
        # Magic
        self.concentrating = False
        self.spellAbility = None
        self.cantrips = []
        self.knownSpells = []
        self.lvl1SlotsLeft = 0
        # Dragonborn
        self.dragonType = None
        # Barbarian
        self.ragesLeft = 0
        self.isRaging = False
        self.rageDamage = 0
        # Bard
        self.inspiresLeft = 0
        self.inspireDice = None
