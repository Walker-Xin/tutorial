# Special Relativity - Foundation

- [Special Relativity - Foundation](#special-relativity---foundation)
    - [Einstein's Postulates and Lorentz Transformation](#einsteins-postulates-and-lorentz-transformation)
        - [Lorentz Invariant](#lorentz-invariant)
    - [4-Vectors](#4-vectors)
        - [Rapidity](#rapidity)
        - [Proper Time](#proper-time)
        - [Velocity and Acceleration](#velocity-and-acceleration)
    - [Dynamics](#dynamics)
    - [Doppler Shift](#doppler-shift)

## Einstein's Postulates and Lorentz Transformation

The theory of Special Relativity is based on its two fundamental postulates:

1. 'Principle of Relativity': The motions bodies included in a given space are the same among themselves, whether that space is at rest or moving uniformly in a straight line.
2. 'Light Speed Postulate': There is a maximum speed for signals.

Based on these postulates, the Lorentz transformation can be derived to replace the Galilean transformation for movements from one coordinate system to another.

Let $S$ and $S'$ be reference frames allowing coordinate systems $(t, x, y, z)$ and $(t', x', y', z')$ to be defined. Let their x-axis be aligned, so that $S'$ has a velocity $v$ in the $x$ direction in reference frame $S$. Also let the origins of the two systems coincide at $t = t' = 0$. This is called the 'standard configuration' of a pair of reference frames. The Lorentz transformation states that for such a standard configuration, if an event has coordinates $(t, x, y, z)$ in $S$, then its coordinates in $S'$ is given by:

$$
\begin{split}
t' &= \gamma \left( t - \frac{vx}{c^{2}} \right) \\
x' &= \gamma (-vt + x) \\
y' &= y \\
z' &= z
\end{split}
$$

where $\gamma \equiv (1 - v^{2}/c^{2})^{-1/2}$ is the Lorentz factor.

The inverse of the transformation is obtained by switching the sign associated with $v$:

$$
\begin{split}
t &= \gamma \left( t' + \frac{vx'}{c^{2}} \right) \\
x &= \gamma (vt + x') \\
y &= y' \\
z &= z'
\end{split}
$$

The Lorentz transformation can be recast into a matrix form. Define the position 4-vector as a column vector $X$ of four components:

$$
X \equiv \begin{pmatrix}
            ct \\
            x \\
            y \\
            z \\
         \end{pmatrix}
$$

components of which are denoted from $X^{0}$ to $X^{3}$

The Lorentz transformation from $X$ in frame $S$ to $X'$ in frame $S'$ can be written as:

$$
X' = \Lambda X
$$

where:

$$
\Lambda \equiv \begin{pmatrix}
                    \gamma         & -\gamma \beta & 0 & 0\\
                    -\gamma \beta  & \gamma        & 0 & 0\\
                    0              & 0             & 1 & 0\\
                    0              & 0             & 0 & 1\\
               \end{pmatrix}
$$

where $\beta \equiv v/c$ and $v$ is the speed of $S'$ in $S$.

The inverse Lorentz transformation is apparently $X = \Lambda^{-1} X'$, and $\Lambda^{-1}$ is obtained by changing the sign of $\beta$:

$$
\Lambda^{-1} \equiv \begin{pmatrix}
                        \gamma        & \gamma \beta & 0 & 0\\
                        \gamma \beta  & \gamma       & 0 & 0\\
                        0             & 0            & 1 & 0\\
                        0             & 0            & 0 & 1\\
                    \end{pmatrix}
$$

### Lorentz Invariant

Like an ordinary 3-dimensional vector, a 4-vector has a size that is not affected by Lorentz transformations. Consider the following quantity, which is called the spacetime interval:

$$
s^{2} \equiv -(X^{0})^{2} + (X^{1})^{2} + (X^{2})^{2} + (X^{3})^{2}
$$

This is a 'Lorentz invariant'. That is:

$$
-c^{2}t^{2} + x^{2} + y^{2} + z^{2} = -c^{2}t'^{2} + x'^{2} + y'^{2} + z'^{2}
$$

We may view Lorentz transformations as rotations of the same vector to different coordinates. If $s^{2} > 0$, it is called a space-like interval, where the time between two events is too short for any physical influence to move between them; if $s^{2} < 0$, it is called a time-like interval, where the time between two events is sufficient for a particle to move from one event to another; if $s^{2} = 0$, it is called a null interval where only a light pulse could move from one event to another.

In matrix notation, the Lorentz invariant can be written as:

$$
s^{2} = X^{\intercal} g X
$$

where:

$$
g \equiv \begin{pmatrix}
            -1 & 0 & 0 & 0  \\
            0  & 1 & 0 & 0  \\
            0  & 0 & 1 & 0  \\
            0  & 0 & 0 & 1
         \end{pmatrix}
$$

$g$ is called the 'metric' or 'metric tensor'.

## 4-Vectors

A 4-vector is any set of four scalar quantities that transform in the same way as $(ct, x, y, z)$, i.e., the 4-displacement under a change of reference frame.

If $A$ is a 4-vector, and $A' = \Lambda A$, then for there to be a Lorentz invariant associated with the matrix $g$, have:

$$
\begin{split}
A'^{\intercal} g A' &= (\Lambda A)^{\intercal} g (\Lambda A) \\
                    &= A^{\intercal} (\Lambda^{\intercal} g \Lambda) A
\end{split}
$$

Therefore, $A^{\intercal} g A$ is a Lorentz invariant as long as:

$$
\Lambda^{\intercal} g \Lambda = g
$$

In fact, the above argument still holds true if the quantity $A^{\intercal} g B$ is considered. Hence, the scalar product of two 4-vectors can be defined as:

$$
A \cdot B \equiv A^{\intercal} g B
$$

This scalar product is a Lorentz invariant and is agreed among all reference frames. For the particular case of $A \cdot A$, the original definition of a Lorentz invariant is obtained.

### Rapidity

Define a parameter $\rho$ by:

$$
\tanh{\rho} = \frac{v}{c} = \beta
$$

such that:

$$
\cosh{\rho} = \gamma, \; \sinh{\rho} = \beta \gamma, \; \exp{\rho} = \left( \frac{1+\beta}{1-\beta} \right)^{1/2}
$$

Then the Lorentz transformation matrix becomes:

$$
\Lambda \equiv \begin{pmatrix}
                    \cosh{\rho}    & -\sinh{\rho}  & 0 & 0\\
                    -\sinh{\rho}   & \cosh{\rho}   & 0 & 0\\
                    0              & 0             & 1 & 0\\
                    0              & 0             & 0 & 1\\
               \end{pmatrix}
$$

$\rho$ is called the rapidity, which is useful for certain consecutive changes of reference frames. Consider, for example, three reference frames $S$, $S'$, $S''$ all moving in the same line, with $\rho_{u}$ being the rapidity of frame $S'$ with respect to $S$ and $\rho_{v}$ being that of frame $S''$ with respect to $S'$. Then the transformation of any 4-vector $V$ from $S$ to its counterpart $V''$ in $S''$ is given by the matrix $\Lambda = \Lambda_{v} \Lambda_{u}$, since:

$$
V'' = \Lambda_{v} V' = \Lambda_{v} \Lambda_{u} V
$$

Expanding the expression for $\Lambda$, have:

$$
\Lambda = \begin{pmatrix}
                    \cosh{(\rho_{v}+\rho_{u})}  & -\sinh{(\rho_{v}+\rho_{u})} & 0 & 0\\
                    -\sinh{(\rho_{v}+\rho_{u})} & \cosh{(\rho_{v}+\rho_{u})}  & 0 & 0\\
                    0                           & 0                           & 1 & 0\\
                    0                           & 0                           & 0 & 1\\
          \end{pmatrix}
$$

Thus it is concluded that for relative motion all in the same direction, the rapidities add together.

### Proper Time

In Newtonian mechanics, time is universal among all reference frames. In special relativity however, universal time is no longer true and the proper time is used. The proper time is the integral of all the infinitesimal elements of proper time experienced by a particle along its worldline.

Let $X$ be the displacement 4-vector describing a given worldline. In a reference frame $S$, its components are $ct$, $x(t)$, $y(t)$ and $z(t)$ for the trajectory relative to this frame. Two events on the worldline, separated by an infinitesimal amount of time $\mathrm{d}t$, are $(ct, x, y, z)$ and $(c(t+\mathrm{d}t), x+\mathrm{d}x, y+\mathrm{d}y, z+\mathrm{d}z)$. The proper time $\mathrm{d}\tau$ between the two events is given by:

$$
\begin{split}
\mathrm{d}\tau &= \frac{1}{c} \sqrt{c^{2} \mathrm{d}t^{2} - \mathrm{d}x^{2} - \mathrm{d}y^{2} - \mathrm{d}z^{2}} \\
               &= \mathrm{d}t \sqrt{1 - \frac{u^{2}}{c^{2}}}
\end{split}
$$

where $\mathbf{u} = (\frac{\mathrm{d}x}{\mathrm{d}t}, \frac{\mathrm{d}y}{\mathrm{d}t}, \frac{\mathrm{d}z}{\mathrm{d}t})$ is the velocity of the particle in $S$.

Then an important conclusion is drawn:

$$
\frac{\mathrm{d}t}{\mathrm{d}\tau} = \gamma
$$

The proper time is infinitesimal amount of time displacement undergone by a particle in its own rest frame where there is no spatial motion. It follows that $\mathrm{d}\tau$ is a space-time interval that is invariant under Lorentz transformation. Thus, the proper time is agreed among all reference frames.

Further note that now the Lorentz invariant of 4-displacement can be written in terms of the proper time:

$$
X \cdot X = -c^{2} \tau^{2}
$$

### Velocity and Acceleration

Consider a particle moving at a velocity $\mathbf{u}$ with respect to a frame $S$. The 4-velocity $U$ is defined as:

$$
U \equiv \frac{\mathrm{d}X}{\mathrm{d}\tau} = \frac{\mathrm{d}X}{\mathrm{d}t} \frac{\mathrm{d}t}{\mathrm{d}\tau} = \gamma_{u}(c, \mathbf{u})
$$

Note that the 4-velocity has a constant Lorentz invariant, as:

$$
U \cdot U = -\gamma_{u}^{2} c^{2} + \gamma_{u}^{2} u^{2} = -c^{2}
$$

Consider a particle of velocity $\mathbf{u}$ observed in frame $S$ and a frame $S'$ moving at velocity $\mathbf{v}$ relative to $S$. Performing the Lorentz transformation on $U$ yields the velocity transformation equations:

$$
u_{\parallel}' = \frac{1}{1 - (\mathbf{v} \cdot \mathbf{u})/c^{2}} (u_{\parallel} - v), \; \mathbf{u}_{\bot}' = \frac{1}{1 - (\mathbf{v} \cdot \mathbf{u})/c^{2}} \mathbf{u}_{\bot}
$$

The 4-acceleration $A$ is defined as:

$$
A \equiv \frac{\mathrm{d}U}{\mathrm{d}\tau} = \frac{\mathrm{d}U}{\mathrm{d}t} \frac{\mathrm{d}t}{\mathrm{d}\tau} = \gamma_{u}^{2} \left( \frac{\mathbf{u} \cdot \mathbf{a}}{c} \gamma_{u}^{2}, \frac{\mathbf{u} \cdot \mathbf{a}}{c^{2}} \gamma_{u}^{2} \mathbf{u} + \mathbf{a} \right)
$$

The Lorentz invariant of the 4-acceleration can be obtained by noting that in the (instantaneously) rest frame of the particle, the 4-acceleration becomes:

$$
A = (0, \mathbf{a}_{0})
$$

where $\mathbf{a}_{0}$ is the proper acceleration observed in the rest frame.

Then the Lorentz invariant of 4-acceleration is:

$$
A \cdot A = a_{0}^{2}
$$

Note further that in the rest frame, the scalar product $U \cdot A$ yields zero. As the scalar product is an invariant, this means that the 4-acceleration is always orthogonal to the 4-velocity, whose constant length depends on this condition.

Explicitly calculating the Lorentz invariant $A \cdot A$, and equating it with $a_{0}^{2}$, yields the equation:

$$
a_{0}^{2} = \gamma_{u}^{4} a^{2} + \gamma_{u}^{6} \frac{(\mathbf{u} \cdot \mathbf{a})^{2}}{c^{2}}
$$

In this equation, $\mathbf{a}_{0}$ is the proper acceleration while $\mathbf{a}$ is the acceleration relative to the frame chosen, where the particle has a velocity $\mathbf{u}$.

## Dynamics

The 4-momentum $P$ of a particle is defined similarly as its classical counterpart:

$$
P \equiv m_{0} U = \gamma_{u}(m_{0} c, m_{0} \mathbf{u})
$$

where $m_{0}$, which is a Lorentz invariant, is the rest mass of the particle moving at velocity $\mathbf{u}$ in a given reference frame.

The quantity $E \equiv \gamma_{u} m_{0} c^{2}$ is found to be the energy of the particle, while the vector $\mathbf{p} \equiv \gamma_{u} m_{0} \mathbf{u}$ is defined as the 3-momentum of the particle. Note how energy and momentum are incorporated into a single 4-vector.

The Lorentz invariant associated with the 4-momentum, evaluated at a general frame $S$ and the rest frame, is:

$$
P \cdot P = -\frac{E^{2}}{c^{2}} + p^{2} = -m_{0}^{2} c^{2}
$$

This leads to the relationship $E^{2} - p^{2} c^{2} = m_{0}^{2} c^{4}$, which is true in any frame of reference.

The 4-force is defined as the proper time derivative of the 4-momentum:

$$
F \equiv \frac{\mathrm{d}P}{\mathrm{d}\tau} = \gamma_{u} \left( \frac{1}{c} \frac{\mathrm{d}E}{\mathrm{d}t}, \mathbf{f} \right)
$$

where $\mathbf{f} \equiv \mathrm{d}\mathbf{p}/\mathrm{d}t$ is defined as the 3-force in a given reference frame.

Suppose a particle with 4-velocity $U$ is subject to a 4-force $F$. Consider the scalar product:

$$
U \cdot F = \gamma_{u}^{2} \left( -\frac{\mathrm{d}E}{\mathrm{d}t} + \mathbf{f} \cdot \mathbf{u} \right)
$$

As this scalar product is Lorentz invariant, the rest frame can be chosen such that $\mathbf{u} = \mathbf{0}$:

$$
U \cdot F = -c^{2} \frac{\mathrm{d}m_{0}}{\mathrm{d}\tau}
$$

since in the rest frame $\mathrm{d}t = \mathrm{d}\tau$.

This means that the rest mass of a particle is constant only when $U \cdot F = 0$. A force that does not change the rest mass is called a pure force, such that $\mathrm{d}E/\mathrm{d}t = \mathbf{f} \cdot \mathbf{u}$, a relationship between force and rate of work done in classical mechanics.

Imposing a Lorentz transformation on a 4-force, the 3-force transformation equations result:

$$
\mathbf{f}_{\parallel}' = \frac{1}{1 - (\mathbf{v} \cdot \mathbf{u})/c^{2}} \left( \mathbf{f}_{\parallel} - \frac{\mathbf{v}}{c^{2}} \frac{\mathrm{d}E}{\mathrm{d}t} \right), \; \mathbf{f}_{\bot}' = \frac{1}{\gamma_{v}[1 - (\mathbf{v} \cdot \mathbf{u})/c^{2}]} \mathbf{f}_{\bot}
$$

where $\mathbf{v}$ is the velocity of the primed frame with respect to the unprimed frame.

In the case of a pure force where the mass is constant, the expression for the parallel component becomes:

$$
\mathbf{f}_{\parallel}' = \frac{\mathbf{f}_{\parallel} - \mathbf{v}(\mathbf{f} \cdot \mathbf{u})/c^{2}}{1 - (\mathbf{v} \cdot \mathbf{u})/c^{2}}
$$

In general, the 3-force is not invariant between reference frames, contrast to the classical case. However, if the force is pure and parallel to the particle's velocity $\mathbf{u}$ and $\mathbf{v}$, then $\mathbf{f}_{\bot}$ becomes zero and $\mathbf{f}_{\parallel}'$ is the same as $\mathbf{f}_{\parallel}$. This means that in this special case, $\mathbf{f}$ is invariant across all frames with $\mathbf{v}$ parallel to $\mathbf{f}$.

From the 4-force, the 4-acceleration is defined as:

$$
\mathbf{a} \equiv \frac{\mathrm{d}U}{\mathrm{d}\tau} = \frac{\mathbf{f}}{m_{0}}
$$

It is worth noting that the 4-acceleration is always orthogonal to the 4-velocity since $U$ has a constant magnitude.

## Doppler Shift

The classical doppler shift is defined as:

$$
f = \left( \frac{c \pm v_{r}}{c \pm v_{s}} \right) f_{0}
$$

where $c$ is the speed of the wave and the velocities are defined such that the positive direction is from the receiver to the source.

In the relativistic case, consider a light source stationary in frame $S'$ which is moving at speed $v$ away from frame $S$. For an observer in $S$, the observed time interval $\tau$ between two successive wave fronts is:

$$
\tau = \gamma \tau' + \frac{\gamma \tau' v}{c} = \sqrt{\frac{1 + \beta}{1 - \beta}} \tau'
$$

where the first term is the time-dilated period and the second term is due to extra distance caused by the source moving away.

The observed frequency is thus:

$$
f = \sqrt{\frac{1 - \beta}{1 + \beta}} f_{0}
$$

and the observed wavelength is:

$$
\lambda = \sqrt{\frac{1 + \beta}{1 - \beta}} \lambda_{0}
$$

where $f_{0}$ and $\lambda_{0}$ are observed in the frame where the source is stationary.
