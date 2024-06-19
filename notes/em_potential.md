# Electromagnetism - Potentials and Fields

## Poisson's and Laplace's Equations

Poisson's equation gives the electric potential $\phi$ for a given charge distribution $\rho$:

$$
\nabla^2 \phi = -\frac{\rho}{\epsilon_0}
$$

This reduces to Laplace's equation in free space where $\rho = 0$:

$$
\nabla^2 \phi = 0
$$

The Laplacian operator takes different forms in different coordinate systems. In Cartesian coordinates, the Laplace's equation reads:

$$
\frac{\partial^2 \phi}{\partial x^{2}} + \frac{\partial^2 \phi}{\partial y^{2}} + \frac{\partial^2 \phi}{\partial z^{2}} = 0
$$

In spherical coordinates, the Laplace's equation is:

$$
\frac{1}{r^{2}} \frac{\partial}{\partial r} \left( r^{2} \frac{\partial \phi}{\partial r} \right) + \frac{1}{r^{2} \sin{\theta}} \frac{\partial}{\partial \theta} \left( \sin{\theta} \frac{\partial \phi}{\partial \theta} \right) + \frac{1}{r^{2} \sin^{2}{\theta}} \frac{\partial^{2} \phi}{\partial \phi^{2}} = 0
$$

In cylindrical coordinates, the equation becomes:

$$
\frac{1}{r} \frac{\partial}{\partial r} \left( r \frac{\partial \phi}{\partial r} \right) + \frac{1}{r^{2}} \frac{\partial^{2} \phi}{\partial \phi^{2}} + \frac{\partial^{2} \phi}{\partial z^{2}} = 0
$$

## Laplace's Equation in Spherical Coordinates

Consider the Laplace's equation in spherical coordinates. Suppose that the solution is separable, i.e. $\phi(r, \theta, \phi) = R(r) \Theta(\theta) \Phi(\phi)$. Then the Laplace's equation becomes:

$$
\frac{1}{r^{2}} \frac{\partial}{\partial r} \left( r^{2} \frac{\partial R}{\partial r} \right) \Theta \Phi + \frac{1}{r^{2} \sin{\theta}} \frac{\partial}{\partial \theta} \left( \sin{\theta} \frac{\partial \Theta}{\partial \theta} \right) R \Phi + \frac{1}{r^{2} \sin^{2}{\theta}} \frac{\partial^{2} \Phi}{\partial \phi^{2}} R \Theta = 0
$$

Dividing through by $\phi = R \Theta \Phi$ and multiplying by $r^{2}\sin^{2}{\theta}$, we get:

$$
\sin^{2}{\theta} \left[ \frac{1}{R} \frac{\mathrm{d}}{\mathrm{d}r} \left( r^{2} \frac{\mathrm{d}R}{\mathrm{d}r} \right) + \frac{1}{\Theta \sin{\theta}} \frac{\mathrm{d}}{\mathrm{d}\theta} \left( \sin{\theta} \frac{\mathrm{d}\Theta}{\mathrm{d}\theta} \right) \right] + \frac{1}{\Phi} \frac{\mathrm{d}^{2}\Phi}{\mathrm{d}\phi^{2}} = 0
$$

The last term does not depend on $r$ or $\theta$ while the first two terms do not depend on $\phi$. The only way for this to be true is if the last term is a constant, say $-m^{2}$. Then:

$$
\frac{\mathrm{d}^{2}\Phi}{\mathrm{d}\phi^{2}} = -m^{2} \Phi
$$

This can be easily solved to give:

$$
\Phi(\phi) = e^{\pm im\phi}
$$

Note that due to the periodicity of the problem, we must have $\Phi(\phi) = \Phi(\phi + 2\pi)$. This means that $m$ must be an integer.

It can be argued the same way that the first two terms must be equal to a constant. Suppose that the first term is equal to $l(l+1)$. Then two equations result:

$$
\frac{\mathrm{d}}{\mathrm{d}r} \left( r^{2} \frac{\mathrm{d}R}{\mathrm{d}r} \right) = l(l+1) R
$$

and

$$
\frac{1}{\sin{\theta}} \frac{\mathrm{d}}{\mathrm{d}\theta} \left( \sin{\theta} \frac{\mathrm{d}\Theta}{\mathrm{d}\theta} \right) = \left[ \frac{m^{2}}{\sin^{2}{\theta}} - l(l+1) \right] \Theta
$$

For the radial equation, the Ansatz $R(r) = r^{n}$ can be used to give the solution:

$$
R(r) = A r^{l} + B r^{-(l+1)}
$$

For the polar equation, the substitution $x \equiv \cos{\theta}$ and $y(x) \equiv \Theta(\theta)$ can be used to transform the equation:

$$
(1-x^2) \frac{\mathrm{d}^{2} y}{\mathrm{d} x^2} - 2x \frac{\mathrm{d} y}{\mathrm{d} x} + \left[ l(l+1) - \frac{m^2}{1-x^2} \right]y = 0
$$

This is the associated Legendre equation. The solutions are the associated Legendre polynomials $P_{l}^{m}(x)$ defined as:

$$
P_{l}^{m}(x) = (1-x^2)^{m/2} \frac{\mathrm{d}^{m}}{\mathrm{d} x^m} P_{l}(x)
$$

where $P_{l}(x)$ are the Legendre polynomials defined as:

$$
P_{l}(x) = \frac{1}{2^{l}l!} \frac{\mathrm{d}^{l}}{\mathrm{d} x^l} (x^2 - 1)^{l}
$$

Note that in the case of $m = 0$, the associated Legendre polynomials reduce to the Legendre polynomials. This can be interpreted as an assumed azimuthal symmetry.

Collecting the results, the general solution to the Laplace's equation in spherical coordinates is:

$$
\phi(r, \theta, \phi) = \sum_{l=0}^{\infty} \sum_{m=-l}^{l} \left[ A_{l}^{m} r^{l} + B_{l}^{m} r^{-(l+1)} \right] P_{l}^{m}(\cos{\theta}) e^{im\phi}
$$

In the case of azimuthal symmetry, the special solution is:

$$
\phi(r, \theta) = \sum_{l=0}^{\infty} \left[ A_{l} r^{l} + B_{l} r^{-(l+1)} \right] P_{l}(\cos{\theta})
$$

## Laplace's Equation in Cylindrical Coordinates

Consider the Laplace's equation in cylindrical coordinates. Suppose that the solution is separable, i.e. $\phi(r, \phi, z) = R(r) \Phi(\phi) Z(z)$. Then the Laplace's equation becomes:

$$
\frac{1}{r} \frac{\mathrm{d}}{\mathrm{d}r} \left( r \frac{\mathrm{d}R}{\mathrm{d}r} \right) \Phi Z + \frac{1}{r^{2}} \frac{\mathrm{d}^{2}\Phi}{\mathrm{d}\phi^{2}} R Z + \frac{\mathrm{d}^{2}Z}{\mathrm{d}z^{2}} R \Phi = 0
$$

Dividing through by $R \Phi Z$ and multiplying by $r^{2}$, we get:

$$
\frac{r}{R} \frac{\mathrm{d}}{\mathrm{d}r} \left( r \frac{\mathrm{d}R}{\mathrm{d}r} \right) + \frac{1}{\Phi} \frac{\mathrm{d}^{2}\Phi}{\mathrm{d}\phi^{2}} + \frac{r^{2}}{Z} \frac{\mathrm{d}^{2}Z}{\mathrm{d}z^{2}} = 0
$$

Following the same argument as in the spherical case, we assert that the second term is a constant, say $-n^{2}$. Then:

$$
\frac{\mathrm{d}^{2}\Phi}{\mathrm{d}\phi^{2}} = -n^{2} \Phi
$$

which has the solution:

$$
\Phi(\phi) = e^{\pm in\phi}
$$

where $n$ is an integer for periodicity.

## Multiple Expansion

The potential due to a charge distribution $\rho$ can be expressed as:

$$
\phi(\mathbf{r}) = \frac{1}{4\pi\epsilon_0} \int \frac{\rho(\mathbf{r}')}{\left\lvert \mathbf{r} - \mathbf{r}' \right\rvert} \, \mathrm{d}V'
$$

We may write $\left\lvert \mathbf{r} - \mathbf{r}' \right\rvert^{2}$ as:

$$
\left\lvert \mathbf{r} - \mathbf{r}' \right\rvert^{2} = r^{2} + r'^{2} - 2rr' \cos{\theta} = r^{2} \left[ 1 + \left( \frac{r'}{r} \right)^{2} - 2 \left( \frac{r'}{r} \right) \cos{\theta} \right]
$$

where $\theta$ is the angle between $\mathbf{r}$ and $\mathbf{r}'$.

This is reminiscent of the generating function for Legendre polynomials, meaning that we can write:

$$
\frac{1}{\left\lvert \mathbf{r} - \mathbf{r}' \right\rvert} = \frac{1}{r} \sum_{n=0}^{\infty} \left( \frac{r'}{r} \right)^{n} P_{l}(\cos{\theta})
$$

Therefore, the potential can be written as:

$$
\begin{split}
\phi(\mathbf{r}) &= \frac{1}{4\pi\epsilon_0} \sum_{n=0}^{\infty} \frac{1}{r^{n+1}} \int (r')^{n} P_{n}(\cos{\theta}) \rho(\mathbf{r}') \, \mathrm{d}V' \\
&= \frac{1}{4\pi\epsilon_0} \left[ \frac{1}{r} \int \rho(\mathbf{r}') \, \mathrm{d}V' + \frac{1}{r^{2}} \int r' \cos{\theta} \rho(\mathbf{r}') \, \mathrm{d}V' + \frac{1}{r^{3}} \int (r')^{2} \left( \frac{3}{2} \cos^{2}{\theta} - \frac{1}{2} \right) \, \mathrm{d}V' + ... \right]
\end{split}
$$

This is called a multipole expansion of the potential due to a charge distribution. The first term is the monopole term, the second term is the dipole term, the third term is the quadrupole term, and so on.
