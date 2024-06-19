# Statistical Mechanics - Quantum Gases

So far it has been assumed that the number of single-particle states available to particles is much greater than the number of the particles, meaning that the probability of one particle occupying any given single-particle state is small, and the probability of more than one particle occupying the same state could be thus ignored. This assumption can be made within the classical limit.

## Fermions and Bosons

To relax this assumption, consider a 2-particle wave function $\psi(1,2)$, where the first argument corresponds to the state of the first particle and the second to that of the second particle. Swapping the two particle means the operation $\psi(1,2) \rightarrow \psi(2,1)$. If the particles are indistinguishable, this operation should be equivalent to a phase change that does not affect the probability density:

$$
\begin{split}
\psi(2,1) &= e^{i \phi} \psi(1,2) \\
\lvert \psi(2,1) \rvert^{2} &= \lvert \psi(1,2) \rvert^{2}
\end{split}
$$

Applying the swapping operation twice:

$$
\psi(2,1) = e^{i \phi} \psi(1,2) = e^{2i \phi} \psi(2,1)
$$

Thus, $e^{2i \phi} = 1$ and $e^{i \phi} = \pm 1$. This implies two types of **exchange symmetries**:

$$
\begin{split}
&\text{bosons: } \psi(2,1) = \psi(1,2) \\
&\text{fermions: } \psi(2,1) = -\psi(1,2)
\end{split}
$$

From quantum mechanics, bosons are particles with integer spin, while fermions are particles with half-integer spin. The fermions are subject to the **Pauli exclusion principle**, which states that if the states 1 and 2 are the same, then:

$$
\psi(1,1) = -\psi(1,1) = 0
$$

This implies that no two fermions can be in the same single-particle state.

Recall that the microstates of a box of ideal gas are specified in terms of the occupation number $n_{i}$ of single-particle states labelled by $i$. The exchange symmetries impose constraints on the values of these occupation numbers can take: for bosons, $n_{i}$ can be any natural number; for fermion, $n_{i}$ is either zero or unity. This implies that the assumption of single-particle states in ideal gas is in fact a requirement for fermion gases.

## Partition Function

The grand partition function $\mathcal{Z}$ is given by:

$$
\mathcal{Z} = \sum_{\alpha} e^{-\beta(E_{\alpha} - \mu N_{\alpha})}
$$

where the microstates are $\alpha = \{n_{i}\}$ and the energy levels $E_{\alpha}$ are given by the single-particle energy level $\varepsilon_{i}$:

$$
E_{\alpha} = \sum_{i} n_{i} \varepsilon_{i}
$$

and the particle number $N_{\alpha}$ in state $\alpha$ is:

$$
N_{\alpha} = \sum_{i} n_{i}
$$

Then:

$$
\begin{split}
\mathcal{Z} &= \sum_{\{n_{i}\}} e^{-\beta \sum_{i} n_{i}(\varepsilon_{i} - \mu)} \\
            &= \sum_{n_{1}} \sum_{n_{2}} \dots \prod_{i} e^{-\beta n_{i}(\varepsilon_{i} - \mu)} \\
            &= \prod_{i} \sum_{n_{i}} e^{-\beta n_{i}(\varepsilon_{i} - \mu)}
\end{split}
$$

Note that we can interpret the grand partition function as the product of many smaller partition functions, each corresponding to a single-particle state:

$$
\mathcal{Z} = \prod_{i} \mathcal{Z}_{i}
$$

where:

$$
\mathcal{Z}_{i} = \sum_{n_{i}} e^{-\beta n_{i}(\varepsilon_{i} - \mu)}
$$

For bosons, the summation index $n_{i}$ ranges from zero to infinity, forming a geometric series, so:

$$
\mathcal{Z} = \prod_{i} \sum_{n_{i}=0}^{\infty} \left[ e^{-\beta (\varepsilon_{i} - \mu)} \right]^{n_{i}} = \prod_{i} \frac{1}{1 - e^{-\beta (\varepsilon_{i} - \mu)}}
$$

For fermions, $n_{i}$ only takes zero or unity, so:

$$
\mathcal{Z} = \prod_{i} \left[ 1 + e^{-\beta (\varepsilon_{i} - \mu)} \right]
$$

These results can be compactly written as:

$$
\boxed{
\ln{\mathcal{Z}} = \pm \sum_{i} \ln{\left[ 1 \pm e^{-\beta (\varepsilon_{i} - \mu)} \right]}
}
$$

where the plus sign corresponds to fermions and the negative sign to bosons.

The probability for a set of occupation numbers, i.e., the probability for a a state to occur, is given by the grand canonical distribution:

$$
p_{\alpha} \equiv p(n_{1}, n_{2}, \dots) = \frac{1}{\mathcal{Z}} e^{-\beta \sum_{i} n_{i}(\varepsilon_{i} - \mu)}
$$

The mean occupation number of a single-particle state $j$ is:

$$
\bar{n}_{j} \equiv \langle n_{j} \rangle = \sum_{\{n_{i}\}} n_{j} p(n_{1}, n_{2}, \dots) = \frac{1}{\mathcal{Z}} \sum_{\{n_{i}\}} n_{j} e^{-\beta \sum_{i} n_{i}(\varepsilon_{i} - \mu)} = -\frac{1}{\beta} \frac{\partial \ln{\mathcal{Z}}}{\partial \mu}
$$

Substituting the expression for $\ln{\mathcal{Z}}$:

$$
\boxed{
\bar{n}_{i} = \frac{1}{e^{\beta (\varepsilon_{i} - \mu)} \pm 1}
}
$$

This equation predicts how many particles will be in any given single-particle state on average. The plus sign gives the **Fermi-Dirac statistics** while the minus sign gives the **Bose-Einstein statistics**. The equation is useful given the single-particle energy levels $\varepsilon_{i}$, which is obtained with quantum mechanics, and the chemical potential $\mu$, which is a function of the particle density and the temperature.

The thermodynamics of a quantum gas can be constructed using the mean energy $U$:

$$
\begin{split}
  U &= -\frac{\partial \ln{\mathcal{Z}}}{\partial \beta} + \frac{\mu}{\beta} \frac{\partial \ln{\mathcal{Z}}}{\partial \mu} \\
    &= \sum_{i} \left[ \frac{e^{-\beta (\varepsilon_{i} - \mu)}(\varepsilon_{i} - \mu)}{1 \pm e^{-\beta (\varepsilon_{i} - \mu)}} + \frac{e^{-\beta (\varepsilon_{i} - \mu)}\mu}{1 \pm e^{-\beta (\varepsilon_{i} - \mu)}} \right] \\
    &= \sum_{i} n_{i} \varepsilon_{i}
\end{split}
$$

along with the grand potential $\Phi$:

$$
\Phi = -k_{B} T \ln{\mathcal{Z}}
$$

and the entropy $S$:

$$
S = \frac{U - \Phi - \mu N}{T}
$$

## Calculation in Continuum Limit

The single-particle states depend on the particles' momentum and spin:

$$
i = (\mathbf{p}, s_{z})
$$

where $\mathbf{p} = \hbar \mathbf{k}$ is the particle momentum and $s_{z}$ is the particle spin projected on an arbitrary axis, allowing $(2s + 1)$ values from $-s$ to $+s$.

Generally, the energy $\varepsilon$ of a particle depends only on the magnitude $k$ of $\mathbf{k}$ via a relativistic dispersion relation:

$$
\varepsilon(k) = \sqrt{m^{2} c^{4} + \hbar^{2} k^{2} c^{2}}
$$

which means that the degeneracy of each energy level is $(2s + 1)$ due to the spin.

For a non-relativistic gas, the dispersion relation is:

$$
\boxed{
\varepsilon(k) = \frac{\hbar^{2} k^{2}}{2m}
}
$$

Since the occupation numbers $\bar{n}_{i}$ depends on $k$ only, if the changes in $k$ are small, the sum $\sum_{i}$ over single-particle states can be approximated with an integral:

$$
\begin{split}
\sum_{i} &= (2s + 1)\sum_{\mathbf{k}} \\
         &= \frac{(2s + 1)V}{(2\pi)^{3}} \int \, \mathrm{d}^{3}\mathbf{k} \\
         &= \frac{(2s + 1)V}{(2\pi)^{3}} \int_{0}^{\infty} 4\pi k^{2} \, \mathrm{d}k \\
         &= \int_{0}^{\infty} g(k) \, \mathrm{d}k
\end{split}
$$

where the density of state is defined as:

$$
\boxed{
g(k) \equiv \frac{(2s + 1)V}{2\pi^{2}} k^2
}
$$

This is the same as in the classical treatment of an ideal gas except for the spin factor, since we have ignored the spin in the classical treatment. As $\bar{n}_{i}$ depend on $k$ via $\varepsilon$, it is convenient to change the integration variable from $k$ to $\varepsilon$ using $k = \sqrt{2m\varepsilon}/\hbar$:

$$
g(k) \, \mathrm{d}k = \tilde{g}(\varepsilon) \, \mathrm{d}\varepsilon
$$

where the density of states per unit energy is:

$$
\boxed{
\tilde{g}(\varepsilon) \equiv \frac{(2s+1)V m^{3/2}}{\sqrt{2} \pi^{2} \hbar^{3}} \sqrt{\varepsilon} = \frac{2(2s+1)}{\sqrt{\pi}} \frac{V}{\lambda_{\text{th}}^3} \beta^{3/2} \sqrt{\varepsilon}
}
$$

where we note the definition of the thermal wavelength:

$$
\lambda_{\text{th}} = \sqrt{\frac{2\pi \hbar^{2}}{m k_{B}T}}
$$

Thus the following approximation results:

$$
\sum_{i} = \int_{0}^{\infty} \tilde{g}(\varepsilon) \, \mathrm{d}\varepsilon
$$

### Grand Potential

We could immediately compute the grand potential $\Phi$ using the integral approximation:

$$
\begin{split}
\Phi &= -k_{B}T \ln{\mathcal{Z}} \\
     &= \mp \frac{1}{\beta} \sum_{i} \ln{\left[ 1 \pm e^{-\beta (\varepsilon_{i} - \mu)} \right]} \\
     &= \mp \frac{1}{\beta} \int_{0}^{\infty} \tilde{g}(\varepsilon) \ln{\left[ 1 \pm e^{-\beta (\varepsilon - \mu)} \right]} \, \mathrm{d}\varepsilon \\
     &= \mp \frac{2(2s+1)}{\sqrt{\pi}} \frac{V}{\lambda_{\text{th}}^3} \sqrt{\beta} \int_{0}^{\infty} \sqrt{\varepsilon} \ln{\left[ 1 \pm e^{-\beta (\varepsilon - \mu)} \right]} \, \mathrm{d}\varepsilon
\end{split}
$$

Consider the convenient substitution $x \equiv \beta \varepsilon$:

$$
\Phi = \mp \frac{2(2s+1)}{\sqrt{\pi}} \frac{V}{\lambda_{\text{th}}^3} \frac{1}{\beta} \int_{0}^{\infty} \sqrt{x} \ln{\left[ 1 \pm e^{-x + \mu)} \right]} \, \mathrm{d}x
$$

The integral can be solved by parts:

$$
\begin{split}
\int_{0}^{\infty} \sqrt{x} \ln{\left[ 1 \pm e^{-x + \mu} \right]} \, \mathrm{d}x &= \left[ \frac{2}{3} x^{3/2} \ln{\left[ 1 \pm e^{-x + \mu} \right]} \right]_{0}^{\infty} - \int_{0}^{\infty} \frac{2}{3} x^{3/2} \frac{\mp e^{-x + \mu}}{1 \pm e^{-x + \mu}} \, \mathrm{d}x \\
&= \pm \frac{2}{3} \int_{0}^{\infty} x^{3/2} \frac{e^{-x + \mu}}{1 \pm e^{-x + \mu}} \, \mathrm{d}x \\
&= \pm \frac{2}{3} \int_{0}^{\infty} x^{3/2} \frac{1}{e^{x - \mu} \pm 1} \, \mathrm{d}x
\end{split}
$$

so that we finally obtain:

$$
\boxed{
\Phi = -\frac{2}{3} \frac{2(2s+1)}{\sqrt{\pi}} \frac{V}{\lambda_{\text{th}}^3} \frac{1}{\beta} \int_{0}^{\infty} \frac{x^{3/2}}{e^{x - \beta \mu} \pm 1} \, \mathrm{d}x
}
$$

### Other Thermodynamic Quantities

Although other thermodynamic quantities, such as the mean energy $U$ and the particle density $n$, can be computed using the grand potential, it is instructive to calculate them using the density of states $\tilde{g}(\varepsilon)$ and the mean occupation number $\bar{n}_{i}$. First consider the particle density $N$, which by definition is the expectation of the occupation number:

$$
\begin{split}
N &= \sum_{i} p_{i} \bar{n}_{i} \\
  &= \int_{0}^{\infty} \tilde{g}(\varepsilon) \frac{1}{e^{\beta (\varepsilon - \mu)} \pm 1} \, \mathrm{d}\varepsilon \\
  &= \frac{2(2s + 1)}{\sqrt{\pi}} \frac{V}{\lambda_{\text{th}}^3} \int_{0}^{\infty} \frac{\sqrt{x}}{e^{x - \beta \mu} \pm 1} \, \mathrm{d}x
\end{split}
$$

where the substitution $x = \beta \varepsilon$ has been made.

The (average) particle density is identified as $n = N/V$. Scaling $n$ to a dimensionless quantity, we have:

$$
\boxed{
\frac{n}{n_{Q}} \equiv \frac{n \lambda_{\text{th}}^3}{2s + 1} = \frac{2}{\sqrt{\pi}} \int_{0}^{\infty} \frac{\sqrt{x}}{e^{x - \beta \mu} \pm 1} \, \mathrm{d}x
}
$$

where scaling parameter called the 'quantum concentration' $n_{Q}$ is similar to the definition in a classical ideal gas:

$$
n_{Q} \equiv \frac{2s + 1}{\lambda_{\text{th}}^3}
$$

Note that the equation provides an implicit equation for the chemical potential $\mu$. It is also possible to write an explicit formula for the mean energy:

$$
\begin{split}
U &= \sum_{i} \varepsilon_{i} \bar{n}_{i} \\
  &= \int_{0}^{\infty} \tilde{g}(\varepsilon) \frac{\varepsilon}{e^{\beta (\varepsilon - \mu)} \pm 1} \, \mathrm{d}\varepsilon \\
  &= \frac{2(2s + 1)}{\sqrt{\pi}} \frac{V}{\lambda_{\text{th}}^3} k_{B} T \int_{0}^{\infty} \frac{\varepsilon^{3/2} \beta^{5/2}}{e^{\beta (\varepsilon - \mu)} \pm 1} \, \mathrm{d}\varepsilon
\end{split}
$$

We discover a simple connection among $U$, $n$, and the grand potential $\Phi$:

$$
\boxed{
U = Nk_{B}T \left( \frac{n}{n_{Q}} \frac{2}{\sqrt{\pi}} \int_{0}^{\infty} \frac{x^{3/2}}{e^{x - \beta \mu} \pm 1} \, \mathrm{d}x \right) = -\frac{3}{2} \Phi
}
$$

### Equation of State and Entropy

With the grand potential, the equation of state can be derived via $\Phi = -PV$. Usiing the fact that $\Phi = -2U/3$, we have the equation of state in terms of $(P, U, V)$:

$$
\boxed{
P = \frac{2}{3} \frac{U}{V}
}
$$

Note that this is exactly the same as the equation of state for a classical ideal gas, which implies that the relation is generally valid for any non-relativistic quantum gas.

The entropy $S$ can be computed via $\Phi = U - TS - \mu N$:

$$
\boxed{
S = \frac{U - \Phi - \mu N}{T} = \frac{5U/3 - \mu N}{T}
}
$$

This implies that in an adiabatic process, where $S$ and $N$ are constant, the temperature $T$ is proportional to the mean energy $U$:

## Classical Limit

In the classical limit (high temperature and low density), $n$ approaches zero. This can be achieved if $e^{-\beta \mu}$ approaches infinity because with $e^{-\beta \mu} \to \infty$:

$$
\frac{n}{n_{Q}} =\frac{2}{\sqrt{\pi}} \int_{0}^{\infty} \frac{\sqrt{x}}{e^{x - \beta \mu} \pm 1} \, \mathrm{d}x \approx \frac{2}{\sqrt{\pi}} e^{\beta \mu} \int_{0}^{\infty} \sqrt{x} e^{-x} \, \mathrm{d}x = e^{\beta \mu} \to 0
$$

where the second integral is computed by noting:

$$
\int_{0}^{\infty} \sqrt{x} e^{-x} \, \mathrm{d}x = \Gamma(\frac{1}{2}) = \frac{\sqrt{\pi}}{2}
$$

This also implies that at the classical limit:

$$
e^{\beta \mu} \approx \frac{n}{n_{Q}} = \frac{n \lambda_{\text{th}}^3}{2s + 1}
$$

This is equivalent to:

$$
\frac{n}{n_{Q}} = \frac{n \lambda_{\text{th}}^3}{2s + 1} \ll 1
$$

which agrees with the limit derived from the ideal gas.

With this approximation, the expressions for $\mu$ and $U$ can be reduced to their classical counterparts.

## Fermi Gas

Let us focus on the case of fermions, which in all previous equations is represented by the upper sign. In particular, the (logarithm of) partition function is:

$$
\ln{\mathcal{Z}} = \sum_{i} \ln{\left[ 1 + e^{-\beta (\varepsilon_{i} - \mu)} \right]}
$$

Consider the case where the temperature very low and the fermions occupy the lowest energy states. Due to the Pauli exclusion principle, each state can be occupied by at most one fermion. This means for every energy level, there is only $(2s + 1)$ fermions that can occupy it. The energy levels are filled from the lowest to the highest, and the highest energy level $\varepsilon_{F}$ that is occupied is called the **Fermi energy**. This is the energy cost to add one more fermion to the system, which we identify as the chemical potential $\mu$ at zero temperature:

$$
\epsilon_{F} = \mu(T = 0)
$$

In fact, given the occupation number $\bar{n}_{i}$ of the form:

$$
\bar{n}_{i} = \frac{1}{e^{\beta (\varepsilon_{i} - \mu)} + 1}
$$

the function approaches a step function as $T \to 0$ and $\beta \to \infty$, which implies that the occupation number is zero for $\varepsilon_{i} > \mu$ and unity for $\varepsilon_{i} < \mu$.

In the case of zero temperature, we may calculate the total number of fermions $N$ by integrating the density of states from $\varepsilon = 0$ to fermi energy:

$$
\begin{split}
N &= \int_{0}^{\varepsilon_{F}} \tilde{g}(\varepsilon) \, \mathrm{d}\varepsilon \\
  &= \frac{2(2s + 1)}{\sqrt{\pi}} \frac{V}{\lambda_{\text{th}}^3} \int_{0}^{\varepsilon_{F}} \sqrt{\varepsilon} \, \mathrm{d}\varepsilon \\
  &= \frac{2(2s + 1) V m^{3/2}}{3\sqrt{2} \pi^{2} \hbar^{3}} \varepsilon_{F}^{3/2} \\
\end{split}
$$

Let us define the Fermi wave vector $k_{F}$ using the dispersion relation:

$$
\boxed{
k_{F} = \frac{\sqrt{2m\varepsilon_{F}}}{\hbar}
}
$$

Then the number of fermions can be written as:

$$
N_{0} = \frac{(2s + 1)V}{6\pi^{2}} k_{F}^{3}
$$

Noting that $n = N_{0}/V$ is the particle density, we have:

$$
n = \frac{(2s + 1)}{6\pi^{2}} k_{F}^{3}
$$

and the Fermi energy can be written as:

$$
\boxed{
\varepsilon_{F} = \frac{\hbar^{2} k_{F}^{2}}{2m} = \frac{\hbar^{2}}{2m} \left( \frac{6\pi^{2} n}{2s + 1} \right)^{2/3}
}
$$

### Thermodynamic Quantities

We may also calculate the mean energy. Noting:

$$
\begin{split}
\frac{U}{N} &= \frac{\int_{0}^{\varepsilon_{F}} \varepsilon \tilde{g}(\varepsilon) \, \mathrm{d}\varepsilon}{\int_{0}^{\varepsilon_{F}} \tilde{g}(\varepsilon) \, \mathrm{d}\varepsilon} \\
            &= \frac{3}{5} \varepsilon_{F}
\end{split}
$$

we have:

$$
\boxed{
U = \frac{3}{5} N \varepsilon_{F}
}
$$

so that we also have the equation of state:

$$
\boxed{
P = \frac{2}{3} \frac{U}{V} = \frac{2}{5} n \varepsilon_{F}
}
$$

### Finite Temperature

The above discussion is incomplete because it only applies to the zero temperature limit. To extend the discussion to finite temperature, we consider the total number of fermions $N$ as an example. When the temperature is finite, the occupation number $\bar{n}_{i}$ is no longer a step function. We must hence incorporate the temperature dependence of the occupation number into the calculation of $N$:

$$
N = \int_{0}^{\infty} \tilde{g}(\varepsilon) \frac{1}{e^{\beta (\varepsilon - \mu)} + 1} \, \mathrm{d}\varepsilon
$$

To solve this integral, we may expand the integrand in a Taylor series about temperature $T$ and arrive at what is known as the Sommerfeld expansion:

$$
\int_{0}^{\infty} \tilde{g}(\varepsilon) \frac{1}{e^{\beta (\varepsilon - \mu)} + 1} \, \mathrm{d}\varepsilon = \int_{0}^{\infty} \left[ \tilde{g}(\varepsilon) + \frac{\pi^{2}}{6} g'(\epsilon = \mu) (k_{B}T)^{2} + \dots \right] \, \mathrm{d}\varepsilon
$$

Using this expansion, we may calculate the total number of fermions $N$ at finite temperature up to the second order in $T$:

$$
N = \frac{(2s + 1)V}{6\pi^{2}} k_{F}^{3} \left[ 1 + \frac{\pi^{2}}{6} \left( \frac{k_{B}T}{\varepsilon_{F}} \right)^{2} \right]
$$

## Bose Gas

Contrary to fermions, bosons do not have the Pauli exclusion principle, which means that any number of bosons can occupy the same single-particle state. This implies that at low temperatures, all particles tend to occupy the lowest energy state. In fact, at zero temperature, we expect $\bar{n}_{0} = N$ and $\bar{n}_{i} = 0$ anywhere else, i.e., all particles are in the ground state. This is known as the **Bose-Einstein condensation**.

The condensation means that calculation at the continuum limit is not valid. In the previous calculation $g(\varepsilon) \propto \sqrt{\varepsilon}$ predicts that the number of particles in the ground state is zero, which clearly is not the case. The critical temperature $T_{c}$ at which the condensation occurs can be found as follows. Note that the particle density $n$ satisfies:

$$
\frac{n \lambda_{\text{th}}^3}{2s + 1} = \frac{2}{\sqrt{\pi}} \int_{0}^{\infty} \frac{\sqrt{x}}{e^{x - \beta \mu} - 1} \, \mathrm{d}x
$$

Whereas the left hand side can be made as large as one pleases by increasing the density $n$ or decreasing the temperature $T$, the right hand side approaches a constant value $\zeta(3/2) \approx 2.612$. This implies that the critical temperature should satisfy:

$$
\frac{n}{2s + 1} \left( \frac{2\pi \hbar^{2}}{m k_{B}T_{c}} \right)^{3/2} = \zeta(3/2)
$$

which can be solved for $T_{c}$:

$$
\boxed{
T_{c} = \frac{2\pi \hbar^{2}}{m k_{B}} \left[ \frac{n}{2.612(2s + 1)} \right]^{2/3}
}
$$

The problem of Bose-Einstein condensation can be solved by splitting $N$ into $N = N_{0} + N_{\text{ex}}$, where $N_{0}$ is the number of particles in the ground state and $N_{\text{ex}}$ is the number of particles in excited states.

We can write the total number of particles as a function of the critical temperature:

$$
N = (2s + 1) \frac{V}{[\lambda_{\text{th}}(T_{c})]^3} \frac{2}{\sqrt{\pi}} \int_{0}^{\infty} \frac{\sqrt{x}}{e^{x - \beta \mu} - 1} \, \mathrm{d}x
$$

Below $T_{c}$, we can approximate $N_{\text{ex}}$ as:

$$
N_{\text{ex}} = (2s + 1) \frac{V}{[\lambda_{\text{th}}(T)]^3} \frac{2}{\sqrt{\pi}} \int_{0}^{\infty} \frac{\sqrt{x}}{e^{x - \beta \mu} - 1} \, \mathrm{d}x
$$

Any remaining particles are in the ground state, so that:

$$
N_{0} = N - N_{\text{ex}} = N - (2s + 1) \frac{V}{[\lambda_{\text{th}}(T)]^3} \zeta(3/2)
$$

This implies:

$$
\boxed{
\frac{N_{0}}{N} = 1 - \left( \frac{T}{T_{c}} \right)^{3/2}
}
$$
