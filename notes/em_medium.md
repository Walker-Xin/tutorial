# Electromagnetism - Fields in Linear Media

- [Electromagnetism - Fields in Linear Media](#electromagnetism---fields-in-linear-media)
    - [Electric Field in Matter](#electric-field-in-matter)
        - [Dielectrics](#dielectrics)
        - [Electric Field in Dielectric](#electric-field-in-dielectric)
        - [Linear Dielectrics](#linear-dielectrics)
        - [Boundary Conditions for Electric Displacement](#boundary-conditions-for-electric-displacement)
    - [Magnetic Field in Matter](#magnetic-field-in-matter)
        - [Magnetic dipole moment](#magnetic-dipole-moment)
        - [Magnetisation of Materials](#magnetisation-of-materials)
        - [Auxiliary Field](#auxiliary-field)
        - [Linear Magnetic Materials](#linear-magnetic-materials)
        - [Boundary Conditions for Auxiliary Field](#boundary-conditions-for-auxiliary-field)
    - [Maxwell's Equations and Boundary Conditions](#maxwells-equations-and-boundary-conditions)

## Electric Field in Matter

### Dielectrics

Electric fields can induce a dipole moment in an atom. We may model the dipole moment as a vector $\mathbf{p}$, which is proportional to the electric field $\mathbf{E}$:

$$
\mathbf{p} = \alpha \mathbf{E}
$$

where the constant of proportionality $\alpha$ is called the polarisability.

Let us define the polarisation density $\mathbf{P}$ as the dipole moment per unit volume, which is in general a function of position $\mathbf{r}$. Referring to the potential due to a single dipole, the potential due to a polarised object is:

$$
\phi(\mathbf{r}) = \frac{1}{4\pi\epsilon_{0}} \int \frac{\mathbf{P}(\mathbf{r}') \cdot (\left\lvert \mathbf{r} - \mathbf{r}'\right\rvert)}{\left\lvert \mathbf{r} - \mathbf{r}'\right\rvert^3} \, \mathrm{d}V'
$$

where $\mathbf{r}'$ is the position of the infinitesimal volume element $\mathrm{d}V'$ that has polarisation density $\mathbf{P}(\mathbf{r}')$.

Note the relation:

$$
\nabla \left( \frac{1}{r} \right) = -\frac{\mathbf{r}}{r^3}
$$

so that:

$$
\nabla' \left( \frac{1}{\left\lvert \mathbf{r} - \mathbf{r}'\right\rvert} \right) = \frac{\left\lvert \mathbf{r} - \mathbf{r}'\right\rvert}{\left\lvert \mathbf{r} - \mathbf{r}'\right\rvert^3}
$$

where the negative sign is cancelled out because the differentiation is with respect to $\mathbf{r}'$.

We can then rewrite the potential as:

$$
\begin{split}
\phi(\mathbf{r}) &= \frac{1}{4\pi\epsilon_{0}} \int \mathbf{P}(\mathbf{r}') \cdot \nabla' \left( \frac{1}{\left\lvert \mathbf{r} - \mathbf{r}'\right\rvert} \right) \, \mathrm{d}V' \\
&= \frac{1}{4\pi\epsilon_{0}} \int \nabla' \cdot \left[ \mathbf{P}(\mathbf{r}') \frac{1}{\left\lvert \mathbf{r} - \mathbf{r}'\right\rvert} \right] \, \mathrm{d}V' - \frac{1}{4\pi\epsilon_{0}} \int \nabla' \cdot \left[ \frac{\mathbf{P}(\mathbf{r}')}{\left\lvert \mathbf{r} - \mathbf{r}'\right\rvert} \right] \, \mathrm{d}V' \\
&= \frac{1}{4\pi\epsilon_{0}} \int \nabla' \cdot \frac{1}{\left\lvert \mathbf{r} - \mathbf{r}'\right\rvert} \mathbf{P} \cdot \, \mathrm{d}\mathbf{S} - \frac{1}{4\pi\epsilon_{0}} \int \frac{1}{\left\lvert \mathbf{r} - \mathbf{r}'\right\rvert} \nabla' \cdot \mathbf{P} \, \mathrm{d}V' \\
&= \frac{1}{4\pi\epsilon_{0}} \int \frac{\sigma_{b}}{\left\lvert \mathbf{r} - \mathbf{r}'\right\rvert} \, \mathrm{d}S' + \frac{1}{4\pi\epsilon_{0}} \int \frac{\rho_{b}}{\left\lvert \mathbf{r} - \mathbf{r}'\right\rvert} \, \mathrm{d}V' \\
\end{split}
$$

Notice that the third step involves a surface integral and a volume integral, which motives the definitions:

$$
\boxed{
\begin{split}
\sigma_{b} &\equiv \mathbf{P} \cdot \hat{n} \\
\rho_{b} &\equiv -\nabla \cdot \mathbf{P}
\end{split}
}
$$

where $\sigma_{b}$ is called the surface bound density and $\rho_{b}$ is called the volume bound density.

This implies that the potential due to a polarised object can be computed once the polarisation density is known.

### Electric Field in Dielectric

Gauss' law gives the electric field due to a charge distribution $\rho$, which can be split into free and bound charge densities:

$$
\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_{0}} = \frac{\rho_{f} + \rho_{b}}{\epsilon_{0}}
$$

where $\rho_{f}$ is everything that is not bound charge.

We can then write $\nabla \cdot \mathbf{E} = \frac{\rho_{f}}{\epsilon_{0}} - \nabla \cdot \mathbf{P}$ so that the electric displacement $\mathbf{D}$ can be defined as:

$$
\mathbf{D} \equiv \epsilon_{0} \mathbf{E} + \mathbf{P}
$$

The electric displacement satisfies the modified Gauss' law:

$$
\nabla \cdot \mathbf{D} = \rho_{f}
$$

and its integral form:

$$
\oint \mathbf{D} \cdot \, \mathrm{d}\mathbf{S} = Q_{f}
$$

However, there is no equivalent to Coulomb's law for the electric displacement, as its curl is not necessarily zero:

$$
\nabla \times \mathbf{D} = \nabla \times \mathbf{P} \neq \mathbf{0}
$$

### Linear Dielectrics

A linear dielectric is one in which the polarisation density is proportional to the electric field:

$$
\mathbf{P} = \epsilon_{0} \chi_{e} \mathbf{E}
$$

where the dimensionless constant $\chi_{e}$ is called the electric susceptibility.

The electric displacement field is then:

$$
\mathbf{D} = \epsilon_{0} \left( 1 + \chi_{e} \right) \mathbf{E} = \epsilon_{0} \epsilon_{r} \mathbf{E}
$$

where $\epsilon_{r} \equiv 1 + \chi_{e}$ is called the relative permittivity.

### Boundary Conditions for Electric Displacement

The boundary conditions for the electric displacement are:

$$
\begin{split}
D_{+}^{\perp} - D_{-}^{\perp} &= \sigma_{f} \\
\mathbf{D}_{+}^{\parallel} - \mathbf{D}_{-}^{\parallel} &= \mathbf{P}_{+}^{\parallel} - \mathbf{P}_{-}^{\parallel}
\end{split}
$$

The second condition is not always useful, so we often supplement it with the boundary conditions for the electric field:

$$
\begin{split}
E_{+}^{\perp} - E_{-}^{\perp} &= \frac{\sigma}{\epsilon_{0}} \\
\mathbf{E}_{+}^{\parallel} - \mathbf{E}_{-}^{\parallel} &= 0
\end{split}
$$

## Magnetic Field in Matter

### Magnetic dipole moment

The magnetic vector potential of a magnetic dipole is given by:

$$
\mathbf{A} = \frac{\mu_0}{4\pi} \frac{\mathbf{m} \times \mathbf{r}}{r^3}
$$

### Magnetisation of Materials

The magnetisation $\mathbf{M}$ of a material is defined as the magnetic dipole moment per unit volume. The vector potential of a magnetised material is given by:

$$
\begin{split}
\mathbf{A} &= \frac{\mu_0}{4\pi} \int_{V} \frac{\mathbf{M} \times \mathbf{r'}}{r'^3} \, \mathrm{d}V' \\
&= \frac{\mu_0}{4\pi} \int_{V} \left[ \mathbf{M} \times \nabla' \left( \frac{1}{r'} \right) \right] \, \mathrm{d}V' \\
&= \frac{\mu_0}{4\pi} \int_{V} \frac{1}{r} \left( \nabla' \times \mathbf{M} \right) \, \mathrm{d}V' - \frac{\mu_0}{4\pi} \int_{V} \nabla' \times \left( \frac{\mathbf{M}}{r'} \right) \, \mathrm{d}V' \\
&= \frac{\mu_0}{4\pi} \int_{V} \frac{1}{r} \left( \nabla' \times \mathbf{M} \right) \, \mathrm{d}V' + \frac{\mu_0}{4\pi} \oint_{S} \frac{1}{r'} \mathbf{M} \times \mathrm{d}\mathbf{S}'  \\
&= \frac{\mu_0}{4\pi} \int_{V} \frac{J_{b}}{r'} \, \mathrm{d}V' + \frac{\mu_0}{4\pi} \oint_{S} \frac{\mathbf{K}_{b}}{r'} \, \mathrm{d}S'
\end{split}
$$

where following a similar argument as in the case of polarisation, we have defined the bound current density as:

$$
\mathbf{J}_{b} = \nabla' \times \mathbf{M}
$$

and the bound surface current as:

$$
\mathbf{K}_{b} = \mathbf{M} \times \hat{n}
$$

### Auxiliary Field

In any case, the total current density in a region can be written as a sum of free and bound currents:

$$
\mathbf{J} = \mathbf{J}_{f} + \mathbf{J}_{b}
$$

where the free current $\mathbf{J}_{f}$ is any current that is not due to the magnetisation of the material.

Ampere' law can be rewritten as:

$$
\frac{1}{\mu_{0}} \nabla \times \mathbf{B} = \mathbf{J}_{f} + \mathbf{J}_{b} = \mathbf{J}_{f} + \nabla \times \mathbf{M}
$$

so that:

$$
\nabla \times \mathbf{H} = \mathbf{J}_{f}
$$

where we have defined the auxiliary field $\mathbf{H}$ as:

$$
\mathbf{H} \equiv \frac{\mathbf{B}}{\mu_{0}} - \mathbf{M}
$$

Although the auxiliary field satisfies the modified Ampere's law, there is no corresponding Biot-Savart law for the auxiliary field, as its divergence is not necessarily zero:

$$
\nabla \cdot \mathbf{H} = -\nabla \cdot \mathbf{M} \neq 0
$$

since $\mathbf{M}$ is not necessarily divergence-free.

### Linear Magnetic Materials

In linear magnetic materials, the magnetisation $\mathbf{M}$ is proportional to the auxiliary field $\mathbf{H}$:

$$
\mathbf{M} = \chi_{m} \mathbf{H}
$$

so that the magnetic field $\mathbf{B}$ is given by:

$$
\mathbf{B} = \mu_{0} \left( 1 + \chi_{m} \right) \mathbf{H} = \mu_{0} \mu_{r} \mathbf{H}
$$

where $\mu_{r} \equiv 1 + \chi_{m}$ is called the relative permeability.

### Boundary Conditions for Auxiliary Field

The boundary conditions for the auxiliary field are:

$$
\begin{split}
H_{+}^{\perp} - H_{-}^{\perp} &= -K_{b}^{\perp} = -(M_{+}^{\perp} - M_{-}^{\perp}) \\
\mathbf{H}_{+}^{\parallel} - \mathbf{H}_{-}^{\parallel} &= \mathbf{K}_{f} \times \hat{n}
\end{split}
$$

The first condition is not always useful, so we often supplement it with the boundary conditions for the magnetic field:

$$
\begin{split}
B_{+}^{\perp} - B_{-}^{\perp} &= 0 \\
\mathbf{B}_{+}^{\parallel} - \mathbf{B}_{-}^{\parallel} &= \mu_{0} (\mathbf{K} \times \hat{n})
\end{split}
$$

## Maxwell's Equations and Boundary Conditions

The Maxwell equations are:

$$
\boxed{
\begin{split}
\nabla \cdot \mathbf{E} &= \frac{\rho}{\epsilon_{0}} \\
\nabla \cdot \mathbf{B} &= 0 \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{B} &= \mu_{0} (\mathbf{J} + \epsilon_{0} \frac{\partial \mathbf{E}}{\partial t})
\end{split}
}
$$

While these are true in general, there are more convenient forms in regions where polarisation and magnetisation are present. Consider the volume charge and current densities produced by a polarisation $\mathbf{P}$ and magnetisation $\mathbf{M}$:

$$
\begin{split}
\rho_{b} &= -\nabla \cdot \mathbf{P} \\
\mathbf{J}_{b} &= \nabla \times \mathbf{M}
\end{split}
$$

These are true in the static case, but in the time-dependent case, a changing charge density produces a current density according to:

$$
\mathbf{J}_{p} = \frac{\partial \mathbf{P}}{\partial t}
$$

which is called the polarisation current.

The polarisation current satisfies the continuity equation:

$$
\nabla \cdot \mathbf{J}_{p} = -\frac{\partial \rho_{p}}{\partial t}
$$

In view of the bound charge and current densities, we can write any charge and current densities as:

$$
\begin{split}
\rho &= \rho_{f} + \rho_{b} = \rho_{f} - \nabla \cdot \mathbf{P} \\
\mathbf{J} &= \mathbf{J}_{f} + \mathbf{J}_{b} + \mathbf{J}_{p} = \mathbf{J}_{f} + \nabla \times \mathbf{M} + \frac{\partial \mathbf{P}}{\partial t}
\end{split}
$$

Substituting the expressions to the Maxwell equations and making use of the definitions of electric displacement $\mathbf{D}$ and auxiliary magnetic field $\mathbf{H}$, we have Maxwell's equations in a medium:

$$
\boxed{
\begin{split}
\nabla \cdot \mathbf{D} &= \rho_{f} \\
\nabla \cdot \mathbf{B} &= 0 \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{H} &= \mathbf{J}_{f} + \frac{\partial \mathbf{D}}{\partial t}
\end{split}
}
$$
