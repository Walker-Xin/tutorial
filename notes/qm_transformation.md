# Quantum Mechanics - Transformations

Broadly speaking, a transformation changes the state $\ket{\psi}$ of the a system to a new one. There are, however, certain transformations that do not change the physical properties of the state. Such transformations represent **symmetries** of the system. Such symmetries are extremely important as they provide information about the problem without having to solve it.

## Translations

Consider an active translation by a small vector $\mathbf{a}$ of a system from $\mathbf{x}$ to $\mathbf{x}' = \mathbf{x} + \mathbf{a}$. The state of the system changes from $\ket{\psi}$ to $\ket{\psi'}$. We can formally write:

$$
\ket{\psi'} = f(\mathbf{a}) \ket{\psi}
$$

Let $f(\mathbf{a})$ act on a position eigenstate $\ket{\mathbf{x}}$:

$$
\ket{\mathbf{x}} \to f(\mathbf{a}) \ket{\mathbf{x}} = \ket{\mathbf{x} + \mathbf{a}}
$$

We can expand the new state in terms of the momentum eigenstates:

$$
\begin{split}
\ket{\mathbf{x} + \mathbf{a}} &= \int \ket{\mathbf{p}} \braket{\mathbf{p} | \mathbf{x} + \mathbf{a}} \, \mathrm{d}\mathbf{p} \\
&= \left( \frac{1}{2\pi \hbar} \right)^{3/2} \int \ket{\mathbf{p}} \exp{\left( -\frac{i}{\hbar} \mathbf{p} \cdot (\mathbf{x} + \mathbf{a}) \right)} \, \mathrm{d}\mathbf{p} \\
&= \left( \frac{1}{2\pi \hbar} \right)^{3/2} \int \ket{\mathbf{p}} \exp{\left( -\frac{i}{\hbar} \mathbf{p} \cdot \mathbf{x} \right)} \exp{\left( -\frac{i}{\hbar} \mathbf{p} \cdot \mathbf{a} \right)} \, \mathrm{d}\mathbf{p} \\
&= \int \exp{\left( -\frac{i}{\hbar} \mathbf{\hat{p}} \cdot \mathbf{a} \right)} \ket{\mathbf{p}} \braket{\mathbf{p} | \mathbf{x}} \, \mathrm{d}\mathbf{p} \\
&= f(\mathbf{a}) \ket{\mathbf{x}}
\end{split}
$$

where we have identified the translation operator as:

$$
f(\mathbf{a}) = \exp{\left( -\frac{i}{\hbar} \mathbf{\hat{p}} \cdot \mathbf{a} \right)}
$$

We have seen that the infinitesimal translation operator is:

$$
f(\mathrm{d}\mathbf{a}) = 1 - \frac{i}{\hbar} \hat{p} \cdot \mathrm{d}\mathbf{a}
$$

where $\mathrm{d}\mathbf{a}$ is the infinitesimal translation vector.

This leads to the canonical commutation relation between the position and momentum operators:

$$
[\hat{x}_{i}, \hat{p}_{j}] = i \hbar \delta_{ij}
$$

A finite translation of $\mathbf{a}$ can be obtained by translating by $N$ number of small translations $\mathbf{a} = \mathbf{a}/N$. Taking the limit as $N \rightarrow \infty$ gives:

$$
f(\mathbf{a}) = \lim_{N \rightarrow \infty} \left(1 - \frac{i}{\hbar} \hat{p} \cdot \frac{\mathbf{a}}{N} \right)^{N} \equiv \exp{\left(- \frac{i}{\hbar} \hat{p} \cdot \mathbf{a} \right)}
$$

This operator is apparently unitary:

$$
f^{\dagger}(\mathbf{a}) f(\mathbf{a}) = \exp{\left(\frac{i}{\hbar} \hat{p} \cdot \mathbf{a} \right)} \exp{\left(- \frac{i}{\hbar} \hat{p} \cdot \mathbf{a} \right)} = \mathbb{I}
$$

and satisfies the composition property:

$$
f(\mathbf{a} + \mathbf{b}) = f(\mathbf{a}) f(\mathbf{b})
$$

An important property of the translation operator is that, on physical grounds, translations in different directions should commute. Take x- and y-directions as an example:

$$
\begin{split}
[f(\mathbf{y}), f(\mathbf{x})] &\approx \left[ \left( 1 - \frac{ip_{y}y}{\hbar} - \frac{p_{y}^{2}y^{2}}{\hbar^{2}} \right), \left( 1 - \frac{ip_{x}x}{\hbar} - \frac{p_{x}^{2}x^{2}}{\hbar^{2}} \right) \right] \\
&\approx - \frac{xy}{\hbar} [p_{y}, p_{x}]
\end{split}
$$

This implies that $[p_{y}, p_{x}] = 0$, or in general:

$$
[p_{i}, p_{j}] = 0
$$

In general, a group of commuting operators are said to be Abelian and they share a common set of eigenkets.

Also note the expectation value of the position operator $\hat{x}$:

$$
\begin{split}
\braket{\psi' | \hat{x} | \psi'} &= \braket{\psi | f^{\dagger}(\mathbf{a}) \hat{x} f(\mathbf{a}) | \psi} \\
\bra{\psi} f^{\dagger}(\mathbf{a}) \hat{x} \int \ket{p} \braket{p | \psi} \, \mathrm{d}p
\end{split}
$$

## Reflections and Parity

Suppose a position eigenket $\ket{\mathbf{x}}$. We consider a unitary operator $\hat{\pi}$ that reflects the position vector $\mathbf{x}$ about the origin:

$$
\ket{\mathbf{x}} \to \hat{\pi} \ket{\mathbf{x}}
$$

We require that the expectation value of $\mathbf{x}$ changes sign:

$$
\braket{\mathbf{x} | \hat{\pi}^{\dagger} \hat{x} \hat{\pi} | \mathbf{x}} = -\braket{\mathbf{x} | \hat{x} | \mathbf{x}}
$$

This means that $\hat{\pi}^{\dagger} \hat{x} \hat{\pi} = -\hat{x}$ or that $\hat{\pi}$ and $\hat{x}$ anticommute:

$$
\hat{\pi} \hat{x} + \hat{x} \hat{\pi} = 0
$$

This can be achieved if $\hat{\pi}$ satisfies:

$$
\hat{\pi} \ket{\mathbf{x}} = \ket{-\mathbf{x}}
$$

Applying $\hat{\pi}$ twice gives:

$$
\hat{\pi}^{2} \ket{\mathbf{x}} = \ket{\mathbf{x}}
$$

which means that $\hat{\pi}$ is Hermitian with eigenvalues $\pm 1$.

Now consider the relation between $\hat{\pi}$ and the momentum operator $\hat{p}$. Since translation followed by reflection is equivalent to reflection followed by translation, we have:

$$
\begin{split}
\hat{\pi} f(\mathrm{d}\mathbf{x}) &= f(-\mathrm{d}\mathbf{x}) \hat{\pi} \\
\hat{\pi} \left( 1 - \frac{i}{\hbar} \hat{\pi} \cdot \mathrm{d}\mathbf{x} \right) &= \left( 1 + \frac{i}{\hbar} \hat{\pi} \cdot \mathrm{d}\mathbf{x} \right) \hat{\pi} \\
\end{split}
$$

which implies that $\hat{\pi} \hat{p} + \hat{p} \hat{\pi} = 0$, similar to the position operator.

If a Hamiltonian commutes with $\hat{\pi}$, we say that the system is **parity invariant**. Since $\hat{H}$ and $\hat{\pi}$ share a common set of eigenkets and the only eigenvalues of $\hat{\pi}$ are $\pm 1$, we call the ones with unity eigenvalues as **parity-even states** and the ones with minus unity eigenvalues as **parity-odd states**.

## Rotations

Unlike translations, rotations in different directions generally do not commute: a $90^{\circ}$ rotation about the x-axis followed by a $90^{\circ}$ rotation about the y-axis is not the same as a $90^{\circ}$ rotation about the y-axis followed by a $90^{\circ}$ rotation about the x-axis.

From linear algebra, a rotation operator $\hat{R}$ is a matrix that has unit determinant and is orthogonal, i,e., $\hat{R}^{\intercal} \hat{R} = \mathbb{I}$. In three dimensions, a rotation around the $z$-axis by an angle $\theta$ is given by:

$$
\hat{R}_{z}(\theta) =
\begin{pmatrix}
\cos{\theta} & -\sin{\theta} & 0 \\
\sin{\theta} & \cos{\theta} & 0 \\
0 & 0 & 1
\end{pmatrix}
$$

We are particularly interested in the infinitesimal version of the rotation operators around the three axes:

$$
\begin{split}
\hat{R}_{z}(\epsilon) &=
\begin{pmatrix}
1 - \epsilon^{2}/2 & -\epsilon & 0 \\
\epsilon & 1 - \epsilon^{2}/2 & 0 \\
0 & 0 & 1
\end{pmatrix} \\
\hat{R}_{x}(\epsilon) &=
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 - \epsilon^{2}/2 & -\epsilon \\
0 & \epsilon & 1 - \epsilon^{2}/2
\end{pmatrix} \\
\hat{R}_{y}(\epsilon) &=
\begin{pmatrix}
1 - \epsilon^{2}/2 & 0 & \epsilon \\
0 & 1 & 0 \\
-\epsilon & 0 & 1 - \epsilon^{2}/2
\end{pmatrix}
\end{split}
$$

An important observation from the above matrices is that infinitesimal rotations about different axes do commute. Consider for example:

$$
\hat{R}_{x}(\epsilon) \hat{R}_{y}(\epsilon) =
\begin{pmatrix}
1 - \epsilon^{2}/2 & 0 & \epsilon \\
\epsilon^{2} & 1 - \epsilon^{2}/2 & -\epsilon \\
-\epsilon & \epsilon & 1 - \epsilon^{2}
\end{pmatrix}
$$

and:

$$
\hat{R}_{y}(\epsilon) \hat{R}_{x}(\epsilon) =
\begin{pmatrix}
1 - \epsilon^{2}/2 & \epsilon^{2} & \epsilon \\
0 & 1 - \epsilon^{2}/2 & -\epsilon \\
-\epsilon & \epsilon & 1 - \epsilon^{2}
\end{pmatrix}
$$

Ignoring terms of order $\epsilon^{2}$, the matrices are the same so that the rotations commute. More importantly:

$$
\hat{R}_{x}(\epsilon) \hat{R}_{y}(\epsilon) - \hat{R}_{y}(\epsilon) \hat{R}_{x}(\epsilon) =
\begin{pmatrix}
0 & -\epsilon^{2} & 0 \\
\epsilon^{2} & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}
= R_{z}(\epsilon^{2}) - 1
$$

which indicates the extent to which the rotations do not commute.

As rotations clearly affect a physical system, the state ket of the system after a rotation must be different from the original one. Given a rotation operation $\hat{R}$, we associate an operator $D(\hat{R})$ that acts on the state ket $\ket{\psi}$ to give the rotated state ket $\ket{\psi'}$:

$$
\ket{\psi} \to \ket{\psi'} = D(\hat{R}) \ket{\psi}
$$

In exact analogy to the translation and time-evolution operators, we can write the infinitesimal rotation operators as:

$$
D(\hat{n}, \mathrm{d}\theta) = 1 - \frac{i}{\hbar} (\hat{J} \cdot \hat{n}) \mathrm{d}\theta
$$

which represents a rotation about the direction $\hat{n}$ by an angle $\mathrm{d}\theta$.

A finite rotation can be obtained by rotating by a large number of small rotations. Take the z-axis as an example:

$$
D_{z}(\theta) = \lim_{N \to \infty} \left( 1 - \frac{i}{\hbar} \hat{J}_{z} \frac{\theta}{N} \right)^{N} \equiv \exp{\left(- \frac{i}{\hbar} \hat{J}_{z} \theta \right)}
$$

To obtain the commutation relations between the angular momentum operators, we postulate that the rotation operators satisfy the same commutator property as the rotation matrices:

$$
D_{x}(\epsilon) D_{y}(\epsilon) - D_{y}(\epsilon) D_{x}(\epsilon) = D_{z}(\epsilon^{2}) - 1
$$

At second order in $\epsilon$, we have:

$$
\left( 1 - \frac{i}{\hbar} \hat{J}_{x} \epsilon - \frac{\hat{J}_{x}^{2} \epsilon^{2}}{2 \hbar^{2}} \right) \left( 1 - \frac{i}{\hbar} \hat{J}_{y} \epsilon - \frac{\hat{J}_{y}^{2} \epsilon^{2}}{2 \hbar^{2}} \right) - \left( 1 - \frac{i}{\hbar} \hat{J}_{y} \epsilon - \frac{\hat{J}_{y}^{2} \epsilon^{2}}{2 \hbar^{2}} \right) \left( 1 - \frac{i}{\hbar} \hat{J}_{x} \epsilon - \frac{\hat{J}_{x}^{2} \epsilon^{2}}{2 \hbar^{2}} \right) = 1 - \frac{i}{\hbar} \hat{J}_{z} \epsilon^{2} - 1
$$

Equating the coefficients of $\epsilon^{2}$ gives:

$$
[\hat{J}_{x}, \hat{J}_{y}] = i \hbar \hat{J}_{z}
$$

With cyclic permutations of the indices, we obtain the fundamental commutation relations for angular momentum operators:

$$
\boxed{
[J_{i}, J_{j}] = i \hbar \epsilon_{ijk} J_{k}
}
$$

where $\epsilon_{ijk}$ is the Levi-Civita symbol.

<!-- In contrast to momentum, the angular momentum operators do not commute with each other. Such a group of operators are said to be non-Abelian. Going back to the infinitesimal rotation matrix $R_{z}(\epsilon)$, it changes the position of a vector as:

$$
\begin{pmatrix}
x \\
y \\
z
\end{pmatrix}
\to
\begin{pmatrix}
x - \epsilon y \\
y + \epsilon x \\
z
\end{pmatrix}
$$

This implies that an infinitesimal rotation can be viewed as two infinitesimal translations in the x- and y-directions:

$$
\begin{split}
D_{z}(\epsilon) &= f_{x}(-y \epsilon) f_{y}(x \epsilon) \\
1 - \frac{i}{\hbar} \hat{J}_{z} \epsilon &= \left( 1 + \frac{i}{\hbar} \hat{p}_{x} \hat{y} \epsilon \right) \left( 1 - \frac{i}{\hbar} \hat{p}_{y} \hat{x} \epsilon \right) \\
\hat{J}_{z} &= \hat{x} \hat{p}_{y} - \hat{y} \hat{p}_{x}
\end{split}
$$

where at the last step we have ignored second order terms in $\epsilon$.

In general, the angular momentum operators can be written as:

$$
\hat{J}_{i} = \sum_{jk} \epsilon_{ijk} \hat{x}_{j} \hat{p}_{k}
$$

or equivalently $\hat{\mathbf{J}} = \hat{\mathbf{x}} \times \hat{\mathbf{p}}$. -->

$\hat{J}$ commute with any operator $\hat{S}$ whose expectation is a scalar. To see this, consider the expectation $\braket{\psi | \hat{S} | \psi}$, a scalar that is invariant under rotations. We can write:

$$
\braket{\psi' | \hat{S} | \psi'} = \braket{\psi | D^{\dagger}(\hat{R}) \hat{S} D(\hat{R}) | \psi} = \braket{\psi | \hat{S} | \psi}
$$

Equating the operators in the middle immediately gives $[D(\hat{R}), \hat{S}] = 0$, or in the infinitesimal case:

$$
\hat{S} = (1 + \frac{i}{\hbar} \hat{J} \cdot \mathrm{d}\theta) \hat{S} (1 - \frac{i}{\hbar} \hat{J} \cdot \mathrm{d}\theta) \approx \mathbf{S} + \frac{i}{\hbar} \mathrm{d}\theta [\hat{J}, \hat{S}]
$$

which implies that $[\hat{J}, \hat{S}] = 0$.

Additionally, for any operator $\mathbf{\hat{v}}$ whose expectation is a vector, we have the commutation relation:

$$
[\hat{J}_{i}, \hat{v}_{j}] = i \hbar \epsilon_{ijk} \hat{v}_{k}
$$
