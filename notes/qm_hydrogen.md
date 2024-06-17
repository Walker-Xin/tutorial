# Quantum Mechanics - Hydrogen Atom

## Three-Dimensional Schrodinger Equation

The Schrodinger equation states that $i \hbar \frac{\partial \Psi}{\partial t} = \hat H \Psi$ for a wave function $\Psi$, where $\hat H$ is the Hamilton operator defined as:

$$
\begin{split}
\hat H &= \frac{\hat p^2}{2m} + V \\
       &= -\frac{\hbar^2}{2m} \nabla^2 + V
\end{split}
$$

Thus, the Schrodinger equation becomes:

$$
\boxed{
i \hbar \frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m} \nabla^2 \Psi + V \Psi
}
$$

The normalisation condition requires:

$$
\int \lvert \Psi \rvert^2 \mathrm{d} V = 1
$$

Now assume that the potential energy $V(\vec{r})$ is not time-dependent and that the wave function can be reduced to a spatial part and a time part so that $\Psi(\vec{r},t) = \psi(\vec{r}) \varphi(t)$. The Schrodinger equation is reduced to:

$$
i \hbar \psi \frac{\mathrm{d} \varphi}{\mathrm{d} t} = -\frac{\hbar^2}{2m} (\psi \nabla^2 \varphi + \varphi \nabla^2 \psi) + V \psi \varphi
$$

Dividing the equation by $\psi \varphi$ and rearranging, have:

$$
i \hbar \frac{1}{\varphi} \frac{\mathrm{d} \varphi}{\mathrm{d} t} + \frac{\hbar^2}{2m} \frac{\nabla^2 \varphi}{\varphi} = V - \frac{\hbar^2}{2m} \frac{\nabla^2 \psi}{\psi}
$$

Now, the left side is a function of $t$ only while the right side is a function of $\vec{r}$ only. So they must each be equal to a constant $E$. Focusing on the time part, as $\varphi$ is a function of time only, its laplacian is zero, leading to:

$$
i \hbar \frac{\mathrm{d} \varphi}{\mathrm{d} t} = E \varphi
$$

Thus, the solution for $\varphi$ is:

$$
\varphi(t) = e^{-iEt/ \hbar}
$$

The part involving $\vec{r}$ reads:

$$
-\frac{\hbar^2}{2m} \nabla^2 \psi + V \psi = E \psi
$$

This is called the time-independent Schrodinger equation, which may be solved given the form of the potential energy $V(\vec{r})$.

## Time-Independent Schrodinger Equation

### Separation of Variables

In many physical systems, the potential energy turns out to be only dependent on the distance to a centre, such that $V(\vec{r}) = V(r)$. Given this assumption, it is natural to adopt the spherical coordinate system. In this coordinate system, the equation becomes:

$$
-\frac{\hbar^2}{2m} (\frac{1}{r^2} \frac{\partial}{\partial r}(r^2 \frac{\partial \psi}{\partial r}) + \frac{1}{r^2 \sin{\theta}} \frac{\partial}{\partial \theta}(\sin{\theta} \frac{\partial \psi}{\partial \theta}) + \frac{1}{r^2 \sin^{2}{\theta}} \frac{\partial^2 \psi}{\partial \phi^2}) + V \psi = E \psi
$$

Suppose further that the solution to $\psi$ can be separated into two parts, so that $\psi(r, \theta, \phi) = R(r)Y(\theta, \phi)$. This leads to:

$$
-\frac{\hbar^2}{2m} (\frac{Y}{r^2} \frac{\partial}{\partial r}(r^2 \frac{\mathrm{d} R}{\mathrm{d} r}) + \frac{R}{r^2 \sin{\theta}} \frac{\partial}{\partial \theta}(\sin{\theta} \frac{\partial Y}{\partial \theta}) + \frac{R}{r^2 \sin^{2}{\theta}} \frac{\partial^2 Y}{\partial \phi^2}) + V RY = E RY
$$

Dividing both sides by $RY$, have:

$$
-\frac{\hbar^2}{2m} (\frac{1}{R} \frac{1}{r^2} \frac{\partial}{\partial r}(r^2 \frac{\mathrm{d} R}{\mathrm{d} r}) + \frac{1}{Y} \frac{1}{r^2 \sin{\theta}} \frac{\partial}{\partial \theta}(\sin{\theta} \frac{\partial Y}{\partial \theta}) + \frac{1}{Y} \frac{1}{r^2 \sin^{2}{\theta}} \frac{\partial^2 Y}{\partial \phi^2}) + V = E
$$

Simplification leads to:

$$
\frac{1}{R} \frac{\mathrm{d}}{\mathrm{d} r}(r^2 \frac{\mathrm{d} R}{\mathrm{d} r}) - \frac{2m r^2}{\hbar^2}(V-E) = -\frac{1}{Y}(\frac{1}{\sin{\theta}} \frac{\partial}{\partial \theta}(\sin{\theta} \frac{\partial Y}{\partial \theta}) + \frac{1}{\sin^{2}{\theta}} \frac{\partial^2 Y}{\partial \phi^2})
$$

Again, the both sides must equal a constant denoted as $l(l+1)$.

### Angular Equation

Focusing on the angular part, the equation reads:

$$
\frac{1}{Y}(\frac{1}{\sin{\theta}} \frac{\partial}{\partial \theta}(\sin{\theta} \frac{\partial Y}{\partial \theta}) + \frac{1}{\sin^{2}{\theta}} \frac{\partial^2 Y}{\partial \phi^2}) = -l(l+1)
$$

Separate $Y(\theta, \phi)$ further into $\Theta(\theta)\Phi(\phi)$. The resulting differential equations are:

$$
\frac{\mathrm{d}^{2} \Phi}{\mathrm{d} \phi^2} = -m^2 \Phi
\tag{1}
$$

$$
\frac{1}{\sin{\theta}} \frac{\mathrm{d}}{\mathrm{d} \theta}(\sin{\theta} \frac{\mathrm{d} \Theta}{\mathrm{d} \theta}) = [\frac{m^2}{\sin^{2}{\theta}} - l(l+1)]\Theta
\tag{2}
$$

where $m$ is another constant.

The solutions are:

$$
\Phi(\phi) = e^{im\phi}
$$

$$
\Theta(\theta) = AP_{l}^{m}(\cos{\theta})
$$

where $m \in \mathbb{Z}$, $\lvert m \rvert \leq l$ and $A$ is a normalisation constant.

Note that $\Phi$ is orthogonal as $\int_{0}^{2\pi} \exp{i(m-n)\phi} = 0$ for $m \ne n$. $\Theta$ is also orthogonal as the associated Legendre functions have the orthogonality property. The normalisation condition for $\psi$ requires:

$$
\int \lvert R \rvert^2 \lvert Y \rvert^2 r^2 \sin{\theta} \mathrm{d} r \mathrm{d} \theta \mathrm{d} \phi = 0
$$

For the angular part, this leads to:

$$
\int_{0}^{\pi} \Theta^2 \sin{\theta} \mathrm{d} \theta \int_{0}^{2\pi} \Phi^{*} \Phi \mathrm{d} \phi = 2\pi A^2 \int_{-1}^{1} (P_{l}^{m}(\cos{\theta}))^2 \mathrm{d} (\cos{\theta}) = 1
$$

After normalisation, the functions $Y_{l}^{m}(\theta, \phi)$, which are called the **spherical harmonics**, are given by:

$$
\boxed{
Y_{l}^{m}(\theta, \phi) = \sqrt{\frac{(2l+1)(l-m)!}{4\pi (l+m)!}} e^{im\phi} P_{l}^{m}(\cos{\theta})
}
$$

### Radial Equation

Now we turn our attention to the radial equation:

$$
\frac{1}{R} \frac{\mathrm{d}}{\mathrm{d} r}(r^2 \frac{\mathrm{d} R}{\mathrm{d} r}) - \frac{2m r^2}{\hbar^2}(V-E) = l(l+1)
\tag{3}
$$

Consider an electron circulating a proton, which is essentially a hydrogen atom. The potential energy of the electron is given by Coulomb\'s law:

$$
V(r) = -\frac{e^2}{4 \pi \epsilon_{0}} \frac{1}{r}
$$

The radial equation reads:

$$
\frac{\mathrm{d}}{\mathrm{d} r}(r^2 \frac{\mathrm{d} R}{\mathrm{d} r}) - \frac{2m_e r^2}{\hbar^2}(V-E)R = l(l+1)R
$$

where $m_e$ is the mass of an electron

Consider the substitution $u(r) = rR(r)$. After simplification:

$$
-\frac{\hbar^2}{2m_e} \frac{\mathrm{d}^2 u}{\mathrm{d} r^2} + [- \frac{e^2}{4 \pi \epsilon_{0}} \frac{1}{r} + \frac{\hbar^2}{2m_e} \frac{l(l+1)}{r^2}]u = Eu
$$

Consider the bound states only, so that $E<0$. Define $\kappa \equiv \frac{\sqrt{-2m_{e}E}}{\hbar}$ so that the equation becomes:

$$
\frac{1}{\kappa^2} \frac{\mathrm{d}^2 u}{\mathrm{d} r^2} = [1 - \frac{m_{e}e^2}{2\pi \epsilon_{0} \hbar^2 \kappa} \frac{1}{\kappa r} + \frac{l(l+1)}{(k\kappa)^2}]u
$$

Define $\rho \equiv \kappa r$ and $\rho_0 \equiv \frac{m_{e}e^2}{2\pi \epsilon_{0} \hbar^2 \kappa}$ so that the equation becomes:

$$
\frac{\mathrm{d}^2 u}{\mathrm{d} \rho^2} = [1 - \frac{\rho_0}{\rho} + \frac{l(l+1)}{\rho^2}]u
\tag{4}
$$

In order to solve equation (4), we first examine its asymptotic behaviours. As $\rho \to \infty$, we have $\frac{\mathrm{d}^2 u}{\mathrm{d} \rho^2} \approx u$, leading to the solution:

$$
u(\rho) = A e^{-\rho} + B e^{\rho}
$$

The second term is not normalisable as $\rho \to \infty$ so $B = 0$. Therefore, $u(\rho) \approx A e^{-\rho}$ for large $\rho$. As $\rho \to 0$, the centrifugal term dominates and we have $\frac{\mathrm{d}^2 u}{\mathrm{d} \rho^2} \approx \frac{l(l+1)}{\rho^2} u$. This is called an Euler-Cauchy equation that has the solution:

$$
u(\rho) = C \rho^{l+1} + D \rho^{-l}
$$

Again, the second term is not normalisable as $\rho \to 0$ so $D = 0$. Therefore, $u(\rho) \approx C \rho^{l+1}$ for small $\rho$. Now suppose we write:

$$
u(\rho) = \rho^{l+1} e^{-\rho} v(\rho)
$$

for some function $v(\rho)$. Substitution into equation (4) yields:

$$
\rho \frac{\mathrm{d}^2 v}{\mathrm{d} \rho^2} + 2(l + 1 - \rho)\frac{\mathrm{d} v}{\mathrm{d} \rho} + (\rho_{0} - 2l - 2)v = 0
$$

Assume a series solution to the above equation of the form:

$$
v(\rho) = \sum_{j=0}^{\infty} c_{j} \rho_{j}
$$

Substitution into the equation leads to the standard recursive relationship for a series solution:

$$
c_{j+1} = \frac{2(j+l+1) - \rho_{0}}{(j+1)(j+2l+2)} c_{j}
$$

For physically possible solutions, we require the series to terminate at some point so that for some integer $N$, we have $c_{N-1} \ne 0$ but $c_{N} = 0$. This leads to $2(N+l) - \rho_{0}$. Define $n \equiv N+l$, then $\rho_{0} = 2n$ and the recursive relationship becomes:

$$
c_{j+1} = \frac{2(j+1+l-n)}{(j+1)(j+2+2l)} c_{j}
$$

But note that $\rho_{0}$ determines $E$ through:

$$
E = - \frac{m_{e} e^{4}}{8 \pi^{2} \epsilon_{0}^{2} \hbar^{2} \rho_{0}^{2}}
$$

Hence, the allowed the energies $E_n$ are given by:

$$
\boxed{
E_{n} = -\left[ \frac{m_e}{2\hbar^2} \left( \frac{e^2}{4\pi \epsilon_0} \right)^2 \right] \frac{1}{n^2} \equiv \frac{E_{R}}{n^2}
}
$$

where we define the Rydberg energy as the ground state energy:

$$
E_{R} \equiv \frac{m_{e} e^{4}}{2 (4\pi \epsilon_{0})^2 \hbar^2}
$$

The polynomials $v(\rho)$ are called associated Laguerre polynomials:

$$
v(\rho) = L_{n-l-1}^{2l+1}(2\rho)
$$

where:

$$
L_{q}^{p}(x) \equiv (-1)^p (\frac{\mathrm{d}}{\mathrm{d} x})^{p} L_{p+q}(x)
$$

is called an associated Laguerre polynomial and:

$$
L_{q}(x) \equiv \frac{e^x}{q!} (\frac{\mathrm{d}}{\mathrm{d} x})^{q} (e^{-x} x^{q})
$$

is called the qth Laguerre polynomial.

The radial wave function is thus:

$$
\boxed{
R_{nl} = \frac{1}{r} (\frac{r}{na})^{l+1} e^{-r/na} L_{n-l-1}^{2l+1}(2r/na)
}
$$

where $a \equiv 4\pi \epsilon_{0} \hbar^2/m_{e} e^2$ is called Bohr radius.

We can now give the full normalised hydrogen wave function:

$$
\boxed{
\psi_{nlm} = \sqrt{(\frac{2}{na})^{3} \frac{(n-l-1)!}{2n (n+l)!}} e^{-r/na} (\frac{2r}{na})^{l} \, L_{n-l-1}^{2l+1}(2r/na) \, Y_{m}^{l}(\theta, \phi)
}
$$

In particular, the ground state wave function is:

$$
\psi_{100} = \frac{1}{\sqrt{\pi a^3}} e^{-r/a}
$$

The first excited states are:

$$
\begin{split}
\psi_{200} &= \frac{1}{\sqrt{8 \pi a^3}} \left( 1 - \frac{r}{2a} \right) e^{-r/2a} \\
\psi_{210} &= \frac{1}{\sqrt{32 \pi a^3}} r e^{-r/2a} \cos{\theta} \\
\psi_{21\pm 1} &= \mp \frac{1}{\sqrt{64 \pi a^3}} r e^{-r/2a} \sin{\theta} e^{\pm i\phi}
\end{split}
$$
