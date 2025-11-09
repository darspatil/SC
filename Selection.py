import numpy as np
import random

# ----- Sample Data -----
population = ['C1', 'C2', 'C3', 'C4']
fitness = np.array([80, 10, 6, 4])

# ----- 1. Roulette Wheel Selection -----
def roulette_wheel_selection(population, fitness, n_select=4):
    prob = fitness / np.sum(fitness)
    selected = np.random.choice(population, size=n_select, p=prob)
    print("\nProbabilities:", np.round(prob, 3))
    return selected

# ----- 2. Rank Selection -----
def rank_selection(population, fitness, n_select=4):
    ranks = np.argsort(np.argsort(fitness)) + 1
    prob = ranks / np.sum(ranks)
    selected = np.random.choice(population, size=n_select, p=prob)
    print("\nRanks:", ranks)
    print("Probabilities:", np.round(prob, 3))
    return selected

# ----- 3. Tournament Selection -----
def tournament_selection(population, fitness, k=2, n_select=4):
    selected = []
    for _ in range(n_select):
        contenders = random.sample(list(zip(population, fitness)), k)
        winner = max(contenders, key=lambda x: x[1])
        selected.append(winner[0])
    return selected

# ----- 4. Stochastic Universal Sampling (Optional Stub) -----
def sus_selection(population, fitness, n_select=4):
    prob = fitness / np.sum(fitness)
    cum_prob = np.cumsum(prob)
    start = random.uniform(0, 1/n_select)
    points = [start + i/n_select for i in range(n_select)]
    selected = []
    i = 0
    for p in points:
        while p > cum_prob[i]:
            i += 1
        selected.append(population[i])
    print("\nProbabilities:", np.round(prob, 3))
    return selected

# ----- 5. Elitism Selection -----
def elitism_selection(population, fitness, elite_size=2):
    sorted_indices = np.argsort(fitness)[::-1]
    elites = [population[i] for i in sorted_indices[:elite_size]]
    return elites

# ----- 6. Steady-State Selection -----
def steady_state_selection(population, fitness, num_replace=2):
    """
    Keeps the best individuals and replaces the worst ones
    with new individuals selected (simulated here).
    """
    # Sort population by fitness (descending)
    sorted_indices = np.argsort(fitness)[::-1]
    sorted_pop = [population[i] for i in sorted_indices]
    sorted_fit = [fitness[i] for i in sorted_indices]

    # Keep all except the worst 'num_replace'
    survivors = sorted_pop[:-num_replace]

    # Generate new random individuals (simulate offspring)
    new_individuals = [f"NewC{i+1}" for i in range(num_replace)]

    new_population = survivors + new_individuals
    print("\nOld Population:", population)
    print("Old Fitness:", fitness)
    print("Survivors (Best):", survivors)
    print("New Individuals Added:", new_individuals)
    return new_population


# ----- Display Menu -----
def menu():
    print("\n===============================")
    print(" GENETIC ALGORITHM SELECTION ")
    print("===============================")
    print("1. Roulette Wheel Selection")
    print("2. Rank Selection")
    print("3. Tournament Selection")
    print("4. Stochastic Universal Sampling (SUS)")
    print("5. Elitism Selection")
    print("6. Steady-State Selection")
    print("7. Exit")

# ----- Main Program -----
while True:
    menu()
    choice = int(input("\nEnter your choice (1-7): "))

    if choice == 1:
        selected = roulette_wheel_selection(population, fitness)
        print("Selected Chromosomes:", selected)

    elif choice == 2:
        selected = rank_selection(population, fitness)
        print("Selected Chromosomes:", selected)

    elif choice == 3:
        k = int(input("Enter tournament size (k): "))
        selected = tournament_selection(population, fitness, k)
        print("Selected Chromosomes:", selected)

    elif choice == 4:
        selected = sus_selection(population, fitness)
        print("Selected Chromosomes:", selected)

    elif choice == 5:
        elites = elitism_selection(population, fitness)
        print("Elite Chromosomes:", elites)

    elif choice == 6:
        num_replace = int(input("Enter number of individuals to replace (e.g., 2): "))
        new_population = steady_state_selection(population, fitness, num_replace)
        print("New Population after Steady-State:", new_population)

    elif choice == 7:
        print("\nExiting... Thank you!")
        break

    else:
        print("Invalid choice! Please enter between 1-7.")
