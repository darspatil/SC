import numpy as np
import math
import random

# ---- Objective Function ----
# Example: maximize f(x) = x * sin(10πx) + 1.0, where 0 ≤ x ≤ 1
def fitness_function(x):
    return x * math.sin(10 * math.pi * x) + 1.0

# ---- GA Parameters ----
POP_SIZE = 10         # number of individuals
GENS = 30             # number of generations
CROSS_RATE = 0.8      # probability of crossover
MUT_RATE = 0.1        # probability of mutation
X_BOUND = [0, 1]      # range of x values

# ---- Helper Functions ----
def init_population(size):
    return np.random.uniform(X_BOUND[0], X_BOUND[1], size)

def get_fitness(pop):
    return np.array([fitness_function(x) for x in pop])

def select(pop, fitness):
    # Roulette Wheel Selection
    probs = fitness / np.sum(fitness)
    return np.random.choice(pop, size=len(pop), p=probs)

def crossover(parent, pop):
    if np.random.rand() < CROSS_RATE:
        mate = np.random.choice(pop)
        alpha = np.random.rand()
        child = alpha * parent + (1 - alpha) * mate
        return np.clip(child, X_BOUND[0], X_BOUND[1])
    return parent

def mutate(child):
    if np.random.rand() < MUT_RATE:
        child += np.random.normal(0, 0.1)
    return np.clip(child, X_BOUND[0], X_BOUND[1])

# ---- Main GA Function ----
def genetic_algorithm():
    pop = init_population(POP_SIZE)
    print("Initial Population:", np.round(pop, 4))

    for gen in range(GENS):
        fitness = get_fitness(pop)
        best_idx = np.argmax(fitness)
        best_x, best_fit = pop[best_idx], fitness[best_idx]
        print(f"Generation {gen+1:02d}: Best X = {best_x:.4f}, Fitness = {best_fit:.4f}")

        # Selection → Crossover → Mutation
        pop = select(pop, fitness)
        pop_copy = pop.copy()
        for i in range(len(pop)):
            child = crossover(pop[i], pop_copy)
            child = mutate(child)
            pop[i] = child

    # ---- Final Result ----
    fitness = get_fitness(pop)
    best_idx = np.argmax(fitness)
    best_x, best_fit = pop[best_idx], fitness[best_idx]
    print("\n==== Final Result ====")
    print(f"Optimal X = {best_x:.4f}")
    print(f"Maximum Fitness = {best_fit:.4f}")

# ---- Run Program ----
if __name__ == "__main__":
    genetic_algorithm()
