class Team:
    def __init__(self, agents):
        self.agents = agents
        self.synergies = self.get_synergies()

    def __str__(self):
        return f"{self.agents}\n{self.synergies}"
    
    def get_synergies(self):
        synergies = {}

        for agent in self.agents:
            for synergy in agent.synergies:
                try:
                    synergies[synergy] += 1
                except KeyError as e:
                    synergies[synergy] = 1

        return synergies

