from Stats import Stats
from Synergy import Synergy
from Agent import Agent


#### RED UNITS
class Scout(Agent):
    def __init__(self):
        super().__init__(1, [Synergy.Rogue])

class Jester(Agent):
    def __init__(self):
        super().__init__(2, [Synergy.Rogue, Synergy.Curser])

class Beastmaster(Agent):
    def __init__(self):
        super().__init__(2, [Synergy.Rogue, Synergy.Swarmer])

class Outlaw(Agent):
    def __init__(self):
        super().__init__(2, [Synergy.Rogue, Synergy.Warrior])

class Pyromancer(Agent):
    def __init__(self):
        super().__init__(3, [Synergy.Mage, Synergy.Nuker, Synergy.Voider])

class Thief(Agent):
    def __init__(self):
        super().__init__(4, [Synergy.Rogue, Synergy.Mercenary])

class Vulcanist(Agent):
    def __init__(self):
        super().__init__(4, [Synergy.Sorcerer, Synergy.Nuker])


#### GREEN UNITS
class Archer(Agent):
    def __init__(self):
        super().__init__(1, [Synergy.Ranger])

class Cleric(Agent):
    def __init__(self):
        super().__init__(1, [Synergy.Healer])

class Carver(Agent):
    def __init__(self):
        super().__init__(2, [Synergy.Conjurer, Synergy.Healer])

class DualGunner(Agent):
    def __init__(self):
        super().__init__(2, [Synergy.Rogue, Synergy.Ranger])

class Hunter(Agent):
    def __init__(self):
        super().__init__(2, [Synergy.Rogue, Synergy.Ranger])

class Barrager(Agent):
    def __init__(self):
        super().__init__(3, [Synergy.Ranger, Synergy.Forcer])

class Fairy(Agent):
    def __init__(self):
        super().__init__(4, [Synergy.Enchanter, Synergy.Healer])

class Priest(Agent):
    def __init__(self):
        super().__init__(4, [Synergy.Healer])


###### BLUE UNITS

class Magician(Agent):
    def __init__(self):
        super().__init__(1, [Synergy.Mage])

class Wizard(Agent):
    def __init__(self):
        super().__init__(2, [Synergy.Mage, Synergy.Nuker])

class Chronomancer(Agent):
    def __init__(self):
        super().__init__(2, [Synergy.Mage, Synergy.Enchanter])

class Cryomancer(Agent):
    def __init__(self):
        super().__init__(2, [Synergy.Mage, Synergy.Voider])

class Spellblade(Agent):
    def __init__(self):
        super().__init__(3, [Synergy.Rogue, Synergy.Mage])

class Stormweaver(Agent):
    def __init__(self):
        super().__init__(3, [Synergy.Enchanter])

class Elementor(Agent):
    def __init__(self):
        super().__init__(3, [Synergy.Mage, Synergy.Nuker])

### INDIGO UNITS

class Arcanist(Agent):
    def __init__(self):
        super().__init__(1, [Synergy.Sorcerer])

class Silencer(Agent):
    def __init__(self):
        super().__init__(2, [Synergy.Sorcerer, Synergy.Curser])

class Illusionist(Agent):
    def __init__(self):
        super().__init__(3, [Synergy.Sorcerer, Synergy.Conjurer])

### YELLOW UNITS

class Swordsman(Agent):
    def __init__(self):
        super().__init__(1, [Synergy.Warrior])

class Barbarian(Agent):
    def __init__(self):
        super().__init__(2, [Synergy.Warrior, Synergy.Curser])

class Squire(Agent):
    def __init__(self):
        super().__init__(2, [Synergy.Warrior, Synergy.Enchanter])

class Juggernaut(Agent):
    def __init__(self):
        super().__init__(3, [Synergy.Forcer, Synergy.Warrior])

class Blade(Agent):
    def __init__(self):
        super().__init__(4, [Synergy.Warrior, Synergy.Nuker])

class Highlander(Agent):
    def __init__(self):
        super().__init__(4, [Synergy.Warrior])

class Warden(Agent):
    def __init__(self):
        super().__init__(4, [Synergy.Sorcerer, Synergy.Forcer])


### GOLD UNITS

class Merchant(Agent):
    def __init__(self):
        super().__init__(1, [Synergy.Mercenary])

class Miner(Agent):
    def __init__(self):
        super().__init__(2, [Synergy.Mercenary])

class Gambler(Agent):
    def __init__(self):
        super().__init__(3, [Synergy.Mercenary, Synergy.Sorcerer])

class Scout(Agent):
    def __init__(self):
        super().__init__(1, [Synergy.Rogue])

### ORANGE UNITS

class Saboteur(Agent):
    def __init__(self):
        super().__init__(2, [Synergy.Rogue, Synergy.Conjurer, Synergy.Nuker])

class Engineer(Agent):
    def __init__(self):
        super().__init__(3, [Synergy.Conjurer])

class Host(Agent):
    def __init__(self):
        super().__init__(3, [Synergy.Swarmer])

class Infestor(Agent):
    def __init__(self):
        super().__init__(3, [Synergy.Curser, Synergy.Swarmer])

class Corruptor(Agent):
    def __init__(self):
        super().__init__(4, [Synergy.Ranger, Synergy.Swarmer])

class Cannoneer(Agent):
    def __init__(self):
        super().__init__(4, [Synergy.Ranger, Synergy.Nuker])

### PURPLE UNITS

class Sage(Agent):
    def __init__(self):
        super().__init__(2, [Synergy.Nuker, Synergy.Forcer])

class Witch(Agent):
    def __init__(self):
        super().__init__(2, [Synergy.Sorcerer, Synergy.Voider])

class Assassin(Agent):
    def __init__(self):
        super().__init__(3, [Synergy.Rogue, Synergy.Voider])

class Bane(Agent):
    def __init__(self):
        super().__init__(3, [Synergy.Curser, Synergy.Voider])

class Userer(Agent):
    def __init__(self):
        super().__init__(3, [Synergy.Curser, Synergy.Mercenary, Synergy.Voider])

class PlagueDoctor(Agent):
    def __init__(self):
        super().__init__(4, [Synergy.Nuker, Synergy.Voider])


### WHITE UNITS
class Vagrant(Agent):
    def __init__(self):
        super().__init__(1, [Synergy.Psyker, Synergy.Ranger, Synergy.Warrior])

class Psychic(Agent):
    def __init__(self):
        super().__init__(2, [Synergy.Sorcerer, Synergy.Psyker])

class Flagellant(Agent):
    def __init__(self):
        super().__init__(3, [Synergy.Psyker, Synergy.Enchanter])

class Psykeeper(Agent):
    def __init__(self):
        super().__init__(3, [Synergy.Healer, Synergy.Psyker])

class Psykino(Agent):
    def __init__(self):
        super().__init__(1, [Synergy.Mage, Synergy.Psyker, Synergy.Forcer])


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


