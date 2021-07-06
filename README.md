# SNAKERX
Shoutout to the makers of [SNKRX](https://store.steampowered.com/app/915310/SNKRX/) for inspiring this project.

This program is designed to find the team composition with the strongest units and the most synergies in the game SNKRX.

# How to run
1. go to main.py
2. make sure profiling is set to False
3. make sure override in the "run" function is set to False
4. run with Python >= 3.7.6

The program will write the team with the highest score to the console, but also check the file output for some other great team compositions.

# Performance (for nerds)
I'm convinced that this program is not completely optimized. I left the profiler in there in case someone wants to analyze and optimize this code further.
As of July 1, 2021, here are the stats:
- Average time per iteration: ~10 microseconds
- Total Time to complete 115 million iterations: ~20 minutes
