# Laplace\'s Equation

Many physical systems can be modelled with equations that involve the use of Laplacian. One such example is the case of heat diffusion:

$$
\frac{\partial T}{\partial t} = D \nabla^2 T
$$

For the steady state case, where $\frac{\partial T}{\partial t} = 0$, the equation is reduced to the **Laplace\'s equation**:

$$
\boxed{
\nabla^2 T = 0
}
$$

Further, in electrodynamics, Gauss\'s law states that $\nabla \cdot \mathbf{E} = \epsilon_{0} \rho$. Noting that $\mathbf{E} = - \nabla V$, in free space where $\rho = 0$, we will have the Laplace\'s equation:

$$
\boxed{
\nabla^2 V = 0
}
$$

## Separation of Variables under Spherical Coordinates

Consider the Laplacian of a function under spherical coordinates:

$$
\nabla^2 T = \frac{1}{r^2} \frac{\partial}{\partial r}(r^2 \frac{\partial T}{\partial r}) + \frac{1}{r^2 \sin{\theta}} \frac{\partial}{\partial \theta}(\sin{\theta} \frac{\partial T}{\partial \theta}) + \frac{1}{r^2 \sin^{2}{\theta}} \frac{\partial^2 T}{\partial \phi^2} = 0
$$

Consider solutions of the form $T(r, \theta, \phi) = R(r)Y(\theta, \phi)$, such that the variables can be separated. Substitutions yields:

$$
\frac{Y}{r^2} \frac{\mathrm{d}}{\mathrm{d} r}(r^2 \frac{\mathrm{d} R}{\mathrm{d} r}) + \frac{R}{r^2 \sin{\theta}} \frac{\partial}{\partial \theta}(\sin{\theta} \frac{\partial Y}{\partial \theta}) + \frac{R}{r^2 \sin^{2}{\theta}} \frac{\partial^2 Y}{\partial \phi^2} = 0
$$

Multiplying by $\frac{r^2}{RY}$, have:

$$
\frac{1}{R} \frac{\mathrm{d}}{\mathrm{d} r}(r^2 \frac{\mathrm{d} R}{\mathrm{d} r}) = -\frac{1}{Y \sin{\theta}} \frac{\partial}{\partial \theta}(\sin{\theta} \frac{\partial Y}{\partial \theta}) - \frac{1}{Y \sin^{2}{\theta}} \frac{\partial^2 Y}{\partial \phi^2}
$$

Notice that the left side of the equation is a function of $r$ only while the right hand side is of $\theta$ and $\phi$ only. This suggests that they must be of a constant:

$$
\boxed{
\frac{\mathrm{d}}{\mathrm{d} r}(r^2 \frac{\mathrm{d} R}{\mathrm{d} r}) = l(l+1)R
}
\tag{1}
$$

$$
\frac{1}{\sin{\theta}} \frac{\partial}{\partial \theta}(\sin{\theta} \frac{\partial Y}{\partial \theta}) + \frac{1}{\sin^{2}{\theta}} \frac{\partial^2 Y}{\partial \phi^2} = -l(l+1)Y
$$

where $l$ is a constant.

We may wish to further separate $Y$ such that $Y(\theta, \phi) = \Theta(\theta) \Phi(\phi)$. This leads to:

$$
\frac{\Phi}{\sin{\theta}} \frac{\mathrm{d}}{\mathrm{d} \theta}(\sin{\theta} \frac{\mathrm{d} \Theta}{\mathrm{d} \theta}) + \frac{\Theta}{\sin^{2}{\theta}} \frac{\mathrm{d} \Phi}{\mathrm{d} \phi^2} = -l(l+1) \Theta \Phi
$$

Similarly, multiplying by $\frac{\sin^{2}{\theta}}{\Theta \Phi}$ yields:

$$
\frac{\sin{\theta}}{\Theta} \frac{\mathrm{d}}{\mathrm{d} \theta}(\sin{\theta} \frac{\mathrm{d} \Theta}{\mathrm{d} \theta}) + l(l+1) \sin^{2}{\theta} = -\frac{1}{\Phi} \frac{\mathrm{d} \Phi}{\mathrm{d} \phi^2}
$$

This suggests that both sides of the equations must also be of a constant:

$$
\boxed{
\frac{\mathrm{d}^{2} \Phi}{\mathrm{d} \phi^2} = -m^2 \Phi
}
\tag{2}
$$

$$
\boxed{
\frac{1}{\sin{\theta}} \frac{\mathrm{d}}{\mathrm{d} \theta}(\sin{\theta} \frac{\mathrm{d} \Theta}{\mathrm{d} \theta}) = [\frac{m^2}{\sin^{2}{\theta}} - l(l+1)]\Theta
}
\tag{3}
$$

where $m$ is a constant.

### Radial Equation

First consider the radial equation $(1)$. Expanding the differential gives:

$$
r^2 \frac{\mathrm{d}^{2} R}{\mathrm{d} r^2} + 2r \frac{\mathrm{d} R}{\mathrm{d} r} - l(l+1)R
$$

Suppose $R(r) \propto r^n$, have $n(n+1) r^n + 2n r^n - l(l+1)r^n = 0$, or $n(n+1) = l(l+1)$. Solving yields $n_1 = l$ and $n_2 = -(l+1)$. Thus the general solution of $R(r)$ is:

$$
R(r) = A r^l + B \frac{1}{r^{l+1}}
$$

### Angular Equations

Next consider the equation involving $\phi$. Clearly the general solution is of the form:

$$
\Phi(\phi) = e^{im\phi}
$$

Note that due to the nature of the spherical coordinate system, we must have $\Phi(\phi) = \Phi(\phi + 2\pi)$ for any value of $\phi$. Therefore, we need $e^{i 2\pi m} = 1$ and thus $m \in \mathbb{Z}$. This is called a natural boundary condition for $\Phi$.

As for the equation involving $\theta$, it may be expanded into the following form with the substitution $x \equiv \cos(\theta)$ and $y(x) \equiv \Theta(\theta)$:

$$
\boxed{
(1-x^2) \frac{\mathrm{d}^{2} y}{\mathrm{d} x^2} - 2x \frac{\mathrm{d} y}{\mathrm{d} x} + [l(l+1) - \frac{m^2}{1-x^2}]y = 0
}
$$

This is a variation of the Legendre differential equation called the **associated Legendre equation**. The equation\'s solutions are **associated Legendre functions** of the form:

$$
P_{l}^{m}(x) \equiv (1-x^2)^{m/2} \frac{\mathrm{d}^{m}}{\mathrm{d} x^m} P_{l}(x)
$$

where

$$
P_{l}(x) \equiv \frac{1}{2^{l}l!} \frac{\mathrm{d}^{l}}{\mathrm{d} x^l} (x^2 - 1)^{l}
$$

are called the **Legendre polynomials**.

Thus, the solution of $\Theta$ is:

$$
\Theta(\theta) = P_{l}^{m}(\cos{\theta})
$$

If, on the other hand, we can assume rotational symmetry about the z-axis, such that the solution does not depend on $\phi$, then $\Phi$ takes a constant value and $m = 0$. In this case, the equation is reduced to the form:

$$
(1-x^2) \frac{\mathrm{d}^{2} y}{\mathrm{d} x^2} - 2x \frac{\mathrm{d} y}{\mathrm{d} x} + l(l+1)y = 0
$$

which is the standard Legendre equation that have **Legendre polynomials** $P_{l}(x)$ as its general solutions.

### General Solution

Collecting every previous solution, we thus obtain the general solution to the Laplace\'s equation under spherical coordinates:

$$
\boxed{
\begin{split}
T(r, \theta, \phi) &= R(r) \Theta(\theta) \Phi(\phi) \\
  &= \sum_{l=0}^{\infty} \sum_{m=0}^{l} [A_{l}^{m} r^l + B_{l}^{m} \frac{1}{r^{l+1}}] e^{im\phi} P_{l}^{m}(\cos{\theta})
\end{split}
}
$$

where two constants $A_{l}^{m}$ and $B_{l}^{m}$ are determined by the boundary conditions of the system.

If azimuthal symmetry is present, the general solution gets simplified to:

$$
\boxed{
T(r, \theta) = \sum_{l=0}^{\infty} [A_{l} r^l + B_{l} \frac{1}{r^{l+1}}] P_{l}(\cos{\theta})
}
$$

where $A_{l}$ and $B_{l}$ are similarly determined by the boundary conditions.

## Separation of Variables under Cylindrical Coordinates
