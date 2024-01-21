class Spell:
    def __init__(self, lvl, name, desc, school, combat = True, cls = []):
        self.name = name
        self.level = lvl
        self.school = school
        self.description = desc
        self.classes = cls
        self.combatOnly = combat
