import random
import math

N = 8

# Calculate the number of attacking queen pairs
def cost(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# Generate a neighbouring state by swapping two queens
def neighbour(state):
    new_state = state[:]
    i, j = random.sample(range(N), 2)
    new_state[i], new_state[j] = new_state[j], new_state[i]
    return new_state


# Simulated Annealing algorithm
def simulated_annealing():
    while True:
        current = list(range(N))
        random.shuffle(current)

        T = 10.0

        while T > 0.01:
            next_state = neighbour(current)

            delta_E = cost(current) - cost(next_state)

            if delta_E > 0:
                current = next_state

            else:
                p = math.exp(delta_E / T)

                if random.random() < p:
                    current = next_state

            if cost(current) == 0:
                return current

            T *= 0.995


# Display the chessboard
def print_board(state):
    print("\n8 Queens Solution:\n")

    for row in range(N):
        for col in range(N):
            if state[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()


# Main program
solution = simulated_annealing()

print_board(solution)
print("\nNumber of conflicts:", cost(solution))