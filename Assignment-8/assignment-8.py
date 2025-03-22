# --- Step 1: Import necessary libraries
import random
from deap import base, creator, tools, algorithms
import multiprocessing

# --- Step 2: Define the evaluation function
def eval_func(individual):
    # Objective: Minimize sum of squares (Simple quadratic minimization)
    return sum(x ** 2 for x in individual),

# --- Step 3: Setup DEAP environment
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# --- Step 4: Register functions to generate individuals and population
toolbox.register("attr_float", random.uniform, -5.0, 5.0)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=3)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# --- Step 5: Register genetic operators
toolbox.register("evaluate", eval_func)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# --- Step 6: Enable multiprocessing (parallel evaluation)
if __name__ == "__main__":
    pool = multiprocessing.Pool()
    toolbox.register("map", pool.map)

    # --- Step 7: Initialize population and set parameters
    population = toolbox.population(n=50)
    generations = 20
    cxpb = 0.5  # Crossover probability
    mutpb = 0.1  # Mutation probability

    # --- Step 8: Evolution Process
    for gen in range(generations):
        offspring = algorithms.varAnd(population, toolbox, cxpb=cxpb, mutpb=mutpb)
        fits = toolbox.map(toolbox.evaluate, offspring)

        for fit, ind in zip(fits, offspring):
            ind.fitness.values = fit

        population = toolbox.select(offspring, k=len(population))

    # --- Step 9: Best Result
    best_ind = tools.selBest(population, k=1)[0]
    print("Best individual:", best_ind)
    print("Best fitness value:", best_ind.fitness.values[0])