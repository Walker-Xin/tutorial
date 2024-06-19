# Classical Mechanics - Conservation Laws and Symmetries

## Conservation Laws

There are certain combinations of coordinates and momenta that do no change during the time evolution of the system. These are called conserved quantities, out of which the most important are the energy, the linear momentum, and the angular momentum. Conservation laws are a consequence of the symmetries of the system studied.

### Homogeneity of Time

It is also reasonable to assume that time is homogeneous, i.e. the laws of physics are the same at all times. This means that the Lagrangian does not depend on time explicitly. In this case, the total differential of the Lagrangian does not depend on time:

$$
\mathrm{d}L = \sum_{i} \left( \frac{\partial L}{\partial q_{i}} \mathrm{d}q_{i} + \frac{\partial L}{\partial \dot{q}_{i}} \mathrm{d}\dot{q}_{i} \right)
$$

But we may replace $\partial L/\partial q_{i}$ using the Euler-Lagrange equation and divide by $\mathrm{d}t$:

$$
\frac{\mathrm{d}L}{\mathrm{d}t} = \sum_{i} \left[ \frac{\mathrm{d}}{\mathrm{d}t} \left( \frac{\partial L}{\partial \dot{q}_{i}} \right) \dot{q}_{i} + \frac{\partial L}{\partial \dot{q}_{i}} \ddot{q}_{i} \right] = \sum_{i} \frac{\mathrm{d}}{\mathrm{d}t} \left( \frac{\partial L}{\partial \dot{q}_{i}} \dot{q}_{i} \right)
$$

Thus, the time derivative of the combination $\sum_{i} p_{i} \dot{q}_{i} - L$ is zero, which leads to a conserved quantity called generalised the energy:

$$
E \equiv \sum_{i} \frac{\partial L}{\partial \dot{q}_{i}} \dot{q}_{i} - L = \sum_{i} p_{i} \dot{q}_{i} - L
$$

Note that this is just the Beltrami's identity for the case of a Lagrangian that does not depend on time.

### Homogeneity of Space

It is reasonable to assume that space is homogeneous, i.e. the laws of physics are the same everywhere. This means that the Lagrangian should be invariant under an infinitesimal displacement $\epsilon$. Consider the effect of this displacement on the Lagrangian:

$$
\delta L = \sum_{i} \frac{\partial L}{\partial q_{i}} \delta q_{i} = \epsilon \cdot \left( \sum_{i} \frac{\partial L}{\partial q_{i}} \right)
$$

Demanding $\delta L = 0$ leads to $\sum_{i} \partial L/\partial q_{i} = 0$. Using Lagrange's equation, we have:

$$
0 = \sum_{i} \frac{\partial L}{\partial q_{i}} = \sum_{i} \frac{\mathrm{d}}{\mathrm{d}t} \left( \frac{\partial L}{\partial \dot{q}_{i}} \right)
$$

That is, the total momentum is conserved:

$$
\sum_{i} p_{i} = \sum_{i} \frac{\partial L}{\partial \dot{q}_{i}} = \text{constant}
$$

### Isotropy of Space

It is also reasonable to assume that space is isotropic, i.e. the laws of physics are the same in all directions. This means that the Lagrangian should be invariant (up to a total derivative) under rotations. In this case, the angular momentum is conserved:

## Noether's Theorem

Recall that the dynamics of a system is unchanged if the Lagrangian is changed by a total time derivative. That is, the action is invariant under the transformation $L \rightarrow L + \mathrm{d}f/\mathrm{d}t$. Consider an infinitesimal transformation of the coordinates of the form:

$$
\mathbf{q} \to \mathbf{q} + \frac{\mathrm{d}\mathbf{q}}{\mathrm{d}\lambda}(\mathbf{q}, \dot{\mathbf{q}}, t) \delta \lambda
$$

The resulting change in the Lagrangian is:

$$
\begin{split}
\delta L &= \sum_{i} \left( \frac{\partial L}{\partial q_{i}} \delta q_{i} + \frac{\partial L}{\partial \dot{q}_{i}} \delta \dot{q}_{i} \right) \\
&= \sum_{i} \left( \frac{\partial L}{\partial q_{i}} \frac{\mathrm{d}q_{i}}{\mathrm{d}\lambda} \delta \lambda + \frac{\partial L}{\partial \dot{q}_{i}} \frac{\mathrm{d}\dot{q}_{i}}{\mathrm{d}\lambda} \delta \lambda \right) \\
&= \delta \lambda \sum_{i} \left[ \frac{\mathrm{d}}{\mathrm{d}t} \left( \frac{\partial L}{\partial \dot{q}_{i}} \right) \frac{\mathrm{d}q_{i}}{\mathrm{d}\lambda} + \frac{\partial L}{\partial \dot{q}_{i}} \frac{\mathrm{d}\dot{q_{i}}}{\mathrm{d}\lambda} \right] \\
&= \delta \lambda \frac{\mathrm{d}}{\mathrm{d}t} \left( \sum_{i} \frac{\partial L}{\partial \dot{q}_{i}} \frac{\mathrm{d}q_{i}}{\mathrm{d}\lambda} \right)
\end{split}
$$

We require this to be equal to some total time derivative $(\mathrm{d}G/\mathrm{d}t) \delta \lambda$, leading to the conservation law:

$$
\frac{\mathrm{d}}{\mathrm{d}t} \left( \sum_{i} \frac{\partial L}{\partial \dot{q}_{i}} \frac{\mathrm{d}q_{i}}{\mathrm{d}\lambda} - G \right) = 0
$$
