from game import *

class Lifeform:
    def __init__(self, ac, max_hp, speed, strength, dex, con, intel, wis, rizz, bonus, percept, lang, size,
                 senses = [], skills = [], saves = [], resist = [], vulnerable = [], immune = []):
        self.baseArmourClass = ac
        self.maxHP = max_hp
        self.hp = max_hp
        self.speed = speed
        self.strength = strength
        self.dexterity = dex
        self.constitution = con
        self.intelligence = intel
        self.wisdom = wis
        self.charisma = rizz
        self.profBonus = bonus
        self.skills = skills
        self.saves = saves
        self.immunities = immune
        self.resistance = resist
        self.vulnerabilities = vulnerable
        self.passivePerception = percept
        self.senses = senses
        self.languages = lang
        self.size = size
