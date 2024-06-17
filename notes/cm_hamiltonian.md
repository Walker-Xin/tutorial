# Classical Mechanics - Hamiltonian Formalism

The Lagrange equations presuppose that the mechanical state of a system is described by a set of generalized coordinates $q_{i}$ and their time derivatives $\dot{q}_{i}$. The Hamiltonian formalism, on the other hand, is a description based on the generalized coordinates and their corresponding momenta.

The total differential of a time-independent Lagrangian $L(q, \dot{q}, t)$ is given by:

$$
\mathrm{d}L = \sum_{i} \left( \frac{\partial L}{\partial q_{i}} \mathrm{d}q_{i} + \frac{\partial L}{\partial \dot{q}_{i}} \mathrm{d}\dot{q}_{i} \right)
$$

Note that we define the generalized momentum $p_{i}$ as:

$$
p_{i} \equiv \frac{\partial L}{\partial \dot{q}_{i}}
$$

so that the total differential of the Lagrangian can be written as:

$$
\mathrm{d}L = \sum_{i} \left( \frac{\partial L}{\partial q_{i}} \mathrm{d}q_{i} + p_{i} \mathrm{d}\dot{q}_{i} \right)
$$

The second term can be rewritten using the chain rule:

$$
\sum_{i} p_{i} \mathrm{d}\dot{q}_{i} = \mathrm{d} \left( \sum_{i} p_{i} q_{i} \right) - \sum_{i} \dot{q}_{i} \mathrm{d}p_{i}
$$

Substituting this to the total differential of the Lagrangian and rearranging the terms, we get:

$$
\mathrm{d}\left( \sum_{i} p_{i} \dot{q}_{i} - L \right) = \sum_{i} \dot{q}_{i} \mathrm{d}p_{i} - \sum_{i} \frac{\partial L}{\partial q_{i}} \mathrm{d}q_{i}
$$

But $\partial L/\partial q_{i} = \mathrm{d}p_{i}/\mathrm{d}t$ and $\sum_{i} p_{i} \dot{q}_{i} - L$ is just the generalised energy. Hence, we arrive at the following result:

$$
\mathrm{d}H = \sum_{i} \left( \dot{q}_{i} \mathrm{d}p_{i} - \dot{p}_{i} \mathrm{d}q_{i} \right)
$$

where we use $H$, called the Hamiltonian, to denote the generalised energy expressed in terms of the generalized coordinates and momenta:

$$
H \equiv \sum_{i} p_{i} \dot{q}_{i} - L
$$

From the differential $\mathrm{d}H$, we can derive the Hamilton equations of motion:

$$
\dot{q}_{i} = \frac{\partial H}{\partial p_{i}} \qquad \dot{p}_{i} = -\frac{\partial H}{\partial q_{i}}
$$

These are a set of $2n$ first-order differential equations, where $n$ is the number of generalized coordinates. Compare this to the set of $n$ second-order differential equations given by the Lagrange equations. The Hamiltonian formalism reduces the order of the differential equations by half at the cost of doubling the number of equations.

## Conservative Fields

Consider the Lagrangian of a system in a conservative field with a potential energy $V(p)$:

$$
L(q, \dot{q}, t) = \frac{1}{2}m \dot{q}^{2} - V(q)
$$

The conjugate momenta are given by:

$$
p = \frac{\partial L}{\partial \dot{q}} = m \dot{q}
$$

The Hamiltonian is then given by:

$$
H = p \dot{q} - L = \frac{1}{2}m = \frac{1}{2}m p^{2} + V(q)
$$

which in this case is just the ordinary energy of the system.

The Hamilton equations of motion are:

$$
\dot{q} = \frac{\partial H}{\partial p} = \frac{p}{m} \qquad \dot{p} = -\frac{\partial H}{\partial q} = -\frac{\partial V}{\partial q}
$$

## Rotating Frames

The Lagrangian of a particle in a rotating frame is given by:

$$
L = \frac{1}{2}m \dot{r}^{2} + m \dot{r} \cdot (\omega \times r) + \frac{1}{2}m (\omega \times r)^{2} - V(r)
$$

so that the conjugate momenta are:

$$
p = \frac{\partial L}{\partial \dot{r}} = m (\dot{r} + \omega \times r)
$$

Note that in this case, the generalised momenta are not simply the mass times the velocity.

The Hamiltonian is then given by:

$$
\begin{split}
H &= p \dot{r} - L \\
&= \frac{1}{2m} p^{2} + V(r) - \omega \cdot (r \times p)
\end{split}
$$

If we further expand $p^{2}$:

$$
\begin{split}
H &= \frac{m}{2} (\dot{r} + \omega \times r)^{2} + V(r) - p \cdot (\omega \times r) \\
&= \frac{m}{2} \dot{r}^{2} + \frac{m}{2} (\omega \times r)^{2} + m \dot{r} \cdot (\omega \times r) + V(r) - m \dot{r} \cdot (\omega \times r) - m (\omega \times r)^{2} \\
&= \frac{1}{2}m \dot{r}^{2} + V(r) - \frac{1}{2}m (\omega \times r)^{2}
\end{split}
$$

which is the ordinary energy of the system plus a contribution from the centrifugal force in the effective potential.
