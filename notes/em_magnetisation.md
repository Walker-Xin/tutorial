# Electromagnetism - Magnetisation

## Magnetic dipole moment

The magnetifc vector potential of a magnetic dipole is given by:

$$
\mathbf{A} = \frac{\mu_0}{4\pi} \frac{\mathbf{m} \times \mathbf{r}}{r^3}
$$

## Magnetisation of Materials

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

whrere we have defined the volume current as:

$$
\mathbf{J}_{b} = \nabla' \times \mathbf{M}
$$

and the surface current as:

$$
\mathbf{K}_{b} = \mathbf{M} \times \hat{n}
$$

## Auxiliary Field

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

Although the auxiliary field satisfies the modified Ampere's law, there is no corresponding Bio-Savart law for the auxiliary field, as its divergence is not necessarily zero:

$$
\nabla \cdot \mathbf{H} = -\nabla \cdot \mathbf{M}
$$

since $\mathbf{M}$ is not necessarily divergence-free.

## Linear Magnetic Materials

In linear magnetic materials, the magnetisation $\mathbf{M}$ is proportional to the auxiliary field $\mathbf{H}$:

$$
\mathbf{M} = \chi_{m} \mathbf{H}
$$

so that the magnetic field $\mathbf{B}$ is given by:

$$
\mathbf{B} = \mu_{0} \left( 1 + \chi_{m} \right) \mathbf{H} = \mu_{0} \mu_{r} \mathbf{H}
$$

where $\mu_{r} \equiv 1 + \chi_{m}$ is called the relative permeability.

## Boundary Conditions

The boundary conditions for the auxiliary field are:

$$
\begin{split}
H_{+}^{\perp} - H_{-}^{\perp} &= -K_{b}^{\perp} = -(M_{+}^{\perp} - M_{-}^{\perp}) \\
\mathbf{H}_{+}^{\parallel} - \mathbf{H}_{-}^{\parallel} &= \mathbf{K}_{b} \times \hat{n}
\end{split}
$$

which often need to the supplemented by the boundary conditions for the magnetic field:

$$
\begin{split}
B_{+}^{\perp} - B_{-}^{\perp} &= 0 \\
\mathbf{B}_{+}^{\parallel} - \mathbf{B}_{-}^{\parallel} &= \mu_{0} (\mathbf{K} \times \hat{n})
\end{split}
$$
