# Statistical Mechanics - Ideal Gas

Consider a single particle in a box of volume $V = L_{x}L_{y}L_{z}$. The energy of the particle is given by:

$$
E = \frac{p^{2}}{2m}
$$

From quantum mechanics, we know that the wave function of the particle is given by:

$$
\psi(x,y,z) = A \sin{(k_{x}x)} \sin{(k_{y}y)} \sin{(k_{z}z)}
$$

where the wave numbers satisfy $k_{i} = \pi n_{i}/L_{i}$ so that the wave function vanishes at the walls.

The energy of the particle becomes quantised:

$$
E_{\mathbf{n}} = \frac{p^{2}}{2m} = \frac{\hbar^{2}}{2m} k^{2}
$$

where we define the wave vector:

$$
\mathbf{k} = (k_{x}, k_{y}, k_{z}) = \pi \left(\frac{n_{x}}{L_{x}}, \frac{n_{y}}{L_{y}}, \frac{n_{z}}{L_{z}}\right)
$$

and the index $\mathbf{n} = (n_{x}, n_{y}, n_{z})$ is a set of integers.

We can then consider the partition function for a single particle:

$$
\begin{split}
Z_{1} &= \sum \exp\left( -\beta E_{\mathbf{n}} \right) \\
&= \frac{V}{\pi^{3}} \sum \exp\left( -\beta \frac{\hbar^{2}}{2m} k^{2} \right) \frac{\pi}{L_{x}} \frac{\pi}{L_{y}} \frac{\pi}{L_{z}}
\end{split}
$$

Note that the quantities $\pi/L_{i}$ are the smallest possible values of $k_{i}$, which we can write as $\Delta k_{i}$. Then the summation can be replaced by an integral:

$$
\begin{split}
Z_{1} &= \frac{V}{\pi^{3}} \sum \exp\left( -\beta \frac{\hbar^{2}}{2m} k^{2} \right) \Delta k_{x} \Delta k_{y} \Delta k_{z} \\
&\approx \frac{V}{\pi^{3}} \int \exp\left( -\beta \frac{\hbar^{2}}{2m} k^{2} \right) \, \mathrm{d}k_{x} \mathrm{d}k_{y} \mathrm{d}k_{z} \\
&= \frac{V}{\pi^{3}} \int \exp\left( -\beta \frac{\hbar^{2}}{2m} k^{2} \right) k^{2} \sin{\theta} \, \mathrm{d}k \mathrm{d}\theta \mathrm{d}\phi \\
&= \frac{V}{\pi^{3}} \int_{0}^{\pi/2} \sin{\theta} \, \mathrm{d}\theta \int_{0}^{\pi/2} \, \mathrm{d}\phi \int_{0}^{\infty} k^{2} \exp\left( -\beta \frac{\hbar^{2}}{2m} k^{2} \right) \, \mathrm{d}k \\
&\equiv \int_{0}^{\infty} g(k) \exp\left( -\beta \frac{\hbar^{2}}{2m} k^{2} \right) \, \mathrm{d}k
\end{split}
$$

where the limits for the angles are chosen so that components of the wave vector are positive and we define $g(k) \equiv Vk^{2}/2\pi^{2}$ as the density of states.

Note that the approximation of the summation by an integral is valid if the number of states is large so that $\Delta k_{i}$ are small enough.

The integral can be evaluated to give the single particle partition function:

$$
Z_{1} = \frac{V}{(2\pi)^{3}} \left( \frac{2\pi m}{\beta \hbar^{2}} \right)^{3/2} \equiv \frac{V}{\lambda_{\text{th}}^{3}}
$$

where we define the thermal wavelength:

$$
\lambda_{\text{th}} = \sqrt{\frac{2\pi \hbar^{2}}{m k_{B}T}}
$$

## Density of States

There is another way of viewing the approximation made in the integration of the partition function. Note that the wave vector lives in a three-dimensional space $(k_{x}, k_{y}, k_{z})$ where each component must be non-negative. In the positive octant of the space, any point $(k_{x}, k_{y}, k_{z})$ represents a state of the particle and the distance from the origin gives the magnitude of the wave vector and thus the energy of the particle:

$$
k = \sqrt{k_{x}^{2} + k_{y}^{2} + k_{z}^{2}}
$$

Consider (an octant of) a sphere of radius $k$ in this space. If the state points are closely packed enough, the total number of states enclosed by the sphere is approximately the volume of the sphere divided by the volume $\prod \Delta k_{i}$ occupied by each state. We can write the number of states enclosed as:

$$
N = \frac{(4\pi k^{3}/3)/8}{\Delta k_{x} \Delta k_{y} \Delta k_{z}} = \frac{\pi k^{3}}{6 (\pi)^{3}} (L_{x}L_{y}L_{z}) = \frac{k^{3}V}{6\pi^{2}}
$$

Now we take the derivative of $N$ with respect to $k$ to find the density of states:

$$
g(k) \equiv \frac{\partial N}{\partial k} = \frac{k^{2}V}{2\pi^{2}}
$$

which agrees with the previous result.

## Multiple Particles

To find the partition function for $N$ particles, we note the issue of indistinguishability. Particles in an ideal gas are by nature indistinguishable, so we cannot choose a particular particle and let it occupy a particular state. Instead, we consider the number of particles occupying the same state designated by a particular $\mathbf{k}$ that represents the 'speed' of the particles. Finding all possible combinations of different numbers of particles occupying different states is in general a difficult combinatorial problem. However, since there are finite particles but an infinite number of states, we assume that for each $\mathbf{k}_{\mathbf{n}}$, there is either zero or one particle occupying that state. In this case, the partition function for $N$ particles can be shown to be:

$$
\boxed{
Z = \frac{Z_{1}^{N}}{N!} = \frac{V^{N}}{\lambda_{\text{th}}^{3N} N!}
}
$$

## Classical Limit

The above approximation is valid based on the premise that the number of available states is much larger than the number of particles $N$. To make an approximation for the former quantity, let us consider the integral in evaluating the single particle partition function:

$$
Z_{1} = \frac{V}{\pi^{3}} \int_{0}^{\infty} g(k) \exp\left( -\beta \frac{\hbar^{2}}{2m} k^{2} \right) \, \mathrm{d}k
$$

The states are characterised by the wave number $k$ and we are only interested in those that are not exponentially unlikely. We can then only evaluate the integral up to $\hbar^{2} k^{2}/2m \sim k_{B}T$:

$$
\frac{V}{\pi^{3}} \int_{0}^{\sqrt{2m k_{B}T/\hbar^{2}}} g(k) \, \mathrm{d}k \sim \frac{V}{\lambda_{\text{th}}^{3}}
$$

Then the condition becomes $V/\lambda_{\text{th}}^{3} \gg N$ or:

$$
\boxed{
n \lambda_{\text{th}}^{3} \ll 1
}
$$

which is known as the classical limit.

## Thermodynamics

Note that we can approximate the logarithm of the partition function using Stirling's approximation:

$$
\begin{split}
\ln{Z} &= N \ln{\left( \frac{V}{\lambda_{\text{th}}^{3}} \right)} - \ln{N!} \\
&\approx N \ln{\left( \frac{V}{\lambda_{\text{th}}^{3}} \right)} - N \ln{N} + N
\end{split}
$$

Then we can write out the free energy:

$$
F = -k_{B}T \ln{Z} = -k_{B}TN \left[ \ln{\left( \frac{V}{N\lambda_{\text{th}}^{3}} \right)} + 1 \right]
$$

and the rest of the thermodynamic quantities readily follow:

$$
\begin{split}
S &= -\left( \frac{\partial F}{\partial T} \right)_{V,N} = k_{B}N \left[ \frac{5}{2} - \ln{\left( \frac{V}{N\lambda_{\text{th}}^{3}} \right)} \right] \\
P &= -\left( \frac{\partial F}{\partial V} \right)_{T,N} = \frac{Nk_{B}T}{V} \\
U &= F + TS = \frac{3}{2} N k_{B}T \\
\end{split}
$$

which agree with the results from thermodynamics.
