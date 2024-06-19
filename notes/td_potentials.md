# Thermodynamics - Thermodynamic Potentials

The internal energy is a function of state whose change only depends on the initial and final states of the system. Additional functions of state can be derived from combinations of quantities such as the internal energy $U$, pressure $p$, volume $V$, entropy $S$, and temperature $T$. These functions are called thermodynamic potentials.

## Internal Energy

The change in internal energy of a system is given by the first law of thermodynamics:

$$
\boxed{
\mathrm{d}U = T\mathrm{d}S - p\mathrm{d}V
}
$$

This equation implies that the natural variables of the internal energy are $S$ and $V$, so that we can write $U(S, V)$ as a function of $S$ and $V$. It is also implied that we can write $T$ and $p$ as partial derivatives of $U$:

$$
\begin{split}
T &= \left( \frac{\partial U}{\partial S} \right)_{V} \\
p &= -\left( \frac{\partial U}{\partial V} \right)_{S}
\end{split}
$$

For an isochoric process, $\mathrm{d}V = 0$, so that $\mathrm{d}U = T\mathrm{d}S$. If the process is also reversible, then:

$$
\mathrm{d}U = \mathrm{d}Q_{\text{rev}} = C_{V}\mathrm{d}T
$$

so that:

$$
\Delta U = \int_{T_{1}}^{T_{2}} C_{V} \, \mathrm{d}T
$$

## Enthalpy

We define the enthalpy $H$ as:

$$
H = U + pV
$$

which implies the differential form:

$$
\boxed{
\mathrm{d}H = T\mathrm{d}S + V\mathrm{d}p
}
$$

which means that the natural variables of the enthalpy are the same as those of the internal energy, $S$ and $V$.

We also have the partial derivative relations:

$$
\begin{split}
T &= \left( \frac{\partial H}{\partial S} \right)_{p} \\
V &= \left( \frac{\partial H}{\partial p} \right)_{S}
\end{split}
$$

We see that for an isobaric process $\mathrm{d}H = T\mathrm{d}S$. If the process is also reversible, then:

$$
\mathrm{d}H = \mathrm{d}Q_{\text{rev}} = C_{p}\mathrm{d}T
$$

so that:

$$
\Delta H = \int_{T_{1}}^{T_{2}} C_{p} \, \mathrm{d}T
$$

This implies that in a reversible isobaric process, the change in enthalpy is equal to the heat transferred to the system.  

## Helmholtz Free Energy

We define the Helmholtz free energy $F$ as:

$$
F = U - TS
$$

and:

$$
\boxed{
\mathrm{d}F = -S\mathrm{d}T - p\mathrm{d}V
}
$$

Note that the natural variables of the Helmholtz free energy are $T$ and $V$. These are variables that are more easily controlled in a laboratory setting than $S$ and $V$. The partial derivative relations are:

$$
\begin{split}
S &= -\left( \frac{\partial F}{\partial T} \right)_{V} \\
p &= -\left( \frac{\partial F}{\partial V} \right)_{T}
\end{split}
$$

Note that for an isothermal process, we have $\mathrm{d}F = -p\mathrm{d}V$ so that:

$$
\Delta F = -\int_{V_{1}}^{V_{2}} p \, \mathrm{d}V
$$

so that a positive change in Helmholtz free energy implies that work is done on the system.

## Gibbs Free Energy

Finally, we define the Gibbs free energy $G$ as:

$$
G = U + pV - TS
$$

and:

$$
\boxed{
\mathrm{d}G = -S\mathrm{d}T + V\mathrm{d}p
}
$$

whose natural variables are $T$ and $p$.

The partial derivative relations are:

$$
\begin{split}
S &= -\left( \frac{\partial G}{\partial T} \right)_{p} \\
V &= \left( \frac{\partial G}{\partial p} \right)_{T}
\end{split}
$$

## Maxwell Relations

Consider a function $f(x, y)$ of two variables $x$ and $y$. We can write the total differential of $f$ as:

$$
\mathrm{d}f = \left( \frac{\partial f}{\partial x} \right)_{y} \mathrm{d}x + \left( \frac{\partial f}{\partial y} \right)_{x} \mathrm{d}y
$$

For an exact differential, we must have:

$$
\frac{\partial^{2} f}{\partial x \partial y} = \frac{\partial^{2} f}{\partial y \partial x}
$$

We can apply these relations to the thermodynamic potentials. For example, for the internal energy $U(S, V)$, we have:

$$
\begin{split}
\frac{\partial}{\partial V} \left( \frac{\partial U}{\partial S} \right)_{V} &= \frac{\partial}{\partial S} \left( \frac{\partial U}{\partial V} \right)_{S} \\
\frac{\partial T}{\partial V} &= -\frac{\partial p}{\partial S} \\
\end{split}
$$

Three more similar relations can be derived from the other thermodynamic potentials. In total, we have:

$$
\boxed{
\begin{split}
\left( \frac{\partial T}{\partial V} \right)_{S} &= -\left( \frac{\partial p}{\partial S} \right)_{V} \\
\left( \frac{\partial T}{\partial p} \right)_{S} &= \left( \frac{\partial V}{\partial S} \right)_{p} \\
\left( \frac{\partial S}{\partial V} \right)_{T} &= \left( \frac{\partial p}{\partial T} \right)_{V} \\
\left( \frac{\partial S}{\partial p} \right)_{T} &= -\left( \frac{\partial V}{\partial T} \right)_{p} \\
\end{split}
}
$$

which are known as the Maxwell relations.

Note that two of these quantities relate directly to heat capacities:

$$
\begin{split}
\frac{C_{V}}{T} &= \left( \frac{\partial S}{\partial T} \right)_{V} \\
\frac{C_{p}}{T} &= \left( \frac{\partial S}{\partial T} \right)_{p}
\end{split}
$$

We can also define some susceptibilities:

$$
\boxed{
\begin{split}
\beta_{p} &\equiv \frac{1}{V} \left( \frac{\partial V}{\partial T} \right)_{p} \\
\beta_{S} &\equiv \frac{1}{V} \left( \frac{\partial V}{\partial T} \right)_{S} \\
\kappa_{T} &\equiv -\frac{1}{V} \left( \frac{\partial V}{\partial p} \right)_{T} \\
\kappa_{S} &\equiv -\frac{1}{V} \left( \frac{\partial V}{\partial p} \right)_{S} \\
\end{split}
}
$$

$\beta_{p}$ and $\beta_{S}$ are expansion coefficients that describe how the volume of a substance changes with temperature. $\kappa_{T}$ and $\kappa_{S}$ are compression coefficients that describe how the volume changes when applied with pressure. Note that by dividing by $V$, they describe fractional changes in volume.

## Chemical Potential

To describe a system whose number of particles is not fixed, we introduce the chemical potential $\mu$ as the change in the internal energy of the system when a particle is added to it. We modify the first law of thermodynamics to include the chemical potential:

$$
\mathrm{d}U = T \mathrm{d}S - p \mathrm{d}V + \mu \mathrm{d}N
$$

where $N$ is the number of particles in the system and $\mu$ can be defined via the partial derivative:

$$
\mu \equiv \left( \frac{\partial U}{\partial N} \right)_{S, V}
$$

We still have the other thermodynamic potentials with the addition of the chemical potential:

$$
\begin{split}
\mathrm{d}H &= T\mathrm{d}S + V\mathrm{d}p + \mu\mathrm{d}N \\
\mathrm{d}F &= -S\mathrm{d}T - p\mathrm{d}V + \mu\mathrm{d}N \\
\mathrm{d}G &= -S\mathrm{d}T + V\mathrm{d}p + \mu\mathrm{d}N
\end{split}
$$

We can also define the grand potential $\Phi$ as:

$$
\Phi = U - TS - \mu N
$$

and:

$$
\mathrm{d}\Phi = -S\mathrm{d}T - p\mathrm{d}V - N\mathrm{d}\mu
$$

It can be shown that the chemical potential is just Gibbs free energy per particle:

$$
\boxed{
\mu = \frac{G}{N}
}
$$

which implies that the grand potential has a simple expression:

$$
\Phi = -pV
$$
