import random
import numpy as np
import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from deap import base, creator, tools, algorithms

# 1. Load data
df = pd.read_csv("data/sample_data.csv")
X = df.drop("particle_size", axis=1).values
y = df["particle_size"].values

# Normalize inputs (optional but helps)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)

# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Fitness function for DEAP
def eval_nn(individual):
    pop_size, cx_rate, mut_rate = int(individual[0]), individual[1], individual[2]

    # Train NN once per individual
    model = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=500, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return (mse,)

# 4. DEAP Setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("population_size", random.randint, 20, 200)
toolbox.register("crossover_rate", random.uniform, 0.5, 0.9)
toolbox.register("mutation_rate", random.uniform, 0.01, 0.2)

toolbox.register("individual", tools.initCycle, creator.Individual,
                 (toolbox.population_size, toolbox.crossover_rate, toolbox.mutation_rate), n=1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", eval_nn)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.05, indpb=0.3)
toolbox.register("select", tools.selTournament, tournsize=3)

# 5. Run GA
population = toolbox.population(n=15)
algorithms.eaSimple(population, toolbox, cxpb=0.5, mutpb=0.3, ngen=10, verbose=True)

# 6. Get best individual
best_ind = tools.selBest(population, k=1)[0]
print("\n✅ Best Parameters Found:")
print(f"Population Size: {int(best_ind[0])}")
print(f"Crossover Rate:  {best_ind[1]:.3f}")
print(f"Mutation Rate:   {best_ind[2]:.3f}")