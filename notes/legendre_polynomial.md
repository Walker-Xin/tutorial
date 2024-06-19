# Legendre Polynomial

## Legendre's Equation

The Legendre differential equation has the following form:

$$
\boxed{
(1-x^2)y'' - 2xy' + l(l+1)y = 0
}
$$

where $l$ is an arbitrary constant.

We may assume a solution of the form $y(x) = \sum_{n=0}^{\infty} a_n x^n$. To find coefficients $a_n$, we substitute the presumed solution into the equation and obtain the following recursive relationship:

$$
a_{k+2} = \frac{(k-l)(k+l+1)}{(k+1)(k+2)} a_{k}
$$

Naturally there are two initial conditions, namely $a_0$ and $a_1$, that need to be given to generate the whole series. Note that the solution may be written in the form $y(x) = a_0 y_0(x) + a_1 y_1(x)$, where $y_0(x)$ is a polynomial series of only even powers and $y_1(x)$ is of only odd powers.

Note that for a general value of $l$, the series $y(x)$ only converges if $\lvert x \rvert < 1$. For certain physical systems, however, we wish the series to also converge for $\lvert x \rvert = 1$. This can be achieved if we only allow for integer values of $l$, such that the above recursive relationship terminates beyond $k=l$. For an even $l$, for example, $a_{l+2} = 0$ and any coefficients above are all zero. Note that the odd power series is not terminated and we must set $a_1$ to be zero so that $y(x)$ converges.

## Legendre Polynomials

For each positive integer $l$, we obtain a polynomial solution to the Legendre equation. If the value of $a_0$ or $a_1$ is set such that $y(1) = 1$, then the resulting polynomials are called **Legendre polynomials**, written as $P_{l}(x)$ corresponding to the specific value of $l$. Note that we have essentially solved an eigenvalue problem, as the Legendre equation can be written in the form $f(D)y(x) = l(l+1)y(x)$, where f(D) is a differential operator. Acting on eigenfunctions $y(x)$ (the Legendre polynomials), the operators produce multiples of the eigenfunctions. The eigenvalues of the system are thus integer values of $l$.

To find a general form for the Legendre polynomials, first consider the function:

$$
v = (x^2 - 1)^l
$$

We wish to prove that $v^{(l)}$ is a solution to the Legendre equation, where $(l)$ denotes the $l$ th derivative, and then we find a suitable coefficient so that $y(1) = 1$. First note:

$$
(x^2 - 1) v^{(1)} = 2lxv
$$

Differentiating both sides $l+1$ times with Leibniz\' rule:

$$
(x^2 - 1) v^{(l+2)} + (l+1) (2x) (v^{(l+1)}) + (\frac{l(l+1)}{2!}) (2) (v^{(l)}) = 2lx v^{(l+1)} + 2l(l+1) v^{(l)}
$$

Simplifying, we obtain:

$$
(1-x^2) (v^{(l)})'' - 2x (v^{(l)})' + l(l+1) v^{(l)} = 0
$$

Further, write $v = (x+1)^{l} (x-1)^{l}$, differentiating $l$ times with Leibniz\' rule:

$$
v^{(l)} = ((x+1)^{l}) (l!) + (l)(l(x+1)^{l-1})((l-1)!(x-1)) + ...
$$

Any term beyond the first one contains a factor $(x-1)$ so they vanish at $x = 1$. Thus if we wish to have $y(x) = kv(x)$ to be unity at $x = 1$, $k$ must take the value $2^{l}l!$. Therefore we obtain the Legendre polynomials:

$$
\boxed{
P_{l}(x) = \frac{1}{2^{l}l!} \frac{\mathrm{d}^{l}}{\mathrm{d} x^l} (x^2 - 1)^{l}
}
$$

The first few Legendre polynomials are:

$$
\boxed{
P_{0}(x) = 1 \quad P_{1}(x) = x \quad P_{2}(x) = \frac{1}{2}(3x^2 - 1) \quad P_{3}(x) = \frac{1}{2}(5x^3 - 3x)
}
$$

### Generating function

The Legendre polynomials can also be defined by a generating function $\Phi(x, t)$:

$$
\boxed{
\Phi(x, t) \equiv \frac{1}{\sqrt{1 - 2xt + t^2}} = \sum_{r=0}^{\infty} P_r(x) t^r
}
$$

### Orthogonality of Legendre Polynomials

Legendre polynomials are orthogonal. Their orthogonality can be proven in the following way.

Assume, without lose of generality, that $m \leq n$. We first investigate the case where $m<n$. The integral becomes:

$$
\frac{1}{2^{m+n}m!n!} \int_{-1}^{1} \frac{\mathrm{d}^{m}}{\mathrm{d} x^{m}} (x^2 - 1)^{m} \frac{\mathrm{d}^{n}}{\mathrm{d} x^{n}} (x^2 - 1)^{n} \mathrm{d} x
$$

Focusing on the integral, we can apply integration by parts multiple times to yield:

$$
\begin{split}
&\int_{-1}^{1} \frac{\mathrm{d}^{m}}{\mathrm{d} x^{m}} (x^2 - 1)^{m} \frac{\mathrm{d}^{n}}{\mathrm{d} x^{n}} (x^2 - 1)^{n} \mathrm{d} x \\
=& \frac{\mathrm{d}^{m}}{\mathrm{d} x^{m}} (x^2 - 1)^{m} \frac{\mathrm{d}^{n-1}}{\mathrm{d} x^{n-1}} (x^2 - 1)^{n} \Bigr|_{-1}^{1} - \int_{-1}^{1} \frac{\mathrm{d}^{m+1}}{\mathrm{d} x^{m+1}} (x^2 - 1)^{m} \frac{\mathrm{d}^{n-1}}{\mathrm{d} x^{n-1}} (x^2 - 1)^{n} \mathrm{d} x \\
=& -\int_{-1}^{1} \frac{\mathrm{d}^{m+1}}{\mathrm{d} x^{m+1}} (x^2 - 1)^{m} \frac{\mathrm{d}^{n-1}}{\mathrm{d} x^{n-1}} (x^2 - 1)^{n} \mathrm{d} x \\
=& (-1)^{m} \int_{-1}^{1} \frac{\mathrm{d}^{2m}}{\mathrm{d} x^{2m}} (x^2 - 1)^{m} \frac{\mathrm{d}^{n-m}}{\mathrm{d} x^{n-m}} (x^2 - 1)^{n} \mathrm{d} x \\
=& (-1)^{m} (2m)! \frac{\mathrm{d}^{n-m-1}}{\mathrm{d} x^{n-m-1}} (x^2 - 1)^{n} \Bigr|_{-1}^{1} \\
=& 0
\end{split}
$$

If on the other hand $m=n$, then the integral becomes:

$$
\begin{split}
&\int_{-1}^{1} \frac{\mathrm{d}^{n}}{\mathrm{d} x^{n}} (x^2 - 1)^{n} \frac{\mathrm{d}^{n}}{\mathrm{d} x^{n}} (x^2 - 1)^{n} \mathrm{d} x \\
=& (-1)^{n} \int_{-1}^{1} \frac{\mathrm{d}^{2n}}{\mathrm{d} x^{2n}} (x^2 - 1)^{n} \frac{\mathrm{d}^{0}}{\mathrm{d} x^{0}} (x^2 - 1)^{n} \mathrm{d} x \\
=& (-1)^{n} (2n)! \int_{-1}^{1} (x^2 - 1)^{n} \mathrm{d} x
\end{split}
$$

Now denote $I_{n} = \int_{-1}^{1} (x^2 - 1)^{n} \mathrm{d} x$. Note the following recursive result:

$$
\begin{split}
I_{n} &= x (x^2 - 1)^{n} \Bigr|_{-1}^{1} - \int_{-1}^{1} x (2nx) (x^2 - 1)^{n-1} \mathrm{d} x \\
    &= -2n \int_{-1}^{1} (x^2 - 1)^{n} (x^2 - 1)^{n-1} \mathrm{d} x \\
    &= -2n I_{n} - 2n I_{n-1}
\end{split}
$$

Thus, $I_{n} = -\frac{2n}{2n+1} I_{n-1}$ and:

$$
I_{n} =(-1)^{n} \frac{2^{2n}(n!)^2}{(2n+1)!}
$$

Combining the above results and simplifying, we have the desired conclusion:

$$
\boxed{
\int_{-1}^{1} P_m(x) P_n(x) \mathrm{d} x = \frac{2}{2n + 1} \delta_{mn}
}
$$

## Associated Legendre Functions

The associated Legendre equation has the form:

$$
\boxed{
(1-x^2)y'' - 2xy' + [l(l+1) - \frac{m^2}{1-x^2}]y = 0
}
$$

with $m^2 \leq l^2$.

While this equation may be solved with the series approach, the Legendre polynomials may be made use of instead.

Consider the function $y(x) = (1-x^2)^{m/2} u$, where $u$ is a function of $x$. Substituting into the associated Legendre equation, have:

$$
(1-x^2)u'' - 2(m+1)xu' + [l(l+1) - m(m+1)]u = 0
$$

If $m = 0$, this is the Legendre\'s equation with solutions $P_{l}(x)$. Differentiating the equation further, we have:

$$
(1-x^2)u''' - 2(m+2)xu'' + [l(l+1) - (m+1)(m+2)]u' = 0
$$

But this has the same form as the previous equation with $u'$ in place of $u$ and $(m+1)$ in place of $m$. Thus, if $P_{l}(x)$ is a solution to the equation with $m = 0$, then $P_{l}'(x)$ is a solution with $m = 1$. In general then, the solution to the associated Legendre equation is:

$$
\begin{split}
\boxed{
P_{l}^{m}(x) = (1-x^2)^{m/2} \frac{\mathrm{d}^{m}}{\mathrm{d} x^m} P_{l}(x)
}
\end{split}
$$

They are called the associated Legendre functions and serve as solutions to the angular parts of the Laplace\'s equation in spherical coordinates.

### Orthogonality of Associated Legendre Functions

Associated Legendre functions are also orthogonal if they have the same $m$ index. Note first that the functions must satisfy the associated Legendre equation, so for $P_{l}^{m}(x)$ and $P_{k}^{m}(x)$, where $l \ne k$:

$$
(1-x^2)P_{l}^{m \prime \prime}(x) - 2xP_{l}^{m \prime}(x) + [l(l+1) - \frac{m^2}{1-x^2}]P_{l}^{m}(x) = 0
\tag{1}
$$

$$
(1-x^2)P_{k}^{m \prime \prime}(x) - 2xP_{k}^{m \prime}(x) + [l(l+1) - \frac{m^2}{1-x^2}]P_{k}^{m}(x) = 0
\tag{2}
$$

Now investigate the integral, which equals zero:

$$
\int_{-1}^{1} (1) \times P_{k}^{m} - (2) \times P_{l}^{m} \equiv 0
$$

Expanding the expression yields:

$$
\int_{-1}^{1} P_{k}^{m} \frac{\mathrm{d}}{\mathrm{d} x}[(1-x^2)P_{l}^{m \prime}] - P_{l}^{m} \frac{\mathrm{d}}{\mathrm{d} x}[(1-x^2)P_{k}^{m \prime}] \mathrm{d} x + \int_{-1}^{1} [l(l+1) - k(k+1)] P_{l}^{m} P_{k}^{m} = 0
$$

Using integration by parts on the first term:

$$
\begin{split}
&\int_{-1}^{1} P_{k}^{m} \frac{\mathrm{d}}{\mathrm{d} x}[(1-x^2)P_{l}^{m \prime}] - P_{l}^{m} \frac{\mathrm{d}}{\mathrm{d} x}[(1-x^2)P_{k}^{m \prime}] \mathrm{d} x \\
=& [(1-x^2) P_{l}^{m \prime} P_{k}^{m} - (1-x^2) P_{k}^{m \prime} P_{l}^{m}] \Bigr|_{-1}^{1} - \int_{-1}^{1} (1-x^2)(P_{l}^{m \prime} P_{k}^{m \prime} - P_{k}^{m \prime}P_{l}^{m \prime}) \\
=& 0
\end{split}
$$

Thus $\int_{-1}^{1} [l(l+1) - k(k+1)] P_{l}^{m} P_{k}^{m} = 0$. Since $l \ne k$, we conclude:

$$
\boxed{
\int_{-1}^{1} P_{l}^{m}(x) P_{k}^{m}(x) \mathrm{d} x = M_{l}^{m} \delta_{kl}
}
$$

where $M_{l}^{m} = \int_{-1}^{1} (P_{l}^{m}(x))^2 \mathrm{d} x = \frac{2}{2l+1} \frac{(l+m)!}{(l-m)!}$.
