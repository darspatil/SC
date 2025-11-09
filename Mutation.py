import random

# ----- Flipping Mutation -----
def flipping(chromosome, rate=0.1):
    mutated = ""
    for bit in chromosome:
        if random.random() < rate:
            mutated += '0' if bit == '1' else '1'
        else:
            mutated += bit
    print("\n[Flipping Mutation]")
    print("Original:", chromosome)
    print("Mutated :", mutated)

# ----- Interchanging Mutation -----
def interchanging(chromosome):
    i, j = random.sample(range(len(chromosome)), 2)
    chromo_list = list(chromosome)
    chromo_list[i], chromo_list[j] = chromo_list[j], chromo_list[i]
    mutated = ''.join(chromo_list)
    print("\n[Interchanging Mutation]")
    print("Original:", chromosome)
    print(f"Swapped positions: {i} and {j}")
    print("Mutated :", mutated)

# ----- Reversing Mutation -----
def reversing(chromosome):
    i, j = sorted(random.sample(range(len(chromosome)), 2))
    mutated = chromosome[:i] + chromosome[i:j][::-1] + chromosome[j:]
    print("\n[Reversing Mutation]")
    print("Original:", chromosome)
    print(f"Reversed segment: {i}-{j}")
    print("Mutated :", mutated)

# ----- Main Program -----
chromosome = "101101"

while True:
    print("\n===============================")
    print("GENETIC ALGORITHM - MUTATION")
    print("===============================")
    print("1. Flipping")
    print("2. Interchanging")
    print("3. Reversing")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        rate = float(input("Enter mutation rate (0.0 - 1.0): "))
        flipping(chromosome, rate)
    elif ch == 2:
        interchanging(chromosome)
    elif ch == 3:
        reversing(chromosome)
    elif ch == 4:
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice! Try again.")
