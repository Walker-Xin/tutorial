# Kinetic Theory - Transport Phenomena

## Transport Equations

So far the discussion is around a simple situation where the gas is homogeneous, i.e., the velocity distribution $f(\mathbf{v})$ is the same everywhere. This would not be true in general and we therefore introduce the particle distribution function in the position and velocity space (phase space) $F(t, \mathbf{r}, \mathbf{v})$. The number of particles in a volume $[\mathbf{r}, \mathbf{r} + \mathrm{d}^{3}\mathbf{r}]$ with velocities in the range $[\mathbf{v}, \mathbf{v} + \mathrm{d}^{3}\mathbf{v}]$ is given by:

$$
F(t, \mathbf{r}, \mathbf{v}) \, \mathrm{d}^{3}\mathbf{r} \, \mathrm{d}^{3}\mathbf{v}
$$

The normalisation condition is:

$$
\int F(t, \mathbf{r}, \mathbf{v}) \, \mathrm{d}^{3}\mathbf{r} \, \mathrm{d}^{3}\mathbf{v} = N
$$

where $N$ is the total number of particles.

The zeroth velocity moment of $F$ is the number density $n(t, \mathbf{r})$:

$$
n(t, \mathbf{r}) = \int F(t, \mathbf{r}, \mathbf{v}) \, \mathrm{d}^{3}\mathbf{v}
$$

which integrates to the total number of particles $N$.

The first velocity moment of $F$ is related to the mean momentum density:

$$
\mathbf{p}(t, \mathbf{r}) = m n(t, \mathbf{r}) \mathbf{u}(t, \mathbf{r}) = \int m \mathbf{v} F(t, \mathbf{r}, \mathbf{v}) \, \mathrm{d}^{3}\mathbf{v}
$$

where $\mathbf{u}(t, \mathbf{r})$ is the mean velocity of the particles at position $\mathbf{r}$ at time $t$.

The second velocity moment of $F$ is related to the mean energy density:

$$
\begin{split}
\int \frac{mv^{2}}{2} F(t, \mathbf{r}, \mathbf{v}) \, \mathrm{d}^{3}\mathbf{v} &= \int \frac{m \left\lvert \mathbf{u} + \mathbf{w} \right\rvert^{2}}{2} F \, \mathrm{d}^{3}\mathbf{w} \\
&= \left( \frac{mu^{2}}{2} \int F \, \mathrm{d}^{3}\mathbf{w} \right) + \left( m \mathbf{u} \cdot \int \mathbf{w} F \, \mathrm{d}^{3}\mathbf{w} \right) + \left( \frac{m}{2} \int w^{2} F \, \mathrm{d}^{3}\mathbf{w} \right) \\
&= \frac{mnu^{2}}{2} + \frac{mn}{2} \left\langle w^{2} \right\rangle
\end{split}
$$

where at the second step we have written $\mathbf{v} = \mathbf{u} + \mathbf{w}$ as a variation around the mean velocity $\mathbf{u}$, and at the second step the middle integral is zero because $\mathbf{w}$ has zero mean by definition.

The first term of the results is the energy density due to the mean motions $\mathbf{u}$ of the particles whereas the second term is the energy density due to the random motions around the mean. Define the second term as the internal energy density $\varepsilon(t, \mathbf{r})$:

$$
\varepsilon(t, \mathbf{r}) \equiv \frac{mn}{2} \left\langle w^{2} \right\rangle
$$

Therefore, we define the total energies due to the mean and random motions as:

$$
K = \int \frac{mnu^{2}}{2} \, \mathrm{d}^{3}\mathbf{r} \quad \text{and} \quad U = \int \frac{mn}{2} \left\langle w^{2} \right\rangle \, \mathrm{d}^{3}\mathbf{r} = \int \varepsilon(t, \mathbf{r}) \, \mathrm{d}^{3}\mathbf{r}
$$

## Conservation Laws

From the definitions of $n$, $\mathbf{u}$, and $\varepsilon$, we can write the conservation laws for the number, momentum, and energy of the particles:

$$
\begin{split}
\int n(t, \mathbf{r}) \, \mathrm{d}^{3}\mathbf{r} &= N = \text{constant} \\
\int m n(t, \mathbf{r}) \mathbf{u}(t, \mathbf{r}) \, \mathrm{d}^{3}\mathbf{r} &= \mathbf{0} = \text{constant} \\
\int \left[ \frac{mnu^{2}}{2} + \varepsilon(t, \mathbf{r}) \right] \, \mathrm{d}^{3}\mathbf{r} &= K + U = \text{constant}
\end{split}
$$

where we have chosen the origin to be the centre of mass of the gas so that the total momentum is zero.

### Temperature

For simplicity, let us assume a situation where $\mathbf{u} = \mathbf{0}$ so that there is no bulk motion of the gas and $n$ is constant. The total energy is then just the internal energy $U$. The temperature is related to the internal energy by:

$$
\epsilon(t, \mathbf{r}) = n c_{p} T(t, \mathbf{r})
$$

where $c_{p}$ is the heat capacity per particle.

Internal energy flows from hotter to colder regions. We define the heat flux $\mathbf{J}(t, \mathbf{r})$ as the energy flowing in the direction $\mathbf{J}$ per unit time per unit area. The energy leaving a region $V$ per unit time is the flux through the surface of the region:

$$
\int_{\partial V} \mathbf{J} \cdot \mathrm{d}\mathbf{A} = \int_{V} \nabla \cdot \mathbf{J} \, \mathrm{d}^{3}\mathbf{r} = - \frac{\partial}{\partial t} \int_{V} \varepsilon(t, \mathbf{r}) \, \mathrm{d}^{3}\mathbf{r}
$$

We can write the right-hand side as:

$$
\frac{\partial}{\partial t} \int \varepsilon(t, \mathbf{r}) \, \mathrm{d}^{3}\mathbf{r} = \frac{\partial}{\partial t} \int n c_{p} T(t, \mathbf{r}) \, \mathrm{d}^{3}\mathbf{r} = \int n c_{p} \frac{\partial T}{\partial t} \, \mathrm{d}^{3}\mathbf{r}
$$

as we have assumed $n$ is constant.

Therefore, we arrive at the heat equation:

$$
\boxed{
    nc_{p} \frac{\partial T}{\partial t} = - \nabla \cdot \mathbf{J}
}
$$

which says that the heat flux $\mathbf{J}$ determines the time evolution of the temperature $T$.

### Momentum

Now only assume constant $n$ but allow $\mathbf{u}$ to vary. Define the momentum flux $\mathbf{\Pi}(t, \mathbf{r})$ as the momentum flowing in the direction $\mathbf{\Pi}$ per unit time per unit area. Similar to the heat flux, the momentum leaving a region $V$ is given by:

$$
\int_{\partial V} \mathbf{\Pi} \cdot \mathrm{d}\mathbf{A} = \int_{V} \nabla \cdot \mathbf{\Pi} \, \mathrm{d}^{3}\mathbf{r} = - \frac{\partial}{\partial t} \int_{V} m n \mathbf{u} \, \mathrm{d}^{3}\mathbf{r}
$$

leading to the equation:

$$
    m n \frac{\partial \mathbf{u}}{\partial t} = - \nabla \cdot \mathbf{\Pi}
$$

Consider the special case where $\mathbf{u}$ has only a z-dependence in the x-direction:

$$
\mathbf{u} = u_{x}(t, z) \hat{\mathbf{x}}
$$

The equation simplifies to:

$$
\boxed{
m n \frac{\partial u_{x}}{\partial t} = - \frac{\partial \Pi_{zx}}{\partial z}
}
$$

### Number Density

We can further relax the assumption of constant $n$ and allow it to vary. Consider a region $V$ with surface $\partial V$. The number of particles leaving the region at a point on $\partial V$ per unit time per unit volume is given by:

$$
n \mathbf{u} \cdot \hat{\mathbf{n}}
$$

We have:

$$
\int_{\partial V} n \mathbf{u} \cdot \hat{\mathbf{n}} \, \mathrm{d}A = \int_{V} \nabla \cdot (n \mathbf{u}) \, \mathrm{d}^{3}\mathbf{r} = - \frac{\partial}{\partial t} \int_{V} n \, \mathrm{d}^{3}\mathbf{r}
$$

so that we have the continuity equation:

$$
\boxed{
    \frac{\partial n}{\partial t} = - \nabla \cdot (n \mathbf{u})
}
$$

## Transport Equations and Coefficients

Consider the heat transport equation. On physical grounds it is reasonable to assume that the heat flux $\mathbf{J}$ is related to the temperature gradient $\nabla T$, as heat flows from hotter to colder regions. We could write $\mathbf{J}$ as a Taylor series in $\nabla T$ and keep only the lowest order term:

$$
\mathbf{J} = -\kappa \nabla T
$$

where $\kappa$ is called the thermal conductivity.

The heat equation then becomes:

$$
nc_{1} \frac{\partial T}{\partial t} = \kappa \nabla^{2} T
$$

In one dimension, this becomes:

$$
nc_{1} \frac{\partial T}{\partial t} = \kappa \frac{\partial^{2} T}{\partial z^{2}}
$$

Similarly, we can write the 1D momentum flux as:

$$
\Pi_{zx} = - \eta \frac{\partial u_{x}}{\partial z}
$$

where $\eta$ is called the dynamic viscosity.

The momentum equation then becomes:

$$
mn \frac{\partial u_{x}}{\partial t} = \eta \frac{\partial^{2} u_{x}}{\partial z^{2}}
$$
