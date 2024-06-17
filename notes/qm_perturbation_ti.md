# Quantum Mechanics - Time-Independent Perturbation Theory

Consider a time-independent Hamiltonian $H$ that can be split into two parts:

$$
\hat{H} = \hat{H}_{0} + \hat{V}
$$

Here, $\hat{H}_{0}$ is a Hamiltonian for which we know the solutions, i.e., the exact energy eigenvalues and eigenstates have been found such that:

$$
\hat{H}_{0} \ket{n^{(0)}} = E_{n}^{(0)} \ket{n^{(0)}}
$$

The task is to find an approximate solution to the eigenvalue problem for the full Hamiltonian $\hat{H}$:

$$
(\hat{H}_{0} + \hat{V}) \ket{n} = E_{n} \ket{n}
$$

where $\hat{V}$ is known as the perturbation.

It is customary to solve instead a modified equation:

$$
(\hat{H}_{0} + \lambda \hat{V}) \ket{n} = E_{n} \ket{n}
$$

where $\lambda$ is a small real parameter.

The idea is that as $\lambda$ varies from zero to unity, the strength of the perturbation can be controlled and we expect to see the system to transition from the unperturbed $\ket{n^{(0)}}$ to the perturbed $\ket{n}$.

## Perturbation Expansion

Given the solved eigenvalue problem for $\hat{H}_{0}$, we obtain a complete set of eigenstates $\ket{n^{(0)}}$ that satisfy:

$$
\sum_{n} \ket{n^{(0)}} \bra{n^{(0)}} = \mathbb{I}
$$

For the moment, assume that the energy spectrum is not degenerate, i.e., each eigenvalue corresponds to a unique eigenstate. We are interested in the eigenvalue problem:

$$
(\hat{H}_{0} + \lambda \hat{V}) \ket{n} = E_{n} \ket{n}
$$

We write the perturbed eigenstates and eigenvalues as power series in $\lambda$:

$$
\begin{split}
\ket{n} &= \ket{n^{(0)}} + \lambda \ket{n^{(1)}} + \lambda^{2} \ket{n^{(2)}} + \ldots \\
E_{n} &= E_{n}^{(0)} + \lambda E_{n}^{(1)} + \lambda^{2} E_{n}^{(2)} + \ldots
\end{split}
$$

Substituting these expansions into the eigenvalue problem, we obtain a series of equations:

$$
\begin{split}
\hat{H}_{0} \ket{n^{(0)}} &= E_{n}^{(0)} \ket{n^{(0)}} \\
\hat{V} \ket{n^{(0)}} + \hat{H}_{0} \ket{n^{(1)}} &= E_{n}^{(0)} \ket{n^{(1)}} + E_{n}^{(1)} \ket{n^{(0)}} \\
\hat{V} \ket{n^{(1)}} + \hat{H}_{0} \ket{n^{(2)}} &= E_{n}^{(0)} \ket{n^{(2)}} + E_{n}^{(1)} \ket{n^{(1)}} + E_{n}^{(2)} \ket{n^{(0)}} \\
&\vdots
\end{split}
$$

The first equation is just the unperturbed eigenvalue problem. The second equation can be solved by left-multiplying by $\bra{n^{(0)}}$ to obtain:

$$
\bra{n^{(0)}} \hat{V} \ket{n^{(0)}} + \bra{n^{(0)}} \hat{H}_{0} \ket{n^{(1)}} =\bra{n^{(0)}} E_{n}^{(0)} \ket{n^{(1)}} + E_{n}^{(1)}
$$

But we note that $\bra{n^{(0)}} \hat{H}_{0} \ket{n^{(1)}} = \bra{n^{(0)}} E_{n}^{(0)} \ket{n^{(1)}}$, and we can solve for $E_{n}^{(1)}$:

$$
\boxed{
E_{n}^{(1)} = \bra{n^{(0)}} \hat{V} \ket{n^{(0)}}
}
$$

To obtain its corresponding eigenstate $\ket{n^{(1)}}$, left-multiply the second equation by $\bra{m^{(0)}}$ with $m \neq n$:

$$
\begin{split}
    \bra{m^{(0)}} \hat{V} \ket{n^{(0)}} + \bra{m^{(0)}} \hat{H}_{0} \ket{n^{(1)}} &= \bra{m^{(0)}} E_{n}^{(0)} \ket{n^{(1)}} + E_{n}^{(1)} \delta_{mn} \\
    \bra{m^{(0)}} \hat{V} \ket{n^{(0)}} &= (E_{n}^{(0)} - E_{m}^{(0)}) \braket{m^{(0)} | n^{(1)}}
\end{split}
$$

which implies:

$$
\braket{m^{(0)} | n^{(1)}} = \frac{\bra{m^{(0)}} \hat{V} \ket{n^{(0)}}}{E_{n}^{(0)} - E_{m}^{(0)}} = \frac{\hat{V}_{mn}}{E_{n}^{(0)} - E_{m}^{(0)}}
$$

where the right-hand side is the coefficient $\hat{V}_{mn}$ of the perturbation term with respect to the unperturbed eigenstates.

But these are just the coefficients of the expansion of $\ket{n^{(1)}}$ in terms of the unperturbed eigenstates:

$$
\boxed{
\ket{n^{(1)}} = \sum_{m \neq n} c_{m} \ket{m^{(0)}} = \sum_{m \neq n} \frac{\hat{V}_{mn}}{E_{n}^{(0)} - E_{m}^{(0)}} \ket{m^{(0)}}
}
$$

Note that the assumption of non-degeneracy is crucial here for a finite value of the coefficient $c_{m}$. Non-degeneracy also implies that the perturbation matrix is diagonal in the basis of the unperturbed eigenstates.

We can derive a similar expression for the second-order energy correction $E_{n}^{(2)}$:

$$
\boxed{
E_{n}^{(2)} = \sum_{m \neq n} \frac{\left| \hat{V}_{mn} \right|^{2}}{E_{n}^{(0)} - E_{m}^{(0)}}
}
$$

## Degenerate Perturbation Theory

Suppose that part of the energy spectrum has a $g$-fold degeneracy, i.e., there are $g$ different eigenkets, denoted by $\ket{m^{(0)}}$, that all correspond to the same unperturbed eigenvalue $E_{D}^{(0)}$. Technically, this leads to a problem in the previous expansion, as the coefficients:

$$
\braket{m^{(0)} | n^{(1)}} = \frac{\hat{V}_{mn}}{E_{n}^{(0)} - E_{m}^{(0)}}
$$

become singular if $\hat{V}_{mn}$ is non-zero but the denominator is vanishing for the degenerate eigenstates.

Note that the presence of degeneracy in the unperturbed spectrum implies there is a freedom of choice in the basis of the unperturbed eigenstates. The goal is to find a new basis such that $\hat{V}$ is diagonal in this basis, so that $\hat{V}_{mn} = 0$ for $m \neq n$, removing the singularities.

In general, the perturbation by $\hat{V}$ removes the degeneracy in the sense that there will be $g$ perturbed eigenkets all with different energies. Suppose that they form a set of kets $\ket{l}$. Apparently as $l \to 0$, the strength of the perturbation vanishes and $\ket{l} \to \ket{l^{(0)}}$, and the various $\ket{l^{(0)}}$ are eigenkets of $\hat{H}_{0}$ all with the same eigenvalue $E_{m}^{(0)}$. However, the set $\ket{l^{(0)}}$ is not necessarily the same as the set $\ket{m^{(0)}}$ even though both sets of unperturbed eigenkets span the same degenerate subspace, which is denoted as $D$. We can write $\ket{l^{(0)}}$ as a linear combination of the $\ket{m^{(0)}}$ via a unitary transformation $U$:

$$
\ket{l^{(0)}} = \sum_{m \in D} U_{lm} \ket{m^{(0)}} \equiv \sum_{m \in D} \braket{m^{(0)} | l^{(0)}} \ket{m^{(0)}}
$$

where the sum happens over the degenerate subspace $D$.

We wish to find a set $\ket{l^{(0)}}$ such that $\hat{V}$ is diagonal in this basis, i.e., $\ket{l^{(0)}}$ is a diagonalising basis for $\hat{V}$. If the transformation $U$ can be found, the previous results for the non-degenerate case can be applied to the new basis $\ket{l^{(0)}}$. In particular, we find the first order energy correction:

$$
\boxed{
E_{l}^{(1)} = \bra{l^{(0)}} \hat{V} \ket{l^{(0)}}
}
$$

To find the transformation $U$, let us consider a rearrangement of the TISE for $\ket{l}$:

$$
(\hat{H}_{0} + \lambda \hat{V}) \ket{l} = E \ket{l}
$$

Define the projection operator $\hat{P}_{0}$ onto the degenerate subspace $D$ defined by the basis $\ket{m^{(0)}}$:

$$
\hat{P}_{0} = \sum_{m \in D} \ket{m^{(0)}} \bra{m^{(0)}}
$$

Let us apply the projection operator $\hat{P}_{1} = \mathbb{I} - \hat{P}_{0}$, which represents the projection operator onto the remaining states, to the TISE:

$$
\begin{split}
0 &= (E - \hat{H}_{0} - \lambda \hat{V}) (\hat{P}_{0} + \hat{P}_{1}) \ket{l} \\
&= (E - E_{D}^{(0)} - \lambda \hat{V}) \hat{P}_{0} \ket{l} + (E - \hat{H}_{0} - \lambda \hat{V}) \hat{P}_{1} \ket{l}
\end{split}
$$

Now, $\hat{P}_{0} \ket{l}$ is some ket in the degenerate subspace, and $\hat{P}_{1} \ket{l}$ is some ket in the non-degenerate subspace. Therefore, we must have $\hat{P}_{0} \hat{P}_{1} \ket{l} = \hat{P}_{1} \hat{P}_{0} \ket{l} = 0$. Let us apply $\hat{P}_{0}$ to the left of the equation. The only surviving term of the second part involves $-\lambda \hat{V} \hat{P}_{1} \ket{l}$:

$$
(E - E_{D}^{(0)} - \lambda \hat{P}_{0} \hat{V}) \hat{P}_{0} \ket{l} - \lambda \hat{P}_{0} \hat{V} \hat{P}_{1} \ket{l} = 0
$$

By the same logic, applying $\hat{P}_{1}$ to the left yields:

$$
-\lambda \hat{P}_{1} \hat{V} \hat{P}_{0} \ket{l} + (E - \hat{H}_{0} - \lambda \hat{P}_{1} \hat{V}) \hat{P}_{1} \ket{l} = 0
$$

We may solve the second equation for $\hat{P}_{1} \ket{l}$:

$$
\hat{P}_{1} \ket{l} = \frac{\lambda}{E - \hat{H}_{0}} \hat{P}_{1} \hat{V} \hat{P}_{0} \ket{l}
$$

## Linear Stark Effect

As an example of the perturbation theory, consider the effect of a uniform electric field on a hydrogen atom. We know that the energy levels of the hydrogen atom only depends on the principal quantum number $n$, whereas the orbital angular momentum quantum number $l$ is allowed to range from $0$ to $n-1$ and the magnetic quantum number $m$ is allowed from $-l$ to $l$. In general, for any level specified by $n$, there are $n^{2}$ degenerate states all with the same energy:

$$
E_{n} = -\frac{E_{R}}{n^{2}}
$$

where $E_{R}$ is the Rydberg energy.

Suppose that the hydrogen atom is perturbed by a uniform electric field in the z-direction, represented by the perturbation:

$$
\hat{V} = e \varepsilon \hat{z}
$$

where $\varepsilon$ is the electric field strength.

Let us focus on the effect of $\hat{V}$ on the first excited state with $n = 2$, i.e., $\ket{2, 0, 0}$, $\ket{2, 1, 0}$, $\ket{2, 1, 1}$ and $\ket{2, 1, -1}$. We first have to construct the $4 \times 4$ matrix with elements $\hat{V}_{mn} = \bra{m^{(0)}} \hat{V} \ket{n^{(0)}}$. To simplify the calculation, note that for any state with a well-defined parity, the expectation value of $\hat{z}$, or indeed any component of $\hat{\mathbf{r}}$, is zero. Therefore, the only non-zero elements of $\hat{V}_{mn}$ are between states with opposite parities. In the present case, these are between $l = 1$ and $l = 0$ states. The matrix is then:

$$
\hat{V} =
\begin{pmatrix}
0 & v & 0 & 0 \\
v & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix}
$$

where we define the element $v$ via the integral:

$$
v \equiv \bra{2, 0, 0} \hat{V} \ket{2, 1, 0} = -3 e \varepsilon a_{0}
$$

The eigenvectors of this matrix are:

$$
\frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \end{pmatrix} \quad \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -1 \\ 0 \\ 0 \end{pmatrix} \quad \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix} \quad \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}
$$

with the corresponding eigenvalues:

$$
v \quad -v \quad 0 \quad 0
$$

The eigenvectors form the new basis $\ket{l^{(0)}}$ and the eigenvalues, which are the diagonal elements of $\hat{V}$ expressed in this basis, are the first order energy corrections:

$$
E_{2, 0, 0}^{(1)} = v \quad E_{2, 1, 0}^{(1)} = -v \quad E_{2, 1, 1}^{(1)} = E_{2, 1, -1}^{(1)} = 0
$$

We may hence write down the perturbed energy levels up to first order:

$$
E_{2, 0, 0} = -\frac{E_{R}}{4} - 3 e \varepsilon a_{0} \quad E_{2, 1, 0} = -\frac{E_{R}}{4} + 3 e \varepsilon a_{0} \quad E_{2, 1, 1} = E_{2, 1, -1} = -\frac{E_{R}}{4}
$$

Note that the shift in the energy levels is linear in the electric field strength $\varepsilon$. This is known as the linear Stark effect. One way to interpret this result is to note that the eigenstate combinations do not have well-defined parities, and are thus allowed to have non-vanishing expectation values of $\hat{z}$. This means that they possess a permanent electric dipole moment, and the electric field exerts a torque on the dipole, which shifts the energy levels.

### Quadratic Stark Effect

Let us contrast the above discussion with the case of the ground state with $n = 1$, i.e., $\ket{1, 0, 0}$. In this case, the perturbation matrix has only one element:

$$
E_{1, 0, 0}^{(1)} = \bra{1, 0, 0} \hat{V} \ket{1, 0, 0} = 0
$$

since $\ket{1, 0, 0}$ has a well-defined parity.

This means that the first order energy correction is zero and the energy shift only manifests at second order:

$$
E_{1, 0, 0}^{(2)} = \sum_{n = 2}^{\infty} \frac{\left| \bra{1, 0, 0} \hat{V} \ket{n, l, m} \right|^{2}}{E_{1} - E_{n}}
$$

The matrix elements are only non-zero for $l = 1$ and $m = 0$, so that:

$$
E_{1, 0, 0}^{(2)} = \sum_{n = 2}^{\infty} \frac{\left| \bra{1, 0, 0} \hat{V} \ket{n, 1, 0} \right|^{2}}{E_{1} - E_{n}} = -C \frac{e^{2} \varepsilon^{2} a_{0}^{2}}{E_{R}}
$$

where $C$ is a numerical constant.

The energy shift is at second order in the electric field strength, and is known as the quadratic Stark effect. This is because the ground state is spherically symmetric and has no permanent electric dipole moment. The electric field has to first interact with the atom to induce a dipole moment, and then exert a torque on the dipole, leading to a much weaker second order effect. In fact, we may evaluate $C = 9/4$ by summing the series of integrals, and we find the ground-state polarisability:

$$
\chi = 2 \frac{\Delta E}{\varepsilon^{2}} = \frac{9}{2} \frac{e^{2} a_{0}^{2}}{E_{R}}
$$

## Zeeman Effect

Consider a hydrogen atom in the presence of a uniform magnetic field $\mathbf{B} = B \hat{z}$, which can be represented by the perturbation in the form of a vector potential:

$$
A = \frac{1}{2} (\mathbf{B} \times \mathbf{r}) = \frac{1}{2} B (-y \hat{x} + x \hat{y})
$$

The Hamiltonian for the system is given by the substitution of the canonical momentum $\hat{p}$ with the mechanical momentum $\hat{\Pi} = \hat{p} - q \mathbf{A}$:

$$
\begin{split}
    \hat{H} &= \frac{1}{2m_{e}} \hat{\Pi}^{2} - \frac{e^{2}}{4\pi \epsilon_{0} r} \\
    &= \frac{1}{2m_{e}} \hat{p}^{2} - \frac{e}{m_{e}} \hat{p} \cdot \mathbf{A} + \frac{e^{2}}{2m_{e}} \mathbf{A}^{2} - \frac{e^{2}}{4\pi \epsilon_{0} r}
\end{split}
$$

We identify the perturbation as the two middle terms:

$$
\begin{split}
\hat{V} &= -\frac{e}{m_{e}} \hat{p} \cdot \mathbf{A} + \frac{e^{2}}{2m_{e}} \mathbf{A}^{2} \\
&= -\frac{e}{2m_{e}} \hat{p} \cdot (\mathbf{B} \times \hat{r}) + \frac{e^{2}}{8m_{e}} B^{2} (\hat{x}^{2} + \hat{y}^{2}) \\
&= -\frac{e}{2m_{e}} \mathbf{B} \cdot (\hat{r} \times \hat{p}) + \frac{e^{2}}{8m_{e}} B^{2} (\hat{x}^{2} + \hat{y}^{2}) \\
&= -\frac{e}{2m_{e}} B \hat{L}_{z} + \frac{e^{2}}{8m_{e}} B^{2} (\hat{x}^{2} + \hat{y}^{2})
\end{split}
$$

where we have used the orbital angular momentum operator $\hat{L} = \hat{r} \times \hat{p}$.

The effect of the second term is very small compared to the first term, and can be neglected. Focusing on the first term, let us consider a state with non-zero $l$, denoted as $\ket{n, l, m}$. Due to the apparent degeneracy, we first consider the matrix elements of $\hat{V}$ in the basis of the unperturbed eigenstates:

$$
\begin{split}
\bra{n_{1}, l_{1}, m_{1}} \hat{V} \ket{n_{2}, l_{2}, m_{2}} &= -\frac{eB}{2m_{e}} \bra{n_{1}, l_{1}, m_{1}} \hat{L}_{z} \ket{n_{2}, l_{2}, m_{2}} \\
&= -\frac{eB\hbar}{2m_{e}} m_{1} \delta_{n_{1}n_{2}} \delta_{l_{1}l_{2}} \delta_{m_{1}m_{2}}
\end{split}
$$

which is already diagonal in the basis of the unperturbed eigenstates.

The first order energy correction is then:

$$
E_{n, l, m}^{(1)} = -\frac{eB\hbar}{2m_{e}} m
$$

which is called the Zeeman effect.
