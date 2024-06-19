# Statistical Mechanics - Photon Gas

In the standard model of particle physics, photons are massless particles that do not interact with each other. Photons are also bosons with $\pm 1$ spin, but not zero. In a sense, photons constitute an ideal gas.

It can be shown that electromagnetic radiation in a cavity, also known as a photon gas, can be described by a group of harmonic oscillators whose angular frequencies are related to the wave numbers via the dispersion relation:

$$
\omega = ck
$$

The wave numbers are quantised due to the boundary conditions of the cavity, similar to the ideal gas:

$$
k_{i} = \frac{\pi n_{i}}{L_{i}}
$$

Following a similar treatment then, we can write the density of states for the photon gas as a function of the wave number:

$$
g(k) \, \mathrm{d}k = \frac{V}{2\pi^{2}} k^{2} \times 2 \, \mathrm{d}k = \frac{V}{\pi^{2}} k^{2} \, \mathrm{d}k
$$

where the factor of two accounts for the two possible polarisations, or spin states, of the photon.

Noting that $\mathrm{d}k = \mathrm{d}\omega/c$, we may instead write the density of states as a function of the angular frequency:

$$
g(\omega) \, \mathrm{d}\omega = \frac{V}{\pi^{2}c^{3}} \omega^{2} \, \mathrm{d}\omega
$$

We know that for a single harmonic oscillator of angular frequency $\omega$, the partition function is given by:

$$
Z_{1} = \frac{\exp\left( -\beta \hbar \omega / 2 \right)}{1 - \exp\left( -\beta \hbar \omega \right)}
$$

so that its internal energy is:

$$
\frac{\hbar \omega}{2} + \frac{\hbar \omega}{\exp\left( \beta \hbar \omega \right) - 1}
$$

With this, we may write the energy density in the frequency domain as:

$$
g(\omega) \frac{\hbar \omega}{2} + g(\omega) \frac{\hbar \omega}{\exp\left( \beta \hbar \omega \right) - 1}
$$

However, this expression is problematic because the constant factor diverges if we integrate over $\omega \in [0, \infty)$. To resolve this, we define the zero energy level in such a way that the constant term vanishes, and the true total internal energy (per unit volume) is given by:

$$
\frac{U}{V} = \frac{1}{V} \int_{0}^{\infty} g(\omega) \frac{\hbar \omega}{\exp\left( \beta \hbar \omega \right) - 1} \, \mathrm{d}\omega \equiv \int_{0}^{\infty} \rho_{\omega} \, \mathrm{d}\omega
$$

where we define the spectral energy density, also known as the Planck distribution:

$$
\boxed{
\rho_{\omega} \equiv \frac{\hbar}{\pi^{2}c^{3}} \frac{\omega^{3}}{\exp\left( \beta \hbar \omega \right) - 1}
}
$$

We could hence evaluate $u = U/V$:

$$
\boxed{
u = \frac{\hbar}{\pi^{2}c^{3}} \int_{0}^{\infty} \frac{\omega^{3}}{\exp\left( \beta \hbar \omega \right) - 1} \, \mathrm{d}\omega = \left( \frac{\pi^{2} k_{B}^{4}}{15 c^{3} \hbar^{3}} \right) T^{4}
}
$$

## Thermodynamic Quantities

The thermodynamics of a photon gas is more easily understood by treating it as a boson gas with $\pm 1$ spin and zero chemical potential. The partition function of the photon gas is then:

$$
\ln{\mathcal{Z}} = -\sum_{i} \ln{\left[ 1 - e^{-\beta (\varepsilon_{i})} \right]}
$$

where the energy levels are quantised as:

$$
\varepsilon_{i} = \hbar \omega_{i} = \hbar c k_{i}
$$

The mean occupation number of the $i$-th energy level is:

$$
\bar{n}_{i} = \frac{1}{\exp{(\beta \hbar \omega_{i})} - 1}
$$

which leads to the internal energy:

$$
\begin{split}
U &= \sum_{i} \varepsilon_{i} \bar{n}_{i} \\
&= \sum_{i} \frac{\hbar \omega_{i}}{\exp{(\beta \hbar \omega_{i})} - 1} \\
&\approx \int_{0}^{\infty} \frac{\hbar \omega}{\exp{(\beta \hbar \omega)} - 1} g(\omega) \, \mathrm{d}\omega
\end{split}
$$

which agrees with the previous result where photons are treated as harmonic oscillators.

It turns out that the grand potential of the photon gas is related to the internal energy:

$$
\begin{split}
\Phi &= -k_{B}T \ln{\mathcal{Z}} \\
&= -k_{B}T \sum_{i} \ln{\left[ 1 - e^{-\beta (\varepsilon_{i})} \right]} \\
&\approx -k_{B}T \int_{0}^{\infty} \ln{\left[ 1 - e^{-\beta \hbar \omega} \right]} g(\omega) \, \mathrm{d}\omega \\
&= -\frac{1}{3} U
\end{split}
$$

so that the equation of state of the photon gas is:

$$
\boxed{
P = -\frac{\Phi}{V} = \frac{1}{3} u
}
$$

## Thermal Radiation

Note that while the power of $T$ is reminiscent of the Stefan-Boltzmann law, the coefficient is different. The equation describes the energy density of a photon gas in a cavity but not how a black body absorbs and emits radiation. To derive the Stefan-Boltzmann law, we invoke Kirchhoff's law of radiation:

$$
\frac{\eta(\omega, \hat{k}, M, T)}{\alpha(\omega, -\hat{k}, M, T)} = \frac{c}{4\pi} \rho_{\omega}(\omega, T) \cos{\theta}
$$

For a blackbody, we take $\alpha = 1$ and integrate emission over all angles to obtain Lambert's law:

$$
\begin{split}
P_{B}(\omega, T) &= \int \eta(\omega, \hat{k}, M, T) \, \mathrm{d}\Omega \\
&= \int_{0}^{2\pi} \int_{0}^{\pi/2} \frac{c}{4\pi} \rho_{\omega}(\omega, T) \cos{\theta} \sin{\theta} \, \mathrm{d}\theta \, \mathrm{d}\phi \\
&= \frac{c}{4} \rho_{\omega}(\omega, T)
\end{split}
$$

Integrating this over all frequencies, we obtain the Stefan-Boltzmann law:

$$
\boxed{
P_{B}(T) = \int_{0}^{\infty} P_{B}(\omega, T) \, \mathrm{d}\omega = \sigma T^{4}
}
$$

where we define the Stefan-Boltzmann constant:

$$
\sigma = \frac{\pi^{2} k_{B}^{4}}{60 c^{2} \hbar^{3}}
$$

Note the simple relation $P_{B} = cu/4$ between the energy density and radiation power.
