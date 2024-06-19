# Electromagnetism - Electrostatics

## Coulomb's Law

Coulomb's law states that the force by a charge $q_{1}$ on another charge $q_{2}$ is given by:

$$
\mathbf{F} = \frac{1}{4\pi \epsilon_{0}} \frac{q_{1} q_{2}}{\left\lvert \mathbf{r}_{2} - \mathbf{r}_{1} \right\rvert^{2}} \hat{\mathbf{d}}
$$

where $\epsilon_{0}$ is the permittivity of free space, and $\hat{\mathbf{d}} \equiv (\mathbf{r}_{2} - \mathbf{r}_{1})/\left\lvert \mathbf{r}_{2} - \mathbf{r}_{1} \right\rvert$ is the unit vector pointing from $q_{1}$ to $q_{2}$.

We may define a vector field called the electric field, as the force per unit charge that would be experienced by a test charge at a given point in space due to a charge $q$ at point $\mathbf{r}_{0}$:

$$
\mathbf{E}(\mathbf{r}) = \frac{1}{4\pi \epsilon_{0}} \frac{q}{\left\lvert \mathbf{r} - \mathbf{r}_{0} \right\rvert^{2}} \hat{\mathbf{d}}
$$

where $\mathbf{r}$ is the position of the test charge and $\hat{\mathbf{d}} \equiv (\mathbf{r} - \mathbf{r}_{0})$ is the unit vector pointing from $\mathbf{r}_{0}$ to $\mathbf{r}$.

The electric force and field obey the principle of superposition, so that the total field(force) produced by a collection of charges $q_{i}$ is the sum of the fields produced by each charge:

$$
\mathbf{E}(\mathbf{r}) = \sum_{i} \mathbf{E}_{i}(\mathbf{r}) = \frac{1}{4\pi \epsilon_{0}} \sum_{i} \frac{q_{i}}{\left\lvert \mathbf{r} - \mathbf{r}_{i} \right\rvert^{2}} \hat{\mathbf{d}}_{i}
$$

## Electric Potential

The electric field is a conservative field, meaning that the path integral of $\mathbf{E}$ along a closed path is zero. This implies that the electric field is a gradient of a scalar field called the electric potential $\phi$:

$$
\mathbf{E} = -\nabla \phi
$$

The electric potential is defined as the (negative of) path integral of $\mathbf{E}$ from a reference point $\mathcal{O}$ to $\mathbf{r}$:

$$
\phi(\mathbf{r}) = -\int_{\mathcal{O}}^{\mathbf{r}} \mathbf{E}(\mathbf{r}) \cdot \mathrm{d}\mathbf{r}
$$

Physically, this is the work done per unit charge by an external agent in moving a test charge from $\mathcal{O}$ to $\mathbf{r}$. We may also define the electric potential energy as $q\phi$, which is the total work done by the external agent in moving a charge $q$ from $\mathcal{O}$ to $\mathbf{r}$. If we define the reference point as the infinity, the electric potential has a simple expression:

$$
\phi(\mathbf{r}) = -\frac{1}{4\pi \epsilon_{0}} \frac{q}{\left\lvert \mathbf{r} - \mathbf{r}_{0} \right\rvert}
$$

Since the potential is a linear function of the field, it too obeys the principle of superposition so that the total potential produced by a collection of charges $q_{i}$ is the sum of the potentials produced by each charge:

$$
\phi(\mathbf{r}) = \sum_{i} \phi_{i}(\mathbf{r}) = -\frac{1}{4\pi \epsilon_{0}} \sum_{i} \frac{q_{i}}{\left\lvert \mathbf{r} - \mathbf{r}_{i} \right\rvert}
$$

## Gauss' Law

### Solid Angle

The solid angle is defined as the portion of the sphere that is enclosed by an object. In spherical coordinates, the infinitesimal area element is given by:

$$
\mathrm{d}A = r^2 \sin{\theta} \, \mathrm{d}\theta \mathrm{d}\phi \equiv r^{2} \mathrm{d}\Omega
$$

where $\mathrm{d}\Omega$ is defined as the infinitesimal solid angle element.

The total solid angle is given by the integral:

$$
\int \mathrm{d}\Omega = \int_{0}^{2\pi} \int_{0}^{\pi} \sin{\theta} \, \mathrm{d}\theta \mathrm{d}\phi = 4\pi
$$

Consider the electric flux produced by a charge $q$ through a closed surface $\mathcal{S}$, which is the integral of the electric field $\mathbf{E}$ over the entire surface:

$$
\oint_{\mathcal{S}} \mathbf{E} \cdot \mathrm{d}\mathbf{a} = \int_{0}^{2\pi} \int_{0}^{\pi} \frac{1}{4\pi \epsilon_{0}} \frac{q}{r^{2}} r^{2} \sin{\theta} \, \mathrm{d}\theta \mathrm{d}\phi = \frac{q}{4\pi\epsilon_{0}} \int \, \mathrm{d}\Omega
$$

where the integral evaluates to $4\pi$ when $q$ is inside the surface and $0$ when $q$ is outside the surface.

Therefore, considering the principle of superposition, the Gauss' law states that the total flux through a closed surface $S$ is proportional to the total charge enclosed by the surface:

$$
\oint_{\mathcal{S}} \mathbf{E} \cdot \mathrm{d}\mathbf{a} = \frac{Q}{\epsilon_{0}}
$$

where $Q$ is the total charge enclosed by the surface.

Gauss' law can be recast into a differential form using the divergence theorem:

$$
\oint_{\mathcal{S}} \mathbf{E} \cdot \mathrm{d}\mathbf{a} = \oint_{V} \nabla \cdot \mathbf{E} \, \mathrm{d}V
$$

where $V$ is the volume enclosed by the surface $\mathcal{S}$.

On the other hand, the total charge enclosed can be expressed as an integral over the volume:

$$
Q = \int_{V} \rho \, \mathrm{d}V
$$

Therefore, Gauss' law can be written as:

$$
\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_{0}}
$$

or, using $\mathbf{E} = -\nabla \phi$:

$$
\nabla^{2} \phi = -\frac{\rho}{\epsilon_{0}}
$$

## Poisson and Laplace Equations

The above equation is called the Poisson equation. When $\rho = 0$, the Poisson equation reduces to the Laplace equation:

$$
\nabla^{2} \phi = 0
$$

Given a charge distribution $\rho$ over some volume $V$ with a boundary surface $S$ and certain boundary conditions, the solution to a Poisson equation is unique. The uniqueness of the solution can be shown by supposing on the contrary that there are two solutions $\phi_{1}$ and $\phi_{2}$ to the Poisson equation:

$$
\begin{split}
\nabla^{2} \phi_{1} &= -\frac{\rho}{\epsilon_{0}} \\
\nabla^{2} \phi_{2} &= -\frac{\rho}{\epsilon_{0}}
\end{split}
$$

Then the function $\phi \equiv \phi_{1} - \phi_{2}$ satisfies the Poisson equation:

$$
\nabla^{2} \phi = 0
$$

Consider the identity $\nabla \cdot (\phi \nabla \phi) = (\nabla \phi)^{2} + \nabla^{2} \phi = (\nabla \phi)^{2}$ and the following integral over $V$:

$$
\int_{V} \nabla \cdot (\phi \nabla \phi) \, \mathrm{d}V = \int_{V} (\nabla \phi)^{2} \, \mathrm{d}V
$$

Applying the divergence theorem to the right hand side, we obtain:

$$
\oint_{S} \phi \nabla \phi \cdot \mathrm{d}\mathbf{a} = \int_{V} (\nabla \phi)^{2} \, \mathrm{d}V
$$

There are two types of boundary conditions: Dirichlet and Neumann. In the Dirichlet boundary condition, we require $\phi_{1}$ and $\phi_{2}$ to both be some $\phi_{0}$ on the boundary. Thus, $\phi = 0$ on the boundary so that the surface integral vanishes. This requires $\nabla \phi = \mathbf{0}$ over the whole volume. Since $\phi$ is zero on the boundary and $\nabla \phi$ is zero everywhere, $\phi$ must be zero everywhere. This means $\phi_{1} = \phi_{2}$ and the solution is unique. In the Neumann boundary condition, we require $\nabla \phi_{1}$ and $\nabla \phi_{2}$ to both be some $\nabla \phi_{0}$ on the boundary. The argument is identical to the Dirichlet case.

This demonstrates that given some charge distribution $\rho$ and some boundary conditions on $\phi$ or $\nabla \phi$, the solution to the Poisson equation is unique.

## Boundary Conditions

The boundary conditions for the electric field are given by:

$$
\begin{split}
E_{+}^{\perp} - E_{-}^{\perp} &= \frac{\sigma_{f}}{\epsilon_{0}} \\
\mathbf{E}_{+}^{\parallel} - \mathbf{E}_{-}^{\parallel} &= 0
\end{split}
$$

These can translate to boundary conditions for the potential:

$$
\begin{split}
\phi_{+} - \phi_{-} &= 0 \\
\frac{\partial \phi_{+}}{\partial n} - \frac{\partial \phi_{-}}{\partial n} &= \frac{\sigma_{f}}{\epsilon_{0}}
\end{split}
$$

## Electric Dipole

Consider a pair of charges $q$ and $-q$ separated by a vector $\mathbf{d}$, with $\mathbf{d}$ pointing from the negative charge to the positive one. Without loss of generality, we can orient the displacement vector with the $z$ axis and the charges are located at $\pm \mathbf{d}/2$. The electric potential at a point $\mathbf{r}$ is given by:

$$
\phi(\mathbf{r}) = \frac{q}{4\pi\epsilon_{0}} \left( \frac{1}{\left\lvert \mathbf{r} - \mathbf{d}/2 \right\rvert} - \frac{1}{\left\lvert \mathbf{r} + \mathbf{d}/2 \right\rvert} \right)
$$

where the distances are given by:

$$
\left\lvert \mathbf{r} \pm \mathbf{d}/2 \right\rvert = \sqrt{r^{2} + \frac{d^{2}}{4} \mp d r \cos{\theta}} = r \sqrt{1 + \frac{d^{2}}{4 r^{2}} \mp \frac{d}{r} \cos{\theta}}
$$

Note that the reciprocal of the square root term is the generating function of the Legendre polynomials:

$$
\frac{1}{\sqrt{1 - 2xt + t^{2}}} = \sum_{n=0}^{\infty} P_{n}(x) t^{n}
$$

where we take $x = \pm \cos{\theta}$ and $t = d/(2r)$.

Thus, we can write the potential as:

$$
\begin{split}
    \phi(\mathbf{r}) &= \frac{q}{4\pi\epsilon_{0}r} \left[ \left( 1 + \frac{d^{2}}{4 r^{2}} - \frac{d}{r} \cos{\theta} \right)^{-1/2} - \left( 1 + \frac{d^{2}}{4 r^{2}} + \frac{d}{r} \cos{\theta} \right)^{-1/2} \right] \\
    &= \frac{q}{4\pi\epsilon_{0}r}  \sum_{n = 0}^{\infty} \left[ P_{n}(\cos{\theta}) - P_{n}(-\cos{\theta}) \right] \left( \frac{d}{2r} \right)^{n} \\
\end{split}
$$

Note that for Legendre polynomials, $P_{n}(x) = P_{n}(-x)$ for even $n$ and $P_{n}(x) = -P_{n}(-x)$ for odd $n$. Thus, we can simplify the expression for the potential to:

$$
\begin{split}
    \phi(\mathbf{r}) &= \frac{q}{2\pi\epsilon_{0}r} \sum_{\text{odd } n}^{\infty} P_{n}(\cos{\theta}) \left( \frac{d}{2r} \right)^{n} \\
    &= \frac{q}{2\pi\epsilon_{0}r} \left[ \cos{\theta} \frac{d}{2r} + \frac{1}{2} (5 \cos^{3}{\theta} - 3 \cos{\theta}) \left( \frac{d}{2r} \right)^{3} + \cdots \right] \\
\end{split}
$$

The first term is called the dipole term, the second term is called the quadrupole term, and so on. In the limit $r \gg d$, we approximate the potential as:

$$
\phi(\mathbf{r}) = \frac{1}{4\pi\epsilon_{0}r^{2}} qd \cos{\theta} = \frac{1}{4\pi\epsilon_{0}} \frac{\mathbf{p} \cdot \mathbf{r}}{r^{3}}
$$

The field is given by:

$$
\mathbf{E} = -\nabla \phi = \frac{1}{4\pi\epsilon_{0}} \frac{3(\mathbf{p} \cdot \mathbf{r}) \mathbf{r} - r^{2} \mathbf{p}}{r^{5}} = \frac{p}{4\pi\epsilon_{0}r^{3}} \left( 2\cos{\theta} \hat{r} + \sin{\theta} \hat{\theta} \right)
$$

## Assembly Energy and Energy Density

For a given charge distribution in a volume $V$, the energy of the system is given by the integral:

$$
W = \frac{1}{2} \int_{V} \phi \, \mathrm{d}q = \frac{1}{2} \int_{V} \phi \rho \, \mathrm{d}V
$$

where the assembly energy $W$ is the total work done by an external agent to build the system.

The differential form of Gauss' law tells us that $\rho = \epsilon_{0} \nabla \cdot \mathbf{E}$, so that

$$
W = \frac{\epsilon_{0}}{2} \int_{V} \phi \nabla \cdot \mathbf{E} \, \mathrm{d}V
$$

Making use of the following identity

$$
\nabla \cdot (\phi \mathbf{E}) = \phi \nabla \cdot \mathbf{E} + \mathbf{E} \cdot \nabla \phi = \phi \nabla \cdot \mathbf{E} - E^{2}
$$

we have:

$$
W = \frac{\epsilon_{0}}{2} \int_{V} \nabla \cdot (\phi \mathbf{E}) \, \mathrm{d}V + \frac{\epsilon_{0}}{2} \int_{V} E^{2} \, \mathrm{d}V
$$

Divergence theorem tells us that the first term is equal to the surface integral over the boundary surface $S$:

$$
W = \frac{\epsilon_{0}}{2} \int_{S} \phi \mathbf{E} \cdot \mathrm{d}\mathbf{S} + \frac{\epsilon_{0}}{2} \int_{V} E^{2} \, \mathrm{d}V
$$

The second term is always non-zero so it must always increase when we choose expand the volume of integration. It follows that if $V$ is all of space, the surface integral vanishes and we have:

$$
W = \frac{\epsilon_{0}}{2} \int_{\text{all space}} E^{2} \, \mathrm{d}V
$$

and the energy density of an electric field is thus defined as:

$$
\frac{\epsilon_{0} E^{2}}{2}
$$
