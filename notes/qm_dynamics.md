# Quantum Mechanics - Dynamics

## Time Evolution of a State

In quantum mechanics, time is treated as a parameter, not an operator. In particular, time is not an observable that can be measured (as opposed to position and momentum).

Suppose that we have a state $\ket{\psi, t_{0}}$ at time $t_{0}$. After some time, the state evolves to $\ket{\psi, t}$, where $t > t_{0}$. We can propose a time-evolution operator $\hat{U}(t, t_{0})$ such that:

$$
\ket{\psi, t} = \hat{U}(t, t_{0}) \ket{\psi, t_{0}}
$$

To find the form of $\hat{U}(t, t_{0})$, several conditions, similar to those for the translation operator, can be imposed. Firstly, we require after the action of $U$, the state is still normalized. This is equivalent to requiring that $U$ is unitary:

$$
\hat{U}^{\dagger} \hat{U} = \mathbb{I}
$$

We also need the composition of two time-evolution operators to be the same as a single time-evolution operator:

$$
\hat{U}(t_{2}, t_{1}) \hat{U}(t_{1}, t_{0}) = \hat{U}(t_{2}, t_{0})
$$

Consider the infinitesimal time-evolution $\hat{U}(t_{0} + \mathrm{d}t, t_{0})$. We expect it to reduce to the identity operator when $\mathrm{d}t \rightarrow 0$:

$$
\lim_{\mathrm{d}t \rightarrow 0} \hat{U}(t_{0} + \mathrm{d}t, t_{0}) = \mathbb{I}
$$

It can be easily verified that, in the limit of an infinitesimal $\mathrm{d}t$, a possible form of the time-evolution operator is:

$$
\hat{U}(t_{0} + \mathrm{d}t, t_{0}) =  1 - i \Omega \mathrm{d}t
$$

where $\Omega$ is a Hermitian operator.

It turns out the physical interpretation of $\Omega$ is the Hamiltonian operator $\hat{H}$ up to a constant factor:

$$
\Omega = \frac{\hat{H}}{\hbar}
$$

so that the infinitesimal time-evolution operator becomes:

$$
\hat{U}(t_{0} + \mathrm{d}t, t_{0}) =  1 - \frac{i}{\hbar} \hat{H} \mathrm{d}t
$$

Consider the composition property of the time-evolution operator. Let $t_{1} = t$ and $t_{2} = t + \mathrm{d}t$. Then:

$$
\hat{U}(t + \mathrm{d}t, t_{0}) = U(t + \mathrm{d}t, t) \hat{U}(t, t_{0}) = \left(1 - \frac{i}{\hbar} \hat{H} \mathrm{d}t \right) \hat{U}(t, t_{0})
$$

Rearranging, we have:

$$
\hat{U}(t + \mathrm{d}t, t_{0}) - \hat{U}(t, t_{0}) = - \frac{i}{\hbar} \hat{H} \mathrm{d}t \hat{U}(t, t_{0})
$$

which results in the differential equation:

$$
\boxed{
i\hbar \frac{\partial}{\partial t} \hat{U}(t, t_{0}) = \hat{H} \hat{U}(t, t_{0})
}
$$

This is the Schrödinger equation for the time-evolution operator. Applying the Schrödinger equation to the state $\ket{\psi, t_{0}}$, we have:

$$
\boxed{
i\hbar \frac{\partial}{\partial t} \ket{\psi, t} = \hat{H} \ket{\psi, t}
}
$$

which is the Schrödinger equation that describes the time evolution of a state.

If the equation pertaining the time-evolution operator is solved, there would be no need to solve the actual Schrödinger equation as we can simply apply the time-evolution operator to the initial state to obtain the state at any time $t$. To solve the time-evolution operator equation, we consider several cases.

### Time-Independent Hamiltonian

If the Hamiltonian is time-independent, then any finite time-evolution operator can be written as a product of infinitesimal time-evolution operators:

$$
\hat{U}(t, t_{0}) = \lim_{N \rightarrow \infty} \left(1 - \frac{i}{\hbar} \hat{H} \frac{t - t_{0}}{N} \right)^{N} = \exp \left[- \frac{i}{\hbar} \hat{H} (t - t_{0}) \right]
$$

where the limit holds as $\hat{H}$ does not change with time.

In the special case where $t_{0} = 0$, the time-evolution operator is:

$$
\boxed{
\hat{U}(t) = \exp \left(- \frac{i}{\hbar} \hat{H} t \right)
}
$$

### Time-Dependent Hamiltonian

If the Hamiltonian is time-dependent but the $\hat{H}(t)$ at different times commute, then the time-evolution operator can be written as the formal solution of the time-evolution operator equation:

$$
\hat{U}(t, t_{0}) = \exp \left[- \frac{i}{\hbar} \int_{t_{0}}^{t} \hat{H}(t') \mathrm{d}t' \right]
$$

### Interpretations of the Wave Function

The wave function $\psi(\mathbf{r}, t)$ is a complex-valued function of position and time. The probability density of finding a particle at position $\mathbf{r}$ at time $t$ is given by:

$$
\rho(\mathbf{r}, t) = \left\lvert \psi(\mathbf{r}, t) \right\rvert^{2}
$$

From the Schrödinger equation in position representation, we can derive the continuity equation:

$$
\boxed{
\frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{j} = 0
}
$$

where $\mathbf{j}$ is the probability current:

$$
\boxed{
\mathbf{j} \equiv \frac{\hbar}{2mi} \left( \psi^{*} \nabla \psi - \psi \nabla \psi^{*} \right) = \frac{\hbar}{m} \Im \left( \psi^{*} \nabla \psi \right)
}
$$

## Energy Eigenstates

Consider an operator $\hat{A}$ that commutes with $\hat{H}$ so that they share a common set of eigenkets $\ket{E_{n}}$ which we call the energy eigenkets with eigenvalues $E_{n}$:

$$
\boxed{
\hat{H} \ket{E_{n}} = E_{n} \ket{E_{n}}
}
$$

Since $\hat{A}$ and $\hat{H}$ commute, $\ket{E_{n}}$ are also eigenkets of the former:

$$
\hat{A} \ket{E_{n}} = a_{n} \ket{E_{n}}
$$

The eigenvalue equation for $\hat{H}$ is also called the time-independent Schrödinger equation. The time-evolution operator can be expanded in terms of these eigenkets:

$$
\begin{split}
\exp{\left(- \frac{i}{\hbar} \hat{H} t \right)} &= \sum_{n, j} \ket{E_{n}} \bra{E_{n}} \exp{\left(- \frac{i}{\hbar} \hat{H} t \right)} \ket{E_{j}} \bra{E_{j}} \\
&= \sum_{n} \ket{E_{n}} \bra{E_{n}} \exp{\left(- \frac{i}{\hbar} E_{n} t \right)}
\end{split}
$$

In this form, the time evolution of a state $\ket{\psi, t_{0}}$ can be easily obtained. Suppose that the initial state can be expanded in terms of the energy eigenkets:

$$
\ket{\psi, t_{0}} = \sum_{n} c_{n} \ket{E_{n}}
$$

where $c_{n} = \braket{E_{n} | \psi, t_{0}}$.

Then, the state at time $t$ is:

$$
\begin{split}
\ket{\psi, t} &= \exp{\left(- \frac{i}{\hbar} \hat{H} t \right)} \ket{\psi, t_{0}} \\
&= \sum_{n} c_{n} \exp{\left(- \frac{i}{\hbar} E_{n} t \right)} \ket{E_{n}}
\end{split}
$$

In other words, each coefficient undergoes a phase change according to:

$$
c_{n}(t) = c_{n}(t_{0}) \exp{\left(- \frac{i}{\hbar} E_{n} t \right)}
$$

We therefore arrive at the conclusion that quantum dynamics is reduced to finding an observable that commutes with $\hat{H}$ and evaluating its eigenvalues. Once this is done, the time evolution of any ket can be done by expressing it as a superposition of energy eigenkets. We call an observable that commutes with a certain Hamiltonian a **good quantum number**.

## Schrödinger's Equation in Position Representation

Applying a bra $\bra{x}$ to the Schrödinger equation, we have its position representation:

$$
i\hbar \frac{\partial}{\partial t} \braket{x | \psi, t} = \braket{x | \hat{H} | \psi, t}
$$

If the Hamiltonian has the form:

$$
\hat{H} = \frac{\hat{p}^{2}}{2m} + V(x)
$$

then the Schrödinger equation becomes:

$$
\boxed{
i\hbar \frac{\partial \psi(x, t)}{\partial t} = -\frac{\hbar^{2}}{2m} \frac{\partial^{2} \psi(x, t)}{\partial x^{2}} + V(x) \psi(x, t)
}
$$

Similarly, the time-independent Schrödinger equation becomes:

$$
\boxed{
\left[-\frac{\hbar^{2}}{2m} \frac{\partial^{2}}{\partial x^{2}} + V(x) \right] \psi(x) = E \psi(x)
}
$$

## Schrödinger and Heisenberg Pictures

In the aforementioned discussion, we have been using the Schrödinger picture, where the concept of time development is realised with the time-evolution operator. The operators corresponding to observables like position and momentum are fixed in time while the state evolves in time:

$$
\ket{\psi} \to \hat{U} \ket{\psi}
$$

The time evolution is unitary so that inner products are preserved:

$$
\braket{\psi_{1} | \psi_{2}} \to \braket{\psi_{1} | \hat{U}^{\dagger} \hat{U} | \psi_{2}} = \braket{\psi_{1} | \psi_{2}}
$$

Observables, however, are in general not preserved:

$$
\braket{\psi | \hat{A} | \psi} \to \braket{\psi | \hat{U}^{\dagger} \hat{A} \hat{U} | \psi}
$$

On the one hand, we can interpret this as the state evolving from $\ket{\psi}$ to $\hat{U} \ket{\psi}$ while the observable $\hat{A}$ remains fixed. On the other hand, we can interpret this as the observable $\hat{A}$ evolving according to:

$$
\hat{A} \to \hat{U}^{\dagger} \hat{A} \hat{U}
$$

This is called the Heisenberg picture, where the state is fixed in time while the operators evolve in time. Consider some operator in Schrödinger picture $\hat{A}_{S}$. The corresponding operator in Heisenberg picture is:

$$
\hat{A}_{H}(t) = \hat{U}^{\dagger}(t) \hat{A}_{S} \hat{U}(t)
$$

We can derive the time evolution of $\hat{A}_{H}(t)$ by differentiating it with respect to time. Assuming that $\hat{A}_{S}$ does not depend on time, we have:

$$
\begin{split}
\frac{\mathrm{d}}{\mathrm{d}t} \hat{A}_{H}(t) &= \frac{\partial \hat{U}^{\dagger}}{\partial t} \hat{A}_{S} \hat{U} + \hat{U}^{\dagger} \hat{A}_{S} \frac{\partial \hat{U}}{\partial t} \\
&= -\frac{1}{i\hbar} \hat{U}^{\dagger} \hat{H} \hat{A}_{S} \hat{U} + \frac{1}{i\hbar} \hat{U}^{\dagger} \hat{A}_{S} \hat{H} \hat{U} \\
&= -\frac{1}{i\hbar} \hat{U}^{\dagger} \hat{H} \hat{U} \hat{U}^{\dagger} \hat{A}_{S} \hat{U} + \frac{1}{i\hbar} \hat{U}^{\dagger} \hat{A}_{S} \hat{U} \hat{U}^{\dagger} \hat{H} \hat{U} \\
&= -\frac{1}{i\hbar} \hat{U}^{\dagger} \hat{H} \hat{U} \hat{A}_{H}(t) + \frac{1}{i\hbar} \hat{A}_{H}(t) \hat{U}^{\dagger} \hat{H} \hat{U} \\
&= \frac{1}{i\hbar} [A_{H}, \hat{U}^{\dagger} \hat{H} \hat{U}]
\end{split}
$$

where we have used the Schrödinger equation for the time-evolution operator.

However, the operator $\hat{U}^{\dagger} \hat{H} \hat{U}$ is just $\hat{H}$ since $\hat{H}$ commutes with $\hat{U}$. Therefore, we have:

$$
\boxed{
\frac{\mathrm{d}}{\mathrm{d}t} \hat{A}_{H}(t) = \frac{1}{i\hbar} [\hat{A}_{H}(t), \hat{H}]
}
$$

This is known as the Heisenberg equation of motion. It is a generalisation of the Ehrenfest theorem. If we take the expectation value of the Heisenberg equation of motion, we have:

$$
\frac{\mathrm{d}}{\mathrm{d}t} \braket{\psi | \hat{A}_{H}(t) | \psi} = \frac{1}{i\hbar} \braket{\psi | [\hat{A}_{H}(t), \hat{H}] | \psi}
$$

which implies that the expectation value of the observable $\hat{A}_{H}(t)$ is conserved if the observable commutes with the Hamiltonian.
