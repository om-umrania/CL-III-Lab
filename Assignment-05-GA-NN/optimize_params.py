# optimize_params.py
import numpy as np
import pandas as pd
from genetic_algorithm import GeneticAlgorithm
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 1. Load data
df = pd.read_csv("data/sample_data.csv")
X = df.drop("particle_size", axis=1).values
y = df["particle_size"].values

# 2. Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Define the neural network model (fixed architecture)
def create_nn():
    return MLPRegressor(
        hidden_layer_sizes=(100,50),
        activation='relu',
        solver='adam',
        max_iter=500,
        random_state=42
    )

# 4. Fitness function for GA: minimize MSE
def fitness_function(params):
    pop_size, cx_rate, mut_rate = params
    nn = create_nn()
    # Initialize GA object
    ga = GeneticAlgorithm(
        population_size=int(pop_size),
        crossover_rate=cx_rate,
        mutation_rate=mut_rate
    )
    # Train NN
    nn.fit(X_train, y_train)
    # Predict & evaluate
    y_pred = nn.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return mse

# 5. Set parameter ranges
parameter_ranges = {
    'population_size': (20, 200),
    'crossover_rate': (0.5, 0.9),
    'mutation_rate': (0.01, 0.2),
}

# 6. Run GA to optimize parameters
ga = GeneticAlgorithm(fitness_function, parameter_ranges)
best_params = ga.optimize()
print("Best Parameters Found:")
print(f"Population Size: {int(best_params[0])}")
print(f"Crossover Rate:   {best_params[1]:.3f}")
print(f"Mutation Rate:    {best_params[2]:.3f}")