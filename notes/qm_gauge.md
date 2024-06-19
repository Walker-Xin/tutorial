# Quantum Mechanics - Potentials and Gauge Transformations

It is well known in classical mechanics that the time evolution of dynamic variables such as $x(t)$ and $v(t)$ is independent of change of potential energy $V(x) \to V(x) + V_{0}$, where $V_{0}$ is a constant. The situation in quantum mechanics deserves a closer look.

Let $\ket{\psi, t}$ be a state ket in the presence of a potential $V(x)$, and $\ket{\psi', t}$ be a state ket in the presence of a potential $V(x) + V_{0}$. Suppose that the initial conditions are such that $\ket{\psi, t=0} = \ket{\psi', t=0} = \ket{\psi_{0}}$. Applying the time evolution operator $\hat U(t,0)$ associated with the modified potential to the initial state ket:

$$
\begin{split}
\ket{\psi', t} &= \exp \left[ -i \left( \frac{\hat{p}^{2}}{2m} + V(x) + V_{0} \right) \frac{t}{\hbar} \right] \ket{\psi_{0}} \\
               &= \exp \left( -i \frac{V_{0}t}{\hbar} \right) \ket{\psi, t}
\end{split}
$$

This indicates that the effect of changing the potential by a constant is a phase factor on the state ket. Formally, we can say that the gauge transformation given by:

$$
V(x) \to V(x) + V_{0}
$$

is accompanied by a change in the state ket:

$$
\ket{\psi, t} \to \exp \left( - \frac{iV_{0}t}{\hbar} \right) \ket{\psi, t}
$$

## Gauge Transformations in Electromagnetism

It is well known that there are two potentials in time-independent electromagnetism: the electric potential $\phi$ and the magnetic vector potential $\vec{A}$:

$$
\mathbf{E} = -\nabla \phi \qquad \mathbf{B} = \nabla \times \mathbf{A}
$$

The Hamiltonian for a charged particle in an electromagnetic field is:

$$
H = \frac{1}{2m} \left( \hat{\mathbf{p}} - q \mathbf{A} \right)^{2} + q \phi
$$

It is instructive to consider the Ehrenfest theorem for the expectation value of the position operator:

$$
\frac{\mathrm{d}}{\mathrm{d}t} \hat{x}_{i} = \frac{1}{i\hbar} [\hat{x}_{i}, \hat{H}] = \frac{1}{m} (\hat{p}_{i} - qA_{i})
$$

This implies that the operator $\hat{p}$, which has been defined as the generator of translations, is not the same as $m \mathrm{d}\hat{x}/\mathrm{d}t$. Often, $\hat{p}$ is called the canonical momentum, distinguished from the mechanical momentum denoted by $\hat{\Pi}$:

$$
\hat{\Pi} \equiv m \frac{\mathrm{d}\hat{x}}{\mathrm{d}t} = \hat{p} - q \mathbf{A}
$$

From the Hamiltonian, we can write the Schrodinger equation in position representation. Focusing on the part that involves the time derivatives:

$$
\begin{split}
\bra{\mathbf{r}} \left( \hat{p} - q \hat{A} \right)^{2} \ket{\psi, t} &= \left[ -i\hbar \nabla - q \mathbf{A}(\mathbf{r}) \right] \bra{\mathbf{r}} \left( \hat{p} - q \hat{A} \right) \ket{\psi, t} \\
&= \left[ -i\hbar \nabla - q \mathbf{A}(\mathbf{r}) \right] \left[ -i\hbar \nabla - q \mathbf{A}(\mathbf{r}) \right] \braket{\mathbf{r} | \psi, t} \\
&= \left[ -i\hbar \nabla - q \mathbf{A}(\mathbf{r}) \right] \left[ -i\hbar \nabla \braket{\mathbf{r} | \psi, t} - q \mathbf{A}(\mathbf{r}) \braket{\mathbf{r} | \psi, t} \right] \\
&= -\hbar^{2} \nabla^{2} \braket{\mathbf{r} | \psi, t} + i\hbar \nabla \left( q \mathbf{A}(\mathbf{r}) \braket{\mathbf{r} | \psi, t} \right) + i\hbar q \nabla \braket{\mathbf{r} | \psi, t} \cdot \mathbf{A}(\mathbf{r}) - \frac{q}{c} \mathbf{A}^{2} \braket{\mathbf{r} | \psi, t} \\
\end{split}
$$

Combining everything, we write the time-dependent Schrodinger equation:

$$
\frac{1}{2m} \left[ -i\hbar \nabla - q \mathbf{A}(\mathbf{r}) \right]^{2} \braket{\mathbf{r} | \psi, t} + q \phi(\mathbf{r}) \braket{\mathbf{r} | \psi, t} = i\hbar \frac{\partial}{\partial t} \braket{\mathbf{r} | \psi, t}
$$

from which we can identify the continuity equation:

$$
\frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{j} = 0
$$

where $\rho = \left\lvert \psi(\mathbf{r}, t) \right\rvert^{2}$ is unchanged but the probability current $\mathbf{j}$ is modified:

$$
\mathbf{j} = \frac{\hbar}{2mi} \left[ \psi^{*} \nabla \psi - \psi \nabla \psi^{*} \right] - \frac{q}{m} \mathbf{A} \left\lvert \psi \right\rvert^{2}
$$

which is the ordinary probability current under the substitution $\nabla \to \nabla - (iq/\hbar) \mathbf{A}$.

Now we consider the gauge transformation in electromagnetism given by:

$$
\phi \to \phi - \frac{\partial \chi}{\partial t} \qquad \mathbf{A} \to \mathbf{A} + \nabla \chi
$$

which leaves the electric and magnetic fields unchanged.

In classical theory, the dynamics of a charged particle is independent of choice of the gauge function $\chi(\mathbf{r}, t)$. In general, the canonical momentum $\mathbf{p}$ is not gauge invariant but the mechanical momentum $\mathbf{\Pi}$ is. Since expectation values in quantum theory should behave like classical observables, we expect $\left\langle \hat{r} \right\rangle$ and $\left\langle \hat{\Pi} \right\rangle$ to be gauge invariant whereas $\left\langle \hat{p} \right\rangle$ is not.

Let us denote $\ket{\psi}$ as the state ket in the presence of a potential $\mathbf{A}$ and $\ket{\psi'}$ as the state ket in the presence of a potential $\mathbf{A}' = \mathbf{A} + \nabla \chi$. We require the expectation values to satisfy:

$$
\begin{split}
\bra{\psi'} \hat{r} \ket{\psi'} &= \bra{\psi} \hat{r} \ket{\psi} \\
\bra{\psi'} \hat{p} - q \mathbf{A}' \ket{\psi'} &= \bra{\psi} \hat{p} - q \mathbf{A} \ket{\psi}
\end{split}
$$

In addition, we require the unity norm of the state ket to be preserved:

$$
\braket{\psi' | \psi'} = \braket{\psi | \psi} = 1
$$

We wish to construct a unitary operator $\hat{F}$ such that:

$$
\ket{\psi'} = \hat{F} \ket{\psi}
$$

It could be shown that the operator $\hat{F}$ follows the form:

$$
\hat{F} = \exp \left( \frac{i}{\hbar} q \chi \right)
$$

Going back to the time-dependent Schrodinger equation, the original state ket $\ket{\psi}$ evolves according to:

$$
\left[ \frac{1}{2m} \left( \hat{p} - q \mathbf{A} \right)^{2} + q \phi \right] \ket{\psi} = i\hbar \frac{\partial}{\partial t} \ket{\psi}
$$

while the modified state ket $\ket{\psi'}$ evolves according to:

$$
\left[ \frac{1}{2m} \left( \hat{p} - q \mathbf{A} - q \nabla \chi \right)^{2} + q \phi - q \frac{\partial \chi}{\partial t} \right] \ket{\psi'} = i\hbar \frac{\partial}{\partial t} \ket{\psi'}
$$

which is a new Schrodinger equation which will be satisfied under the substitution $\ket{\psi'} = \hat{F} \ket{\psi}$, verifying that $\hat{F}$ is the correct transformation operator.

## Landau Levels

Consider a magnetic field $\mathbf{B} = B \hat{z}$ in the $z$-direction. We may choose a gauge such that:

$$
\mathbf{A} = \frac{B}{2} (-y, x, 0)^{\intercal}
$$

We have the Hamiltonian:

$$
\begin{split}
\hat{H} &= \frac{1}{2m} \left( \hat{p} - q \hat{A} \right)^{2} \\
&= \frac{1}{2m} \left[ \left( \hat{p}_{x} + \frac{qB}{2} y \right)^{2} + \left( \hat{p}_{y} - \frac{qB}{2} x \right)^{2} + \hat{p}_{z}^{2} \right]
\end{split}
$$

Let us define $\omega = qB/m$ called the Larmor frequency and the dimensionless operators:

$$
\pi_{x} = \frac{\hat{p}_{x} + m\omega \hat{y}/2}{\sqrt{m\omega\hbar}} \qquad \pi_{y} = \frac{\hat{p}_{y} - m\omega \hat{x}/2}{\sqrt{m\omega\hbar}}
$$

The Hamiltonian becomes:

$$
\hat{H} = \frac{\hbar \omega}{2} \left( \pi_{x}^{2} + \pi_{y}^{2} \right) + \frac{\hat{p}_{z}^{2}}{2m}
$$

The last term just describes a free particle in the $z$-direction. The first two terms describe a harmonic oscillator in the $x$ and $y$ directions, because they satisfy the same commutation relations as $\hat{x}_{i}$:

$$
[\pi_{x}, \pi_{y}] = \frac{1}{2\hbar}([\hat{y}, \hat{p}_{y}] - [\hat{p}_{x}, \hat{x}]) = i
$$

We have the ladder operators:

$$
\hat{a} = \frac{1}{\sqrt{2}} \left( \pi_{x} + i\pi_{y} \right) \qquad \hat{a}^{\dagger} = \frac{1}{\sqrt{2}} \left( \pi_{x}^{\dagger} - i\pi_{y}^{\dagger} \right)
$$

and the Hamiltonian becomes:

$$
\hat{H} = \hbar \omega \left( \hat{a}^{\dagger} \hat{a} + \frac{1}{2} \right) + \frac{\hat{p}_{z}^{2}}{2m}
$$

The first part is exactly the Hamiltonian of a harmonic oscillator with the energy eigenvalues:

$$
E_{n} = \hbar \omega \left( n + \frac{1}{2} \right)
$$

These discrete energy levels for a charged particle in a magnetic field are called Landau levels. If the energy can move freely in the $z$-direction, the energy spectrum will still be continuous due to the free particle term in the Hamiltonian.
