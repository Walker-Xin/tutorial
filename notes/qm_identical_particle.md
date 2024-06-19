# Quantum Mechanics - Identical Particles

## Permutation Symmetry

Consider a system of two particles, one characterised by the quantum number $k$ and the other by $k'$. We write the state ket of the system as:

$$
\ket{\psi} = \ket{k'} \otimes \ket{k''} = \ket{k'} \ket{k''}
$$

which is understood to be a tensor product representing the first particle in the state $\ket{k'}$ and the second particle in $\ket{k''}$.

Consider the state $\ket{\psi'}$ obtained by swapping the two particles:

$$
\ket{\psi'} = \ket{k''} \ket{k'}
$$

which represents the first particle in the state $\ket{k''}$ and the second particle in $\ket{k'}$.

We define the permutation operator $\hat{P}$ as the operator that swaps the two particles:

$$
\hat{P} \ket{k'} \ket{k''} = \ket{k''} \ket{k'}
$$

Clearly, $\hat{P}^2 = \hat{I}$ so that the eigenvalues of $\hat{P}$ are $\pm 1$. Consider a system of two identical particles. The observables, such as position, momentum, must appear symmetrically in the Hamiltonian. For example:

$$
\hat{H} = \frac{\hat{p}_{1}^{2}}{2m} + \frac{\hat{p}_{2}^{2}}{2m} + V(\hat{r}_{1}, \hat{r}_{2}) + \hat{V}_{1}(r_{1}) + \hat{V}_{2}(r_{2})
$$

We see that $\hat{H}\hat{P} = \hat{P}\hat{H}$, which implies that the Hamiltonian commutes with the permutation operator so that a symmetric state remains symmetric at all times.

Consider the eigenstates of the permutation operator $\hat{P}$. We have two possibilities:

$$
\begin{split}
\ket{k' k''}_{+} &= \frac{1}{\sqrt{2}} \left( \ket{k'} \ket{k''} + \ket{k''} \ket{k'} \right) \\
\ket{k' k''}_{-} &= \frac{1}{\sqrt{2}} \left( \ket{k'} \ket{k''} - \ket{k''} \ket{k'} \right)
\end{split}
$$

We can define the symmetriser and antisymmetriser operators:

$$
\begin{split}
\hat{S} &= \frac{1}{\sqrt{2}} \left( \hat{I} + \hat{P} \right) \\
\hat{A} &= \frac{1}{\sqrt{2}} \left( \hat{I} - \hat{P} \right)
\end{split}
$$

Applying the symmetriser/antisymmetriser operators to a state necessarily gives a symmetric/antisymmetric state.

## Particle Exchange

A system containing $N$ identical particles are either totally symmetric or totally antisymmetric under particle exchange. The former are called bosons and the latter fermions. They satisfy the following properties:

$$
\begin{split}
\hat{P}_{ij} \ket{\text{N identical bosons}} &= \ket{\text{N identical bosons}} \\
\hat{P}_{ij} \ket{\text{N identical fermions}} &= -\ket{\text{N identical fermions}}
\end{split}
$$

meaning that bosons correspond to $+1$ eigenvalues of the permutation operator and fermions correspond to $-1$ eigenvalues.

Fermions suffer from the Pauli exclusion principle, which states that no two fermions can occupy the same quantum state. Bosons, on the other hand, can occupy the same quantum state.

Consider a system of two identical particles. For a system of Fermions, the state must be antisymmetric with only one possible state:

$$
\ket{\psi} = \frac{1}{\sqrt{2}} \left( \ket{k'} \ket{k''} - \ket{k''} \ket{k'} \right)
$$

which is called a singlet state.

For a system of Bosons, the state must be symmetric with three choices:

$$
\begin{split}
\ket{\psi} &= \frac{1}{\sqrt{2}} \left( \ket{k'} \ket{k''} + \ket{k''} \ket{k'} \right) \\
\ket{\psi} &= \ket{k'} \ket{k''} \\
\ket{\psi} &= \ket{k''} \ket{k'}
\end{split}
$$

which are called triplet states.

## Two-Electron System
