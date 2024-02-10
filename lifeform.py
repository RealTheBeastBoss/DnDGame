class Lifeform:
    def __init__(self, ac, max_hp, speed, bonus, percept, lang, size, abilities,
                 senses = [], skills = [], saves = [], resist = [], vulnerable = [], immune = []):
        self.baseArmourClass = ac
        self.maxHP = max_hp
        self.hp = max_hp
        self.speed = speed
        self.abilities = abilities
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
