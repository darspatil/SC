# -------------------------------------------------------------
# Title   : Demonstration of Crossover Techniques in Genetic Algorithm
# Subject : Soft Computing / Artificial Intelligence Lab
# Author  : Pranav Anil Dhebe
# -------------------------------------------------------------

import random

# Helper function to print crossover results
def display(p1, p2, c1, c2, title):
    print(f"\n[{title}]")
    print(f"Parent 1: {p1}")
    print(f"Parent 2: {p2}")
    print("-----------------------------")
    print(f"Child 1 : {c1}")
    print(f"Child 2 : {c2}")
    print("-----------------------------\n")

# =============================================================
# 1. Single Point Crossover
# =============================================================
def single_point_crossover(p1, p2):
    point = random.randint(1, len(p1) - 2)
    c1 = p1[:point] + p2[point:]
    c2 = p2[:point] + p1[point:]
    print(f"Crossover Point: {point}")
    display(p1, p2, c1, c2, "Single Point Crossover")

# =============================================================
# 2. Two Point Crossover
# =============================================================
def two_point_crossover(p1, p2):
    point1 = random.randint(1, len(p1) - 3)
    point2 = random.randint(point1 + 1, len(p1) - 2)
    c1 = p1[:point1] + p2[point1:point2] + p1[point2:]
    c2 = p2[:point1] + p1[point1:point2] + p2[point2:]
    print(f"Crossover Points: {point1}, {point2}")
    display(p1, p2, c1, c2, "Two Point Crossover")

# =============================================================
# 3. Uniform Crossover
# =============================================================
def uniform_crossover(p1, p2):
    mask = [random.randint(0, 1) for _ in range(len(p1))]
    c1, c2 = "", ""
    for i in range(len(p1)):
        if mask[i] == 0:
            c1 += p1[i]
            c2 += p2[i]
        else:
            c1 += p2[i]
            c2 += p1[i]
    print("Mask:", mask)
    display(p1, p2, c1, c2, "Uniform Crossover")

# =============================================================
# 4. Arithmetic Crossover (for numeric parents)
# =============================================================
def arithmetic_crossover(p1, p2):
    alpha = random.random()
    c1 = [round(alpha * x + (1 - alpha) * y, 2) for x, y in zip(p1, p2)]
    c2 = [round(alpha * y + (1 - alpha) * x, 2) for x, y in zip(p1, p2)]
    print(f"Alpha = {alpha:.2f}")
    print(f"Parent 1: {p1}")
    print(f"Parent 2: {p2}")
    print("-----------------------------")
    print(f"Child 1 : {c1}")
    print(f"Child 2 : {c2}")
    print("-----------------------------\n")

# =============================================================
# 5. Half Uniform Crossover (HUX)
# =============================================================
def half_uniform_crossover(p1, p2):
    diff_positions = [i for i in range(len(p1)) if p1[i] != p2[i]]
    random.shuffle(diff_positions)
    half = len(diff_positions) // 2
    c1, c2 = list(p1), list(p2)

    for i in range(half):
        pos = diff_positions[i]
        c1[pos], c2[pos] = c2[pos], c1[pos]

    print("Swapped Positions:", diff_positions[:half])
    display(p1, p2, "".join(c1), "".join(c2), "Half Uniform Crossover (HUX)")

# =============================================================
# Main Program (Menu-Driven)
# =============================================================
def main():
    parent1 = "110011"
    parent2 = "101101"
    parent_num1 = [2.5, 3.0, 4.5]
    parent_num2 = [3.5, 2.0, 5.5]

    while True:
        print("\n===============================")
        print("GENETIC ALGORITHM - CROSSOVER")
        print("===============================")
        print("1. Single Point Crossover")
        print("2. Two Point Crossover")
        print("3. Uniform Crossover")
        print("4. Arithmetic Crossover")
        print("5. Half Uniform Crossover (HUX)")
        print("6. Exit")

        choice = int(input("\nEnter your choice (1-6): "))

        if choice == 1:
            single_point_crossover(parent1, parent2)
        elif choice == 2:
            two_point_crossover(parent1, parent2)
        elif choice == 3:
            uniform_crossover(parent1, parent2)
        elif choice == 4:
            arithmetic_crossover(parent_num1, parent_num2)
        elif choice == 5:
            half_uniform_crossover(parent1, parent2)
        elif choice == 6:
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Try again.")

# Run program
if __name__ == "__main__":
    main()
