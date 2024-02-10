from game import *

class Weapon:
    def __init__(self, name, cost, dmg, dmg_type, properties = [], weapon_type = WeaponType.MARTIAL_MELEE):
        self.name = name
        self.cost = cost
        self.properties = properties
        self.damageType = dmg_type
        self.damage = dmg
        self.type = weapon_type
class Club(Weapon):
    def __init__(self):
        super().__init__("Club", 10, (1, 4), Damage.BLUDGEONING, [Properties.LIGHT], WeaponType.SIMPLE_MELEE)
class Dagger(Weapon):
    def __init__(self):
        super().__init__("Dagger", 200, (1, 4), Damage.PIERCING, [Properties.LIGHT, Properties.FINESSE, Properties.THROWN20_60],
                         WeaponType.SIMPLE_MELEE)
class Greatclub(Weapon):
    def __init__(self):
        super().__init__("Greatclub", 20, (1, 8), Damage.BLUDGEONING, [Properties.TWOHANDED], WeaponType.SIMPLE_MELEE)
class Handaxe(Weapon):
    def __init__(self):
        super().__init__("Handaxe", 500, (1, 6), Damage.SLASHING, [Properties.LIGHT, Properties.THROWN20_60], WeaponType.SIMPLE_MELEE)
class Javelin(Weapon):
    def __init__(self):
        super().__init__("Javelin", 50, (1, 6), Damage.PIERCING, [Properties.THROWN30_120], WeaponType.SIMPLE_MELEE)
class LightHammer(Weapon):
    def __init__(self):
        super().__init__("Light Hammer", 200, (1, 4), Damage.BLUDGEONING, [Properties.LIGHT, Properties.THROWN20_60], WeaponType.SIMPLE_MELEE)
class Mace(Weapon):
    def __init__(self):
        super().__init__("Mace", 500, (1, 6), Damage.BLUDGEONING, WeaponType.SIMPLE_MELEE)
class Quarterstaff(Weapon):
    def __init__(self):
        super().__init__("Quarterstaff", 20, (1, 4), Damage.BLUDGEONING, [Properties.VERSATILE1_8], WeaponType.SIMPLE_MELEE)
class Sickle(Weapon):
    def __init__(self):
        super().__init__("Sickle", 100, (1, 4), Damage.SLASHING, [Properties.LIGHT], WeaponType.SIMPLE_MELEE)
class Spear(Weapon):
    def __init__(self):
        super().__init__("Spear", 100, (1, 6), Damage.PIERCING, [Properties.THROWN20_60, Properties.VERSATILE1_8], WeaponType.SIMPLE_MELEE)
class LightCrossbow(Weapon):
    def __init__(self):
        super().__init__("Light Crossbow", 2500, (1, 8), Damage.PIERCING, [Properties.AMMO80_320, Properties.TWOHANDED, Properties.LOADING],
                         WeaponType.SIMPLE_RANGED)
class Dart(Weapon):
    def __init__(self):
        super().__init__("Dart", 5, (1, 4), Damage.PIERCING, [Properties.FINESSE, Properties.THROWN20_60], WeaponType.SIMPLE_RANGED)
class Shortbow(Weapon):
    def __init__(self):
        super().__init__("Shortbow", 2500, (1, 6), Damage.PIERCING, [Properties.AMMO80_320, Properties.TWOHANDED], WeaponType.SIMPLE_RANGED)
class Sling(Weapon):
    def __init__(self):
        super().__init__("Sling", 10, (1, 4), Damage.BLUDGEONING, [Properties.AMMO30_120], WeaponType.SIMPLE_RANGED)
class Battleaxe(Weapon):
    def __init__(self):
        super().__init__("Battleaxe", 1000, (1, 8), Damage.SLASHING, [Properties.VERSATILE1_10])
class Flail(Weapon):
    def __init__(self):
        super().__init__("Flail", 1000, (1, 8), Damage.BLUDGEONING)
class Glaive(Weapon):
    def __init__(self):
        super().__init__("Glaive", 2000, (1, 10), Damage.SLASHING, [Properties.HEAVY, Properties.REACH, Properties.TWOHANDED])
class Greataxe(Weapon):
    def __init__(self):
        super().__init__("Greataxe", 3000, (1, 12), Damage.SLASHING, [Properties.HEAVY, Properties.TWOHANDED])
class Greatsword(Weapon):
    def __init__(self):
        super().__init__("Greatsword", 5000, (2, 6), Damage.SLASHING, [Properties.HEAVY, Properties.TWOHANDED])
class Halberd(Weapon):
    def __init__(self):
        super().__init__("Halberd", 2000, (1, 10), Damage.SLASHING, [Properties.HEAVY, Properties.REACH, Properties.TWOHANDED])
class Lance(Weapon):
    def __init__(self):
        super().__init__("Lance", 1000, (1, 12), Damage.PIERCING, [Properties.REACH])
class Longsword(Weapon):
    def __init__(self):
        super().__init__("Longsword", 1500, (1, 8), Damage.SLASHING, [Properties.VERSATILE1_10])
class Maul(Weapon):
    def __init__(self):
        super().__init__("Maul", 1000, (2, 6), Damage.BLUDGEONING, [Properties.HEAVY, Properties.TWOHANDED])
class Morningstar(Weapon):
    def __init__(self):
        super().__init__("Morningstar", 1500, (1, 8), Damage.PIERCING)
class Pike(Weapon):
    def __init__(self):
        super().__init__("Pike", 500, (1, 10), Damage.PIERCING, [Properties.HEAVY, Properties.REACH, Properties.TWOHANDED])
class Rapier(Weapon):
    def __init__(self):
        super().__init__("Rapier", 2500, (1, 8), Damage.PIERCING, [Properties.FINESSE])
class Schimitar(Weapon):
    def __init__(self):
        super().__init__("Schimitar", 2500, (1, 6), Damage.SLASHING, [Properties.LIGHT, Properties.FINESSE])
class Shortsword(Weapon):
    def __init__(self):
        super().__init__("Shortsword", 1000, (1, 6), Damage.PIERCING, [Properties.LIGHT, Properties.FINESSE])
class Trident(Weapon):
    def __init__(self):
        super().__init__("Trident", 500, (1, 6), Damage.PIERCING, [Properties.THROWN20_60, Properties.VERSATILE1_8])
class WarPick(Weapon):
    def __init__(self):
        super().__init__("War Pick", 500, (1, 8), Damage.PIERCING)
class Warhammer(Weapon):
    def __init__(self):
        super().__init__("Warhammer", 1500, (1, 8), Damage.BLUDGEONING, [Properties.VERSATILE1_10])
class Whip(Weapon):
    def __init__(self):
        super().__init__("Whip", 200, (1, 4), Damage.SLASHING, [Properties.FINESSE, Properties.REACH])
class Blowgun(Weapon):
    def __init__(self):
        super().__init__("Blowgun", 1000, 1, Damage.PIERCING, [Properties.AMMO25_100, Properties.LOADING], WeaponType.MARTIAL_RANGED)
class HandCrossbow(Weapon):
    def __init__(self):
        super().__init__("Hand Crossbow", 7500, (1, 6), Damage.PIERCING, [Properties.AMMO30_120, Properties.LIGHT, Properties.LOADING],
                         WeaponType.MARTIAL_RANGED)
class HeavyCrossbow(Weapon):
    def __init__(self):
        super().__init__("Heavy Crossbow", 5000, (1, 10), Damage.PIERCING, [Properties.AMMO100_400, Properties.HEAVY, Properties.LOADING, Properties.TWOHANDED],
                         WeaponType.MARTIAL_RANGED)
class Longbow(Weapon):
    def __init__(self):
        super().__init__("Longbow", 5000, (1, 8), Damage.PIERCING, [Properties.AMMO150_600, Properties.HEAVY, Properties.TWOHANDED],
                         WeaponType.MARTIAL_RANGED)
class Net(Weapon):
    def __init__(self):
        super().__init__("Net", 100, 0, Damage.BLUDGEONING, [Properties.THROWN5_15], WeaponType.MARTIAL_RANGED)