# Quantum Mechanics - Harmonic Oscillator

The harmonic oscillator is described by the Hamiltonian:

$$
\hat{H} = \frac{\hat{p}^{2}}{2m} + \frac{1}{2} m \omega^{2} \hat{x}^{2}
$$

and the time independent Schrödinger equation:

$$
\hat{H} \ket{\psi} = E \ket{\psi}
$$

In the position representation:

$$
-\frac{\hbar^{2}}{2m} \frac{\partial^{2} \psi(x)}{\partial x^{2}} + \frac{1}{2} m \omega^{2} x^{2} \psi(x) = E \psi(x)
$$

where $\psi(x) = \braket{x | \psi}$.

Consider the dimensionless variable:

$$
\xi = \sqrt{\frac{m \omega}{\hbar}} x
$$

The equation reduces to:

$$
\hat{\mathcal{H}} \psi(\xi) = \epsilon \psi(\xi)
$$

where we have defined the dimensionless Hamiltonian:

$$
\hat{\mathcal{H}} = -\frac{1}{2} \frac{\mathrm{d}^{2}}{\mathrm{d} \xi^{2}} + \frac{1}{2} \xi^{2}
$$

and the dimensionless energy $\epsilon = E / \hbar \omega$.

Note that reverting back to ket notation, the Schrödinger equation expressed using the dimensionless Hamiltonian is:

$$
\hat{\mathcal{H}} \ket{\psi} = \epsilon \ket{\psi}
$$

and $\psi(\xi) = \braket{\xi | \psi}$.

## Solution to the Schrödinger Equation

To solve the dimensionless equation in position representation, consider the Ansatz $\psi(\xi) = e^{-\xi^{2}/2} y(\xi)$ that leads to a differential equation for $y(\xi)$:

$$
y'' - 2 \xi y' + (2\epsilon - 1) y = 0
$$

This is the Hermite differential equation of order $n = \epsilon - 1/2$. The solutions to $y(\xi)$ are thus Hermite polynomials $H_{n}(\xi)$ where $n \in \mathbb{N}$ and $\epsilon = n + 1/2$. The solutions to the Schrödinger equation are:

$$
\psi_{n}(\xi) = A_{n} e^{-\xi^{2}/2} H_{n}(\xi)
$$

where the normalisation constants are:

$$
A_{n} = \left( \frac{1}{2^{n} n!} \right)^{1/2} \left( \frac{m \omega}{\pi \hbar} \right)^{1/4} = \frac{1}{\sqrt{2^{n} n!}} \left( \frac{1}{\pi l^{2}} \right)^{1/4}
$$

where $l = \sqrt{h/(m \omega)}$ is the characteristic length scale of the harmonic oscillator.

## Energy Eigenkets and Ladder Operators

Consider the operators:

$$
\begin{split}
\hat{a} &= \frac{1}{\sqrt{2}} \left( \frac{\hat{x}}{l} + i \frac{\hat{p}}{m \omega l} \right) = \frac{1}{\sqrt{2}} \left( \xi + \frac{\mathrm{d}}{\mathrm{d} \xi} \right) \\
\hat{a}^{\dagger} &= \frac{1}{\sqrt{2}} \left( \frac{\hat{x}}{l} - i \frac{\hat{p}}{m \omega l} \right) = \frac{1}{\sqrt{2}} \left( \xi - \frac{\mathrm{d}}{\mathrm{d} \xi} \right)
\end{split}
$$

Consider $\hat{a}^{\dagger} \hat{a}$ acting on a ket $\ket{f}$:

$$
\begin{split}
\hat{a}^{\dagger} \hat{a} \ket{f} &= \frac{1}{2} \left( \xi - \frac{\mathrm{d}}{\mathrm{d} \xi} \right) \left( \xi + \frac{\mathrm{d}}{\mathrm{d} \xi} \right) \ket{f} \\
&= \hat{\mathcal{H}} \ket{f} - \frac{1}{2} \ket{f} \\
\end{split}
$$

Similarly, $\hat{a} \hat{a}^{\dagger} \ket{f} = (\hat{\mathcal{H}} + 1/2) \ket{f}$. This means that the commutator $[\hat{a}, \hat{a}^{\dagger}] = \mathbb{I}$. Suppose we have some eigenket $\ket{\psi}$ that satisfies the Schrödinger equations. Applying $\hat{a}^{\dagger} \hat{a}$ to $\ket{\psi}$:

$$
\hat{a}^{\dagger} \hat{a} \ket{\psi} = \hat{\mathcal{H}} \ket{\psi} - \frac{1}{2} \ket{\psi} = \left( \epsilon - \frac{1}{2} \right) \ket{\psi}
$$

This means that this operator, which we denote as $\hat{N}$, share the same eigenkets as $\hat{\mathcal{H}}$ with eigenvalues $\epsilon - 1/2$. $\hat{N}$ is called the number operator. Let us denote the energy eigenkets as $\ket{n}$ such that:

$$
\hat{N} \ket{n} = n \ket{n}
$$

Applying $\hat{\mathcal{H}}$ to $\ket{n}$ gives:

$$
\hat{\mathcal{H}} \ket{n} = (\hat{N} + 1/2) \ket{n} = \left( n + \frac{1}{2} \right) \ket{n}
$$

This means that the dimensionless energy eigenvalues are $\epsilon_{n} = n + 1/2$. Note that this is exactly the same relation as the definition of $\epsilon_{n}$ via the order of the Hermite polynomial $H_{n}(\xi)$. We thus denote the energy eigenkets as $\ket{n}$ where $n \in \mathbb{N}$.

Consider the action of $\hat{a}^{\dagger}$ on $\ket{n}$:

$$
\hat{N} \hat{a}^{\dagger} \ket{n} = \hat{a}^{\dagger} \hat{a} \hat{a}^{\dagger} \ket{n} = \hat{a}^{\dagger} (\mathbb{I} + \hat{N}) \ket{n} = (n + 1) \hat{a}^{\dagger} \ket{n}
$$

where at the second step we have used the previous commutation relation.

This implies that the ket $\hat{a}^{\dagger} \ket{n}$ is also an eigenket of $\hat{N}$ with eigenvalue $n + 1$. This eigenket has the dimensionless energy eigenvalue $\epsilon_{n+1} = (n + 1) + 1/2 = \epsilon_{n} + 1$. This means that $\hat{a}^{\dagger}$ increases the dimensionless energy of an eigenket $\ket{n}$ by 1. Similarly:

$$
\hat{N} \hat{a} \ket{n} = \hat{a} \hat{a}^{\dagger} \hat{a} \ket{n} = \hat{a} (\mathbb{I} + \hat{N}) \ket{n} = (n - 1) \hat{a} \ket{n}
$$

so that $\hat{a}$ decreases the dimensionless energy of an eigenket $\ket{n}$ by 1.

These imply that $\hat{a} \ket{n}$ and $\ket{n - 1}$ should be the same up to a constant. Indeed, we can show that:

$$
\begin{split}
\hat{a} \ket{n} & = \sqrt{n} \ket{n - 1} \\
\hat{a}^{\dagger} \ket{n} & = \sqrt{n + 1} \ket{n + 1}
\end{split}
$$

The lowering of the eigenkets will terminate when $n = 0$ since $n \in \mathbb{N}$ for Hermite polynomials. $\ket{0}$ is called the ground state of the harmonic oscillator with the dimensionless energy $\epsilon_{0} = 1/2$. To convert to the actual energy, we note $E = \hbar \omega \epsilon$ so that the ground state energy is:

$$
E_{0} = \frac{1}{2} \hbar \omega
$$

and each raising or lowering of the energy increases or decreases the energy by $\hbar \omega$:

$$
E_{n} = \left( n + \frac{1}{2} \right) \hbar \omega
$$

The position representation of the eigenkets are given by the solution to the differential equations:

$$
\braket{x | n} = \psi_{n}(x) = \frac{1}{\sqrt{2^{n} n!}} \left( \frac{1}{\pi l^{2}} \right)^{1/4} e^{-\xi^{2}/2} H_{n}(\xi)
$$

where $\xi = x/l$.

In particular, the ground state wavefunction is:

$$
\braket{x | 0} = \left( \frac{1}{\pi l^{2}} \right)^{1/4} e^{-x^{2}/2l^{2}}
$$

and the first excited state wavefunction is:

$$
\braket{x | 1} = \left( \frac{1}{\pi l^{2}} \right)^{1/4} \frac{\sqrt{2}x}{l} e^{-x^{2}/2l^{2}}
$$

## Expectation Values

Let us work in dimensionless units. First note that the dimensionless position operator $\hat{\xi}$ can be written as:

$$
\hat{\xi} = \frac{1}{\sqrt{2}} \left( \hat{a} + \hat{a}^{\dagger} \right)
$$

and its square is:

$$
\hat{\xi}^{2} = \frac{1}{2} \left( \hat{a}^{2} + \hat{a}^{\dagger 2} + \hat{a} \hat{a}^{\dagger} + \hat{a}^{\dagger} \hat{a} \right)
$$

The expectation value of $\hat{\xi}$ in the eigenket $\ket{n}$ is:

$$
\begin{split}
\braket{n | \hat{\xi} | n} &= \frac{1}{\sqrt{2}} \left( \braket{n | \hat{a} | n} + \braket{n | \hat{a}^{\dagger} | n} \right) \\
&= \frac{1}{\sqrt{2}} \left( \sqrt{n} \braket{n | n - 1} + \sqrt{n + 1} \braket{n | n + 1} \right) \\
&= 0
\end{split}
$$

as expected for a harmonic oscillator.

The expectation value of $\hat{\xi}^{2}$ in the eigenket $\ket{n}$ is:

$$
\begin{split}
\braket{n | \hat{\xi}^{2} | n} &= \frac{1}{2} \left( \braket{n | \hat{a}^{2} | n} + \braket{n | \hat{a}^{\dagger 2} | n} + \braket{n | \hat{a} \hat{a}^{\dagger} | n} + \braket{n | \hat{a}^{\dagger} \hat{a} | n} \right) \\
&= \frac{1}{2} \left( \sqrt{n(n-1)} \braket{n | n - 2} + \sqrt{(n+1)(n+2)} \braket{n | n + 2} + n + 1 + n \right) \\
&= n + \frac{1}{2}
\end{split}
$$

The actual expectation value of the position operator is:

$$
\begin{split}
\braket{\hat{x}} &= l \braket{\hat{\xi}} = 0 \\
\braket{\hat{x}^{2}} &= l^{2} \braket{\hat{\xi}^{2}} = l^{2} \left( n + \frac{1}{2} \right)
\end{split}
$$

For the momentum, note that the dimensionless momentum operator is just the derivative of $\hat{\xi}$:

$$
\frac{\mathrm{d}}{\mathrm{d} \xi} = \frac{1}{\sqrt{2}} \left( \hat{a} - \hat{a}^{\dagger} \right) = i \frac{\hat{p}}{m \omega l}
$$

The expectation values for the dimensionless momentum operators are:

$$
\begin{split}
\braket{n | \frac{\mathrm{d}}{\mathrm{d} \xi} | n} &= \frac{1}{\sqrt{2}} \left( \braket{n | \hat{a} | n} - \braket{n | \hat{a}^{\dagger} | n} \right) = 0 \\
\braket{n | \frac{\mathrm{d}^{2}}{\mathrm{d} \xi^{2}} | n} &= \frac{1}{2} \left( \braket{n | \hat{a} \hat{a}^{\dagger} | n} - \braket{n | \hat{a}^{\dagger} \hat{a} | n} \right) = n + \frac{1}{2}
\end{split}
$$

The expectation values for the actual momentum operators are:

$$
\begin{split}
\braket{\hat{p}} &= 0 \\
\braket{\hat{p}^{2}} &= \left(n + \frac{1}{2} \right) m^{2} \omega^{2} l^{2} = \left( n + \frac{1}{2} \right) \hbar m \omega
\end{split}
$$

These give the standard deviations:

$$
\begin{split}
\Delta x &= \sqrt{\frac{\hbar}{m \omega}} \sqrt{n + 1/2} \\
\Delta p &= \sqrt{\hbar m \omega} \sqrt{n + 1/2}
\end{split}
$$

so that:

$$
\Delta x \Delta p = \hbar \left( n + \frac{1}{2} \right)
$$

The uncertainty principle is satisfied and the ground state $n = 0$ has the minimum uncertainty, i.e., it saturates the inequality.
