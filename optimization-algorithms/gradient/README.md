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

## 🚀 Optimization Algorithms (How They Work)

### 1. Gradient Descent (GD)

**Gradient Descent** is a basic optimization method where we move in the opposite direction of the gradient to reach a local minimum.

**How it works:**

1. Choose a random initial point.
2. Compute the gradient at that point.
3. Update parameters by subtracting the gradient scaled by the learning rate \( \eta \).
4. Repeat for a number of steps.

**Update Rule:**

\[
x_{\text{new}} = x_{\text{old}} - \eta \cdot \nabla f(x)
\]

- ✅ Simple and intuitive
- ❌ Can be slow or stuck in local minima

---

### 2. Momentum

**Momentum** accelerates gradient descent by building up a velocity vector in directions of persistent reduction.

**How it works:**

1. Initialize velocity \( v \) to zero.
2. At each step:
   - Update \( v \) using past velocity and current gradient.
   - Update position using the new velocity.

**Update Rules:**

\[
v_t = \beta \cdot v_{t-1} + (1 - \beta) \cdot \nabla f(x)
\]
\[
x = x - \eta \cdot v_t
\]

- ✅ Faster convergence in ravines and narrow valleys

---

### 3. Adam (Adaptive Moment Estimation)

**Adam** combines ideas from both Momentum and RMSProp. It keeps track of both the first moment (mean) and second moment (variance) of the gradients.

**How it works:**

1. Initialize first and second moment estimates \( m \), \( v \) to zero.
2. Update them with moving averages.
3. Apply bias correction.
4. Update parameters using scaled gradients.

**Update Rules:**

\[
m_t = \beta_1 \cdot m_{t-1} + (1 - \beta_1) \cdot \nabla f(x)
\]
\[
v_t = \beta_2 \cdot v_{t-1} + (1 - \beta_2) \cdot (\nabla f(x))^2
\]
\[
\hat{m}_t = \frac{m_t}{1 - \beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1 - \beta_2^t}
\]
\[
x = x - \eta \cdot \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}
\]

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
