# Quantum Mechanics - Variational Methods

While the perturbation theory is powerful, it is not helpful if the exact solution to the original Hamiltonian is not known. In such cases, we can employ similar methods used in perturbation theory to approximate the ground state energy and wave function of the unperturbed Hamiltonian. This is known as the variational method.

Consider a trail ket $\ket{\tilde{0}}$ that is a guess for the actual ground state $\ket{0}$ of the Hamiltonian $\hat{H}$. Let us define the quantity:

$$
\bar{H} = \frac{\braket{\tilde{0}|\hat{H}|\tilde{0}}}{\braket{\tilde{0}|\tilde{0}}}
$$

where we allow the possibility that $\ket{\tilde{0}}$ is not normalised.

We now attempt to show that $\bar{H}$ is an upper bound to the ground state energy of the Hamiltonian $\hat{H}$, that is:

$$
\bar{H} \geq E_0
$$

To do this, we can always write $\ket{\tilde{0}}$ as a linear combination of the eigenkets of $\hat{H}$:

$$
\ket{\tilde{0}} = \sum_{n} \braket{n|\tilde{0}}\ket{n}
$$

where $\ket{n}$ satisfies the eigenvalue equation:

$$
\hat{H}\ket{n} = E_{n}\ket{n}
$$

We can then write:

$$
\begin{split}
\bar{H} &= \frac{\braket{\tilde{0}|\hat{H}|\tilde{0}}}{\braket{\tilde{0}|\tilde{0}}} \\
&= \frac{\sum_{n} \braket{\tilde{0}|\hat{H}|n}\braket{n|\tilde{0}}}{\sum_{n} \braket{\tilde{0}|n}\braket{n|\tilde{0}}} \\
&= \frac{\sum_{n} E_{n}|\braket{n|\tilde{0}}|^2}{\sum_{n} |\braket{n|\tilde{0}}|^2}
\end{split}
$$

We may write $E_{k} = E_{k} - E_{0} + E_{0}$ and note that $E_{k} - E_{0} \geq 0$ for all $k$, which can always be done if we arrange the eigenvalues in ascending order. We then have:

$$
\begin{split}
\bar{H} &= \frac{\sum_{n} (E_{n} - E_{0} + E_{0})|\braket{n|\tilde{0}}|^2}{\sum_{n} |\braket{n|\tilde{0}}|^2} \\
&= \frac{\sum_{n} (E_{n} - E_{0})|\braket{n|\tilde{0}}|^2}{\sum_{n} |\braket{n|\tilde{0}}|^2} + E_{0} \\
&\geq E_{0}
\end{split}
$$

We thus establish an upper bound $\bar{H}$ to the true ground state energy $E_{0}$, given any trial ket $\ket{\tilde{0}}$. Even a relatively poor guess for $\ket{\tilde{0}}$ can give a reasonable upper bound to the ground state energy. To see this, suppose that the error in $\ket{\tilde{0}}$ is of linear order in some small parameter $\epsilon$, that is:

$$
\braket{n|\tilde{0}} \sim O(\epsilon)
$$

for $n \neq 0$.

Then from the above expression for $\bar{H}$, we have see that $\bar{H} - E_{0} \sim O(\epsilon^2)$, so that $\bar{H}$ is at least a second order approximation to the ground state energy. In practice, we characterise the trail ket via one or more parameters $\lambda_{1}, \lambda_{2}, \ldots$ and then attempt to minimise $\bar{H}$ with respect to these parameters:

$$
\frac{\partial \bar{H}}{\partial \lambda_{i}} = 0
$$

However, the method per se does not inform us how to choose a good trial ket $\ket{\tilde{0}}$, which often is a problem of physical intuition.
