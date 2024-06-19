# Quantum Mechanics - Foundation

## Bra-kets and Operators

In quantum mechanics, a physical state of a system is represented by a state vector in a complex vector space. This vector is called a ket and denoted by $\ket{a}$. This state ket is postulated to contain complete information about the state of the system. It is postulated that a linear multiple $c\ket{a}$ of a ket $\ket{a}$ represents the same physical state, as long as $c \ne 0$.

An observable, such as the position of a particle, is represented by an operator. An operator $A$ acts on a ket to produce another ket:

$$
A \ket{a} = \ket{\beta}
$$

The eigenkets of an operator are the kets that produce linear multiples of themselves when acted on by the operator:

$$
A \ket{a'} = a' \ket{a'}
$$

where the set $\{a'\}$ is the eigenvalues of the operator.

The eigenkets of an operator form a complete set of kets. This means that any ket $\ket{b}$ can be expressed as a linear combination of the eigenkets of the operator:

$$
\ket{b} = \sum_{a'} b_{a'} \ket{a'} = \sum_{a'} \ket{a'} \braket{a' | b}
$$

The completeness of the eigenkets of an operator means:

$$
\sum_{a'} \ket{a'} \bra{a'} = \mathbb{I}
$$

Using the completeness identity, any operator can be expressed as a linear combination of the outer products of the eigenkets of the operator:

$$
A = \sum_{a', a''} \ket{a'} \braket{a' | A | a''} \bra{a''}
$$

which implies that we can define the matrix elements of an operator as:

$$
A_{ij} \equiv \braket{a_{i} | A | a_{j}}
$$

It is postulated that for every ket $\ket{a}$, there exists a dual bra $\bra{a}$ such that:

$$
\braket{b | a} = \braket{a | b}^{*}
$$

and:

$$
\braket{a | a} \ge 0
$$

The hermitian conjugate of an operator $A$ is defined as the operator $A^{\dagger}$ such that $A\ket{a}$ is the dual corresponding to $\bra{a}A^{\dagger}$. Equivalently:

$$
\braket{b | A | a} = \braket{a | A^{\dagger} | b}^{*}
$$

Two operators $A$ and $B$ are said to commute if:

$$
[A, B] \equiv AB - BA = 0
$$

where $[A, B]$ is called the commutator of $A$ and $B$.

It can be proven that there exists a set of simultaneous eigenkets of two operators $A$ and $B$ if and only if $A$ and $B$ commute. A simultaneous eigenket of $A$ and $B$, denoted as $\ket{a', b'}$, satisfies:

$$
A \ket{a', b'} = a' \ket{a', b'}, \quad B \ket{a', b'} = b' \ket{a', b'}
$$

The uncertainty principle states that the product of the standard deviations of two non-commuting operators $A$ and $B$ is bounded from below. First define thee operator:

$$
\Delta A \equiv A - \braket{A}
$$

The dispersion of an operator $A$ is defined as:

$$
\sigma_{A}^{2} \equiv \braket{\Delta A^{2}} = \braket{A^{2}} - \braket{A}^{2}
$$

It can be proven that, given two operators $A$ and $B$, for any state:

$$
\sigma_{A}^{2} \sigma_{B}^{2} = \braket{\Delta A^{2}} \braket{\Delta B^{2}} \ge \frac{1}{4} \left\lvert \braket{[A, B]} \right\rvert^{2}
$$

which is called the uncertainty principle.

## Continuous Spectra

In quantum mechanics, some observables, such as momentum and position, have continuous eigenvalues. While the dimensionality of a vector space describing such an observable is infinite, the results from finite-dimensional vector spaces can be generalised. Consider the eigenvalue equation:

$$
\zeta \ket{\zeta'} = \zeta' \ket{\zeta'}
$$

where $\zeta$ is an operator and $\zeta'$ is a scalar.

Generalising from finite-dimensional vector spaces, we can have the following results:

$$
\begin{split}
\braket{\zeta' | \zeta''} &= \delta(\zeta' - \zeta'') \\
\int \ket{\zeta'} \bra{\zeta'} \, \mathrm{d}\zeta' &= \mathbb{I} \\
\ket{\alpha} &= \int \ket{\zeta'} \braket{\zeta' | \alpha} \, \mathrm{d}\zeta' \\
\int \left\lvert \braket{\zeta' | \alpha} \right\rvert^{2} \, \mathrm{d}\zeta' &= 1 \\
\braket{\beta | \alpha} &= \int \braket{\beta | \zeta'} \braket{\zeta' | \alpha} \, \mathrm{d}\zeta' \\
\braket{\zeta'' | \zeta | \zeta'} &= \zeta' \delta(\zeta' - \zeta'')
\end{split}
$$

where $\delta$ is the Dirac delta function, the continuous analogue of the Kronecker delta function.

Let us investigate the position operator $\hat{x}$ satisfying the eigenvalue equation:

$$
\hat{x} \ket{x'} = x' \ket{x'}
$$

An arbitrary state vector $\ket{\alpha}$ can be expanded in terms of the eigenkets of $\hat{x}$:

$$
\ket{\alpha} = \int \ket{x'} \braket{x' | \alpha} \, \mathrm{d}x'
$$

We may express any operator $A$ in terms of the eigenkets of $\hat{x}$. This is called the position representation of the operator:

$$
A = \int \ket{x'} \braket{x' | A | x''} \bra{x''} \, \mathrm{d}x' \mathrm{d}x''
$$

The position operator described above can be easily generalised to three dimensions. Consider the position eigenkets $\ket{\mathbf{x}'} \equiv \ket{x', y', z'}$, where:

$$
\hat{x} \ket{\mathbf{x}'} = x' \ket{\mathbf{x}'}, \quad \hat{y} \ket{\mathbf{x}'} = y' \ket{\mathbf{x}'}, \quad \hat{z} \ket{\mathbf{x}'} = z' \ket{\mathbf{x}'}
$$

An arbitrary state vector $\ket{\alpha}$ can be expanded in terms of the eigenkets of $\hat{\mathbf{x}}$:

$$
\ket{\alpha} = \int \ket{\mathbf{x}'} \braket{\mathbf{x}' | \alpha} \, \mathrm{d}\mathbf{x}'
$$

For there to exist a simultaneous eigenket for $\hat{x}$, $\hat{y}$ and $\hat{z}$, these operator must commute:

$$
[x_{i}, x_{j}] = 0
$$

## Translation

Consider an active translation of a system from a state $\ket{\mathbf{x}'}$ to a state $\ket{\mathbf{x}' + \mathrm{d}\mathbf{x}'}$ with nothing else changing. We define such a change to be represented by the operator $f(\mathrm{d}\mathbf{x}')$:

$$
{f}(\mathrm{d}\mathbf{x}') \ket{\mathbf{x}'} = \ket{\mathbf{x}' + \mathrm{d}\mathbf{x}'}
$$

Let the operator act on an arbitrary state vector $\ket{\alpha}$ expressed in its position eigenkets:

$$
{f}(\mathrm{d}\mathbf{x}') \ket{\alpha} = {f}(\mathrm{d}\mathbf{x}') \int \ket{\mathbf{x}'} \braket{\mathbf{x}' | \alpha} \, \mathrm{d}\mathbf{x}' = \int \ket{\mathbf{x}' + \mathrm{d}\mathbf{x}'} \braket{\mathbf{x}' | \alpha} \, \mathrm{d}\mathbf{x}'
$$

Changing the integration variable $\mathbf{x}' \to \mathbf{x}' + \mathrm{d}\mathbf{x}'$ in the last integral, we note:

$$
\int \ket{\mathbf{x}' + \mathrm{d}\mathbf{x}'} \braket{\mathbf{x}' | \alpha} \, \mathrm{d}\mathbf{x}' = \int \ket{\mathbf{x}'} \braket{\mathbf{x}' - \mathrm{d}\mathbf{x}'| \alpha} \, \mathrm{d}\mathbf{x}'
$$

There are certain properties to be satisfied by a translation operator that will help us determine the form of $f(\mathrm{d}\mathbf{x}')$. Firstly, a translation should not affect the normalisation of a state vector:

$$\
\braket{\alpha | \alpha} = \braket{\alpha | f^{\dagger}(\mathrm{d}\mathbf{x}') f(\mathrm{d}\mathbf{x}') | \alpha}
$$

so that the translation operator must be unitary:

$$
f^{\dagger}(\mathrm{d}\mathbf{x}') f(\mathrm{d}\mathbf{x}') = \mathbb{I}
$$

Secondly, we expect the result of two successive translations to be the same as a single translation:

$$
f(\mathrm{d}\mathbf{x}') f(\mathrm{d}\mathbf{x}'') = f(\mathrm{d}\mathbf{x}' + \mathrm{d}\mathbf{x}'')
$$

Thirdly, a translation in the opposite direction should be the inverse of the original translation:

$$
f(\mathrm{d}\mathbf{x}') f(-\mathrm{d}\mathbf{x}') = \mathbb{I}
$$

Lastly, in the limit of a very small translation, we expect the translation operator to be the identity operator:

$$
\lim_{\mathrm{d}\mathbf{x}' \to \mathbf{0}} f(\mathrm{d}\mathbf{x}') = \mathbb{I}
$$

It can be easily verified that, in the limit of an infinitesimal $\mathrm{d}\mathbf{x}'$, a possible form of the translation operator that satisfies all of these properties is:

$$
\boxed{
f(\mathrm{d}\mathbf{x}') = 1 - i \mathbf{K} \cdot \mathrm{d}\mathbf{x}'
}
$$

where the components $K_{i}$ of $\mathbf{K}$ are Hermitian operators.

A fundamental relation can be derived based on the above definition of the translation operator. First note that:

$$
\mathbf{x} f(\mathrm{d}\mathbf{x}') \ket{\mathbf{x}'} = \mathbf{x} \ket{\mathbf{x}' + \mathrm{d}\mathbf{x}'} = (\mathbf{x}' + \mathrm{d}\mathbf{x}') \ket{\mathbf{x}' + \mathrm{d}\mathbf{x}'}
$$

On the other hand:

$$
f(\mathrm{d}\mathbf{x}') \mathbf{x} \ket{\mathbf{x}'} = \mathbf{x}' f(\mathrm{d}\mathbf{x}') \ket{\mathbf{x}'} = \mathbf{x}' \ket{\mathbf{x}' + \mathrm{d}\mathbf{x}'}
$$

so that:

$$
[\mathbf{x}, f(\mathrm{d}\mathbf{x}')] \ket{\mathbf{x}'} = \mathrm{d}\mathbf{x}' \ket{\mathbf{x}' + \mathrm{d}\mathbf{x}'} \approx \mathrm{d}\mathbf{x}' \ket{\mathbf{x}'}
$$

where the error incurred by the approximation is of order $\mathrm{d}\mathbf{x}'^2$.

Since $\ket{\mathbf{x}'}$ is arbitrary, we conclude that:

$$
[\mathbf{x}, f(\mathrm{d}\mathbf{x}')] = \mathrm{d}\mathbf{x}'
$$

or

$$
-i \mathbf{x} \mathbf{K} \cdot \mathrm{d}\mathbf{x}' + i \mathbf{K} \cdot \mathrm{d}\mathbf{x}' \mathbf{x} = \mathrm{d}\mathbf{x}'
$$

where $\mathrm{d}\mathbf{x}'$ is understood to be the vector $\mathrm{d}\mathbf{x}'$ times the identity operator.

Choosing $\mathrm{d}\mathbf{x}'$ to be in the direction of $\hat{x}_{j}$, we have:

$$
[\hat{x}_{i}, K_{j}] = i \delta_{ij}
$$

It turns out that the physical significance attached the operator $\mathbf{K}$ is that $\mathbf{K}$ is the momentum operator up to a constant factor:

$$
\boxed{
\mathbf{K} = \frac{1}{\hbar} \hat{p}
}
$$

where $\hat{p}$ is the momentum operator and $\hbar$ is the reduced Planck constant.

Then the translation operator can be written as:

$$
f(\mathrm{d}\mathbf{x}') = 1 - \frac{i}{\hbar} \hat{p} \cdot \mathrm{d}\mathbf{x}'
$$

and the commutation relation between the position and momentum operators can be written as:

$$
\boxed{
[x_{i}, p_{j}] = i \hbar \delta_{ij}
}
$$

This is called the canonical commutation relation. The momentum operator is called the generator of translations.

A finite translation $\Delta \mathbf{x}'$ in the direction of $\mathbf{x}'$ can be treated as a sum of infinitesimal translations:

$$
\boxed{
f(\Delta \mathbf{x}') = \lim_{N \to \infty} \prod_{n=1}^{N} f(\Delta \mathbf{x}'/N) = \lim_{N \to \infty} \prod_{n=1}^{N} (1 - \frac{i}{\hbar} \hat{p} \cdot \Delta \mathbf{x}'/N) = \exp \left( - \frac{i}{\hbar} \hat{p} \cdot \Delta \mathbf{x}' \right)
}
$$

where the exponential is understood to be a function for operators:

$$
\exp(X) \equiv \sum_{n=0}^{\infty} \frac{X^{n}}{n!}
$$

## Wave Functions in Position Space

Any state can be expressed as a linear combination of the eigenkets of the position operator:

$$
\ket{a} = \int \ket{\mathbf{x}'} \braket{\mathbf{x}' | a} \, \mathrm{d}\mathbf{x}'
$$

We call the inner product $\braket{\mathbf{x}' | a}$ the wave function of the state $\ket{a}$ in position space:

$$
\psi(\mathbf{x}') \equiv \braket{\mathbf{x}' | a}
$$

The product $\braket{b | A | a}$ can be expressed as:

$$
\begin{split}
\braket{b | A | a} &= \int \braket{b | \mathbf{x}'} \braket{\mathbf{x}' | A | \mathbf{x}''} \braket{\mathbf{x}'' | a} \, \mathrm{d}\mathbf{x}' \mathrm{d}\mathbf{x}'' \\
&= \int \psi_{b}^{*}(\mathbf{x}') \braket{\mathbf{x}' | A | \mathbf{x}''} \psi_{a}(\mathbf{x}'') \, \mathrm{d}\mathbf{x}' \mathrm{d}\mathbf{x}''
\end{split}
$$

Let us consider the momentum operator $\hat{p}$. Starting from the definition of momentum as the generator of translations:

$$
\begin{split}
\left( 1 - \frac{i}{\hbar} \hat{p} \Delta x' \right) \ket{a} &= f(\Delta x') \int \ket{x'} \braket{x' | a} \, \mathrm{d}x' \\
&= \int \ket{x' + \Delta x'} \braket{x' | a} \, \mathrm{d}x' \\
&= \int \ket{x'} \braket{x' - \Delta x' | a} \, \mathrm{d}x' \\
&= \int \ket{x'} \left( \braket{x' | a} - \Delta x' \frac{\partial}{\partial x'} \braket{x' | a} \right) \, \mathrm{d}x' \\
&= \ket{a} - \Delta x' \int \ket{x'} \frac{\partial}{\partial x'} \braket{x' | a} \, \mathrm{d}x'
\end{split}
$$

Comparing both sides gives:

$$
\hat{p} \ket{a} = -i \hbar \int \ket{x'} \frac{\partial}{\partial x'} \braket{x' | a} \, \mathrm{d}x'
$$

which gives the form of the momentum operator in position representation:

$$
\boxed{
\braket{x' | \hat{p} | a} = -i \hbar \frac{\partial}{\partial x'} \braket{x' | a}
}
$$

Replacing $\ket{a}$ with $\ket{x''}$, we have the momentum operator in position representation:

$$
\braket{x' | \hat{p} | x''} = -i \hbar \frac{\partial}{\partial x'} \braket{x' | x''} = -i \hbar \frac{\partial}{\partial x'} \delta(x' - x'')
$$

The product $\braket{b | \hat{p} | a}$ can thus be expressed as:

$$
\begin{split}
\braket{b | \hat{p} | a} &= \int \psi_{b}^{*}(x) \braket{x' | \hat{p} | x''} \psi_{a}(x'') \, \mathrm{d}x' \mathrm{d}x'' \\
&= -i \hbar \int \psi_{b}^{*}(x) \frac{\partial}{\partial x'} \psi_{a}(x') \, \mathrm{d}x'
\end{split}
$$

We can also derive the results:

$$
\begin{split}
\braket{x' | \hat{p}^{n} | a} &= (-i \hbar)^{n} \frac{\partial^{n}}{\partial x'^{n}} \braket{x' | a} \\
\braket{b | \hat{p}^{n} | a} &= (-i \hbar)^{n} \int \psi_{b}^{*}(x) \frac{\partial^{n}}{\partial x'^{n}} \psi_{a}(x') \, \mathrm{d}x'
\end{split}
$$

## Wave Functions in Momentum Space

Consider the eigenkets of the momentum operator $\hat{p}$:

$$
\hat{p} \ket{p'} = p' \ket{p'}
$$

with:

$$
\braket{p' | p''} = \delta(p' - p'')
$$

An arbitrary state vector $\ket{a}$ can be expanded in terms of the eigenkets of $\hat{p}$:

$$
\ket{a} = \int \ket{p'} \braket{p' | a} \, \mathrm{d}p'
$$

We call the inner product $\braket{p' | a}$ the wave function of the state $\ket{a}$ in momentum space:

$$
\phi(p') \equiv \braket{p' | a}
$$

Consider the product $\braket{x' | \hat{p} | p'}$:

$$
\braket{x' | \hat{p} | p'} = -i \hbar \frac{\partial}{\partial x'} \braket{x' | p'} = p' \braket{x' | p'}
$$

This is a differential equation for $\braket{x' | p'}$, which is the position representation of the momentum eigenket $\ket{p'}$. The solution is:

$$
\braket{x' | p'} = \frac{1}{\sqrt{2 \pi \hbar}} e^{i p' x' / \hbar}
$$

where the normalisation factor is chosen such that:

$$
\int \braket{p' | x'} \braket{x' | p''} \, \mathrm{d}x' = \delta(p' - p'')
$$

This reveals the connection between the wave functions in position space and momentum space. Consider:

$$
\begin{split}
\braket{x' | a} &= \int \braket{x' | p'} \braket{p' | a} \, \mathrm{d}p' \\
\braket{p' | a} &= \int \braket{p' | x'} \braket{x' | a} \, \mathrm{d}x'
\end{split}
$$

Writing them as wave functions:

$$
\begin{split}
\psi(x') &= \frac{1}{\sqrt{2 \pi \hbar}} \int e^{i p' x' / \hbar} \phi(p') \, \mathrm{d}p' \\
\phi(p') &= \frac{1}{\sqrt{2 \pi \hbar}} \int e^{-i p' x' / \hbar} \psi(x') \, \mathrm{d}x'
\end{split}
$$

This means that the wave functions in the two spaces are Fourier transforms of each other.

If we further make the substitution $k = p' / \hbar$ as indicated by the translation operator, we have:

$$
\begin{split}
\psi(x') &= \frac{1}{\sqrt{2 \pi}} \int e^{i k x'} \phi(\hbar k) \, \mathrm{d}k \\
\phi(\hbar k) &= \frac{1}{\sqrt{2 \pi}} \int e^{-i k x' / \hbar} \psi(x') \, \mathrm{d}x'
\end{split}
$$

which is the proper ordinary Fourier transform.
