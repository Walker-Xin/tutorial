# Classical Mechanics Foundation

## Calculus of Variations

Consider a function $L(f, \dot{f}, t)$, where $f$ is a function of $t$ and $\dot{f}$ is the ordinary time derivative. We wish to find a form of $L$ that extremise the integral

$$
S = \int_{t_{1}}^{t_{2}} L(f, \dot{f}, t) \, \mathrm{d}t
$$

where $S$ as a function of $f$ is formally called a functional.

We take the variation of $S$ with respect to $f$ and $\dot{f}$:

$$
\delta S = \int_{t_{1}}^{t_{2}} \left( \frac{\partial L}{\partial f} \delta f + \frac{\partial L}{\partial \dot{f}} \delta \dot{f} \right) \, \mathrm{d}t
$$

The second term can be integrated by parts:

$$
\int_{t_{1}}^{t_{2}} \frac{\partial L}{\partial \dot{f}} \delta \dot{f} \, \mathrm{d}t = \left[ \frac{\partial L}{\partial \dot{f}} \delta f \right]_{t_{1}}^{t_{2}} - \int_{t_{1}}^{t_{2}} \frac{\mathrm{d}}{\mathrm{d}t} \left( \frac{\partial L}{\partial \dot{f}} \right) \delta f \, \mathrm{d}t
$$

We impose constraints such that the boundary term vanish. This means that the variation of $f$ is zero at the boundaries so tha the starting and ending points are fixed. we thus arrive at the expression:

$$
\delta S = \int_{t_{1}}^{t_{2}} \left[ \frac{\partial L}{\partial f} - \frac{\mathrm{d}}{\mathrm{d}t} \left( \frac{\partial L}{\partial \dot{f}} \right) \right] \delta f \, \mathrm{d}t
$$

Since $\delta f$ is arbitrary, to achieve extremum we must have:

$$
\frac{\partial L}{\partial f} - \frac{\mathrm{d}}{\mathrm{d}t} \left( \frac{\partial L}{\partial \dot{f}} \right) = 0
$$

This is the Euler-Lagrange equation.

### Beltrami's Identity

Consider a function $L(f, \dot{f})$ that does not depend on $t$. We may write the total differential of $L$ as:

$$
\mathrm{d}L = \frac{\partial L}{\partial f} \mathrm{d}f + \frac{\partial L}{\partial \dot{f}} \mathrm{d}\dot{f}
$$

We may replace $\partial L/\partial f$ using the Euler-Lagrange equation and divide by $\mathrm{d}t$:

$$
\frac{\mathrm{d}L}{\mathrm{d}t} = \frac{\mathrm{d}}{\mathrm{d}t} \left( \frac{\partial L}{\partial \dot{f}} \right) \dot{f} + \frac{\partial L}{\partial \dot{f}} \frac{\mathrm{d}\dot{f}}{\mathrm{d}t} = \frac{\mathrm{d}}{\mathrm{d}t} \left( \frac{\partial L}{\partial \dot{f}} \dot{f} \right)
$$

This implies that the combination $\partial L/\partial \dot{f} \dot{f} - L$ does not depend on time:

$$
\frac{\mathrm{d}}{\mathrm{d}t} \left( \frac{\partial L}{\partial \dot{f}} \dot{f} - L \right) = 0
$$

This is called Beltrami's identity.

## Lagrangian Mechanics

The mechanical state of a system is described by a set of generalized coordinates $q_{i}$ and their time derivatives $\dot{q}_{i}$. The time evolution of the system is governed by a function of coordinates, velocities, and time called the Lagrangian, $L(q, \dot{q}, t)$. This function contains all the information about the system's dynamics and the evolution of the system is such that the action defined as:

$$
S = \int_{t_{1}}^{t_{2}} L(q, \dot{q}, t) \, \mathrm{d}t
$$

is extremised.

Therefore, the system obeys the Euler-Lagrange equation:

$$
\frac{\partial L}{\partial q_{i}} - \frac{\mathrm{d}}{\mathrm{d}t} \left( \frac{\partial L}{\partial \dot{q}_{i}} \right) = 0
$$

Typically, the Lagrangian is the difference between the kinetic and potential energies:

$$
L(q, \dot{q}, t) = T(\dot{q}) - V(q, t)
$$

We define the generalized momentum $p_{i}$ with respect to the generalized coordinate $q_{i}$ as:

$$
p_{i} \equiv \frac{\partial L}{\partial \dot{q}_{i}}
$$

A coordinate is called cyclic if the Lagrangian does not depend on it explicitly. For each cyclic coordinate, a conserved quantity can be found:

$$
\frac{\mathrm{d}}{\mathrm{d}t} \left( \frac{\partial L}{\partial \dot{q}_{i}} \right) = 0
$$

## Non-Inertial Frames

Consider some inertial frame $K_{0}$ in which a system has the Lagrangian $L_{0} = m \dot{r}^{2}/2 - V(r)$. Now, consider some (non-inertial) frame $K'$ that moves with a translational velocity $\mathbf{V}(t)$ with respect to $K_{0}$. The velocities in $K'$ are related to those in $K_{0}$ by:

$$
\dot{\mathbf{r}}_{0} = \dot{\mathbf{r}}' + \mathbf{V}
$$

The Lagrangian in $K'$ is then given by:

$$
L = \frac{1}{2}m \left( \dot{\mathbf{r}}' + \mathbf{V} \right)^{2} - V(\mathbf{r}') = \frac{1}{2}m \dot{\mathbf{r}}'^{2} + m \dot{\mathbf{r}}' \cdot \mathbf{V} + \frac{1}{2}m \mathbf{V}^{2} - V(\mathbf{r}')
$$

The third term is some known function of time so it can always be written as a total time derivative of some function, and hence can be ignored. The second term can be rewritten as:

$$
m \dot{\mathbf{r}}' \cdot \mathbf{V} = \frac{\mathrm{d}}{\mathrm{d}t} \left( m \mathbf{r}' \cdot \mathbf{V} \right) - m \mathbf{r}' \cdot \dot{\mathbf{V}}
$$

Omitting the time derivative again, we get:

$$
L' = \frac{1}{2}m \dot{\mathbf{r}}'^{2} - m \mathbf{A}(t) \cdot \dot{\mathbf{r}}' - V(\mathbf{r}')
$$

where $\mathbf{A}(t) = \dot{\mathbf{V}}$ is the acceleration of the frame $K'$ with respect to $K_{0}$.

Consider further a frame $K$ with its origin coinciding with $K'$ and rotating with an angular velocity $\omega(t)$. The velocity in $K$ is related to that in $K'$ by:

$$
\dot{\mathbf{r}}' = \dot{\mathbf{r}} + \omega \times \mathbf{r}
$$

The Lagrangian in $K$ is then given by:

$$
L = \frac{1}{2}m \dot{\mathbf{r}}^{2} + m \dot{\mathbf{r}} \cdot (\omega \times \mathbf{r}) + \frac{1}{2}m (\omega \times \mathbf{r})^{2} - m \mathbf{A} \cdot \dot{\mathbf{r}} - V(\mathbf{r})
$$

This is the general Lagrangian of a particle in a non-inertial frame with translational and rotational accelerations. Taking the Euler-Lagrange equations, we get the equations of motion of a particle in a non-inertial frame:

$$
m \ddot{\mathbf{r}} = -\frac{\partial U}{\partial \mathbf{r}} - m \mathbf{A} + m \mathbf{r} \times \dot{\omega} + 2m \dot{\mathbf{r}} \times \omega + m \omega \times (\omega \times \mathbf{r})
$$

The third to fifth terms are the Euler, Coriolis, and centrifugal forces, respectively.

## Constraints

Suppose that the system is subject to constraints, i.e. the generalized coordinates are not independent. We can express the constraints as integral equations:

$$
\int_{t_{1}}^{t_{2}} f_{i}(q, t) \, \mathrm{d}t = 0
$$

Instead of the original action, we now extremise a modified version:

$$
S' = \int_{t_{1}}^{t_{2}} L(q, \dot{q}, t) \, \mathrm{d}t + \sum_{i} \int_{t_{1}}^{t_{2}} \lambda_{i}(t) f_{i}(q, t) \, \mathrm{d}t
$$

where we introduce Lagrange multipliers $\lambda_{i}(t)$ to enforce the constraints.

This means that we have the modified Lagrangian:

$$
L' = L + \sum_{i} \lambda_{i} f_{i}
$$

and the modified Euler-Lagrange equations:

$$
\frac{\partial L'}{\partial q_{i}} - \frac{\mathrm{d}}{\mathrm{d}t} \left( \frac{\partial L'}{\partial \dot{q}_{i}} \right) = 0
$$

Physically, the Lagrange multipliers are generalised forces that enforce the constraints. They are physical forces up to some constant factors.
