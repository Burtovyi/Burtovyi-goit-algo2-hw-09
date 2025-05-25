import random
import math


# Визначення функції Сфери
def sphere_function(x):
    return sum(xi ** 2 for xi in x)


# Допоміжна функція для генерації випадкової точки в межах bounds
def random_point(bounds):
    return [random.uniform(b[0], b[1]) for b in bounds]


# Допоміжна функція для створення сусіда
def neighbor(x, bounds, step_size=0.1):
    return [
        min(max(xi + random.uniform(-step_size, step_size), b[0]), b[1])
        for xi, b in zip(x, bounds)
    ]


# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    current = random_point(bounds)
    current_val = func(current)

    for _ in range(iterations):
        next_point = neighbor(current, bounds)
        next_val = func(next_point)

        if abs(current_val - next_val) < epsilon:
            break

        if next_val < current_val:
            current, current_val = next_point, next_val

    return current, current_val


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    best = random_point(bounds)
    best_val = func(best)

    for _ in range(iterations):
        candidate = random_point(bounds)
        candidate_val = func(candidate)

        if abs(best_val - candidate_val) < epsilon:
            break

        if candidate_val < best_val:
            best, best_val = candidate, candidate_val

    return best, best_val


# Simulated Annealing
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    current = random_point(bounds)
    current_val = func(current)
    best = current
    best_val = current_val

    for _ in range(iterations):
        temp *= cooling_rate
        if temp < epsilon:
            break

        next_point = neighbor(current, bounds)
        next_val = func(next_point)

        delta = next_val - current_val
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current, current_val = next_point, next_val

        if current_val < best_val:
            best, best_val = current, current_val

    return best, best_val


if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]  # 2-вимірна задача

    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
