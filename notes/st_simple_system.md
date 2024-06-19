# Statistical Mechanics - Simple Systems

We have introduced the partition function of a system as:

$$
Z = \sum_{i} \exp\left( -\beta E_{i} \right)
$$

where $\beta = 1/k_{B} T$ and $E_{i}$ are the energy levels of the system.

Given the partition function, we can calculate the free energy of the system as:

$$
F = -k_{B} T \ln Z
$$

We can also calculate the entropy of the system as:

$$
S = -\left( \frac{\partial F}{\partial T} \right)_{V}
$$

and the internal energy as:

$$
U = F + TS
$$

There is another equivalent route to the internal energy and entropy:

$$
\begin{split}
U &= -\left( \frac{\partial \ln Z}{\partial \beta} \right)_{V} \\
S &= \frac{U - F}{T}
\end{split}
$$

## Paramagnetic Solid

Consider a spin-half paramagnet consisting of $N$ atoms, each with a magnetic moment $\mu$ associated with its spin via the relation:

$$
\mu = g \mu_{B} S
$$

where $S$ is the spin quantum number that takes the values $\pm 1/2$.

For spin-half systems, $g$ evaluates to $2$. This means that under the influence of an external magnetic field $B$ aligned along the $z$-axis, the energy levels of the system are given by:

$$
E_{\pm} = \pm \mu B
$$

The partition function of the system is then:

$$
Z_{1} = \exp\left( -\beta \mu B \right) + \exp\left( \beta \mu B \right) = 2 \cosh\left( \beta \mu B \right)
$$

The free energy of the system is:

$$
F_{1} = -k_{B} T \ln \left[ 2 \cosh\left( \beta \mu B \right) \right]
$$

with the entropy:

$$
S_{1} = -\left( \frac{\partial F}{\partial T} \right)_{B} = k_{B} \ln \left[ 2 \cosh\left( \beta \mu B \right) \right] - \frac{\mu B}{T} \tanh\left( \beta \mu B \right)
$$

and the internal energy:

$$
U_{1} = F_{1} + TS_{1} = -\mu B \tanh\left( \beta \mu B \right)
$$

In a paramagnetic solid, each atom is fixed in space so that they are distinguishable and their interactions are weak so that they can be treated as independent. The partition function of the whole system is then:

$$
Z = Z_{1}^{N}
$$

The free energy, entropy and internal energy of the system are then:

$$
\begin{split}
F &= -N k_{B} T \ln \left[ 2 \cosh\left( \beta \mu B \right) \right] \\
S &= N k_{B} \ln \left[ 2 \cosh\left( \beta \mu B \right) \right] - \frac{N\mu B}{T} \tanh\left( \beta \mu B \right) \\
U &= -N \mu B \tanh\left( \beta \mu B \right)
\end{split}
$$

We can compute the heat capacity of the system at constant magnetic field as:

$$
C_{B} = \left( \frac{\partial U}{\partial T} \right)_{B} = N k_{B} \left( \frac{\mu B}{k_{B}T} \right)^{2} \frac{1}{\cosh^{2}\left( \beta \mu B \right)}
$$

To derive an equation of state from the free energy, we draw upon the relation from thermodynamics:

$$
\mathrm{d}F = -S \mathrm{d}T - m \mathrm{d}B
$$

where $m = \sum_{i} \mu_{i}$ is the total magnetic moment of the system.

In analogy to the ideal gas, we can write an equation of state between $m$ and $B$:

$$
m = -\left( \frac{\partial F}{\partial B} \right)_{T} = N \mu \tanh\left( \beta \mu B \right)
$$

Introducing the magnetization per atom $M = m/N$ and assuming weak fields such that $\mu B \ll k_{B}T$, we can write the magnetization as:

$$
\boxed{
M = \frac{N \mu}{V} \tanh\left( \frac{\mu B}{k_{B}T} \right) \approx \frac{N\mu^{2}B}{k_{B}T}
}
$$

which is known as the Curie law.

## Harmonic Oscillator

### One-Dimensional Oscillator

It is known from quantum mechanics that the energy levels of a one-dimensional harmonic oscillator are given by:

$$
E_{n} = \left( n + \frac{1}{2} \right) \hbar \omega
$$

This means that the partition function of a single one-dimensional harmonic oscillator is:

$$
Z_{1} = \sum_{n} \exp\left( -\beta E_{n} \right) = \frac{\exp\left( -\beta \hbar \omega / 2 \right)}{1 - \exp\left( -\beta \hbar \omega \right)} = \frac{1}{2 \sinh{\left( \beta \hbar \omega / 2 \right)}}
$$

where the sum can be treated as a geometric series.

We can immediately write the internal energy of the system as:

$$
U_{1} = -\left( \frac{\partial \ln Z_{1}}{\partial \beta} \right)_{V} = \frac{\hbar \omega}{2} + \frac{\hbar \omega}{\exp\left( \beta \hbar \omega \right) - 1}
$$

For a system of $N$ independent one-dimensional harmonic oscillators, the partition function is:

$$
Z = Z_{1}^{N} = \left[ \frac{\exp\left( -\beta \hbar \omega / 2 \right)}{1 - \exp\left( -\beta \hbar \omega \right)} \right]^{N} = \left[ \frac{1}{2 \sinh{\left( \beta \hbar \omega / 2 \right)}} \right]^{N}
$$

The internal energy of the system is just $N$ times that of the single particle case:

$$
U = -\left( \frac{\partial \ln Z}{\partial \beta} \right)_{V} = \frac{N \hbar \omega}{2} + \frac{N \hbar \omega}{\exp\left( \beta \hbar \omega \right) - 1}
$$

Observe that as $T \to 0$ and $\beta \to \infty$, the internal energy approaches $N \hbar \omega / 2$. As $T \to \infty$:

$$
U \approx \frac{N \hbar \omega}{2} + \frac{N \hbar \omega}{1 + \beta \hbar \omega - 1} = \frac{N \hbar \omega}{2} + N k_{B} T \approx N k_{B} T
$$

which is independent of the frequency of the oscillator.

The result at high temperatures is consistent with the classical equipartition theorem. The theorem states that if the energy of a classical system is the sum of $N$ quadratic terms (i.e. $N$ degrees of freedom) and the system is in thermal equilibrium at temperature $T$, then the mean energy of the system is $N k_{B} T / 2$.

### Three-Dimensional Oscillator

As each of the three dimensions of a three-dimensional harmonic oscillator is independent, the energy levels of the system are given by:

$$
E = \sum_{x, y, z} E_{i} = \left( n_{x} + \frac{1}{2} \right) \hbar \omega + \left( n_{y} + \frac{1}{2} \right) \hbar \omega + \left( n_{z} + \frac{1}{2} \right) \hbar \omega = \left( n_{x} + n_{y} + n_{z} + \frac{3}{2} \right) \hbar \omega
$$

where we have assumed that the oscillator is isotropic so that the frequency is the same in all three dimensions.

The single particle partition function is then:

$$
\begin{split}
    Z_{1}^{(3D)} &= \sum_{x, y, z} \exp\left( -\beta \sum_{x, y, z} E_{i} \right) \\
    &= \sum_{x, y, z} \exp\left( -\beta E_{x} \right) \exp\left( -\beta E_{y} \right) \exp\left( -\beta E_{z} \right) \\
    &= \sum_{x} \exp\left( -\beta E_{x} \right) \sum_{y} \exp\left( -\beta E_{y} \right) \sum_{z} \exp\left( -\beta E_{z} \right) \\
    &= Z_{1}^{3} \\
    &= \left[ \frac{\exp\left( -\beta \hbar \omega / 2 \right)}{1 - \exp\left( -\beta \hbar \omega \right)} \right]^{3}
\end{split}
$$

The partition function of $N$ independent three-dimensional harmonic oscillators is similarly given by:

$$
Z^{(3D)} = Z_{1}^{N} = \left[ \frac{1}{1 - \exp\left( -\beta \hbar \omega \right)} \right]^{3N}
$$

The internal energy of the system is just three times that of the one-dimensional case:

$$
U = \frac{3N \hbar \omega}{2} + \frac{3N \hbar \omega}{\exp\left( \beta \hbar \omega \right) - 1}
$$

The heat capacity of the system at constant volume is:

$$
C_{V} = \left( \frac{\partial U}{\partial T} \right)_{V} = 3N k_{B} \left( \frac{\hbar \omega}{k_{B}T} \right)^{2} \frac{\exp\left( \beta \hbar \omega \right)}{\left[ \exp\left( \beta \hbar \omega \right) - 1 \right]^{2}} = 3N k_{B} \left[ \frac{\beta \hbar \omega/2}{\sinh\left( \beta \hbar \omega / 2 \right)} \right]^{2}
$$

In high temperature limit, the heat capacity approaches $3N k_{B}$, which is consistent with the classical equipartition theorem. In the low temperature limit, the heat capacity approaches zero.

## Polyatomic Ideal Gas

We can extend the results of the ideal gas to polyatomic molecules by considering the single particle partition function of the form:

$$
Z_{1} = \frac{V}{\lambda_{\text{th}}^{3}} Z_{\text{int}}(\beta)
$$

where the additional partition function $Z_{\text{int}}$ depends on the internal structure of the molecule.

In general, we consider vibrational and rotational degrees of freedom in a polyatomic molecule such that the single particle partition function can be written as:

$$
Z_{1} = Z_{\text{trans}} Z_{\text{rot}} Z_{\text{vib}}
$$

Note that the internal energy is the sum of the translational, rotational and vibrational energies:

$$
U = -\left( \frac{\partial \ln Z}{\partial \beta} \right)_{V} = \frac{3}{2} k_{B}T + U_{\text{rot}} + U_{\text{vib}}
$$

and the same can be said for the heat capacity:

$$
C_{V} = \left( \frac{\partial U}{\partial T} \right)_{V} = \frac{3}{2} k_{B} + C_{\text{rot}} + C_{\text{vib}}
$$

### Vibration

We model the vibrational motion of a molecule as a one-dimensional harmonic oscillator with the frequency $\omega$. The energy levels of the system are then:

$$
E_{n} = \left( n + \frac{1}{2} \right) \hbar \omega
$$

so that we have the partition function that accounts for the vibrational motion:

$$
Z_{\text{vib}} = \frac{1}{1 - \exp\left( -\beta \hbar \omega \right)}
$$

We know the internal energy and heat capacity of a harmonic oscillator:

$$
\begin{split}
U_{\text{vib}} &= \frac{\hbar \omega}{2} + \frac{\hbar \omega}{\exp\left( \beta \hbar \omega \right) - 1} \\
C_{\text{vib}} &= k_{B} \left[ \frac{\beta \hbar \omega/2}{\sinh\left( \beta \hbar \omega / 2 \right)} \right]^{2}
\end{split}
$$

Let us define the characteristic temperature scale for the vibrational motion:

$$
\theta_{\text{vib}} = \frac{\hbar \omega}{k_{B}}
$$

For $T \ll \theta_{\text{vib}}$, the heat capacity approaches zero, in which case we say that the vibrational motion is frozen out. For $T \gg \theta_{\text{vib}}$, the heat capacity approaches $k_{B}$, which is consistent with the classical equipartition theorem.

### Rotation

We model the rotational motion of a molecule as a rigid rotor. The energy levels of the system are quantised by the total angular momentum:

$$
E_{l} = \frac{\hbar^{2}}{2I} l(l + 1)
$$

where $l$ is the quantum number associated with the angular momentum and $I$ is the moment of inertia of the molecule.

Noting that each energy level is $(2l + 1)$-fold degenerate due to quantum number $m$, we have the partition function that accounts for the rotational motion:

$$
\begin{split}
    Z_{\text{rot}} &= \sum_{l} (2l + 1) \exp\left[ -\beta \frac{\hbar^{2}}{2I} l(l + 1) \right] \\
    &= 1 + 3 \exp\left( -2\beta \frac{\hbar^{2}}{2I} \right) + 5 \exp\left( -6\beta \frac{\hbar^{2}}{2I} \right) + \ldots
\end{split}
$$

This is a difficult sum to evaluate, but approximations can be made for the high and low temperature limits. We define the characteristic temperature scale for the rotational motion:

$$
\theta_{\text{rot}} = \frac{\hbar^{2}}{2Ik_{B}}
$$

For $T \ll \theta_{\text{rot}}$, we consider only the first two terms of the sum:

$$
Z_{\text{rot}} \approx 1 + 3 \exp\left( -2\beta \frac{\hbar^{2}}{2I} \right)
$$

which gives the internal energy and heat capacity:

$$
\begin{split}
    U_{\text{rot}} &\approx \frac{\hbar^{2}}{I} \frac{3}{3 + \exp\left( \beta \hbar^{2}/I \right)} \\
    C_{\text{rot}} &\approx k_{B} \left( \frac{\hbar^{2}/I}{\exp\left( \beta \hbar^{2}/I \right) - 1} \right)^{2}
\end{split}
$$

For $T \gg \theta_{\text{rot}}$, we consider the sum as a continuous integral:

$$
Z_{\text{rot}} \approx \int_{0}^{\infty} (2l + 1) \exp\left[ -\beta \frac{\hbar^{2}}{2I} l(l + 1) \right] \, \mathrm{d}l = \frac{T}{\theta_{\text{rot}}}
$$

which gives the internal energy and heat capacity:

$$
\begin{split}
    U_{\text{rot}} &\approx k_{B}T \\
    C_{\text{rot}} &\approx k_{B}
\end{split}
$$

as expected from the classical equipartition theorem.

### Transition between regimes

In general, the temperature scale of vibrational motion is much larger than that of rotational motion. This means that the typical graph of heat capacity against temperature for a polyatomic molecule have three plateaus. In $T \ll \theta_{\text{rot}} \ll \theta_{\text{vib}}$, the heat capacity is $3Nk_{B}/2$ due to the translational motion. In $\theta_{\text{rot}} \ll T \ll \theta_{\text{vib}}$, the heat capacity increases to $5Nk_{B}/2$ due to the activation of the rotational motion. In $T \gg \theta_{\text{vib}}$, the heat capacity increases to $7Nk_{B}/2$ due to the activation of the vibrational motion.
