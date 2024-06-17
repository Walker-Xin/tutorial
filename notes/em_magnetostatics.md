# Electromagnetism - Magnetostatics

## Lorentz Force Law and Continuity Equation

The Lorentz force law states that the force $\mathbf{F}$ on a charge $q$ moving with velocity $\mathbf{v}$ in a magnetic field $\mathbf{B}$ and an electric field $\mathbf{E}$ is given by:

$$
\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})
$$

A line charge $\lambda$ moving with velocity $\mathbf{v}$ creates a current $\mathbf{I} = \lambda \mathbf{v}$, so that for a steady current, the magnetic component Lorentz force is given by:

$$
\mathbf{F}_{\text{mag}} = \int \mathbf{v} \times \mathbf{B} \, \mathrm{d}q = \int \mathbf{v} \times \mathbf{B} \lambda \, \mathrm{d}l = \int \mathbf{I} \times \mathbf{B} \, \mathrm{d}l
$$

or more succinctly:

$$
\mathbf{F}_{\text{mag}} = I \int \mathrm{d}\mathbf{l} \times \mathbf{B}
$$

A flow of surface charge distribution creates a surface current density defined as:

$$
\mathbf{K} \equiv \frac{\mathrm{d}\mathbf{I}}{\mathrm{d}l_{\perp}} = \sigma \mathbf{v}
$$

For a surface current density, the magnetic component Lorentz force is given by:

$$
\mathbf{F}_{\text{mag}} = \int \mathbf{K} \times \mathbf{B} \, \mathrm{d}A
$$

A flow of volume charge distribution creates a volume current density defined as:

$$
\mathbf{J} \equiv \frac{\mathrm{d}\mathbf{I}}{\mathrm{d}A_{\perp}} = \rho \mathbf{v}
$$

and the magnetic component Lorentz force is given by:

$$
\mathbf{F}_{\text{mag}} = \int \mathbf{J} \times \mathbf{B} \, \mathrm{d}V
$$

Apparently, the relation $\mathrm{d}\mathbf{I} = \mathbf{K} \mathrm{d}l_{\perp} = \mathbf{J} \mathrm{d}A_{\perp}$ holds for a steady current. The total current crossing a surface $S$ can be written as the surface integral $I = \int_{S} \mathbf{J} \cdot \mathrm{d}\mathbf{A}$. By divergence theorem:

$$
\int_{S} \mathbf{J} \cdot \mathrm{d}\mathbf{A} = \int_{V} \nabla \cdot \mathbf{J} \, \mathrm{d}V = -\frac{\mathrm{d}}{\mathrm{d}t} \int \rho \, \mathrm{d}V
$$

where the second equality must hold for charges to be conserved.

This leads to the continuity equation:

$$
\nabla \cdot \mathbf{J} = -\frac{\partial \rho}{\partial t}
$$

## Biot-Savart Law and Ampere's Law

The Biot-Savart law states that the magnetic field $\mathrm{d}\mathbf{B}$ at a point $\mathbf{r}$ produced by a current element $\mathrm{d}\mathbf{I}$ at a point $\mathbf{r}_{0}$  is given by:

$$
\mathrm{d}\mathbf{B}(\mathbf{r}) = \frac{\mu_{0}}{4\pi} \frac{\mathrm{d}\mathbf{I} \times \hat{\mathbf{d}}}{\left\lvert \mathbf{r} - \mathbf{r}_{0} \right\rvert^{2}}
$$

where $\hat{\mathbf{d}} \equiv (\mathbf{r} - \mathbf{r}_{0})/\left\lvert \mathbf{r} - \mathbf{r}_{0} \right\rvert$ is the unit vector from $\mathbf{r}_{0}$ to $\mathbf{r}$.

Replacing $\mathrm{d}\mathbf{I}$ with $\mathbf{K} \mathrm{d}l_{\perp}$ or $\mathbf{J} \mathrm{d}A_{\perp}$, we have the alternative forms:

$$
\mathrm{d}\mathbf{B}(\mathbf{r}) = \frac{\mu_{0}}{4\pi} \frac{\mathbf{K} \times \hat{\mathbf{d}}}{\left\lvert \mathbf{r} - \mathbf{r}_{0} \right\rvert^{2}} \, \mathrm{d}A = \frac{\mu_{0}}{4\pi} \frac{\mathbf{J} \times \hat{\mathbf{d}}}{\left\lvert \mathbf{r} - \mathbf{r}_{0} \right\rvert^{2}} \, \mathrm{d}V
$$

It can be shown that the magnetic field is divergence-free and has a curl:

$$
\nabla \cdot \mathbf{B} = 0, \quad \nabla \times \mathbf{B} = \mu_{0} \mathbf{J}
$$

Applying Stoke's theorem to the curl, we have the Ampere's law:

$$
\oint \mathbf{B} \cdot \mathrm{d}\mathbf{l} = \mu_{0} \int \mathbf{J} \cdot \mathrm{d}\mathbf{A} = \mu_{0} I_{\text{encl}}
$$

## Magnetic Dipole

A magnetic dipole is a current loop with current $I$ and area $A$. The magnetic dipole moment is defined as:

$$
\mathbf{m} \equiv I \mathbf{A}
$$

where $\mathbf{A}$ is the area vector of the loop.

The magnetic field at a point $\mathbf{r}$ due to a magnetic dipole $\mathbf{m}$ is given by:

$$
\mathbf{B}(\mathbf{r}) = \frac{\mu_{0}}{4\pi} \frac{3(\mathbf{m} \cdot \mathbf{r}) \mathbf{r} - r^{2} \mathbf{m}}{r^{5}} = \frac{\mu_{0}}{4\pi r^{3}} \left( 2\cos{\theta} \hat{r} + \sin{\theta} \hat{\theta} \right)
$$

which is identical to the electric field of an electric dipole up to the constant factor.

## Magnetic Vector Potential

We may define a magnetic potential $\mathbf{A}$ so that the magnetic field is given by its curl:

$$
\boxed{
\mathbf{B} = \nabla \times \mathbf{A}
}
$$

The magnetic vector potential is not unique, since we can add a gradient of a scalar field $\phi$ to it without changing the magnetic field because the curl of a gradient is zero:

$$
\mathbf{A} \to \mathbf{A} + \nabla \phi
$$

From the Biot-Savart law, we have:

$$
\nabla \times (\nabla \times \mathbf{A}) = \mu_{0} \mathbf{J}
$$

Consider the vector identity $\nabla \times (\nabla \times \mathbf{A}) = \nabla (\nabla \cdot \mathbf{A}) - \nabla^{2} \mathbf{A}$. If we can choose a $\phi$ such that $\nabla \cdot \mathbf{A} = 0$, then we have:

$$
\nabla^{2} \mathbf{A} = -\mu_{0} \mathbf{J}
$$

Such a choice of $\phi$ is called the Coulomb gauge, which leads a Poisson equation for each component of $\mathbf{A}$ in the Cartesian coordinate system. Following the same method of solving the Poisson equation for the electric potential, we have:

$$
\mathbf{A}(\mathbf{r}) = \frac{\mu_{0}}{4\pi} \int \frac{\mathbf{J}(\mathbf{r}')}{\left\lvert \mathbf{r} - \mathbf{r}' \right\rvert} \, \mathrm{d}V'
$$

which is only valid for $\nabla \cdot \mathbf{A} = 0$ and in Cartesian coordinates.

## Magnetic Scalar Potential

In regions free of any current, the magnetic field becomes curl-free like the electric field. We may thus define a magnetic scalar potential $\phi_{B}$ so that the magnetic field is given by its gradient:

$$
\boxed{
\mathbf{B} = -\nabla \phi_{B}
}
$$
