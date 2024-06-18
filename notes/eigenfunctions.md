# Eigenfunctions of Differential Equations

Consider the infinite-dimensional space of all reasonably well-behaved functions $f(x)$ over the interval $a \le x \le b$. The functions form a linear space. We may introduce a set of linearly independent functions $y_{r}(x)$ such that any function satisfying the Dirichlet conditions in the interval $a \le x \le b$ can be expressed as a linear sum of these functions:

$$
f(x) = \sum_{r=0}^{\infty} c_{r} y_{r}(x)
$$

Define an **inner product** on the function space as:

$$
\braket{f|g} \equiv \int_{a}^{b} f^{*}(x) g(x) \rho(x) \, \mathrm{d} x
$$

where $\rho(x)$ is a weight function that is real and non-negative over the interval and is unity for all $x$ most of the time.

Two functions are said to be **orthogonal** if their inner product is zero:

$$
\braket{f|g} = 0
$$

The norm of a function is defined as:

$$
|f| \equiv \sqrt{\braket{f|f}}
$$

The normalised version of a function is defined as:

$$
\hat f \equiv \frac{f}{|f|}
$$

An infinite-dimensional vector space of functions, for which an inner product is defined, is called a **Hilbert space**. We can choose a set of linearly independent functions $\hat{\phi}_{r}(x)$ that are orthonormal. such that:

$$
\braket{\hat{\phi}_{i}|\hat{\phi}_{j}} = \delta_{ij}
$$

Given a set $f_{r}$ of linearly independent basis for the Hilbert space, an orthonormal basis $\hat{\phi}_{r}$ may be produced with **Gram-Schmidt orthogonalisation**:

$$
\begin{split}
& \phi_{0} = y_{0} \\
& \phi_{1} = y_{1} - \hat{\phi}_{0} \braket{\hat{\phi}_{0}|y_{1}} \\
& \phi_{n} = y_{n} - \sum_{r=1}^{n-1} \hat{\phi}_{r} \braket{\hat{\phi}_{r}|y_{n}}
\end{split}
$$

## Hermitian Operators

An operator $\mathcal{L}$ acts on a function. The adjoint of the operator, $\mathcal{L}^{\dag}$ is defined by:

$$
\int_{a}^{b} f^{*}(x) [\mathcal{L}g(x)] \, \mathrm{d}x = \int_{a}^{b} [\mathcal{L}^{\dag}f(x)]^{*} g(x) \, \mathrm{d}x + C
$$

where $C$ denotes the boundary terms evaluated at the end-points of the interval.

An operator is called **self-adjoint** if $\mathcal{L} = \mathcal{L}^{\dag}$. A self-adjoint operator is called **Hermitian** if the boundary term $C$ vanishes, such that:

$$
\int_{a}^{b} f^{*}(x) [\mathcal{L}g(x)] \, \mathrm{d}x = \int_{a}^{b} [\mathcal{L}f(x)]^{*} g(x) \, \mathrm{d}x
$$

If there exists a function $f(x)$ that satisfies:

$$
\mathcal{L}f(x) = \lambda \rho(x) f(x)
$$

for some constant $\lambda$ and where $\rho(x)$ is a weight function that is often unity, the function $f$ is called the eigenfunction of the operator and the constant $\lambda$ is called the eigenvalue.

Suppose a Hermitian operator has at least two eigenfunctions $y_i$ and $y_j$ and the corresponding eigenvalues $\lambda_i$ and $\lambda_j$:

$$
\begin{split}
\mathcal{L}y_{i}(x) &= \lambda_{i} \rho(x) y_{i}(x) \\
\mathcal{L}y_{j}(x) &= \lambda_{j} \rho(x) y_{j}(x)
\end{split}
$$

It follows that:

$$
\begin{split}
\int_{a}^{b} y_{j}^{*} \mathcal{L}y_{i} \, \mathrm{d}x &= \lambda_{i} \int_{a}^{b} y_{j}^{*} y_{i} \rho \, \mathrm{d}x \\
\int_{a}^{b} y_{i}^{*} \mathcal{L}y_{j} \, \mathrm{d}x &= \lambda_{j} \int_{a}^{b} y_{i}^{*} y_{j} \rho \, \mathrm{d}x
\end{split}
$$

As $\rho$ must be a real function, the complex conjugate of the first equality leads to:

$$
\int_{a}^{b} y_{j} (\mathcal{L} y_{i})^{*} \, \mathrm{d}x = \lambda_{i}^{*} \int_{a}^{b} y_{i}^{*} y_{j} \rho \, \mathrm{d}x
$$

Based on the definition of a Hermitian operator, we conclude:

$$
(\lambda_{i}^{*} - \lambda_{j}) \int_{a}^{b} y_{i}^{*} y_{j} \rho \, \mathrm{d}x = 0
$$

If $i = j$, then $\lambda_{i} = \lambda_{i}^{*}$, implying that the eigenvalues of a Hermitian operator are real. If $i \ne j$, then the inner product of any two distinct eigenfunctions of a Hermitian operator is zero, implying the orthogonality of the eigenfunctions. For normalised eigenfunctions $\hat{y}_{i}(x)$, have:

$$
\int_{a}^{b} \hat{y}_{i}^{*} \hat{y}_{j} \rho \, \mathrm{d}x = \delta_{ij}
$$

## Sturm-Liouville Equations

The discussion on Hermitian operators finds its application in the analysis of **Sturm-Liouville equations**, which take the form:

$$
\frac{\mathrm{d}}{\mathrm{d}x} (p(x) \frac{\mathrm{d}y}{\mathrm{d}x}) + q(x)y + \lambda \rho(x) y = 0
$$

where $p$, $q$, $\rho$ are real functions of $x$.

The equation can be rewritten in an operator form:

$$
\mathcal{L} y = \lambda \rho(x) y
$$

where $\mathcal{L} \equiv -[\frac{\mathrm{d}}{\mathrm{d}x} (p \frac{\mathrm{d}}{\mathrm{d}x}) + q]$.

Thus the solution to Sturm-Liouville equations becomes an eigenfunction problems for the differential operator $\mathcal{L}$. If the eigenfunctions $y_{i}$ satisfy the condition:

$$
[y_{i}^{*}py_{j}]_{x=a}^{x=b} = 0
$$

then the Sturm-Liouville operator can be shown to be Hermitian.

### Green\'s Function

Given the eigenfunctions of the Sturm-Liouville operator:

$$
\mathcal{L} y_{n}(x) = \lambda_{n} \rho(x) y_{n}(x)
$$

then the eigenvalues $\lambda_{n}$ are real and the eigenfunctions $\lambda_{n}$ are orthogonal.

Suppose that the eigenfunctions of $\mathcal{L}$ and some boundary conditions are known. Consider the following inhomogeneous differential equation:

$$
\mathcal{L} y(x) = f(x)
$$

for some function $f(x)$ and subject to the same boundary conditions.

The solution $y(x)$ can be written as a linear combination of the eigenfunctions, which form a complete set:

$$
y(x) = \sum_{r=0}^{\infty} c_{r} y_{r}(x)
$$

The constants $c_r$ can be determined as follows. First note:

$$
f(x) = \mathcal{L} y(x) = \sum_{r=0}^{\infty} c_{r} (\mathcal{L} y_{r}(x)) = \sum_{r=0}^{\infty} c_{r} \lambda_{r} \rho(x) y_{r}(x)
$$

Multiplying both sides by $y_{j}^{*}$ and integrating:

$$
\int_{a}^{b} y_{j}^{*}(z) f(z) \, \mathrm{d}z= \sum_{r=0}^{\infty} \int_{a}^{b} c_{r} \lambda_{r} \rho(z) y_{j}^{*}(z) y_{r}(z) \, \mathrm{d}z
$$

where the integration variable has been switched to $z$.

By the orthogonality of the eigenfunctions, the integrals on the right side vanish unless $j = r$. Therefore, the constants $c_{r}$ are given by:

$$
c_{r} = \frac{1}{\lambda_{r}} \frac{\int_{a}^{b} y_{r}^{*}(z) f(z) \, \mathrm{d}z}{\int_{a}^{b} \rho(z) y_{r}^{*}(z) y_{r}(z) \, \mathrm{d}z}
$$

If the eigenfunctions are normalised, so that:

$$
\int_{a}^{b} \rho(z) \hat{y}_{r}^{*}(z) \hat{y}_{r}(z) \, \mathrm{d}z = 1
$$

then the desired solution $y(x)$ can be solved and rewritten as:

$$
\begin{split}
y(x) &= \sum_{r=0}^{\infty} \hat{y}_{r}(x) \frac{1}{\lambda_{r}} \int_{a}^{b} y_{r}^{*}(z) f(z) \, \mathrm{d}z \\
     &= \int_{a}^{b} G(x, z) f(z) \, \mathrm{d}z
\end{split}
$$

where the **Green\'s function** $G(x, z)$ of the problem is defined as:

$$
G(x, z) \equiv \sum_{r=0}^{\infty} \frac{\hat{y}_{r}(x) \hat{y}_{r}^{*}(z)}{\lambda_{r}}
$$

Note that the Green\'s function is completely determined by the eigenfunctions and boundary conditions, and thus is solely dependent on $\mathcal{L}$. Note also that the only only requirement for $\mathcal{L}$ is that there exists a set of eigenfunctions for the operators. Thus it is not mandatory for the differential operator $\mathcal{L}$ to take the Sturm-Liouville form.
