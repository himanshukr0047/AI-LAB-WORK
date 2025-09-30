import random

# Step 1: Function jiska maximum value hum find karna chahte hain
def f(x):
    return -(x - 3) ** 2 + 9   # maximum value at x = 3

# Step 2: Hill Climbing function
def hill_climbing():
    # random starting point (between -10 and 10)
    current_x = random.uniform(-10, 10)
    current_value = f(current_x)

    print("Starting at x =", round(current_x, 2), "f(x) =", round(current_value, 2))

    # run for fixed number of steps
    for i in range(100):
        # ek chhota step left ya right
        step_size = 0.1
        next_x = current_x + random.choice([-step_size, step_size])
        next_value = f(next_x)

        # agar next solution better hai to usko le lo
        if next_value > current_value:
            current_x = next_x
            current_value = next_value
            print("Moved to x =", round(current_x, 2), "f(x) =", round(current_value, 2))

    return current_x, current_value

# Step 3: Run algorithm
best_x, best_value = hill_climbing()
print("\nBest solution found: x =", round(best_x, 2), "f(x) =", round(best_value, 2))
