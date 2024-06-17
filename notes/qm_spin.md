# Quantum Mechanics - Spin

## Spin-Half Systems

The lowest quantum number for total angular momentum operator $\hat{J}^{2}$ is $j = 1/2$ that correspond to two possible values of $\hat{J}_z$ being $\pm \hbar/2$. We can write the base ket as:

$$
\ket{1/2, \pm 1/2}
$$

which satisfy the eigenvalue equations:

$$
\begin{split}
\hat{J}^{2} \ket{1/2, \pm 1/2} &= \frac{3 \hbar^{2}}{4} \ket{1/2, \pm 1/2} \\
\hat{J}_{z} \ket{1/2, \pm 1/2} &= \pm \frac{\hbar}{2} \ket{1/2, \pm 1/2}
\end{split}
$$

Let us name the ket $\ket{1/2, +1/2}$ as $\ket{+}$ and $\ket{1/2, -1/2}$ as $\ket{-}$. They can also be denoted as column vectors:

$$
\ket{+} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \quad \ket{-} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$

We may express the total angular momentum operator $\hat{J}$ in the angular momentum representation:

$$
(\hat{J}_{i})_{ab} = \braket{a | \hat{J}_{i} | b}
$$

where $a$ and $b$ take the values $+$ and $-$.

It is easy to show that $\hat{J}_{i}$ are the Pauli matrices up to a factor of $\hbar/2$:

$$
\hat{J}_{i} = \frac{\hbar}{2} \sigma_{i}
$$

where $\sigma_{i}$ are defined as:

$$
\sigma_{x} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \quad \sigma_{y} = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \quad \sigma_{z} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

The Pauli matrices satisfy the commutation relations:

$$
\begin{split}
[\sigma_{i}, \sigma_{j}] &= 2 i \epsilon_{ijk} \sigma_{k} \\
\{\sigma_{i}, \sigma_{j}\} &= 2 \delta_{ij}
\end{split}
$$

## Formal Theory of Spin

The spin angular momentum is defined as the difference between the total angular momentum and the orbital angular momentum:

$$
\mathbf{S} \equiv \mathbf{J} - \mathbf{L}
$$

The Stern-Gerlach experiment shows that position alone is not enough to describe the state of a particle and new quantum numbers are needed. A realistic description of a particle must account for both the spatial degrees of freedom and the internal degrees of freedom. We call the latter part the spin of the particle. To describe such a particle, we can use the base ket:

$$
\ket{\mathbf{x}, s} \equiv \ket{\mathbf{x}} \otimes \ket{s}
$$

where the index $s$ specifies the spin state of the particle.

The total angular momentum $\mathbf{J}$ is still the generator of rotations. Consider two angular momentum operators $\mathbf{J}_1$ and $\mathbf{J}_2$ in different subspaces. The components of the two operators satisfy the commutation relations:

$$
\begin{split}
[\hat{J}_{1i}, \hat{J}_{1j}] &= i \hbar \epsilon_{ijk} \hat{J}_{1k} \\
[\hat{J}_{2i}, \hat{J}_{2j}] &= i \hbar \epsilon_{ijk} \hat{J}_{2k}
\end{split}
$$

whereas a cross commutator vanishes:

$$
[\hat{J}_{1i}, \hat{J}_{2j}] = 0
$$

The infinitesimal rotation operator that affects both subspaces is the product of two rotations on each subspace:

$$
\left( 1 - \frac{i}{\hbar} \delta \phi \hat{J}_{1k} \right) \otimes \left( 1 - \frac{i}{\hbar} \delta \phi \hat{J}_{2k} \right) = 1 - \frac{i}{\hbar} \delta \phi \left( \hat{J}_{1k} \otimes \mathbb{I} + \mathbb{I} \otimes \hat{J}_{2k} \right)
$$

Therefore, we can define the total angular momentum operator as:

$$
\mathbf{J} \equiv \mathbf{J}_{1} \otimes \mathbb{I} + \mathbb{I} \otimes \mathbf{J}_{2}
$$

which is more simply written as $\mathbf{J} = \mathbf{J}_{1} + \mathbf{J}_{2}$.

It is important to note that $\mathbf{J}$ defined this way still obeys the commutation relation that underpins the notion of angular momentum. Any previous results, such as the eigenvalue properties, still hold.

In the current case, we identify $\mathbf{J}_1$ as the orbital angular momentum operator $\mathbf{L}$ and $\mathbf{J}_2$ as the spin angular momentum operator $\mathbf{S}$. We can thus write the general rotation operator as:

$$
D(R) = D_{\text{orb}}(R) \otimes D_{\text{spin}}(R) = \exp \left( - \frac{i}{\hbar} \phi \mathbf{L} \cdot \mathbf{n} \right) \otimes \exp \left( - \frac{i}{\hbar} \phi \mathbf{S} \cdot \mathbf{n} \right)
$$

Consider the simplest $\pm 1/2$ spin system with the base ket:

$$
\ket{\mathbf{x}, \pm} \equiv \ket{\mathbf{x}} \otimes \ket{\pm}
$$

A wave function of a particle can be written as:

$$
\psi_{\pm}(\mathbf{x}) = \braket{\mathbf{x}, \pm | \psi}
$$

Instead of using $\ket{\mathbf{x}}$ for the spatial part, we can employ $\ket{n, l, m}$, which are the eigenstates $\mathbf{L}^2$ and $\hat{L}_z$ with eigenvalues $\hbar^{2} l (l + 1)$ and $\hbar m$ respectively. $n$ is some other quantum number that is usually related to the radial behaviour of the Hamiltonian. Then for the spin part, $\ket{\pm}$ are the eigenstates of $\mathbf{S}^2$ and $\hat{S}_z$ with eigenvalues $3 \hbar^{2}/ 4$ and $\pm \hbar/2$ respectively. We can write the base ket as:

$$
\ket{n, l, m, \pm} \equiv \ket{n, l, m} \otimes \ket{\pm}
$$

This implies that we can expand any state ket in terms of simultaneous eigenstates of $\mathbf{L}^2$, $\hat{L}_z$, $\mathbf{S}^2$ and $\hat{S}_z$. However, this is not the only possible choice of base kets.

## Addition of Angular Momenta

There exist two general choices of base kets in describing a system with two angular momenta. The first choice is the simultaneous eigenstates of $\hat{J}_{1}^{2}$, $\hat{J}_{1z}$, $\hat{J}_{2}^{2}$ and $\hat{J}_{2z}$ denoted as $\ket{j_{1}, j_{2}; m_{1}, m_{2}}$. The four operators obviously commute with each other, and the eigenkets satisfy the eigenvalue equations:

$$
\begin{split}
\hat{J}_{1}^{2} \ket{j_{1}, j_{2}; m_{1}, m_{2}} &= j_{1} (j_{1} + 1) \hbar^{2} \ket{j_{1}, j_{2}; m_{1}, m_{2}} \\
\hat{J}_{1z} \ket{j_{1}, j_{2}; m_{1}, m_{2}} &= m_{1} \hbar \ket{j_{1}, j_{2}; m_{1}, m_{2}} \\
\hat{J}_{2}^{2} \ket{j_{1}, j_{2}; m_{1}, m_{2}} &= j_{2} (j_{2} + 1) \hbar^{2} \ket{j_{1}, j_{2}; m_{1}, m_{2}} \\
\hat{J}_{2z} \ket{j_{1}, j_{2}; m_{1}, m_{2}} &= m_{2} \hbar \ket{j_{1}, j_{2}; m_{1}, m_{2}}
\end{split}
$$

The second choice is the simultaneous eigenstates of $\hat{J}^{2}$, $\hat{J}_{z}$, $\hat{J}_{1}^{2}$ and $\hat{J}_{2}^{2}$ denoted as $\ket{j_{1}, j_{2}; j, m}$. The four operators also commute with each other, and the eigenkets satisfy the eigenvalue equations:

$$
\begin{split}
\hat{J}^{2} \ket{j_{1}, j_{2}; j, m} &= j (j + 1) \hbar^{2} \ket{j_{1}, j_{2}; j, m} \\
\hat{J}_{z} \ket{j_{1}, j_{2}; j, m} &= m \hbar \ket{j_{1}, j_{2}; j, m} \\
\hat{J}_{1}^{2} \ket{j_{1}, j_{2}; j, m} &= j_{1} (j_{1} + 1) \hbar^{2} \ket{j_{1}, j_{2}; j, m} \\
\hat{J}_{2}^{2} \ket{j_{1}, j_{2}; j, m} &= j_{2} (j_{2} + 1) \hbar^{2} \ket{j_{1}, j_{2}; j, m}
\end{split}
$$

Note that while $\hat{J}^{2}$ commutes with $\hat{J}_{z}$, it does not commute with $\hat{J}_{1z}$ or $\hat{J}_{2z}$. This means that it is not possible to simply add $\hat{J}^{2}$ to the first choice of base kets. It is therefore worthwhile to investigate the connection between the two choices of base kets. Consider the transformation:

$$
\ket{j_{1}, j_{2}; j, m} = \sum_{m_{1}, m_{2}} C \ket{j_{1}, j_{2}; m_{1}, m_{2}}
$$

where the summation happens over $m_{1}$ and $m_{2}$ for a fixed set of $j_{1}$ and $j_{2}$ and the coefficients $C$ are given by:

$$
C(j, m; j_{1}, m_{1}, j_{2}, m_{2}) = \braket{j_{1}, j_{2}; m_{1}, m_{2} | j_{1}, j_{2}; j, m}
$$

The coefficients $C(j, m; j_{1}, m_{1}, j_{2}, m_{2})$ form a unitary transformation matrix whose elements are called Clebsch-Gordan coefficients. Since the matrix is unitary and taken as real, its coefficients are symmetric so that:

$$
C(j, m; j_{1}, m_{1}, j_{2}, m_{2}) = \braket{j_{1}, j_{2}; m_{1}, m_{2} | j_{1}, j_{2}; j, m} = \braket{j_{1}, j_{2}; j, m | j_{1}, j_{2}; m_{1}, m_{2}}
$$

A real unitary matrix is orthogonal, so that:

$$
\sum_{j, m} \braket{j_{1}, j_{2}; m_{1}, m_{2} | j_{1}, j_{2}; j, m} \braket{j_{1}, j_{2}; j, m | j_{1}, j_{2}; m_{1}', m_{2}'} = \delta_{m_{1} m_{1}'} \delta_{m_{2} m_{2}'}
$$

We can also write this in terms of $j$ and $m$:

$$
\sum_{m_{1}, m_{2}} \braket{j_{1}, j_{2}; m_{1}, m_{2} | j_{1}, j_{2}; j, m} \braket{j_{1}, j_{2}; j', m' | j_{1}, j_{2}; m_{1}, m_{2}} = \delta_{j j'} \delta_{m m'}
$$

There are some important properties of the Clebsch-Gordan coefficients, the first of which is that $C_{m_{1}, m_{2}}$ is non-zero only if:

$$
\boxed{
m_{1} + m_{2} = m
}
$$

which implies conservation of angular momentum along the $z$-axis.

To see this, consider the equality:

$$
(\hat{J}_{z} - \hat{J}_{1z} - \hat{J}_{2z}) \ket{j_{1}, j_{2}; j, m} = 0
$$

This implies that:

$$
(\hat{J}_{z} - \hat{J}_{1z} - \hat{J}_{2z}) \braket{j_{1}, j_{2}; m_{1}, m_{2} | j_{1}, j_{2}; j, m} = (m - m_{1} - m_{2}) C_{m_{1}, m_{2}} = 0
$$

which gives the desired result.

We can also prove that the coefficients vanish unless:

$$
\boxed{
\left\lvert j_{1} - j_{2} \right\rvert \leq j \leq \left\lvert j_{1} + j_{2} \right\rvert
}
$$

### Recurrence Relations

Consider the action of the raising and lowering operators on the base kets:

$$
\hat{J}_{\pm} \ket{j_{1}, j_{2}; j, m} = \hbar \sqrt{j(j + 1) - m(m \pm 1)} \ket{j_{1}, j_{2}; j, m \pm 1}
$$

On the other hand, $\hat{J}_{\pm} = J_{1\pm} \otimes \mathbb{I} + \mathbb{I} \otimes J_{2\pm}$, so that:

$$
\begin{split}
\hat{J}_{\pm} \ket{j_{1}, j_{2}; j, m} &= (J_{1\pm} + J_{2\pm}) \sum_{m_{1}, m_{2}} C \ket{j_{1}, j_{2}; m_{1}, m_{2}} \\
&= \sum_{m_{1}, m_{2}} C \left( J_{1\pm} \ket{j_{1}, j_{2}; m_{1}, m_{2}} + J_{2\pm} \ket{j_{1}, j_{2}; m_{1}, m_{2}} \right) \\
&= \sum_{m_{1}', m_{2}'} C \hbar \left( \sqrt{j_{1}(j_{1} + 1) - m_{1}'(m_{1}' \pm 1)} \ket{j_{1}, j_{2}; m_{1}' \pm 1, m_{2}'} + \sqrt{j_{2}(j_{2} + 1) - m_{2}'(m_{2}' \pm 1)} \ket{j_{1}, j_{2}; m_{1}', m_{2}' \pm 1} \right)
\end{split}
$$

where we change the summation indices to $m_{1}'$ and $m_{2}'$ at the last step.

We can multiply by $\bra{j_{1}, j_{2}; m_{1}, m_{2}}$. For the first term in the summation, only terms with $m_{1}' = m_{1} \mp 1$ and $m_{2}' = m_{2}$ survive. For the second term, only terms with $m_{1}' = m_{1}$ and $m_{2}' = m_{2} \mp 1$ survive. This gives:

$$
\begin{split}
\sqrt{j(j + 1) - m(m \pm 1)} \braket{j_{1}, j_{2}; m_{1}, m_{2} | j_{1}, j_{2}; j, m \pm 1} &=
\sqrt{j_{1}(j_{1} + 1) - m_{1}(m_{1} \mp 1)} \braket{j_{1}, j_{2}; m_{1} \mp 1, m_{2} | j_{1}, j_{2}; j, m} \\
&+ \sqrt{j_{2}(j_{2} + 1) - m_{2}(m_{2} \mp 1)} \braket{j_{1}, j_{2}; m_{1}, m_{2} \mp 1 | j_{1}, j_{2}; j, m}
\end{split}
$$

Since applying the raising and lowering operators have changed the value of $m$ by $\pm 1$, the nonvanishing condition now becomes $m_{1} + m_{2} = m \pm 1$.
