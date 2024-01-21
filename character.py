from lifeform import *

class Character(Lifeform):
    def __init__(self, fname, lname, ac, max_hp, speed, strength, dex, con, intel, wis, rizz, bonus, percept, lang, size, race, class_, lvl,
                 senses = [], inv = [], prof = [], skills = [], saves = [], resist = [], vulnerable = [], immune = []):
        super().__init__(ac, max_hp, speed, strength, dex, con, intel, wis, rizz, bonus, percept, lang, size, senses, skills, saves, resist, vulnerable, immune)
        self.race = race
        self.class_ = class_
        self.inventory = inv
        self.proficiencies = prof
        self.firstName = fname
        self.lastName = lname
        self.level = lvl
        self.deathS = 0
        self.deathF = 0
        self.twoFreeHands = True
        self.equippedArmour = None
        # Magic
        self.cantrips = []
        # Dragonborn
        self.dragonType = None
