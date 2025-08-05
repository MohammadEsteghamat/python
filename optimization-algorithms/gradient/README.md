# Gradient Optimization Algorithms in Python

This project demonstrates the implementation of **three popular gradient-based optimization algorithms** to minimize a given objective function:

- Gradient Descent
- Momentum
- Adam

---

## 🧠 Objective Function

The function we aim to minimize is:

```
f(x, y) = sin(x) * cos(y) + 0.1 * (x^2 + y^2)
```

This function combines trigonometric and quadratic terms, providing a non-convex landscape suitable for testing optimization methods.

---

## 📐 Gradient (Partial Derivatives)

The gradient of the function f(x, y) is calculated as:

- df/dx = cos(x) * cos(y) + 0.2 * x
- df/dy = -sin(x) * sin(y) + 0.2 * y

These are used in all optimization methods to update the position in the search space.

---

## 🚀 Optimization Algorithms (How They Work)

### 1. Gradient Descent (GD)

**Gradient Descent** is a basic optimization method where we move in the opposite direction of the gradient to reach a local minimum.

**How it works:**

1. Choose a random initial point.
2. Compute the gradient at that point.
3. Update parameters by subtracting the gradient scaled by the learning rate (eta).
4. Repeat for a number of steps.

**Update Rule:**

```
x_new = x_old - eta * grad_f(x)
```

- ✅ Simple and intuitive
- ❌ Can be slow or stuck in local minima

---

### 2. Momentum

**Momentum** accelerates gradient descent by building up a velocity vector in directions of persistent reduction.

**How it works:**

1. Initialize velocity v to zero.
2. At each step:
   - Update v using past velocity and current gradient.
   - Update position using the new velocity.

**Update Rules:**

```
v_t = beta * v_{t-1} + (1 - beta) * grad_f(x)
x = x - eta * v_t
```

- ✅ Faster convergence in ravines and narrow valleys

---

### 3. Adam (Adaptive Moment Estimation)

**Adam** combines ideas from both Momentum and RMSProp. It keeps track of both the first moment (mean) and second moment (variance) of the gradients.

**How it works:**

1. Initialize first and second moment estimates m, v to zero.
2. Update them with moving averages.
3. Apply bias correction.
4. Update parameters using scaled gradients.

**Update Rules:**

```
m_t = beta1 * m_{t-1} + (1 - beta1) * grad_f(x)
v_t = beta2 * v_{t-1} + (1 - beta2) * (grad_f(x))^2
m_hat = m_t / (1 - beta1^t)
v_hat = v_t / (1 - beta2^t)
x = x - eta * m_hat / (sqrt(v_hat) + epsilon)
```

- ✅ Adaptive learning rate
- ✅ Robust in practice
- ✅ Commonly used in training deep neural networks

---

## 🏁 Running the Program

Simply run the Python script:

```bash
python optimization.py
```

Each algorithm will print the optimized point and the corresponding function value.

---

## 📊 Example Output

```
--- Gradient Descent ---
[GD] : x = [1.22738, 1.45092], f = 0.218967

--- Momentum ---
[Momentum] : x = [1.22765, 1.45145], f = 0.218967

--- Adam ---
[Adam] : x = [1.22723, 1.45057], f = 0.218967
```

(Note: Exact values vary due to random initialization.)

---

## ⚙️ Dependencies

Only standard Python libraries are used:

- `math`
- `random`

---

## 📚 License

This project is licensed under the MIT License.
