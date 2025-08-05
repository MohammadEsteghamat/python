import random

def fitness(subset, target):
    total = sum(subset)
    return total if total <= target else - float('inf')

def get_neighbors(current, items):
    neighbors = []
    for item in items:
        if item in current:
            neighbor = current.copy()
            neighbor.remove(item)
            neighbors.append(neighbor)
        else:
            neighbor = current.copy()
            neighbor.append(item)
            neighbors.append(neighbor)
    return neighbors

def hill_climbing(items, target, max_iterations=1000):
    current = random.sample(items, random.randint(1, len(items)))
    best_fitness = fitness(current, target)
    
    for _ in range(max_iterations):
        neighbors = get_neighbors(current, items)
        next_move = current
        for neighbor in neighbors:
            f = fitness(neighbor, target)
            if f > best_fitness:
                next_move = neighbor
                best_fitness = f
        current = next_move
    return current, sum(current)

# تست:
items = [3, 7, 10, 2, 8, 4, 1,20,-10]
target = 20

solution, total = hill_climbing(items, target)
print("Best subset found:", solution)
print("Total sum:", total)
