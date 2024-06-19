# Kinetic Theory - Foundation

## Statistical Definition of Temperature

The concept of temperature can be defined with a statistical approach. Suppose two systems with energies $E_{1}$ and $E_{2}$, and the total number of microstates $\Omega_{1}(E_{1})$ and $\Omega_{2}(E_{2})$, respectively. There are then $\Omega_{1}(E_{1}) \Omega_{2}(E_{2})$ possible microstates for the composite system. The ergodic hypothesis implies that the system will tend towards a macroscopic configuration that maximises the number of microstates:

$$
\begin{split}
\frac{\mathrm{d}}{\mathrm{d}E_{1}} \left[ \Omega_{1}(E_{1}) \Omega_{2}(E_{2}) \right] &= 0 \\
\Omega_{2} \frac{\mathrm{d}\Omega_{1}}{\mathrm{d}E_{1}} + \Omega_{1} \frac{\mathrm{d}\Omega_{2}}{\mathrm{d}E_{2}} \frac{\mathrm{d}E_{2}}{\mathrm{d}E_{1}} &= 0 \\
\end{split}
$$

Assuming the total energy $E = E_{1} + E_{2}$ is constant, we have $\mathrm{d}E_{2} = -\mathrm{d}E_{1}$, and hence:

$$
\begin{split}
\frac{1}{\Omega_{1}} \frac{\mathrm{d}\Omega_{1}}{\mathrm{d}E_{1}} &= \frac{1}{\Omega_{2}} \frac{\mathrm{d}\Omega_{2}}{\mathrm{d}E_{2}} \\
\frac{\mathrm{d}\ln{\Omega_{1}}}{\mathrm{d}E_{1}} &= \frac{\mathrm{d}\ln{\Omega_{2}}}{\mathrm{d}E_{2}} \\
\end{split}
$$

This represents the most likely division of energy between two thermally connected systems, i.e., two systems at the same temperature. We can therefore define the temperature $T$ as:

$$
\boxed{
\frac{1}{k_{B}T} \equiv \frac{\mathrm{d}\ln{\Omega}}{\mathrm{d}E}
}
$$

where $k_{B} = 1.38 \times 10^{-23} \mathrm{J} \cdot \mathrm{K}^{-1}$ is the Boltzmann constant.

The temperature is a measure of the average energy per degree of freedom of a system.

## Canonical Ensemble

Consider two connected systems where one of them has an enormous amount of energy and is called the reservoir. Let the other system, which is the one of interest, take a small amount of energy $\epsilon$ such that it only has one single possible microstate. If the total energy is $E$, the reservoir has an energy $E - \epsilon$. The probability $P(\epsilon)$ of the system having energy $\epsilon$ is proportional to the number of microstates $\Omega(E - \epsilon)$ of the reservoir times the number for the system, which is unity:

$$
P(\epsilon) \propto \Omega(E - \epsilon)
$$

Consider the logarithm of $\Omega(E - \epsilon)$:

$$
\begin{split}
\ln{\Omega(E - \epsilon)} &\approx \ln{\Omega(E)} - \epsilon \frac{\mathrm{d}\ln{\Omega}}{\mathrm{d}E} = \ln{\Omega(E)} - \epsilon \frac{1}{k_{B}T} \\
\end{split}
$$

where we have made use of the previous definition of temperature.

The probability $P(\epsilon)$ is therefore given by:

$$
P(\epsilon) \propto e^{-\epsilon/k_{B}T}
$$

This is known as the Boltzmann distribution or the canonical distribution. The constant of proportionality is determined by the normalisation condition. If we define $\beta \equiv 1/k_{B}T$, the factor:

$$
\boxed{
e^{-\beta \epsilon} = e^{-E/k_{B}T}
}
$$

is called the Boltzmann factor.

## Maxwell-Boltzmann Distribution

In an ideal gas, we neglect any rotational or vibrational degrees of freedom and assume that the particles are point particles with no interaction among them. The energy of a single particle is then given by:

$$
\frac{1}{2}m v^{2} = \frac{1}{2} m \left( v_{x}^{2} + v_{y}^{2} + v_{z}^{2} \right)
$$

First consider a single direction, say $x$. We define the velocity distribution $g(v_{x})\mathrm{d}v_{x}$ as the fraction of particles with velocities between $v_{x}$ and $v_{x} + \mathrm{d}v_{x}$ in the $x$ direction. From Boltzmann distribution, we have:

$$
g(v_{x}) \mathrm{d}v_{x} \propto e^{-\beta m v_{x}^{2}/2} \mathrm{d}v_{x}
$$

where $\beta = 1/k_{B}T$ is given by the temperature of the gas.

Normalising the distribution, we have:

$$
\boxed{
g(v_{x}) = \left( \frac{m}{2\pi k_{B}T} \right)^{1/2} e^{-\beta m v_{x}^{2}/2}
}
$$

Some expected values of the distribution are:

$$
\begin{split}
\langle v_{x} \rangle &= \int_{-\infty}^{\infty} v_{x} g(v_{x}) \mathrm{d}v_{x} = 0 \\
\langle v_{x}^{2} \rangle &= \int_{-\infty}^{\infty} v_{x}^{2} g(v_{x}) \mathrm{d}v_{x} = \frac{k_{B}T}{m} \\
\end{split}
$$

Let us define another distribution $g(\mathbf{v})$ such that $g(\mathbf{v}) \mathrm{d}^{3}v = g(\mathbf{v}) \mathrm{d}v_{x} \mathrm{d}v_{y} \mathrm{d}v_{z}$ is the fraction of particles with velocities in the range $[v_{x}, v_{x} + \mathrm{d}v_{x}] \times [v_{y}, v_{y} + \mathrm{d}v_{y}] \times [v_{z}, v_{z} + \mathrm{d}v_{z}]$. Mathematically, $g(\mathbf{v})$ is a joint probability distribution of the velocities. Apparently, we have the following relation:

$$
g(v_{x}) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(\mathbf{v}) \mathrm{d}v_{y} \mathrm{d}v_{z}
$$

Since we can assume that the ideal gas is isotropic, $g$ should be a function of the magnitude $v$ of the velocity. We expect $g(\mathbf{v})$ to be a product of three velocity distributions $g(v_{x})$, $g(v_{y})$, and $g(v_{z})$:

$$
\boxed{
\begin{split}
g(\mathbf{v}) &= g(v_{x}) g(v_{y}) g(v_{z}) \\
&= \left( \frac{m}{2\pi k_{B}T} \right)^{3/2} e^{-\beta m v^{2}/2}
\end{split}
}
$$

We can change the variables from $(v_{x}, v_{y}, v_{z})$ to $(v, \theta, \phi)$ and obtain a new joint distribution $f(v, \theta, \phi)$. From multivariable calculus, we have:

$$
g(\mathbf{v}) \,  \mathrm{d}^{3}v = g(\mathbf{v}) v^{2} \sin{\theta} \, \mathrm{d}v \mathrm{d}\theta \mathrm{d}\phi = f(v, \theta, \phi) \, \mathrm{d}v \mathrm{d}\theta \mathrm{d}\phi
$$

where the extra factor $v^{2} \sin{\theta}$ is the Jacobian of the transformation.

The joint distribution $f(v, \theta, \phi)$ is therefore given by:

$$
f(v, \theta, \phi) = g(\mathbf{v}) v^{2} \sin{\theta} = g(\mathbf{v}) v^{2} \sin{\theta}
$$

The distribution for particle speeds $f(v)$ is then given by:

$$
f(v) = \int_{0}^{\pi} \int_{0}^{2\pi} f(v, \theta, \phi) \, \mathrm{d}\theta \mathrm{d}\phi = 4\pi v^{2} g(v)
$$

Substituting the expression for the velocity distribution $g(\mathbf{v})$, we have:

$$
\boxed{
f(v) = \left( \frac{m}{2\pi k_{B}T} \right)^{3/2} 4\pi v^{2} e^{-\beta m v^{2}/2}
}
$$

whose normalisation can be easily verified.

This is known as the **Maxwell-Boltzmann distribution**. Some expected values of the distribution are:

$$
\begin{split}
\langle v \rangle &= \int_{0}^{\infty} v f(v) \mathrm{d}v = \left( \frac{8k_{B}T}{\pi m} \right)^{1/2} \\
\langle v^{2} \rangle &= \int_{0}^{\infty} v^{2} f(v) \mathrm{d}v = \frac{3k_{B}T}{m} = \frac{1}{3} \langle v_{x} \rangle^{2} \\
\end{split}
$$

We also define the thermal speed $v_{\text{th}} \equiv \sqrt{2k_{B}T/m}$, which is the most probable speed of the particles where the distribution peaks.

### Local Equilibrium

Note that the $T$ function usde in the distributions has been assumed to be a global constant. In fact, we may treat it as a position function as long as the temperature varies slowly enough. That is, the change

## Pressure and Equation of State

Suppose a wall perpendicular to the z-axis. Consider the particles with z-velocity between $v_{z}$ and $v_{z} + \mathrm{d}v_{z}$. The momentum of these particles is $mv_{z}$. The pressure $\mathrm{d}P$ exerted by these particles on the wall is:

$$
\mathrm{d}P(v_{z}) = 2mv_{z} \mathrm{d}\Phi(v_{z})
$$

where $\mathrm{d}\Phi(v_{z})$ is the differential of the particle flux, i.e., the number of particles with z-velocity between $v_{z}$ and $v_{z} + \mathrm{d}v_{z}$ crossing the wall per unit time per unit area.

The flux is given by:

$$
\mathrm{d}\Phi(v_{z}) = \frac{\mathrm{d}N(v_{z})}{At} = n v_{z} g(v_{z}) \mathrm{d}v_{z}
$$

The pressure $\mathrm{d}P(v_{z})$ is therefore given by:

$$
\mathrm{d}P(v_{z}) = 2mnv_{z}^{2} g(v_{z}) \mathrm{d}v_{z}
$$

so that the total pressure $P$ is given by:

$$
P = \int_{0}^{\infty} 2mnv_{z}^{2} g(v_{z}) \mathrm{d}v_{z} = \int_{-\infty}^{\infty} mnv_{z}^{2} g(v_{z}) \mathrm{d}v_{z} = mn \langle v_{z}^{2} \rangle
$$

where at the first step we choose the particles moving towards the wall, and at the second step we use the fact that the distribution is symmetric.

This implies that the pressure of an ideal gas is directly proportional to the average kinetic energy of the particles. Substituting the expected value of the distribution and rearranging, we have:

$$
\boxed{
P = n m \langle v_{z}^{2} \rangle = \frac{1}{3} n m \langle v^{2} \rangle = n k_{B}T
}
$$

We can use the thermal speed $v_{\text{th}} \equiv \sqrt{2P/nm}$ to write:

$$
\boxed{
\frac{mv_{\text{th}}^{2}}{2} = k_{B}T
}
$$

Writing $N = nV$, where $N$ is the total number of particles and $V$ is the volume of the gas, we have the ideal gas law:

$$
\boxed{
PV = N k_{B}T
}
$$
