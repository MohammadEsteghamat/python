import math
from random import randint
# تابع هدف
def f(x):
    return math.sin(x[0]) * math.cos(x[1]) + 0.1 * (x[0]**2 + x[1]**2)

# گرادیان‌ها
def grad_f(x):
    g = list()
    df_dx = math.cos(x[0]) * math.cos(x[1]) + 0.2 * x[0]
    df_dy = -math.sin(x[0]) * math.sin(x[1]) + 0.2 * x[1]
    g.append(df_dx)
    g.append(df_dy)
    return g

# --- 1. Gradient Descent ---
def gradient_descent(dim=2, lr=0.05, steps=100):
    x = [randint(0, 10) for _ in range(dim)]  # نقطه شروع
    for i in range(steps):
        grad = grad_f(x)
        x = [xi - lr * gi for xi, gi in zip(x, grad)]
        
    return x

# --- 2. Momentum ---
def momentum(dim=2, lr=0.05, steps=100, beta=0.9):
    x = [randint(0, 10) for _ in range(dim)]
    v = [0.0 for _ in range(dim)]
    for i in range(steps):
        grad = grad_f(x)
        v = [beta * vi + (1 - beta) * gi for vi, gi in zip(v, grad)]
        x = [xi - lr * vi for xi, vi in zip(x, v)]
        
    return x

# --- 3. Adam ---
def adam(dim=2, lr=0.05, steps=100, beta1=0.9, beta2=0.999, epsilon=1e-8):
    x = [randint(0, 10) for _ in range(dim)]
    m = [0.0 for _ in range(dim)]
    v = [0.0 for _ in range(dim)]
    for t in range(1, steps + 1):
        grad = grad_f(x)
        m = [beta1 * mi + (1 - beta1) * gi for mi, gi in zip(m, grad)]
        v = [beta2 * vi + (1 - beta2) * (gi ** 2) for vi, gi in zip(v, grad)]
        m_hat = [mi / (1 - beta1 ** t) for mi in m]
        v_hat = [vi / (1 - beta2 ** t) for vi in v]
        x = [xi - lr * mi / (math.sqrt(vi) + epsilon) for xi, mi, vi in zip(x, m_hat, v_hat)]
        
    return x


print("\n--- Gradient Descent ---")
x = gradient_descent(steps=1200)
print(f"\n[GD] : x = {x}, f = {f(x):.6f}")

print("\n--- Momentum ---")
x = momentum(steps=1200)
print(f"\n[Momentum] : x = {x}, f = {f(x):.6f}")

print("\n--- Adam ---")
x = adam(steps=1200)
print(f"\n[Adam] : x = {x}, f = {f(x):.6f}")
