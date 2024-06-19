# Normal Modes and Waves

- [Normal Modes in the Continuous Limit](#normal-modes-in-the-continuous-limit)
- [The Wave Equation](#the-wave-equation)
    - [d'Alembert's Solution](#dalemberts-solution)
    - [Separation of Variables](#separation-of-variables)
    - [Energy Stored in a Wave](#energy-stored-in-a-wave)
- [Dispersion](#dispersion)
- [Reflection and Transmission](#reflection-and-transmission)
    - [Boundary Conditions](#boundary-conditions)

## Normal Modes

From the discussion of a system of general linear differential equations, we consider the special case of a system of second order linear differential equations with constant coefficients:

$$
\ddot{\mathbf{y}} = -\mathbf{A} \cdot \mathbf{y}
$$

where $\mathbf{A}$ is a constant matrix.

Diagonalising $\mathbf{A}$ yields:

$$
\ddot{(\mathbf{R}^{-1}\mathbf{y})} = -\mathbf{L} (\mathbf{R}^{-1} \mathbf{y})
$$

and we are actually solving the equations:

$$
\ddot{\xi}_{i}(t) = -\lambda_{i} \xi_{i}(t)
$$

where $\lambda_{i}$ are the eigenvalues of $\mathbf{A}$ and $\xi_{i}(t)$ are the elements of the transformed vector $\mathbf{Y} = \mathbf{R}^{-1} \mathbf{y}$.

Returning to the original variables, we have:

$$
\mathbf{y} = \mathbf{R} \mathbf{Y}(t) = \sum_{i} \mathbf{v}_{i} \xi_{i}(t)
$$

It is often convenient to make sure that the eigenvectors are normalised, so that $\mathbf{R}$ is an orthogonal matrix and $\mathbf{R}^{-1} = \mathbf{R}^{T}$.

The individual solutions $\mathbf{v}_{i} \xi_{i}(t)$ are called the normal modes of the system.

### Energies of Normal Modes

The total energy of a physical system represented by the above equations is given by:

$$
\epsilon = \frac{\left\lvert \dot{\mathbf{y}} \cdot \dot{\mathbf{y}} \right\rvert}{2} + \frac{\mathbf{y} \cdot \mathbf{A} \cdot \mathbf{y}}{2} \equiv T + U
$$

which is the energy of the system up to a constant factor.

Using the transformation $\mathbf{y} = \mathbf{R} \mathbf{Y}(t)$, we have:

$$
\epsilon = \frac{\left\lvert \dot{\mathbf{Y}} \cdot \dot{\mathbf{Y}} \right\rvert}{2} + \frac{\mathbf{Y} \cdot \mathbf{L} \cdot \mathbf{Y}}{2} = \sum_{i} \left( \frac{\dot{\xi}^{2}}{2} + \frac{\lambda_{i} \xi^{2}}{2} \right)
$$

Thus, the total energy is the sum of the energies of the individual normal modes.

## Normal Modes in the Continuous Limit

Consider a stretched string of total mass $M$ and length $L$, which can be split into small mass elements labelled by $p \in [1, \infty]$. Assuming that the angle $\alpha_{p}$ between the string and the horizontal is small, the force balance is given by:

$$
\begin{split}
F_{py} = T \sin{\alpha_{p}} - T \sin{\alpha_{p-1}} \\
F_{px} = T \cos{\alpha_{p}} - T \cos{\alpha_{p-1}}
\end{split}
$$

In the small angle limit, there will be zero horizontal net force and in the vertical direction:

$$
F_{py} = m \ddot{y}_{p} \approx T \tan{\alpha_{p}} - T \tan{\alpha_{p-1}} = \frac{T}{l}(y_{p+1} - 2y_{p} + y_{p-1})
$$

where $l$ and $m$ are the length and mass of the segment satisfying $(N + 1)l = L$ and $Nm = M$.

Define $\omega_{0}^{2} \equiv T/ml$, we have:

$$
\ddot{y}_{p} + 2\omega_{0}^{2}y_{p} - \omega_{0}^{2}(y_{p+1} + y_{p-1}) = 0
$$

We should expect trigonometric solutions, so first consider a solution of the form:

$$
y_{p}(t) = A_{p} \cos{(\omega t + \phi)}
$$

Substituting into the equation gives:

$$
\begin{split}
(2\omega_{0}^{2} - \omega^{2})A_{p} - \omega_{0}^{2}(A_{p+1} + A_{p-1}) &= 0 \\
\frac{A_{p+1} + A_{p-1}}{A_{p}} &= \frac{2\omega_{0}^{2} - \omega^{2}}{\omega_{0}^{2}}
\end{split}
$$

But $\omega$ should be the identical across the whole string so it does not depend on $p$. Therefore, the ratio on the left hand side should be independent of $p$. We also know that if the string is fixed at both ends, then $A_{0} = A_{N+1} = 0$. Consider an expression for $A_{p}$ in the form:

$$
A_{p} = C \sin{p \theta}
$$

so that the left hand side becomes:

$$
\frac{\sin{(p+1)\theta} + \sin{(p-1)\theta}}{\sin{p\theta}} = 2 \cos{\theta}
$$

which is independent of $p$.

For the boundary conditions, we require $(N+1)\theta = n\pi$ for $n \in \mathbb{z}$. Given the expression for $A_{p}$, we can solve for $\omega$:

$$
\omega = 2\omega_{0} \sin{\frac{\theta}{2}} = 2\omega_{0} \sin{\frac{n\pi}{2(N + 1)}}
$$

so that the general solution for $y_{p}$ is:

$$
y_{pn}(t) = C_{n} \sin{\frac{pn\pi}{2(N + 1)}} \sin{(\omega_{n} t + \phi)}
$$

where:

$$
\omega_{n} = 2\omega_{0} \sin{\frac{n\pi}{2(N + 1)}}
$$

In the limit of $N \to \infty$, $\omega_{n}$ becomes:

$$
\omega_{n} = 2\sqrt{\frac{T}{ml}} \frac{n\pi}{2(N + 1)} = \frac{n\pi}{L} \sqrt{\frac{T}{\rho}}
$$

where $\rho \equiv m/l$ is the linear density of the string.

This means that all the normal frequencies are integer multiples of the fundamental frequency:

$$
\omega_{n} = n\omega_{1} = n \frac{\pi}{L} \sqrt{\frac{T}{\rho}}
$$

## The Wave Equation

Consider a string of linear density $\rho$ stretched under a tension $T$. For a small segment of the string, the force balance is given by:

$$
\begin{split}
F_{y} &= T \sin{(\theta + \delta \theta)} - T \sin{\theta} \approx T [\tan{(\theta + \delta \theta)} - \tan{\theta}] \\
F_{x} &= T \cos{(\theta + \delta \theta)} - T \cos{\theta} \approx 0
\end{split}
$$

where $\theta$ is the angle between the string and the x-axis along the length of the string.

But $\tan{\theta}$ is just $y_{x}$ and a small change $\delta \theta$ can be expressed as:

$$
\tan{(\theta + \delta \theta)} = y_{x}(x + \delta x) \approx y_{x}(x) + \delta x y_{xx}(x)
$$

so that:

$$
F_{y} \approx T \delta x \frac{\partial^{2} y}{\partial x^{2}}
$$

Newton's second law gives:

$$
\begin{split}
\delta m \frac{\partial^{2} y}{\partial t^{2}} &= T \delta x \frac{\partial^{2} y}{\partial x^{2}} \\
\rho \sqrt{\delta x^{2} + \delta y^{2}} \frac{\partial^{2} y}{\partial t^{2}} &= T \delta x \frac{\partial^{2} y}{\partial x^{2}} \\
\frac{\partial^{2} y}{\partial t^{2}} &= \frac{T}{\rho \sqrt{1 + (\delta y/\delta x)^{2}}} \frac{\partial^{2} y}{\partial x^{2}}
\end{split}
$$

In the limit of small $\theta$, $(\delta y/\delta x)^{2} \approx 0$ and we have:

$$
\frac{\partial^{2} y}{\partial t^{2}} = \frac{T}{\rho} \frac{\partial^{2} y}{\partial x^{2}} \equiv c^{2} \frac{\partial^{2} y}{\partial x^{2}}
$$

This is called the wave equation where $c \equiv \sqrt{T/\rho}$ is the wave speed.

In general, the three-dimensional wave equation satisfied by a scalar field $u(x, y, z, t)$ has the form:

$$
\frac{\partial^{2} u}{\partial t^{2}} = c^{2} \left( \frac{\partial^{2} u}{\partial x^{2}} + \frac{\partial^{2} u}{\partial y^{2}} + \frac{\partial^{2} u}{\partial z^{2}} \right) = c^{2} \nabla^{2} u
$$

### d'Alembert's Solution

Consider the one dimensional wave equation. By introducing two new variables $u = x - ct$ and $v = x + ct$, it can be shown that the general solution to the equation has the form:

$$
y(x, t) = f(x - ct) + g(x + ct)
$$

where $f$ represents a wave travelling to positive $x$ and $g$ represents a wave travelling to negative $x$.

Suppose that at $t = 0$, $y(x, 0) = U(x)$, corresponding to an initial displacement, and $\partial y(x, 0)/\partial t = V(x)$, corresponding to an initial velocity. The initial displacement gives the condition $U(x) = f(x) + g(x)$ while the initial velocity means:

$$
V(x) = -c \frac{\mathrm{d}}{\mathrm{d}x} f(x) + c \frac{\mathrm{d}}{\mathrm{d}x} g(x)
$$

Integrating this equation:

$$
f(x) - g(x) = -\frac{1}{c} \int_{x_{0}}^{x} V(x) \, \mathrm{d}x
$$

Solving for $f$ and $g$:

$$
\begin{split}
f(x) = \frac{1}{2} U(x) - \frac{1}{2c} \int_{x_{0}}^{x} V(x) \, \mathrm{d}x \\
g(x) = \frac{1}{2} U(x) + \frac{1}{2c} \int_{x_{0}}^{x} V(x) \, \mathrm{d}x
\end{split}
$$

so that the general solution under these conditions is:

$$
y(x, t) = \frac{1}{2} \left[ U(x - ct) + U(x + ct) \right] + \frac{1}{2c} \int_{x-ct}^{x+ct} V(x) \, \mathrm{d}x
$$

### Separation of Variables

There is another way to solve the wave equation. Suppose that we can write the solution as a product of a spatial function $X(x)$ and a temporal function $T(t)$:

$$
y(x, t) = X(x) T(t)
$$

The wave equation then becomes:

$$
\frac{1}{c^{2}} \frac{1}{T} \frac{\mathrm{d}^{2}T}{\mathrm{d}t^{2}} =\frac{1}{X} \frac{\mathrm{d}^{2}X}{\mathrm{d}x^{2}}
$$

Since the left hand side is a function of $t$ only while the right hand side is a function of $x$ only, we can assert that they must both equate to a constant $C$. This yields two second order differential equations that can be solved for $X$ and $T$.

Consider the case where $C$ is negative so that we write $C = -\Omega^{2}$. In this case, the solutions are oscillatory:

$$
\begin{split}
X(x) = A \cos(\Omega x + \phi) \\
T(t) = B \cos(c \Omega t + \psi)
\end{split}
$$

and the general solution is:

$$
y(x, t) = D \cos(\Omega x + \phi) \cos(c\Omega t + \psi)
$$

With this solution, consider the the conditions $\partial y/\partial t = 0$ at $t = 0$, which means the string is at rest initially, and $y(0, t) = y(L, t) = 0$, which means the string is clamped at both ends. This gives the conditions $\psi = 0$, $\phi = \pi/2$ and $\Omega L = n\pi$ for some integer $n$. The solution is then a superposition of $n$ standing waves:

$$
y(x, t) = \sum_{n=1}^{n} D_{n} \sin{\frac{n\pi x}{L}} \cos{\frac{n\pi ct}{L}}
$$

where $D_{n}$ are constants determined by the form of the wave at some point in time.

### Energy Stored in a Wave

Consider an infinitesimal element of string. The kinetic energy stored in the element is:

$$
\delta K = \frac{1}{2} \rho \delta x \left( \frac{\partial y}{\partial t} \right)^{2}
$$

while the potential energy is:

$$
\delta U = \frac{1}{2} T \delta x \left( \frac{\partial y}{\partial x} \right)^{2}
$$

so that the energy densities are given by:

$$
\begin{split}
\frac{\mathrm{d}K}{\mathrm{d}x} &= \frac{1}{2} \rho \left( \frac{\partial y}{\partial t} \right)^{2} \\
\frac{\mathrm{d}U}{\mathrm{d}x} &= \frac{1}{2} T \left( \frac{\partial y}{\partial x} \right)^{2}
\end{split}
$$

For a sinusoidal wave of the form $y = A\sin{(kx - \omega t)}$, it is easy to show that the kinetic and potential energy densities are the same. The total energy per unit length is then:

$$
\frac{\mathrm{d}E}{\mathrm{d}x} = \frac{1}{2} \rho A^{2} \omega^{2}
$$

The energy flow per unit time, which is also the power required to maintain the wave, is:

$$
P = \frac{1}{2} \rho A^{2} \omega^{2} v
$$

## Dispersion

A dispersive medium is where the velocity of a wave has a dependence on the frequency and wavelength. Consider the simple case where two waves differ in frequency by $2\delta \omega$ and wave number by $2\delta k$:

$$
y_{1} = A \cos{[(k + \delta k)x - (\omega + \delta \omega)t]} \\
y_{2} = A \cos{[(k - \delta k)x - (\omega - \delta \omega)t]}
$$

so that the superposition of the two waves can be written as:

$$
y = 2A \cos{(kx - \omega t)} \cos{(\delta kx - \delta \omega t)}
$$

There are two frequencies in this wave: $\omega$ and $\delta \omega$, and two wave numbers: $k$ and $\delta k$. While the velocity of the individual waves is simply $\omega/k$, the velocity of the wave packet is $\delta \omega/\delta k$.

We define the phase velocity of a wave as the velocity of the wave at a given frequency and wavelength. On the other hand, the group velocity is the velocity of the wave packet:

$$
v_{p} = \frac{\omega}{k}, \quad v_{g} = \frac{\mathrm{d}\omega}{\mathrm{d}k}
$$

## Reflection and Transmission

Consider a wave travelling along a string that has density $\rho_{1}$ in $(-\infty, 0)$ and density $\rho_{2}$ in $(0, \infty)$. The tension in the string must be uniform to have zero horizontal acceleration. Suppose that the wave travels in the positive direction. In the region $(-\infty, 0)$, there will be an incident wave and a reflected wave; in the region $(0, \infty)$, there will be a transmitted wave:

$$
y(x, t) =
\begin{cases}
A \cos{(k_{1}x - \omega t)} + B \cos{(k_{1}x + \omega t)} & x < 0 \\
C \cos{(k_{2}x - \omega t)} & x > 0
\end{cases}
$$

Using complex notation, we can write the solution as:

$$
\tilde{y}(x, t) =
\begin{cases}
\tilde{A} e^{i(\omega t - k_{1}x)} + \tilde{B} e^{i(\omega t + k_{1}x)} & x < 0 \\
\tilde{C} e^{i(\omega t - k_{2}x)} & x > 0
\end{cases}
$$

### Boundary Conditions

Let us denote the wave in the negative region by $y_{1}(x, t)$ and the wave in the positive region by $y_{2}(x, t)$. For the string to be continuous, we must have $y_{1}(0, t) = y_{2}(0, t)$.

Suppose that at the boundary, there is a mass $m$ attached to the string. The mass experiences two tensions of the same magnitude but in different directions. The acceleration of $y_{1}$ must be the same as $y_{2}$, and they both fulfil Newton's second law at the boundary:

$$
T \frac{\partial y_{2}(0, t)}{\partial x} - T \frac{\partial y_{1}(0, t)}{\partial x} = M \frac{\partial^{2} y_{1}(0, t)}{\partial t^{2}} = M \frac{\partial^{2} y_{2}(0, t)}{\partial t^{2}}
$$

These conditions yield two equations for the constants:

$$
\begin{split}
\tilde{A} + \tilde{B} &= \tilde{C} \\
\tilde{A} - \tilde{B} &= - \frac{1}{k_{1}} \left( k_{2} + i \frac{\omega^{2} M}{T} \right) \tilde{C}
\end{split}
$$

Expressing everything in terms $\tilde{A}$, we have:

$$
\begin{split}
\tilde{B} = \frac{k_{1} + k_{2} + i \omega^{2} M/T}{k_{1} - k_{2} - i \omega^{2} M/T} \tilde{A} \\
\tilde{C} = \frac{2k_{1}}{k_{1} - k_{2} - i \omega^{2} M/T} \tilde{A}
\end{split}
$$

Define the reflection coefficient $R$ as:

$$
R = \left\lvert \frac{\tilde{B}}{\tilde{A}} \right\rvert = \left\lvert \frac{k_{1} + k_{2} + i \omega^{2} M/T}{k_{1} - k_{2} - i \omega^{2} M/T} \right\rvert = \left\lvert R e^{i\theta} \right\rvert
$$

and the transmission coefficient $T$ as:

$$
T = \left\lvert \frac{\tilde{C}}{\tilde{A}} \right\rvert = \left\lvert \frac{2k_{1}}{k_{1} - k_{2} - i \omega^{2} M/T} \right\rvert = \left\lvert T e^{i\phi} \right\rvert
$$

Note how the existence of the mass $m$ leads to a phase shift in the reflected and transmitted waves from the incident wave. If $m = 0$, we have the simplified case:

$$
\begin{split}
R &= \frac{k_{1} + k_{2}}{k_{1} - k_{2}} \\
T &= \frac{2k_{1}}{k_{1} - k_{2}}
\end{split}
$$

where there is no phase shift.
