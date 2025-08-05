# Gradient Optimization Algorithms in Python

This project demonstrates the implementation of **three popular gradient-based optimization algorithms** to minimize a given objective function:

- Gradient Descent
- Momentum
- Adam

---

## 🧠 Objective Function

The function we aim to minimize is:

\[
f(x, y) = \sin(x) \cdot \cos(y) + 0.1 \cdot (x^2 + y^2)
\]

This function combines trigonometric and quadratic terms, providing a non-convex landscape suitable for testing optimization methods.

---

## 📐 Gradient (Partial Derivatives)

The gradient of the function \( f(x, y) \) is calculated as:

- \( \frac{\partial f}{\partial x} = \cos(x) \cdot \cos(y) + 0.2x \)
- \( \frac{\partial f}{\partial y} = -\sin(x) \cdot \sin(y) + 0.2y \)

These are used in all optimization methods to update the position in the search space.

---

## 🚀 Optimization Algorithms

### 1. Gradient Descent (GD)
A basic first-order optimization method.

**Update rule:**
\[
x = x - \eta \cdot \nabla f(x)
\]

Where:
- \( \eta \) is the learning rate
- \( \nabla f(x) \) is the gradient vector

### 2. Momentum
Improves convergence by adding a velocity term to accelerate updates in consistent directions.

**Update rules:**
- \( v_t = \beta \cdot v_{t-1} + (1 - \beta) \cdot \nabla f(x) \)
- \( x = x - \eta \cdot v_t \)

Where:
- \( \beta \) is the momentum coefficient

### 3. Adam (Adaptive Moment Estimation)
Combines momentum with adaptive learning rates.

**Update rules:**
- \( m_t = \beta_1 \cdot m_{t-1} + (1 - \beta_1) \cdot \nabla f(x) \)
- \( v_t = \beta_2 \cdot v_{t-1} + (1 - \beta_2) \cdot (\nabla f(x))^2 \)
- Bias correction:
    - \( \hat{m}_t = \frac{m_t}{1 - \beta_1^t} \)
    - \( \hat{v}_t = \frac{v_t}{1 - \beta_2^t} \)
- Parameter update:
    - \( x = x - \eta \cdot \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon} \)

---
