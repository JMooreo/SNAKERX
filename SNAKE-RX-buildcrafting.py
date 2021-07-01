from Agents import allAgents
from Synergy import allSetBonuses
from Team import Team
import copy
import random
import itertools
import math
import operator as op
import time
from functools import reduce
from Output import ConsoleOutput, FileOutput
from Performance import Performance

def get_agents():
    return allAgents.copy()

def get_set_bonuses():
    return allSetBonuses.copy()

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def display_profiling_info(output, num_iterations, performance):
    total_time = performance.get_diff()
    total_time_with_label = f"{total_time} seconds" if total_time < 3600 else f"{round(total_time/3600, 2)} hours" 

    output.write_line(f"Went through {num_iterations} iterations.")
    output.write_line("")
    output.write_line(f"Total Time: {total_time_with_label}")
    output.write_line(f"Average iteration time: {1000000*total_time/num_iterations} microseconds")

def display_best_teams(output, best_team, other_good_teams):
    best_team_set_bonuses = []
    
    for setBonus in allSetBonuses:
        bonus = setBonus.get_bonus_level_achieved(best_team.synergies)
        if bonus > 0:
            best_team_set_bonuses.append(f"{str(setBonus)}: {bonus}")

    output.write_line("")
    output.write_line(f"Best Team: {best_team}")
    output.write_line(f"Set Bonuses: {best_team_set_bonuses}")
    output.write_line(f"Score: {best_team.score}")
    output.write_line("")

    if isinstance(output, FileOutput):
        output.write_line("Other Good Teams")

        for team in other_good_teams:
            team_set_bonuses = []
            for setBonus in allSetBonuses:
                bonus = setBonus.get_bonus_level_achieved(best_team.synergies)
                if bonus > 0:
                    team_set_bonuses.append(f"{str(setBonus)}: {bonus}")
            output.write_line(team)
            output.write_line(team_set_bonuses)
            output.write_line(f"Score{team.score}")
            output.write_line("")

def run(num_agents_per_team=7, override=False, override_max_iters=1000000, logging_threshold=100000):
    i = 0
    num_combinations = ncr(len(allAgents), num_agents_per_team)
    num_iterations = num_combinations if not override else override_max_iters

    best_team = []
    other_good_teams = []
    best_team_score = 0

    # For all the combinations of 7 of these agents:
    for agent_combination in itertools.combinations(allAgents, num_agents_per_team):
        if override:
            if i >= override_max_iters:
                break

        # Logging
        if i % 100000 == 0:
            print(f"{i}/{num_iterations} - {int(100*i/num_iterations)}%", end="\r")

        # Create the team + calculate scores
        team = Team(agent_combination)

        # Set the best team stats so far
        if (team.score > best_team_score):
            best_team_score = team.score
            best_team = team
            other_good_teams = []
        elif (team.score >= best_team_score - 1):
            other_good_teams.append(team)

        i += 1
    
    return best_team, other_good_teams, num_iterations

def main():
    run(
        num_agents_per_team=7, 
        override=True, 
        override_max_iters=100000,
        logging_threshold=10000
    )


if __name__ == "__main__":
    import cProfile
    cProfile.run('main()', 'performance/output.dat')

    import pstats
    from pstats import SortKey

    with open("performance/output_time.txt", "w") as f:
        p = pstats.Stats("performance/output.dat", stream=f)
        p.sort_stats("time").print_stats()

    with open("performance/output_calls.txt", "w") as f:
        p = pstats.Stats("performance/output.dat", stream=f)
        p.sort_stats("calls").print_stats()


    # performance = Performance()

    # # performance.start()
    # main()
        
    # stats = pstats.Stats(pr)
    # stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()

    # performance.stop()

    # for output in [FileOutput(f"output/snake-rx-results-{time.time()}.txt")]:
    #     display_profiling_info(output, num_iterations, performance)
    #     display_best_teams(output, best_team, other_good_teams)