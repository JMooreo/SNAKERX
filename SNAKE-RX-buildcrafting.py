from Agents import allAgents
from Synergy import allSetBonuses
from Team import Team
import copy
import random
import itertools
import math
import operator as op
from functools import reduce
import time

def get_agents():
    return allAgents.copy()

def get_set_bonuses():
    return allSetBonuses.copy()

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

if __name__ == "__main__":
    #### CONFIG
    num_agents_per_team = 7
    override = True
    override_max_iters = 1000000

    # Create all the unique Agents and put them in a list
    agents = get_agents()

    # Init variables
    best_team = []
    other_good_teams = []
    best_team_bonuses = []
    best_team_score = 0
    i = 0
    num_combinations = ncr(len(allAgents), num_agents_per_team)
    totalTime = 0
    num_iterations = num_combinations if not override else override_max_iters
    
    # Begin Performance
    t0 = time.perf_counter()

    # For all the combinations of 7 of these characters:
    for agent_combination in itertools.combinations(agents, num_agents_per_team):
        if override:
            if i >= override_max_iters:
                break

        # Logging
        if i % 100000 == 0:
            print(f"{i}/{num_iterations} - {int(100*i/num_iterations)}%", end="\r")

        # Create the team
        team = Team(agent_combination)

        # Sum the level of the set bonuses
        team_score = sum([setBonus.get_bonus_level_achieved(team.synergies) for setBonus in allSetBonuses])

        # Set the best team stats so far
        if (team_score > best_team_score):
            best_team_score = team_score
            best_team = team
            other_good_teams = []
        elif (team_score == best_team_score):
            other_good_teams.append(team)

        i += 1

    # End Perforance
    t1 = time.perf_counter()
    totalTime = t1-t0

    best_team_set_bonuses = []
    for setBonus in allSetBonuses:
        bonus = setBonus.get_bonus_level_achieved(best_team.synergies)
        if bonus > 0:
            best_team_set_bonuses.append(f"{str(setBonus)}: {bonus}")
    
    print(f"Went through {num_iterations} iterations.")
    print(f"Total Time: {totalTime} seconds")
    print(f"Average iteration time: {1000000*totalTime/num_iterations} microseconds")
    print()
    print(f"Best Team: {best_team}")
    print(f"Set Bonuses: {best_team_set_bonuses}")
    print(f"Score: {best_team_score}")
    print(f"Bonuses: {best_team_bonuses}")
    print()
    print("Other Good teams")
    file = open("Desktop/snake-rx-results.txt", "w")

    file.write(f"Went through {num_iterations} iterations.\n")
    file.write(f"Average iteration time: {totalTime/num_iterations}\n")
    file.write(f"Best Team: {best_team}\n")
    file.write(f"Set Bonuses: {best_team_set_bonuses}\n")
    file.write(f"Score: {best_team_score}\n")
    file.write(f"Bonuses: {best_team_bonuses}\n")
    file.write("\nOther Good teams\n")

    for team in other_good_teams:
        file.write(f"{team}\n")


    # t2 = time.perf_counter()
    # x = 0
    # for i in range(150000000):
    #     x = i
    #     if (i % 1000000 == 0):
    #         print(i, end="\r")
    # t3 = time.perf_counter()

    # print("Looping 150 mil times took", t3-t2, "seconds")
    