# Ordinary Differential Equations

A general ordinary differential equation (ODE) can be written in the form:

$$
F(x, y, y^{(1)}, y^{(2)}, \dots, y^{(n)}) = 0
$$

where $n$ is the order of the DE.

A linear differential equation can be written as:

$$
a_{n} y^{(n)}(x) + a_{n - 1} y^{(n - 1)}(x) + \dots + a_{0} y(x) = b(x)
$$

More formally, the DE is linear if the equation still holds under the transformation $y^{(i)} \to \lambda y^{(i)}$ for $\lambda \in \mathbb{R}$.

The general solution to a $n$th order DE is an infinite family of functions characterised by $n$ parameters.

## First Order Differential Equations

In general, a first order ODE can be written in the form:

$$
y' = f(x, y)
$$

for some function $f$ of $x$ and $y$.

A useful symmetric form is:

$$
A(x, y) \, \mathrm{d}x + B(x, y) \, \mathrm{d}y = 0
$$

for some functions $A$ and $B$ of $x$ and $y$.

### Exact Equations

Consider the first order DE in the symmetric form. If $A$ and $B$ satisfy the condition:

$$
\frac{\partial A}{\partial y} = \frac{\partial B}{\partial x}
$$

then there exists a function $\Phi(x, y)$ such that:

$$
A(x, y) = \frac{\partial \Phi}{\partial y} \quad \text{and} \quad B(x, y) = - \frac{\partial \Phi}{\partial x}
$$

In this case, the equation is said to be exact because the it is the total derivative of $\Phi$:

$$
\frac{\partial \Phi}{\partial x} \, \mathrm{d}x + \frac{\partial \Phi}{\partial y} \, \mathrm{d}y = 0
$$

so that the solution is just $\Phi(x, y) = C$ for some constant $C$.

If the condition is not satisfied, then the equation is said to be inexact. However, it is always possible to multiply the equation by a function $\Lambda(x, y)$ called the integration factor such that:

$$
\frac{\partial (\Lambda A)}{\partial y} \, \mathrm{d}y =  \frac{\partial (\Lambda B)}{\partial x} \, \mathrm{d}x
$$

There is no general method of finding the integration factor, but sometimes we may assume that $\Lambda$ is a function of $x$ only, in which case the condition becomes:

$$
\Lambda \frac{\partial A}{\partial y} = \Lambda \frac{\partial B}{\partial x} + B \frac{\mathrm{d}\Lambda}{\mathrm{d}x}
$$

so that:

$$
\Lambda \left( \frac{\partial A}{\partial y} - \frac{\partial B}{\partial x} \right) = B \frac{\mathrm{d}\Lambda}{\mathrm{d}x}
$$

which may be solved if $y$ is not involved in the equation.

### Linear Equations

A linear first order ODE is a special class of the inexact equations written in the form:

$$
y' + p(x) y = q(x)
$$

which can be solved by considering the integration factor $\Lambda(x)$ defined as:

$$
\Lambda(x) = \exp{\left( \int p(x) \, \mathrm{d}x \right)}
$$

Multiplying both sides of the equation by $\Lambda(x)$ yields:

$$
\Lambda(x) y' + \Lambda(x) p(x) y = \frac{\mathrm{d}}{\mathrm{d}x} \left( \Lambda(x) y \right) = \Lambda(x) q(x)
$$

which can be integrated directly.

### Separable Equations

If the equation can be reduced to the form:

$$
\begin{split}
    p_{1}(x) q_{1}(y) \, \mathrm{d}x + p_{2}(x) q_{2}(y) \, \mathrm{d}y &= 0 \\
    \frac{p_{1}(x)}{p_{2}(x)} \, \mathrm{d}x + \frac{q_{2}(y)}{q_{1}(y)} \, \mathrm{d}y &= 0
\end{split}
$$

Then the equation can be solved through direct integration, assuming that the integration has a closed form solution.

Special care must be taken with the values where $p_{2}(x)$ or $q_{1}(y)$ becomes zero. At these points, the division is not valid. Nevertheless, consider the case where $q_{1}(y_{0}) = 0$ for some $y_{0}$. At this point, $\mathrm{d}y/\mathrm{d}x$ satisfies the equation, so there is an additional solution to the equation apart from the results from direct integration.

In fact, in cases where division happens and there are possible singularities, such points and the derivative at such points must be investigated to reveal any special solutions.

### Homogeneous Equations

A homogenous function $f(x, y)$ of degree $n \in \mathbb{R}$ satisfies the condition:

$$
f(\lambda x, \lambda y) = \lambda^{n} f(x, y)
$$

for some $\lambda \in \mathbb{R}$.

If $A(x, y)$ and $B(x, y)$ in the symmetric form are both homogenous functions of the same degree, then we have:

$$
\frac{\mathrm{d}y}{\mathrm{d}x} = - \frac{A(x, y)}{B(x, y)}
$$

In general, it is always possible to express the right hand side as a function $F$ of $y/x$, such that the substitution $z = y/x$ yields:

$$
\frac{\mathrm{d}y}{\mathrm{d}x} = v + x \frac{\mathrm{d}z}{\mathrm{d}x} = F(v)
$$

which can be integrated directly.

To prove the that the function $F$ exists, we have:

$$
\begin{split}
\frac{\mathrm{d}y}{\mathrm{d}x} &= - \frac{p(x, zx)}{q(x, yx)} \\
    &= -\frac{x^{n} p(1, z)}{x^{n} q(1, z)} \\
x \frac{\mathrm{d}z}{\mathrm{d}x} + z &= -\frac{p(1, z)}{q(1, z)}
\end{split}
$$

### Bernoulli Equations

A Bernoulli equation has the form:

$$
y' + a(x)y = b(x) y^{n}
$$

Dividing by $y^{n}$, we have:

$$
b(x) - a(x) y^{1-n} = \frac{y'}{y^{n}} = \frac{\mathrm{d}}{\mathrm{d}x} \left( \frac{y^{1-n}}{1 - n} \right)
$$

A substitution $z = y^{1-n}$ leads to a readily solvable equation.

### Riccati Equations

A Riccati equation has the form:

$$
y' = a(x)y^{2} + b(x)y + c(x)
$$

which is generally impossible to solve.

However, if a particular solution $y_{0}(x)$ can be guessed, then the substitution $y(x) = z(x) + y_{0}(x)$ turns the equation into a Bernoulli equation:

$$
z' = \left[ 2a(x) y_{0}(x) + b(x) \right]z + a(x) z^{2}
$$

which can be solved via the method described above.

## General Linear Ordinary Differential Equations

Any ODE can be viewed as a system of first order ODEs, and the system can be formally written in the matrix form:

$$
\dot{\mathbf{y}} = \mathbf{A}(t) \cdot \mathbf{y} + \mathbf{f}(t)
$$

For example, consider the second order ODE:

$$
a_{2}(t) \ddot{y} + a_{1}(t) \dot{y} + a_{0}(t) y = f(t)
$$

which can be recast in the matrix form:

$$
    \frac{\mathrm{d}}{\mathrm{d}t}
    \begin{pmatrix}
        y \\
        y'
    \end{pmatrix}
    =
    \begin{pmatrix}
        0 & 1 \\
        -a_{1}/a_{2} & -a_{0}/a_{2}
    \end{pmatrix}
    \begin{pmatrix}
        y \\
        y'
    \end{pmatrix}
    +
    \begin{pmatrix}
        0 \\
        f(t)
    \end{pmatrix}
$$

For the inhomogeneous case where $\mathbf{f}(t)$ is non-zero, the general solution can be obtained by finding a particular solution and adding it to the solution to the homogenous case. It is obvious that for the homogenous equation, the principle of superposition holds such that if $\mathbf{y}_{1}$ and $\mathbf{y}_{2}$ are two solutions to the homogenous equation, then $C_{1} \mathbf{y}_{1} + C_{2} \mathbf{y}_{2}$ is also a solution.

### General Solution to Homogenous Equations

The solutions to the homogeneous equation form a vector space, and its basis can be expressed as a set of $n$ linearly independent solutions $\left\{ \mathbf{y}_{i}(t) \right\}$, where $n$ in general equals the order of the equation. Linear independence means that for the equation:

$$
\sum_{i} C_{i} \mathbf{y}_{i}(t) = 0
$$

there is only the trivial solution $C_{i} = 0$ for all $i$.

Introduce the fundamental matrix $Y(t)$ with $\mathbf{y}_{i}(t)$ as its columns:

$$
Y(t) = \left( \mathbf{y}_{1}(t) \dots \mathbf{y}_{n}(t) \right)
$$

and the Wronskian which is the determinant of this matrix:

$$
W(t) = \det Y(t)
$$

If the set of solutions $\left\{ \mathbf{y}_{i}(t) \right\}$ is linearly independent, then the Wronskian is non-zero for all $t$. In fact, it suffices to check that the Wronskian is non-zero at a single point $t_{0}$. Note that a zero Wronskian at $t_{0}$ does not necessarily mean that the set of solutions is linearly dependent over the entire domain of the equation.

### Constant Coefficient Linear Equations

Consider the case where the coefficients of the ODE are constants. In this case, the matrix $\mathbf{A}(t)$ is constant and the equation can be written as:

$$
\dot{\mathbf{y}} = \mathbf{A} \cdot \mathbf{y}
$$

Suppose that the matrix $\mathbf{A}$ has $n$ linearly independent eigenvectors $\mathbf{v}_{i}$ with eigenvalues $\lambda_{i}$, so that:

$$
\mathbf{A} \mathbf{v}_{i} = \lambda_{i} \mathbf{v}_{i}
$$

We can guess a solution of the form:

$$
\mathbf{y}_{i}(t) = \xi_{i}(t) \mathbf{v}_{i}
$$

$\xi_{i}(t)$ satisfies:

$$
\dot{\xi}_{i}(t) = \lambda_{i} \xi_{i}(t)
$$

which means that $\xi_{i}(t) = C_{i} e^{\lambda_{i} t}$ for some constant $C_{i}$.

Apparently $\mathbf{y}_{i}(t)$ are linearly independent because $\mathbf{v}_{i}$ are. Therefore, the Wronskian is non-zero and the general solution is:

$$
\mathbf{y}(t) = \sum_{i} C_{i} \mathbf{v}_{i} e^{\lambda_{i} t}
$$

In practice, we diagonalise the matrix $\mathbf{A}$ to obtain:

$$
\mathbf{A} = \mathbf{R} \mathbf{L} \mathbf{R}^{-1}
$$

where $\mathbf{R} = (\mathbf{v}_{1}, \dots, \mathbf{v}_{n})$ is the matrix whose columns are the eigenvectors, and $\mathbf{L}$ is the diagonal matrix whose diagonal elements are the eigenvalues.

The ODE becomes $\dot{\mathbf{y}} = \mathbf{R} \mathbf{L} \mathbf{R}^{-1} \cdot \mathbf{y}$ or:

$$
\dot{(\mathbf{R}^{-1}\mathbf{y})} = \mathbf{L} (\mathbf{R}^{-1} \mathbf{y})
$$

Define $\mathbf{Y} = \mathbf{R}^{-1} \mathbf{y}$, then $\dot{\mathbf{Y}} = \mathbf{L} \mathbf{Y}$, which is just a collection of first order ODEs that are the same as the equations for $\xi_{i}(t)$.

## Normal Modes of a Linear System

The above discussion can be readily extended to the special case of the form:

$$
\ddot{\mathbf{y}} = -\mathbf{A} \cdot \mathbf{y}
$$

where $\mathbf{A}$ is a constant matrix.

Diagonalising $\mathbf{A}$ yields:

$$
\ddot{(\mathbf{R}^{-1}\mathbf{y})} = -\mathbf{L} (\mathbf{R}^{-1} \mathbf{y})
$$

and we are actually solving the equations:

$$
\ddot{\xi}_{i}(t) = -\lambda_{i} \xi_{i}(t)
$$

where $\lambda_{i}$ are the eigenvalues of $\mathbf{A}$ and $\xi_{i}(t)$ are the elements of the transformed vector $\mathbf{Y} = \mathbf{R}^{-1} \mathbf{y}$.

Returning to the original variables, we have:

$$
\mathbf{y} = \mathbf{R} \mathbf{Y}(t) = \sum_{i} \mathbf{v}_{i} \xi_{i}(t)
$$

It is often convenient to make sure that the eigenvectors are normalised, so that $\mathbf{R}$ is an orthogonal matrix and $\mathbf{R}^{-1} = \mathbf{R}^{T}$.

The individual solutions $\mathbf{v}_{i} \xi_{i}(t)$ are called the normal modes of the system.

## Sturm-Liouville Theory

### Second Order Linear Differential Operators

Consider the linear second order differential equation of the form:

$$
\alpha_{2}(x) y'' + \alpha_{1}(x) y' + \alpha_{0}(x) y = f(x)
$$

where $\alpha_{2}$, $\alpha_{1}$, $\alpha_{0}$ and $f$ are given functions of $x$.

We may define an operator $T$ such that:

$$
T \equiv \alpha_{2} \frac{\mathrm{d}^{2}}{\mathrm{d}x^{2}} + \alpha_{1} \frac{\mathrm{d}}{\mathrm{d}x} + \alpha_{0}
$$

so that the equation can be written as $T y = f$.

It is clear that a second order linear differential equation can be written as a system of two first order linear differential equations. Consider the state vector $\mathbf{y} = (y, y')^{T}$ and the matrix $A$:

$$
A =
\begin{pmatrix}
0 & 1 \\
-\alpha_{0}/\alpha_{2} & -\alpha_{1}/\alpha_{2}
\end{pmatrix}
$$

with the vector $\mathbf{f} = (0, f/\alpha_{2})^{T}$.

The equation $T y = f$ can be written as:

$$
\frac{\mathrm{d}}{\mathrm{d}x} \mathbf{y} = A \mathbf{y} + \mathbf{f}
$$

First consider the homogeneous equation $T y = 0$. Given two solutions $\mathbf{y}_{1}$ and $\mathbf{y}_{2}$, the general solution is given by a linear combination of the two. This is true if the solutions are linearly independent, or the Wronskian is non-zero for at least one value of $x$:

$$
W(x) \equiv \det
\begin{pmatrix}
y_{1} & y_{2} \\
y_{1}' & y_{2}'
\end{pmatrix}
$$

If the solutions to the homogeneous equation are known, then the general solution to the inhomogeneous equation can be found by through the Green function defined as:

$$
\boxed{
G(x, t) \equiv \frac{y_{1}(t) y_{2}(x) - y_{1}(x) y_{2}(t)}{\alpha_{2}(t) W(t)}
}
$$

where the Wronskian is defined previously.

Through direct substitution, it can be shown that the solution to the inhomogeneous equation is given by:

$$
y(x) = \int_{a}^{b} G(x, t) f(t) \mathrm{d}t
$$

Further, consider a Dirichlet boundary condition $y(a) = y(b) = 0$. If two solutions $\mathbf{y}_{1}$ and $\mathbf{y}_{2}$ are known satisfying $y_{1, 2}(a) = y_{1, 2}(b) = 0$, then the Green function can be modified to satisfy the boundary conditions:

$$
G(x, t) \equiv \frac{y_{1}(t) y_{2}(x) \theta(x - t) + y_{1}(x) y_{2}(t) \theta(t - x)}{\alpha_{2}(t) W(t)}
$$

where $\theta$ is the Heaviside step function defined as:

$$
\theta(x) =
\begin{cases}
0 & x < 0 \\
1 & x \geq 0
\end{cases}
$$

We can write $G(x, t)$ more explicitly as:

$$
\boxed{
G(x, t) =
\begin{cases}
y_{1}(t) y_{2}(x) / \alpha_{2}(t) W(t) & x \geq t \\
y_{1}(x) y_{2}(t) / \alpha_{2}(t) W(t) & x < t
\end{cases}
}
$$

## Sturm-Liouville Operators

Let us restrict our attention to a special class of linear differential operators of the form:

$$
T_{SL} \equiv \frac{1}{w} \left[ \frac{\mathrm{d}}{\mathrm{d}x} \left( p \frac{\mathrm{d}}{\mathrm{d}x} \right) + q \right]
$$

where $w$, $p$ and $q$ are given smooth functions of $x$ on the interval $[a, b]$.

It can be shown that any second order linear differential operator with $\alpha_{2} \neq 0$ can be written in the form of a Sturm-Liouville operator with:

$$
\boxed{
\begin{split}
p(x) &= \exp \left[ \int_{a}^{x} \frac{\alpha_{1}(t)}{\alpha_{2}(t)} \mathrm{d}t \right] \\
w(x) &= \frac{1}{\alpha_{2}(x)} \exp \left[ -\int_{a}^{x} \frac{\alpha_{1}(t)}{\alpha_{2}(t)} \mathrm{d}t \right] = \frac{p(x)}{\alpha_{2}(x)} \\
q(x) &= \alpha_{0}(x) w(x)
\end{split}
}
$$

$T_{SL}$ is Hermitian on the space $L_{w}^{2}[a, b]$ with respect to the weight function $w$ if it satisfies:

$$
p(a) = p(b) = 0
$$

### Eigenfunctions

It is instructive to consider the eigenvalue problem for the Sturm-Liouville operator:

$$
T_{SL} y = \lambda y
$$

where $\lambda \in \mathbb{R}$ since $T_{SL}$ is Hermitian.

Suppose that the eigenvalue problem has been solved and the eigenfunctions $y_{n}(x)$ and eigenvalues $\lambda_{n}$ are known. Then let us return to the inhomogeneous equation:

$$
T_{SL} y = f
$$

Since the eigenfunctions form a complete set, the solution $y(x)$ can be written as a linear combination of the eigenfunctions:

$$
y(x) = \sum_{r=0}^{\infty} c_{r} y_{r}(x)
$$

To determine $c_{r}$, note that:

$$
f(x) = T_{SL} y(x) = \sum_{r=0}^{\infty} c_{r} T_{SL} y_{r}(x) = \sum_{r=0}^{\infty} c_{r} \lambda_{r} y_{r}(x)
$$

Then, knowing $f(x)$ and the eigenfunctions, the constants $c_{r}$ can be determined by exploiting the orthogonality of the eigenfunctions. Taking the inner product (with the weight function) of both sides with $y_{j}$ and integrating:

$$
\int_{a}^{b} w(t) y_{j}^{*}(t) f(t) \, \mathrm{d}z = \sum_{r=0}^{\infty} \int_{a}^{b} c_{r} \lambda_{r} w(t) y_{j}^{*}(t) y_{r}(t) \, \mathrm{d}z
$$

The integrals on the right side vanish unless $j = r$ due to the orthogonality of the eigenfunctions. Therefore, the constants $c_{r}$ are given by:

$$
c_{r} = \frac{1}{\lambda_{r}} \frac{\int_{a}^{b} w(t) y_{r}^{*}(t) f(t) \, \mathrm{d}z}{\int_{a}^{b} w(t) y_{r}^{*}(t) y_{r}(t) \, \mathrm{d}z}
$$

Suppose that the eigenfunctions are normalised to $\hat{y}_{n}$ so that the denominator is unity. We the solution:

$$
\boxed{
y(x) = \sum_{r=0}^{\infty} \hat{y}_{r}(x) \frac{1}{\lambda_{r}} \int_{a}^{b} w(t) \hat{y}_{r}^{*}(t) f(t) \, \mathrm{d}t
}
$$

Compare this with the Green's function solution, we have an expression for $G(x, t)$:

$$
\boxed{
G(x, t) = w(t) \sum_{r=0}^{\infty} \frac{\hat{y}_{r}^{*}(t) \hat{y}_{r}(x)}{\lambda_{r}}
}
$$
