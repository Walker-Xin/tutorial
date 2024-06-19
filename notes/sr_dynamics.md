# Special Relativity - Dynamics

## Motion in a Straight Line

Consider a particle subject to a pure force. The rest mass is constant so $\mathrm{d}m_{0}/\mathrm{d}t = \mathrm{d}m_{0}/\mathrm{d}\tau = 0$. The 3-force becomes:

$$
\mathbf{f} = \frac{\mathrm{d}}{\mathrm{d}t} (\gamma_{u} m_{0} \mathbf{u}) = \gamma_{u} m_{0} \mathbf{a} + m_{0} \frac{\mathrm{d}\gamma_{u}}{\mathrm{d}t} \mathbf{u}
$$

with the condition:

$$
\frac{\mathrm{d}E}{\mathrm{d}t} - \mathbf{f} \cdot \mathbf{u} = \frac{\mathrm{d}K}{\mathrm{d}t} - \mathbf{f} \cdot \mathbf{u} = 0
$$

where $K \equiv E - m_{0} c^{2}$ is defined as the kinetic energy of the particle.

Suppose that a particle accelerates in a straight line under the effect of a pure force. Let $S_{A}$ be an instantaneous rest frame of reference at some event $A$ along the world line of the particle. In $S_{A}$ at event $A$, the particle has a zero velocity and some proper acceleration $a_{0}(\tau)$ as a function of the proper time. In an infinitesimal time interval $\mathrm{d}\tau$, the velocity increases to $\mathrm{d}v = a_{0} \mathrm{d}\tau$ in the instantaneous rest frame. Hence the proper rapidity $\rho_{0}$ increases from zero to $\tanh^{-1}(a_{0} \mathrm{d}\tau/c) \approx a_{0} \mathrm{d}\tau/c$. Hence:

$$
\frac{\mathrm{d}\rho_{0}}{\mathrm{d}\tau} = \frac{a_{0}}{c}
$$

Now recall that for collinear motion, rapidities add. Hence in any frame $S$ moving along the line of acceleration, the observed rapidity satisfies $\rho = \rho_{0} + \rho_{A}$, where $\rho_{A}$ is the rapidity of the instantaneous rest frame $S_{A}$. However, as $S_{A}$ is an inertial frame, its rapidity has a zero time derivative. Hence, in frame $S$:

$$
\frac{\mathrm{d}\rho}{\mathrm{d}t} = \frac{\mathrm{d}\rho_{0}}{\mathrm{d}\tau} = \frac{a_{0}(\tau)}{c}
$$

Given the form of $a_{0}(\tau)$, the differential equation can be integrated to yield $\rho$, and consequently the speed of the particle observed in $S$, as a function of the proper time $\tau$.

### Relativistic Rocket

Consider the elementary case where $a_{0}(\tau) = a_{0}$ is a constant. This constant proper acceleration is sometimes referred to as the 'relativistic rocket'. Solving the differential equation:

$$
\rho(\tau) = \frac{a_{0}}{c}\tau + \text{constant}
$$

If $S$ is chosen such that the rocket started at rest, the constant equates to zero and the velocity of the rocket as observed in $S$ becomes:

$$
v(\tau) = c \tanh{\rho} = c \tanh{\left( \frac{a_{0}}{c} \tau \right)}
$$

To express the velocity as a function of time in frame $S$, note that:

$$
\begin{split}
\frac{\mathrm{d}t}{\mathrm{d}\tau} &= \gamma_{v} = \cosh{\rho} \\
t &= \frac{c}{a_{0}} \sinh{\rho} = \frac{c}{a_{0}} \beta_{v} \gamma_{v}
\end{split}
$$

Solving the equation for $v$ yields:

$$
v(t) = \frac{a_{0}t}{\sqrt{1 + a_{0}^{2} t^{2}/c^{2}}}
$$

Note that the velocity observed in $S$ approaches light speed but can never truly reach it, implying that the acceleration observed gradually approaches to zero.

The distance travelled by the rocket observed in $S$ is given by:

$$
\frac{\mathrm{d}x}{\mathrm{d}\tau} = \frac{\mathrm{d}x}{\mathrm{d}t} \frac{\mathrm{d}t}{\mathrm{d}\tau} = (c \tanh{\rho}) \cosh{\rho} = c \sinh{\left( \frac{a_{0}}{c} \tau \right)}
$$

Integration yields $(x - b) = (c^{2}/a_{0}) \cosh{\rho}$ or:

$$
(x - b)^{2} - c^{2} t^{2} = \left( \frac{c^{2}}{a_{0}} \right)^{2}
$$

This represents a hyperbola in spacetime.
