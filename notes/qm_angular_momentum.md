# Quantum Mechanics - Theory of Angular Momentum

We have defined the total angular momentum operators $\hat{J}_{i}$ as the generators of rotations:

$$
D_{i}(\theta) \equiv \exp{\left(-\frac{i}{\hbar} \hat{J}_{i} \theta \right)}
$$

where $D_{i}(\theta)$ is the rotation operator about the $i$-axis by an angle $\theta$.

The commutation relation between the angular momentum operators is:

$$
[\hat{J}_{i}, \hat{J}_{j}] = i \hbar \epsilon_{ijk} \hat{J}_{k}
$$

## Eigenvalues and Eigenstates

Define the total angular momentum operator $\hat{J}^{2}$ as:

$$
\hat{J}^{2} \equiv \hat{J}_{x}^{2} + \hat{J}_{y}^{2} + \hat{J}_{z}^{2}
$$

It is easy to show that $[\hat{J}^{2}, \hat{J}_{i}] = 0$ for $i = x, y, z$. This means that $\hat{J}^{2}$ commutes with all the components of the angular momentum operator. We seek a common set of eigenstates for $\hat{J}^{2}$ and $\hat{J}_{z}$:

$$
\hat{J}^{2} \ket{a, b} = a \ket{a, b} \qquad \hat{J}_{z} \ket{a, b} = b \ket{a, b}
$$

where $a$ and $b$ are the eigenvalues of $\hat{J}^{2}$ and $\hat{J}_{z}$ respectively.

We define the ladder operators $\hat{J}_{\pm}$ as:

$$
\hat{J}_{\pm} \equiv \hat{J}_{x} \pm i \hat{J}_{y}
$$

Some commutator results immediately follow:

$$
\begin{split}
[\hat{J}_{z}, \hat{J}_{\pm}] &= \pm \hbar \hat{J}_{\pm} \\
[\hat{J}_{+}, \hat{J}_{-}] &= 2 \hbar \hat{J}_{z} \\
[\hat{J}^{2}, \hat{J}_{\pm}] &= 0
\end{split}
$$

Consider the effect of $\hat{J}_{z}$ on an eigenstate affected by $\hat{J}_{\pm}$:

$$
\begin{split}
\hat{J}_{z} \hat{J}_{\pm} \ket{a, b} &= \left( [\hat{J}_{z}, \hat{J}_{\pm}] + \hat{J}_{\pm} \hat{J}_{z} \right) \ket{a, b} \\
&= \left( \pm \hbar \hat{J}_{\pm} + \hat{J}_{\pm} \hat{J}_{z} \right) \ket{a, b} \\
&= (b \pm \hbar) \hat{J}_{\pm} \ket{a, b}
\end{split}
$$

This implies that $\hat{J}_{\pm} \ket{a, b}$ is also an eigenstate of $\hat{J}_{z}$ with a changed eigenvalue $b \pm \hbar$. This is reminiscent of the ladder operators used in analysing the harmonic oscillator. We can also show that $\hat{J}_{\pm} \ket{a, b}$ is an eigenstate of $\hat{J}^{2}$ with the same eigenvalue $a$:

$$
\hat{J}^{2} \hat{J}_{\pm} \ket{a, b} = \hat{J}_{\pm} \hat{J}^{2} \ket{a, b} = a \hat{J}_{\pm} \ket{a, b}
$$

since the two operators commute.

We may thus write $\hat{J}_{\pm} \ket{a, b}$ as (up to a constant factor) a new eigenstate of $\hat{J}^{2}$ and $\hat{J}_{z}$:

$$
\hat{J}_{\pm} \ket{a, b} = c_{\pm} \ket{a, b \pm \hbar}
$$

It turns out that we cannot keep applying $\hat{J}_{+}$ to $\ket{a, b}$ since there exists an upper bound on the eigenvalue $b$:

$$
b^{2} \leq a
$$

This implies that there exists a maximum value $b_{\text{max}}$ such that:

$$
\hat{J}_{+} \ket{a, b_{\text{max}}} = 0
$$

which also implies $\hat{J}_{-} \hat{J}_{+} \ket{a, b_{\text{max}}} = 0$.

On the other hand, we have the relation:

$$
\begin{split}
\hat{J}_{-} \hat{J}_{+} &= \left( \hat{J}_{x} - i \hat{J}_{y} \right) \left( \hat{J}_{x} + i \hat{J}_{y} \right) \\
&= \hat{J}_{x}^{2} + \hat{J}_{y}^{2} + i [\hat{J}_{x}, \hat{J}_{y}] \\
&= \hat{J}^{2} - \hat{J}_{z}^{2} - \hbar \hat{J}_{z}
\end{split}
$$

which leads to $(\hat{J}^{2} - \hat{J}_{z}^{2} - \hbar \hat{J}_{z}) \ket{a, b_{\text{max}}} = 0$.

This is only possible if $a - b_{\text{max}}^{2} - \hbar b_{\text{max}} = 0$ or $a = b_{\text{max}} (b_{\text{max}} + \hbar)$. Similarly, we can show that there exists a minimum value $b_{\text{min}}$ such that $a = b_{\text{min}} (b_{\text{min}} - \hbar)$. Comparing the two equations, we have $b_{\text{max}} = -b_{\text{min}}$ and $b$ satisfies:

$$
-b_{\text{max}} \leq b \leq b_{\text{max}}
$$

Since $b$ changes in discrete steps of $\hbar$, we can only apply $\hat{J}_{+}$ a finite number of times $n$, such that:

$$
b_{\text{max}} = b_{\text{min}} + n \hbar = -b_{\text{max}} + n \hbar
$$

which implies $b_{\text{max}} = n \hbar / 2$.

We define a new index $j = b_{\text{max}} / \hbar$ so that the maximum eigenvalue of $\hat{J}_{z}$ is $j \hbar$, where $j$ is either an integer or half-integer. We can then write the eigenvalues of $\hat{J}^{2}$ as:

$$
a = j(j + 1) \hbar^{2}
$$

Let us define another index $m$ such that $b \equiv m \hbar$. The allowed values of $m$ are:

$$
m = -j, -j + 1, \ldots, j - 1, j
$$

which total to $2j + 1$ values.

Further, consider the product $\hat{J}_{+}^{\dagger} \hat{J}_{+}$:

$$
\hat{J}_{+}^{\dagger} \hat{J}_{+} = \hat{J}_{x}^{2} + \hat{J}_{y}^{2} - i [\hat{J}_{x}, \hat{J}_{y}] = \hat{J}^{2} - \hat{J}_{z}^{2} - \hbar \hat{J}_{z}
$$

which implies:

$$
\braket{j, m | \hat{J}_{+}^{\dagger} \hat{J}_{+} | j, m} = \hbar^{2} \left[ j(j + 1) - m(m + 1) \right] = c_{+}^{2}
$$

A similar result can be obtained for $\hat{J}_{-}^{\dagger} \hat{J}_{-}$ so that:

$$
\braket{j, m | \hat{J}_{-}^{\dagger} \hat{J}_{-} | j, m} = \hbar^{2} \left[ j(j + 1) - m(m - 1) \right] = c_{-}^{2}
$$

We can thus write the eigenstates of $\hat{J}^{2}$ and $\hat{J}_{z}$ as $\ket{j, m}$ that satisfy the eigenvalue equations:

$$
\hat{J}^{2} \ket{j, m} = j(j + 1) \hbar^{2} \ket{j, m} \qquad \hat{J}_{z} \ket{j, m} = m \hbar \ket{j, m}
$$

and the ladder relations:

$$
\hat{J}_{\pm} \ket{j, m} = \hbar \sqrt{j(j + 1) - m(m \pm 1)} \ket{j, m \pm 1}
$$

This implies a quantisation of angular momentum, a direct consequence of the commutation relations between the angular momentum operators.

## Orbital Angular Momentum

There is another way to define the angular momentum. Assuming that the angular momentum due to spin is zero, the orbital angular momentum is defined as:

$$
\mathbf{L} \equiv \mathbf{r} \times \mathbf{p}
$$

or:

$$
\hat{L}_{i} = \epsilon_{ijk} \hat{x}_{j} \hat{p}_{k}
$$

The same commutation relation applies to the orbital angular momentum operators:

$$
[\hat{L}_{i}, \hat{L}_{j}] = i \hbar \epsilon_{ijk} \hat{L}_{k}
$$

Define the total orbital angular momentum operator $\hat{L}^{2}$ as:

$$
\hat{L}^{2} \equiv \hat{L}_{x}^{2} + \hat{L}_{y}^{2} + \hat{L}_{z}^{2}
$$

where it can be easily shown that $[\hat{L}^{2}, \hat{L}_{i}] = 0$ for $i = x, y, z$.

Whereas $\hat{J}_{i}$ are generators of rotations, $\hat{L}_{i}$ are generators of circular translations: the former turns a vector about an axis, while the latter shifts a vector in a plane without changing its orientation. Since $\hat{L}_{i}$ satisfy exactly the same commutation relations as $\hat{J}_{i}$, we can use the same ladder operators approach to conclude that the eigenvalues of $\hat{L}^{2}$ and $\hat{L}_{z}$ are $l(l + 1) \hbar^{2}$ and $m \hbar$ respectively.

On the other hand, since $\hat{L}_{i}$ generate circular translations, we expect a rotation of $2 \pi$ to be the identity operator. Consider an eigenstate $\ket{l, m}$ of $\hat{L}^{2}$ and $\hat{L}_{z}$:

$$
\ket{l, m} = \exp \left(-\frac{i}{\hbar} \hat{L}_{z} 2 \pi \right) \ket{l, m} = \exp{\left(-\frac{i}{\hbar} m 2 \pi \right)} \ket{l, m}
$$

This is only possible if $m$ is an integer, which demands that $l$ is also an integer. This is in contrast to the total angular momentum, where $m$ and $j$ can be half-integers. We can thus write the eigenstates of $\hat{L}^{2}$ and $\hat{L}_{z}$ as $\ket{l, m}$ that satisfy:

$$
\hat{L}^{2} \ket{l, m} = l(l + 1) \hbar^{2} \ket{l, m} \qquad \hat{L}_{z} \ket{l, m} = m \hbar \ket{l, m}
$$

where $l$ is an integer and $m$ is an integer between $-l$ and $l$.

The ladder operators for the orbital angular momentum are:

$$
\hat{L}_{\pm} \equiv \hat{L}_{x} \pm i \hat{L}_{y}
$$

which give rise to the ladder relations:

$$
\hat{L}_{\pm} \ket{l, m} = \hbar \sqrt{l(l + 1) - m(m \pm 1)} \ket{l, m \pm 1}
$$

## Position Representation of Eigenstates

It is trivial to see that in Cartesian coordinates, the position representation of $\hat{L}_{i}$ is:

$$
\hat{L}_{i} = -i \hbar \epsilon_{ijk} x_{j} \frac{\partial}{\partial x_{k}}
$$

The partial derivatives can be transformed to spherical coordinates so that the position representation of $\hat{J}_{i}$ become:

$$
\begin{split}
\hat{L}_{x} &= -i \hbar \left( -\sin{\phi} \frac{\partial}{\partial \theta} - \cot{\theta} \cos{\phi} \frac{\partial}{\partial \phi} \right) \\
\hat{L}_{y} &= -i \hbar \left( \cos{\phi} \frac{\partial}{\partial \theta} - \cot{\theta} \sin{\phi} \frac{\partial}{\partial \phi} \right) \\
\hat{L}_{z} &= -i \hbar \frac{\partial}{\partial \phi}
\end{split}
$$

which leads to the total angular momentum operator $\hat{J}^{2}$:

$$
\hat{L}^{2} = -\hbar^{2} \left[ \frac{1}{\sin{\theta}} \frac{\partial}{\partial \theta} \left( \sin{\theta} \frac{\partial}{\partial \theta} \right) + \frac{1}{\sin^{2}{\theta}} \frac{\partial^{2}}{\partial \phi^{2}} \right]
$$

Consider a spinless particle in a spherically symmetric potential. The wave equation is known to be sperable in spherical coordinates so that the energy eigenfunctions can be written as:

$$
\psi(r, \theta, \phi) \equiv \braket{\mathbf{r} | n, l, m} = R_{n, l}(r) Y_{l}^{m}(\theta, \phi)
$$

where the position vector $\mathbf{r}$ is written in spherical coordinates and $n$ is some quantum number other than $l$ and $m$.

We can isolate the angular part of the wave equation and consider:

$$
Y_{l}^{m}(\theta, \phi) \equiv \braket{\theta, \phi | l, m}
$$

Consider the eigenvalue equation for $\hat{L}_{z}$:

$$
\hat{L}_{z} \ket{l, m} = m \hbar \ket{l, m}
$$

In position representation, this becomes:

$$
-i \hbar \frac{\partial}{\partial \phi} Y_{l}^{m}(\theta, \phi) = m \hbar Y_{l}^{m}(\theta, \phi)
$$

which implies that the $Y_{l}^{m}$ must have a dependence on $\phi$ of the form $e^{i m \phi}$.

Likewise, the eigenvalue equation for $\hat{L}^{2}$ is:

$$
\left[ \frac{1}{\sin{\theta}} \frac{\partial}{\partial \theta} \left( \sin{\theta} \frac{\partial}{\partial \theta} \right) + \frac{1}{\sin^{2}{\theta}} \frac{\partial^{2}}{\partial \phi^{2}} + l(l + 1) \right] Y_{l}^{m}(\theta, \phi) = 0
$$

This is known as the associated Legendre equation, which has solutions of the form:

$$
Y_{l}^{m}(\theta, \phi) = A_{l}^{m} P_{l}^{m}(\cos{\theta}) e^{i m \phi}
$$

where $P_{l}^{m}$ are the associated Legendre functions and $A_{l}^{m}$ are normalisation constants.

The associated Legendre functions for $m \ge 0$ are defined as:

$$
P_{l}^{m}(x) \equiv (1 - x^{2})^{m/2} \frac{\mathrm{d}^{m}}{\mathrm{d} x^{m}} P_{l}(x)
$$

These functions are polynomials of degree $l - \left\lvert m \right\rvert$. This implies that $Y_{l}^{m}$ is a polynomial of degree $l - \left\lvert m \right\rvert$ in $\cos{\theta}$ multiplied by $(\sin{\theta})^{\left\lvert m \right\rvert}$.

We define $Y_{l}^{-m}$ by:

$$
Y_{l}^{-m}(\theta, \phi) \equiv (-1)^{m}[ Y_{l}^{m}(\theta, \phi)]^{*}
$$

The normalised eigenfunctions are called the **spherical harmonics** of the form:

$$
Y_{l}^{m}(\theta, \phi) = \sqrt{\frac{(2l + 1)(l - m)!}{4 \pi (l + m)!}} P_{l}^{m}(\cos{\theta}) e^{i m \phi}
$$

When $m = 0$, the spherical harmonics are real and independent of $\phi$. The associated Legendre functions reduce to the Legendre polynomials so that:

$$
Y_{l}^{0}(\theta, \phi) = \sqrt{\frac{2l + 1}{4 \pi}} P_{l}(\cos{\theta})
$$
