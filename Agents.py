from Stats import Stats
from Agent import Agent


#### RED UNITS
class Scout(Agent):
    def __init__(self):
        super().__init__(1, ["Rogue"])

class Jester(Agent):
    def __init__(self):
        super().__init__(2, ["Rogue", "Curser"])

class Beastmaster(Agent):
    def __init__(self):
        super().__init__(2, ["Rogue", "Swarmer"])

class Outlaw(Agent):
    def __init__(self):
        super().__init__(2, ["Rogue", "Warrior"])

class Pyromancer(Agent):
    def __init__(self):
        super().__init__(3, ["Mage", "Nuker", "Voider"])

class Thief(Agent):
    def __init__(self):
        super().__init__(4, ["Rogue", "Mercenary"])

class Vulcanist(Agent):
    def __init__(self):
        super().__init__(4, ["Sorcerer", "Nuker"])


#### GREEN UNITS
class Archer(Agent):
    def __init__(self):
        super().__init__(1, ["Ranger"])

class Cleric(Agent):
    def __init__(self):
        super().__init__(1, ["Healer"])

class Carver(Agent):
    def __init__(self):
        super().__init__(2, ["Conjurer", "Healer"])

class DualGunner(Agent):
    def __init__(self):
        super().__init__(2, ["Rogue", "Ranger"])

class Hunter(Agent):
    def __init__(self):
        super().__init__(2, ["Rogue", "Ranger"])

class Barrager(Agent):
    def __init__(self):
        super().__init__(3, ["Ranger", "Forcer"])

class Fairy(Agent):
    def __init__(self):
        super().__init__(4, ["Enchanter", "Healer"])

class Priest(Agent):
    def __init__(self):
        super().__init__(4, ["Healer"])


###### BLUE UNITS

class Magician(Agent):
    def __init__(self):
        super().__init__(1, ["Mage"])

class Wizard(Agent):
    def __init__(self):
        super().__init__(2, ["Mage", "Nuker"])

class Chronomancer(Agent):
    def __init__(self):
        super().__init__(2, ["Mage", "Enchanter"])

class Cryomancer(Agent):
    def __init__(self):
        super().__init__(2, ["Mage", "Voider"])

class Spellblade(Agent):
    def __init__(self):
        super().__init__(3, ["Rogue", "Mage"])

class Stormweaver(Agent):
    def __init__(self):
        super().__init__(3, ["Enchanter"])

class Elementor(Agent):
    def __init__(self):
        super().__init__(3, ["Mage", "Nuker"])

### INDIGO UNITS

class Arcanist(Agent):
    def __init__(self):
        super().__init__(1, ["Sorcerer"])

class Silencer(Agent):
    def __init__(self):
        super().__init__(2, ["Sorcerer", "Curser"])

class Illusionist(Agent):
    def __init__(self):
        super().__init__(3, ["Sorcerer", "Conjurer"])

### YELLOW UNITS

class Swordsman(Agent):
    def __init__(self):
        super().__init__(1, ["Warrior"])

class Barbarian(Agent):
    def __init__(self):
        super().__init__(2, ["Warrior", "Curser"])

class Squire(Agent):
    def __init__(self):
        super().__init__(2, ["Warrior", "Enchanter"])

class Juggernaut(Agent):
    def __init__(self):
        super().__init__(3, ["Forcer", "Warrior"])

class Blade(Agent):
    def __init__(self):
        super().__init__(4, ["Warrior", "Nuker"])

class Highlander(Agent):
    def __init__(self):
        super().__init__(4, ["Warrior"])

class Warden(Agent):
    def __init__(self):
        super().__init__(4, ["Sorcerer", "Forcer"])


### GOLD UNITS

class Merchant(Agent):
    def __init__(self):
        super().__init__(1, ["Mercenary"])

class Miner(Agent):
    def __init__(self):
        super().__init__(2, ["Mercenary"])

class Gambler(Agent):
    def __init__(self):
        super().__init__(3, ["Mercenary", "Sorcerer"])

class Scout(Agent):
    def __init__(self):
        super().__init__(1, ["Rogue"])

### ORANGE UNITS

class Saboteur(Agent):
    def __init__(self):
        super().__init__(2, ["Rogue", "Conjurer", "Nuker"])

class Engineer(Agent):
    def __init__(self):
        super().__init__(3, ["Conjurer"])

class Host(Agent):
    def __init__(self):
        super().__init__(3, ["Swarmer"])

class Infestor(Agent):
    def __init__(self):
        super().__init__(3, ["Curser", "Swarmer"])

class Corruptor(Agent):
    def __init__(self):
        super().__init__(4, ["Ranger", "Swarmer"])

class Cannoneer(Agent):
    def __init__(self):
        super().__init__(4, ["Ranger", "Nuker"])

### PURPLE UNITS

class Sage(Agent):
    def __init__(self):
        super().__init__(2, ["Nuker", "Forcer"])

class Witch(Agent):
    def __init__(self):
        super().__init__(2, ["Sorcerer", "Voider"])

class Assassin(Agent):
    def __init__(self):
        super().__init__(3, ["Rogue", "Voider"])

class Bane(Agent):
    def __init__(self):
        super().__init__(3, ["Curser", "Voider"])

class Userer(Agent):
    def __init__(self):
        super().__init__(3, ["Curser", "Mercenary", "Voider"])

class PlagueDoctor(Agent):
    def __init__(self):
        super().__init__(4, ["Nuker", "Voider"])


### WHITE UNITS
class Vagrant(Agent):
    def __init__(self):
        super().__init__(1, ["Psyker", "Ranger", "Warrior"])

class Psychic(Agent):
    def __init__(self):
        super().__init__(2, ["Sorcerer", "Psyker"])

class Flagellant(Agent):
    def __init__(self):
        super().__init__(3, ["Psyker", "Enchanter"])

class Psykeeper(Agent):
    def __init__(self):
        super().__init__(3, ["Healer", "Psyker"])

class Psykino(Agent):
    def __init__(self):
        super().__init__(1, ["Mage", "Psyker", "Forcer"])


allAgents = [
    Scout(),
    Jester(),
    Beastmaster(),
    Outlaw(),
    Pyromancer(),
    Thief(),
    Vulcanist(),
    Archer(),
    Cleric(),
    Carver(),
    DualGunner(),
    Hunter(),
    Barrager(),
    Fairy(),
    Priest(),
    Magician(),
    Wizard(),
    Chronomancer(),
    Cryomancer(),
    Spellblade(),
    Stormweaver(),
    Elementor(),
    Arcanist(),
    Silencer(),
    Illusionist(),
    Swordsman(),
    Barbarian(),
    Squire(),
    Juggernaut(),
    Blade(),
    Highlander(),
    Warden(),
    # Merchant(),
    # Miner(),
    Gambler(),
    Scout(),
    Saboteur(),
    Engineer(),
    Host(),
    Infestor(),
    Corruptor(),
    Cannoneer(),
    Sage(),
    Witch(),
    Assassin(),
    Bane(),
    Userer(),
    PlagueDoctor(),
    Vagrant(),
    Psychic(),
    Flagellant(),
    Psykeeper(),
    Psykino(),
]


