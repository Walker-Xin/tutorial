# Thermodynamics - Foundation

Functions of state are important quantities in thermodynamics, changes in which are independent of the path taken to reach the final state. A function of state can be either extensive or intensive. Extensive functions of state (energy, volume, etc.) are proportional to the size of the system, while intensive functions (temperature, pressure, etc.) of state are independent of size.

In general, an equation of state connects functions of state to each other. For example, the ideal gas law connects pressure, volume, and temperature via $PV = nRT$.

## The First Law of Thermodynamics

The first law of thermodynamics states that energy is conserved and heat and work are both forms of energy:

$$
\mathrm{d}U = \delta Q + \delta W
$$

where we define $U$ as the internal energy of the system, $Q$ as the heat added to it and $W$ as the work done on it.

In the context of a gas, we may write $\delta W = -p \mathrm{d}V$ for a slow enough process so that the first law becomes:

$$
\mathrm{d}U = \delta Q - p \mathrm{d}V
$$

### Heat Capacities

The internal energy is expressed as a function of temperature and volume, $U = U(T, V)$. Its infinitesimal change can thus be expressed as partial derivatives:

$$
\mathrm{d}U = \left( \frac{\partial U}{\partial T} \right)_{V} \mathrm{d}T + \left( \frac{\partial U}{\partial V} \right)_{T} \mathrm{d}V
$$

We can also express it as a function of temperature and pressure, $U = U(T, p)$, and its infinitesimal change as:

$$
\mathrm{d}U = \left( \frac{\partial U}{\partial T} \right)_{p} \mathrm{d}T + \left( \frac{\partial U}{\partial p} \right)_{T} \mathrm{d}p
$$

Consider the derivative $\mathrm{d}U/\mathrm{d}T$ with $p$ held constant, we have the following relation:

$$
\left( \frac{\partial U}{\partial T} \right)_{p} = \left( \frac{\partial U}{\partial T} \right)_{V} + \left( \frac{\partial U}{\partial V} \right)_{T} \left( \frac{\partial V}{\partial T} \right)_{p}
$$

We define the heat capacity at constant volume as:

$$
C_{V} \equiv \left( \frac{\partial Q}{\partial T} \right)_{V} = \left( \frac{\partial U}{\partial T} \right)_{V}
$$

where the equality follows from the fact that $\mathrm{d}V = 0$ at constant volume.

Similarly, we can define the heat capacity at constant pressure:

$$
\begin{split}
C_{p} &\equiv \left( \frac{\partial Q}{\partial T} \right)_{p} \\
&= \left( \frac{\partial U}{\partial T} \right)_{p} + p \left( \frac{\partial V}{\partial T} \right)_{p} \\
&= \left( \frac{\partial U}{\partial T} \right)_{V} + \left[ \left( \frac{\partial U}{\partial V} \right)_{T} + p \right] \left( \frac{\partial V}{\partial T} \right)_{p} \\
\end{split}
$$

using the previous relation.

For an ideal gas, this reduces to:

$$
C_{p} = C_{V} + nR
$$

We define the adiabatic index $\gamma$ as:

$$
\gamma \equiv \frac{C_{p}}{C_{V}}
$$

### Processes

A quasi-static process is one that occurs slowly enough that the system remains in equilibrium at all times. A quasi-static process without any hysterisis is called a reversible process.

An isothermal process is one that occurs at constant temperature. It is easy to show that for an ideal gas, the heat added to the system is equal to the work done on it:

$$
\Delta Q = nRT \ln \left( \frac{V_{f}}{V_{i}} \right) = -\Delta W
$$

An adiabatic process is one that occurs without any heat added to or removed from the system so that $\delta Q = 0$. It is easy to show that for an ideal gas, the pressure and volume are related by:

$$
pV^{\gamma} = \text{constant}
$$

## The Second Law of Thermodynamics

There are two most common statements of the second law of thermodynamics:

1. The Clausius statement: There is no process whose sole result is the transfer of heat from a cooler to a hotter body.
2. The Kelvin-Planck statement: There is no cyclic process that converts heat entirely into work.

### Carnot's Engine

Suppose a machine connects two heat reservoirs at temperatures $T_{+}$ and $T_{-}$ and extracts heat $Q_{+}$ from the hotter reservoir and rejects heat $Q_{-}$ to the colder reservoir, doing work $W$ in the process. The efficiency of the machine is defined as:

$$
\eta \equiv \frac{W}{Q_{+}} = 1 - \frac{Q_{-}}{Q_{+}}
$$

A Carnot engine is a reversible engine that executes a cycle that consists of two isothermal processes and two adiabatic processes. In a Carnot engine, the ratio of the heat extracted and ejected is the same as the ratio of the temperatures of the two reservoirs:

$$
\frac{Q_{+}}{Q_{-}} = \frac{T_{+}}{T_{-}}
$$

which means that the efficiency of a Carnot engine is only a function of the temperatures of the two reservoirs:

$$
\eta = 1 - \frac{T_{-}}{T_{+}}
$$

The Carnot theorem states that no engine can be more efficient than a Carnot engine operating between the same two temperatures. Using Carnot's theorem, we can prove that the two statements of the second law are equivalent.

### Entropy

The equation $Q_{+}/T_{+} = Q_{-}/T_{-}$ implies that for a Carnot cycle, the quantity $Q/T$ sums to zero over a cycle. Clausius' theorem states that for any closed cycle, the exchange in heat obeys:

$$
\oint \frac{\delta Q}{T} \leq 0
$$

where the equality holds for a reversible cycle.

This implies that $\delta Q_{\text{rev}}/T$ is an exact differential, which motivates the definition of a new state function called entropy:

$$
\mathrm{d}S \equiv \frac{\delta Q_{\text{rev}}}{T}
$$

Using entropy, we can rewrite the first law of thermodynamics as:

$$
\mathrm{d}U = T \mathrm{d}S - p \mathrm{d}V
$$

which is a more general form of the first law that applies to both reversible and irreversible processes.

We can also rewrite the definition of the heat capacities:

$$
C_{V} = T \left( \frac{\partial S}{\partial T} \right)_{V} \qquad C_{p} = T \left( \frac{\partial S}{\partial T} \right)_{p}
$$

## Energy Equation

Consider the following equation obtained from the definition of $C_{p}$:

$$
\left( \frac{\partial U}{\partial V} \right)_{T} = \frac{C_{p} - \left( \frac{\partial U}{\partial T} \right)_{V}}{\left( \frac{\partial V}{\partial T} \right)_{p}} - p = \frac{C_{p} - C_{V}}{\left( \frac{\partial V}{\partial T} \right)_{p}} - p
$$

The denominator is the coefficient of volume expansion at constant pressure:

$$
\kappa_{p} \equiv \frac{1}{V} \left( \frac{\partial V}{\partial T} \right)_{p}
$$

Therefore, we can write the equation as:

$$
\left( \frac{\partial U}{\partial V} \right)_{T} = \frac{C_{p} - C_{V}}{\kappa_{p} V} - p
$$

Substituting this into the equation for $\mathrm{d}U$, we obtain what is known as the energy equation:

$$
\mathrm{d}U = C_{V} \mathrm{d}T + \left( \frac{C_{p} - C_{V}}{\kappa_{p} V} - p \right) \mathrm{d}V
$$

This implies that once we know the heat capacities and the coefficient of volume expansion as functions of $T$ and $V$, we can integrate the energy equation to find the internal energy. The expansion coefficient is derived from the equation of state while the heat capacities are usually measured experimentally.

Let us further consider the quantity $C_{p} - C_{V}$. Let us consider entropy as a function of $T$ and $V$, $S = S(T, V)$. Its infinitesimal change can be expressed as partial derivatives:

$$
\begin{split}
    \mathrm{d}S &= \left( \frac{\partial S}{\partial T} \right)_{V} \mathrm{d}T + \left( \frac{\partial S}{\partial V} \right)_{T} \mathrm{d}V \\
    &= \frac{C_{V}}{T} \mathrm{d}T + \left( \frac{\partial p}{\partial T} \right)_{V} \mathrm{d}V \\
    &= \frac{C_{V}}{T} \mathrm{d}T - \left( \frac{\partial p}{\partial V} \right)_{T} \left( \frac{\partial V}{\partial T} \right)_{p} \mathrm{d}V \\
    &= \frac{C_{V}}{T} \mathrm{d}T + \frac{\kappa_{p}}{\kappa_{T}} \mathrm{d}V
\end{split}
$$

where we define the coefficient of isothermal compressibility as:

$$
\kappa_{T} \equiv -\frac{1}{V} \left( \frac{\partial V}{\partial p} \right)_{T}
$$

We can also express entropy as a function of $T$ and $p$, $S = S(T, p)$, and its infinitesimal change as:

$$
\begin{split}
    \mathrm{d}S &= \left( \frac{\partial S}{\partial T} \right)_{p} \mathrm{d}T + \left( \frac{\partial S}{\partial p} \right)_{T} \mathrm{d}p \\
    &= \frac{C_{p}}{T} \mathrm{d}T - \left( \frac{\partial V}{\partial T} \right)_{p} \mathrm{d}p \\
    &= \frac{C_{p}}{T} \mathrm{d}T - V \kappa_{p} \mathrm{d}p
\end{split}
$$

Consider the derivative $\mathrm{d}S/\mathrm{d}T$ with $p$ held constant, we have the following relation:

$$
\frac{C_{p}}{T} = \frac{C_{V}}{T} + \frac{\kappa_{p}}{\kappa_{T}} \left( \frac{\partial V}{\partial T} \right)_{p} = \frac{C_{V}}{T} + V \frac{\kappa_{p}^{2}}{\kappa_{T}}
$$

This implies that the difference in heat capacities is determined by the equation of state:

$$
C_{p} - C_{V} = TV \frac{\kappa_{p}^{2}}{\kappa_{T}}
$$

Substituting this into the energy equation, we obtain the following expression for the internal energy:

$$
\mathrm{d}U = C_{V} \mathrm{d}T + \left( T \frac{\kappa_{p}}{\kappa_{T}} - p \right)\mathrm{d}V
$$
