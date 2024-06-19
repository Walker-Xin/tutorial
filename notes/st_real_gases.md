# Statistical Mechanics - Real Gases

In the study of ideal gases, we have ignored any interactions between molecules, that is, we have assumed a zero potential energy between them. This is an acceptable approximation for gases at low pressures and high temperatures, but it soon becomes inadequate for gases at lower temperatures or higher densities.

In general, the partition function of a system of $N$ identical particles is given by:

$$
\begin{split}
    Z &= \frac{1}{N!} \int \mathrm{d}^{3} p_{1} \cdots \mathrm{d}^{3} p_{N} \int \mathrm{d}^{3} r_{1} \cdots \mathrm{d}^{3} r_{N} \exp \left( -\beta H \right) \\
\end{split}
$$

where the Hamiltonian $H$ is given by:

$$
H = \sum_{i=1}^{N} \frac{p_{i}^{2}}{2m} + U(r_{1}, \ldots, r_{N})
$$

We can alway integrate over the momenta to arrive at:

$$
Z = \frac{1}{N!} \frac{1}{\lambda_{\text{th}}^{3N}} \int \mathrm{d}^{3} r_{1} \cdots \mathrm{d}^{3} r_{N} \exp \left( -\beta U(r_{1}, \ldots, r_{N}) \right)
$$

Notice that if the potential energy is negligible, this expression reduces to the partition function of an ideal gas $Z = (V/N\lambda_{\text{th}}^{3})^{N}/N!$. In general, however, we should express the potential energy as sums of pairwise interactions:

$$
U(r_{1}, \ldots, r_{N}) = \frac{1}{2} \sum_{i \neq j} u(r_{ij})
$$

where $r_{ij} = \left\lvert \mathbf{r}_{i} - \mathbf{r}_{j} \right\rvert$ and the half factor is included to avoid double counting.

The actual form of $u(r)$ depends on the quantum mechanical properties of the particles and is very difficult to calculate. In practice, we rely on empirical models to describe the potential energy of real gases. The most common of these is the Lennard-Jones potential:

$$
u_{\text{LJ}}(r) = u_{0} \left[ \left( \frac{r_{0}}{r} \right)^{12} - 2 \left( \frac{r_{0}}{r} \right)^{6} \right]
$$

Even with this simple model, the partition function is still intractable when calculating the integrals. We therefore make another simplification called the mean field approximation.

## Mean Field Approximation

Consider a given particle $i$ in the system. We can assert that at a zeroth order approximation, the effect of the other particles on it is to create a mean field potential $u_{\text{eff}}(r_{i})$ such that the potential only depends on the position of this particular particle and not those of the others. This is as if the other particles are fixed in place in a lattice. Extending this approximation to every particle, we can write the potential energy as:

$$
U(r_{1}, \ldots, r_{N}) = \frac{1}{2} \sum_{i=1}^{N} u_{\text{eff}}(r_{i})
$$

which is now separable.

The partition function can now be written as:

$$
\begin{split}
    Z &= \frac{1}{N!} \frac{1}{\lambda_{\text{th}}^{3N}} \int \mathrm{d}^{3} r_{1} \cdots \mathrm{d}^{3} r_{N} \exp \left[ -\frac{\beta}{2} \sum_{i=1}^{N} u_{\text{eff}}(r_{i}) \right] \\
    &= \frac{1}{N!} \frac{1}{\lambda_{\text{th}}^{3N}} \left[ \int \mathrm{d}^{3} r \exp \left( -\frac{\beta}{2} u_{\text{eff}} \right) \right]^{N}
\end{split}
$$

In the mean field approximation, the particles are uniformly distributed in the volume $V$, so that the effective potential should be constant for all $r$. However, this is not true as on small distances, particles exert strong repulsive forces on each other, while on large distances, the forces are negligible. We crudely account for this by assuming that a fraction $V_{0}/V$ of the volume is forbidden to any given particle. This means that instead of integrating to $V$, we integrate to $(V - V_{0})$ in the potential integral:

$$
\int \mathrm{d}^{3} r \exp \left( -\beta u_{\text{eff}, 0} \right) = (V - V_{0}) \exp \left( -\frac{u_{\text{eff}, 0}}{2k_{B}T} \right)
$$

We now need to find approximations to $V_{0}$ and $u_{\text{eff}, 0}$. It is easy to see that since each particle occupies the same volume, $V_{0}$ should be proportional to $N$, that is, $V_{0} = bN$ for some constant $b$. The effective potential $u_{\text{eff}}$ can also be approximated as a first order function of $N$, that is, $u_{\text{eff}} = -2aN/V$ for some constant $a$. We can the finally write the partition function as:

$$
\boxed{
Z = \frac{V^{N}}{N!} \frac{1}{\lambda_{\text{th}}^{3N}} \left[ \left( 1 - \frac{bN}{V} \right) \exp \left( \frac{aN}{k_{B}TV} \right) \right]^{N}
}
$$

This is the partition function of a gas under the Van der Waals approximation. Note that this is the same as the partition function of an ideal gas, but with a correction factor that accounts for the interactions between the particles.

## Thermodynamics in a Van der Waals Gas

We can immediately write the Helmholtz free energy as:

$$
F = -k_{B}T \ln{Z} = -Nk_{B}T \left[ \ln{\left( \frac{V}{N\lambda_{\text{th}}^{3}} \right)} + 1 \right] - Nk_{B}T \ln{\left( 1 - \frac{bN}{V} \right)} - \frac{aN^{2}}{V}
$$

which can be seen as an ideal gas free energy plus a correction term.

We can then find the equation of state:

$$
p = -\left( \frac{\partial F}{\partial V} \right)_{T} = \frac{Nk_{B}T}{V - bN} - \frac{aN^{2}}{V^{2}}
$$

This is the Van der Waals equation of state that is more commonly written as:

$$
\boxed{
\left( p + \frac{aN^{2}}{V^{2}} \right) (V - bN) = Nk_{B}T
}
$$

The entropy can also be found:

$$
S = -\left( \frac{\partial F}{\partial T} \right)_{V} = Nk_{B} \left[ \frac{5}{2} - \ln{\left( \frac{V}{N\lambda_{\text{th}}^{3}} \right)} \right] + Nk_{B} \ln{\left( 1 - \frac{bN}{V} \right)}
$$

which is still the ideal gas entropy plus a correction term.

The internal energy can be found by using the relation $U = F + TS$:

$$
\boxed{
U = \frac{3}{2} Nk_{B}T - \frac{aN^{2}}{V}
}
$$

## Phase Transitions

The Van der Waals equation of state predicts a phase transition at a critical temperature $T_{c}$ and a critical volume $V_{c}$. To see this, consider the derivative of the pressure with respect to the volume:

$$
\left( \frac{\partial p}{\partial V} \right)_{T, N} = -\frac{Nk_{B}T}{(V - bN)^{2}} + \frac{2aN^{2}}{V^{3}}
$$

and the second derivative:

$$
\left( \frac{\partial^{2} p}{\partial V^{2}} \right)_{T, N} = \frac{2Nk_{B}T}{(V - bN)^{3}} - \frac{6aN^{2}}{V^{4}}
$$

The critical point is defined by the condition that both of these derivatives vanish. This gives us the critical temperature, volume and pressure:

$$
\boxed{
\begin{split}
    T_{c} &= \frac{8a}{27k_{B}b} \\
    V_{c} &= 3bN \\
    p_{c} &= \frac{a}{27b^{2}}
\end{split}
}
$$

The significance of the critical point lies in the thermal stability of the system. To see this, consider the compressibility of the gas. For temperatures above $T_{c}$, the Van der Waals gas behaves like an ideal gas, in the sense that the pressure is a monotonically decreasing function of the volume along an isotherm. This means that the compressibility, defined as:

$$
\kappa_{T} = -\frac{1}{V} \left( \frac{\partial V}{\partial p} \right)_{T, N}
$$

will be positive since $(\partial V/\partial p)_{T, N} < 0$ in this regime.

The compressibility also increases as the fluid expands, meaning that the substance is moving from a weak compressibility regime (liquid) to a strong compressibility regime (gas). A system is in thermodynamic equilibrium when its available energy is minimised, and in our case of constant temperature and volume, this means minimum free energy $F$. This means that we should require the following:

$$
\begin{split}
    \left( \frac{\partial F}{\partial V} \right)_{T, N} &= -p = 0 \\
    \left( \frac{\partial^{2} F}{\partial V^{2}} \right)_{T, N} &= -\left( \frac{\partial p}{\partial V} \right)_{T, N} > 0
\end{split}
$$

that is, the curve $F(V)$ should be convex.

However, for temperatures below $T_{c}$, there exists a range of $V$ where $(\partial p/\partial V)_{T, N} > 0$, meaning that the compressibility is negative. This means that the system becomes unstable since the liquid tends to expand when compressed. This means that the system is no longer in thermodynamic equilibrium. The isotherm that divides the two regimes with $T = T_{c}$ is called the critical isotherm. Physically, when the system passes the critical temperature, there will be both liquid and gas phases present so the system is no longer homogeneous so the treatment using the Van der Waals equation is no longer valid. These transitions are called phase transitions.

The critical point motivates the scaling of the variables used via:

$$
\tilde{T} \equiv \frac{T}{T_{c}} \quad \tilde{V} \equiv \frac{V}{V_{c}} \quad \tilde{p} \equiv \frac{p}{p_{c}}
$$

which leads to a dimensionless equation of state:

$$
\boxed{
\left( \tilde{p} + \frac{3}{\tilde{V}^{2}} \right) \left( 3 \tilde{V} - 1 \right) = 8\tilde{T}
}
$$

Since the constants $a$ and $b$ vanish in the scaled variables, the critical equation of state is universal for any van der Waals gas. That is, any gas behaves the same way when scaled by the critical parameters. This is called the law of corresponding states and has been verified empirically for many gases.

### Latent Heat

The latent heat of a phase transition is the amount of heat required to change the phase of a substance without changing its temperature. We may relate it to the entropy change during the phase transition:

$$
L = \Delta Q_{\text{rev}} = T \Delta S
$$

since phase transitions are reversible processes.

When $n$ molecules out of $N$ go from the liquid to the gas phase, the entropy change is:

$$
\Delta S = \frac{n}{N} (S_{\text{gas}} - S_{\text{liq}}) = nk_{B} \ln{\left( \frac{V_{\text{gas}} - bN}{V_{\text{liq}} - bN} \right)}
$$

where $V_{\text{gas}}$ is the volume of the system completely in the gas phase and $V_{\text{liq}}$ is similarly defined.

We can then write the latent heat as:

$$
L = T \Delta S = RT \ln{\left( \frac{V_{\text{gas}} - bN}{V_{\text{liq}} - bN} \right)}
$$

The presence of the latent heat means that the $S-T$ curve is not continuous during a phase transition. This is called a first order phase transition. There exist phase transitions where the curve is continuous and they are called continuous phase transitions.

## Clausius-Clapeyron Equation

For a system under $T_{c}$, we have seen that liquid and vapour phases can coexist in equilibrium for a range of $V$ during a phase transition. It can be shown that during a phase transition, the Gibbs free energy of the system is constant. We can then deduce that the Gibbs free energy of the liquid and vapour phases are equal:

$$
G_{\text{liq}}(p, T, N) = G_{\text{vap}}(p, T, N)
$$

Since the chemical potential is just Gibbs free energy per particle, we can write:

$$
\mu_{\text{liq}}(p, T, N) = \mu_{\text{vap}}(p, T, N)
$$

Consider a curve in the pressure-temperature plane that represents the coexistence of the liquid and vapour phases. This curve is called the coexistence curve. As we cross the curve, a phase transition occurs but the Gibbs free energy remains constant. It is also constant along the coexistence curve. We can consider the change in Gibbs free energy for liquid and vapour phases separately:

$$
\begin{split}
\mathrm{d}G_{\text{liq}} &= -S_{\text{liq}} \mathrm{d}T + V_{\text{liq}} \mathrm{d}p \\
\mathrm{d}G_{\text{gas}} &= -S_{\text{gas}} \mathrm{d}T + V_{\text{gas}} \mathrm{d}p
\end{split}
$$

Equating these, we obtain an equation for the slope of the coexistence curve:

$$
\boxed{
\frac{\mathrm{d}p}{\mathrm{d}T} = \frac{L}{T\Delta V} = \frac{L}{T(V_{\text{gas}} - V_{\text{liq}})}
}
$$

where we use the definition of the latent heat $L = T \Delta S = T(S_{\text{gas}} - S_{\text{liq}})$.

This is the Clausius-Clapeyron equation, which also applies to liquid-solid phase transitions. It is a differential equation that relates the slope of the coexistence curve to the latent heat of the phase transition, which can be solved to find the coexistence curve.
