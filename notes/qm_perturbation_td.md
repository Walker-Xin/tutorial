# Quantum Mechanics - Time-Dependent Perturbation Theory

Many quantum mechanical systems are described by a Hamiltonian that contains some time dependence. For any general problem, we would like to solve the time-dependent Schrödinger equation:

$$
i\hbar\frac{\partial}{\partial t}\ket{\psi(t)} = \hat{H}(t)\ket{\psi(t)}
$$

If $\hat{H}$ is time-independent, this equation is solved by determining the time evolution operator:

$$
\hat{U}(t, t_{0}) = \exp \left[- \frac{i}{\hbar} \hat{H} (t - t_{0}) \right]
$$

and then apply it to the energy eigenstates of the Hamiltonian, which are solutions to the TDSE.

Note that for a time-independent Hamiltonian, the time evolution does not change the energy eigenstates, who are hence called stationary states. However, if the Hamiltonian is time-dependent, the problem is no longer stationary and one energy eigenstate can evolve into another. Let us consider a time-dependent Hamiltonian of the form:

$$
\hat{H}(t) = \hat{H}_{0} + \hat{V}(t)
$$

where $\hat{H}_{0}$ is a time-independent Hamiltonian that has been solved and $\hat{V}(t)$ is a time-dependent perturbation.

Suppose that at time $t = 0$, the system is in a state:

$$
\ket{\psi(0)} = \sum_{n} c_{n}(0) \ket{n}
$$

where $\ket{n}$ are the energy eigenstates of $\hat{H}_{0}$ and $c_{n}(0) = \braket{n | \psi}$.

We wish to find $c_{n}(t)$ for $t > 0$, such that:

$$
\ket{\psi(t)} = \sum_{n} c_{n}(t) \exp \left( - \frac{i}{\hbar} E_{n} t \right) \ket{n}
$$

This expression implies that the effect of $\hat{V}(t)$ is solely to change the coefficients $c_{n}(t)$, since without $\hat{V}$, the coefficients would remain as $c_{n}(0)$. There is no restriction imposed on $\psi(t)$ since $\ket{n}$ form a complete set of states. Substituting this expression into the TDSE, we obtain:

$$
\begin{split}
i\hbar\frac{\partial}{\partial t}\ket{\psi(t)} &= (\hat{H}_{0} + \hat{V})\ket{\psi(t)} \\
\sum_{n} \left( i\hbar \frac{\partial c_{n}}{\partial t} + c_{n} E_{n} \right) \exp \left( - \frac{i}{\hbar} E_{n} t \right) \ket{n} &= \sum_{n} c_{n} E_{n} \exp \left( - \frac{i}{\hbar} E_{n} t \right) \ket{n} + \sum_{n} c_{n} \exp \left( - \frac{i}{\hbar} E_{n} t \right) \hat{V}\ket{n} \\
\sum_{n} i\hbar \frac{\partial c_{n}}{\partial t} \exp \left( - \frac{i}{\hbar} E_{n} t \right) \ket{n} &= \sum_{n} c_{n} \exp \left( - \frac{i}{\hbar} E_{n} t \right) \hat{V}\ket{n}
\end{split}
$$

We may left-multiply by $\bra{m}$ and move the exponential factor to the right-hand side:

$$
i\hbar \frac{\partial c_{m}}{\partial t} = \sum_{n} c_{n} \exp \left[ -\frac{i}{\hbar} (E_{n} - E_{m}) t \right] \braket{m | \hat{V} | n}
$$

This constitute a set of coupled first-order differential equations for the coefficients $c_{n}(t)$ to be solved under the initial condition $c_{n}(0)$. Exact solutions to these equations are difficult to obtain, but we can obtain approximate solutions under certain regimes.

## Sudden Approximation

If a Hamiltonian changes very rapidly, the system 'does not have time' to adjust to the change and the system remains in the same state while it 'enters' the new Hamiltonian. In particular, let us consider the following time-dependent Hamiltonian:

$$
\hat{H}(t) =
\begin{cases}
\hat{H}_{i} & \text{for } t < 0 \\
\hat{H}_{f} & \text{for } t \geq 0
\end{cases}
$$

where $\hat{H}_{i}$ and $\hat{H}_{f}$ are both time-independent.

Even if the system starts in some stationary state of $\hat{H}_{i}$, there is no guarantee that it will remain in a stationary state of $\hat{H}_{f}$. Suppose that the system starts in some arbitrary state $\ket{\psi(0)}$. After the sudden change, the state of the system is still $\ket{\psi(0)}$ which is to be expressed in terms of the energy eigenstates of $\hat{H}_{f}$:

$$
\ket{\psi(0)} = \sum_{n} \braket{n | \psi(0)} \ket{n}
$$

where $\ket{n}$ are energy eigenstates of $\hat{H}_{f}$ that satisfy:

$$
\hat{H}_{f}\ket{n} = E_{n}\ket{n}
$$

The state evolves according to the time evolution operator associated with $\hat{H}_{f}$:

$$
\ket{\psi(t)} = \hat{U}_{f}(t, 0) \ket{\psi(0)} = \sum_{n} \braket{n | \psi(0)} \exp \left( -\frac{i}{\hbar} E_{n} t \right) \ket{n}
$$

## Adiabatic Approximation

## Perturbation Theory

Since the full set of solutions are difficult to obtain, it is often the case that we can only obtain approximate solutions in the form of a series expansion:

$$
c_{n}(t) = c_{n}^{(0)}(t) + c_{n}^{(1)}(t) + c_{n}^{(2)}(t) + \ldots
$$

We restrict ourselves to a single 'pure' state $\ket{\psi(0)} = \ket{j}$, which means that $c_{n}(0) = \delta_{jn}$. We are interested in finding out how $\ket{j}$ evolves into other energy eigenstates. In the zero-order solution, $\hat{V}$ is zero and the solution is just $c_{n}^{0}(t) = \delta_{jn}$ for all $t$. The first order result is obtained by substituting the zero-order solution into the above equation:

$$
i\hbar \frac{\partial c_{m}}{\partial t} \approx \sum_{n} \delta_{jn} \exp \left[ -\frac{i}{\hbar} (E_{n} - E_{m}) t \right] \braket{m | \hat{V} | n} = \exp \left[ -\frac{i}{\hbar} (E_{j} - E_{m}) t \right] \braket{m | \hat{V} | j}
$$

This can be integrated to obtain a first-order correction to the coefficients $c_{m}(t)$:

$$
c_{m}^{(1)}(t) = -\frac{i}{\hbar} \int_{0}^{t} \exp \left( i \omega_{mj} t' \right) V_{mj}(t) \, \mathrm{d}t'
$$

where we define $\omega_{mj} = (E_{m} - E_{j})/\hbar$ and the matrix elements $V_{mj}(t) = \braket{m | \hat{V} | j}$.

Similarly, we can substitute the first-order solution into the equation to obtain the second-order correction:

$$
c_{m}^{(2)}(t) = \left( -\frac{i}{\hbar} \right)^{2} \sum_{k} \int_{0}^{t} \exp \left( i \omega_{mk} t' \right) V_{mk}(t') \left[ \int_{0}^{t'} \exp \left( i \omega_{kj} t'' \right) V_{kj}(t'') \, \mathrm{d}t'' \right] \, \mathrm{d}t'
$$

We also define the transition probability from state $\ket{j}$ to state $\ket{m}$ with $m \neq j$ as:

$$
\boxed{
P_{j \to m} = \left| c_{m}^{(1)}(t) + c_{m}^{(2)}(t) + \ldots \right|^{2}
}
$$

## Periodic Perturbations

Often the perturbation can be modelled as a periodic function of time:

$$
\hat{V}(t) = \hat{V}_{0} e^{-i\omega t}
$$

where $\hat{V}_{0}$ is a time-independent operator.

The first-order correction $c_{m}^{(1)}(t)$ can be solved:

$$
\begin{split}
c_{m}^{(1)}(t) &= -\frac{i}{\hbar} \int_{0}^{t} \exp \left[ -\frac{i}{\hbar} (E_{j} - E_{m}) t' \right] \braket{m | \hat{V} | j} \, \mathrm{d}t' \\
&= -\frac{i}{\hbar} \int_{0}^{t} \exp \left[ i(\omega_{mj} - \omega) t' \right] \braket{m | \hat{V}_{0} | j} \, \mathrm{d}t' \\
&= -\frac{1}{\hbar} \braket{m | \hat{V}_{0} | j} \frac{\exp \left[ i(\omega_{mj} - \omega) t \right] - 1}{\omega_{mj} - \omega}
\end{split}
$$

We can compute the transition probability based on a first-order correction:

$$
P_{j \to m} = \left| c_{m}^{(1)}(t) \right|^{2} = \frac{1}{\hbar^{2}} \left| \braket{m | \hat{V}_{0} | j} \right|^{2} \frac{\sin^{2}{[(\omega_{mj} - \omega) t/2]}}{[(\omega_{mj} - \omega)/2]^{2}}
$$

The square of the sinc function is sharply peaked at $\omega_{mj} = \omega$. In fact, for large $t$, the function can be approximated as a delta function:

$$
\lim_{t \to \infty} \frac{\sin^{2}{[(\omega_{mj} - \omega) t/2]}}{[(\omega_{mj} - \omega)/2]^{2}} = 2\pi t \delta(\omega_{mj} - \omega)
$$

Then the transition probability becomes:

$$
P_{j \to m} = \frac{2\pi}{\hbar} t \left| \braket{m | \hat{V}_{0} | j} \right|^{2} \delta(\omega_{mj} - \omega)
$$

Omitting the time factor, we define the transition rate as the probability per unit time:

$$
W_{j \to m} = \frac{2\pi}{\hbar} \left| \braket{m | \hat{V}_{0} | j} \right|^{2} \delta(\omega_{mj} - \omega)
$$

Note that with $\omega > 0$, the time dependence $\hat{V}(t) = \hat{V}_{0} e^{-i\omega t}$ is a perturbation that drives the system from state $\ket{j}$ to some higher energy state $\ket{m}$, since we have $\omega_{mj} = (E_{m} - E_{j})/\hbar > 0$. Vice versa, with $\omega < 0$, the perturbation drives the system to some lower energy state.
