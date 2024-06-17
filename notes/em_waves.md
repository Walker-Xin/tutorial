# Electromagnetism - Electromagnetic Waves

## Electromagnetic Waves in a Medium

Consider a medium where no free charges or currents are present. If the medium is linear, such that $\mathbf{D} = \epsilon_{0} \epsilon_{r} \mathbf{E}$ and $\mathbf{B} = \mu_{0} \mu_{r} \mathbf{H}$, the Maxwell equations become:

$$
\begin{split}
\nabla \cdot \mathbf{E} &= 0 \\
\nabla \cdot \mathbf{B} &= 0 \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{B} &= \mu \epsilon \frac{\partial \mathbf{E}}{\partial t}
\end{split}
$$

where we define $\mu \equiv \mu_{0} \mu_{r}$ and $\epsilon \equiv \epsilon_{0} \epsilon_{r}$.

Note that this only differs from the vacuum case by replacement of $\epsilon_{0} \rightarrow \epsilon$ and $\mu_{0} \rightarrow \mu$. This means that any mathematical results from the vacuum case carry over. Taking the curl of the last two equations, we have:

$$
\begin{split}
\nabla^{2} \mathbf{E} = \mu \epsilon \frac{\partial^{2} \mathbf{E}}{\partial t^{2}} \\
\nabla^{2} \mathbf{B} = \mu \epsilon \frac{\partial^{2} \mathbf{B}}{\partial t^{2}}
\end{split}
$$

which are the wave equations for $\mathbf{E}$ and $\mathbf{B}$.

These are three dimensional wave equations that admit the plane wave solution:

$$
\begin{split}
\mathbf{E} &= \mathbf{E}_{0} \cos{\left( \mathbf{k} \cdot \mathbf{r} - \omega t + \phi \right)} \\
\mathbf{B} &= \mathbf{B}_{0} \cos{\left( \mathbf{k} \cdot \mathbf{r} - \omega t + \phi \right)}
\end{split}
$$

where $\mathbf{k}$ with $k = 2 \pi / \lambda$ is the wave vector pointing in the direction of propagation.

From the Maxwell equations, it can be shown that $\mathbf{E}_{0}$, $\mathbf{B}_{0}$, and $\mathbf{k}$ are mutually perpendicular, and that $\mathbf{E}_{0}$ and $\mathbf{B}_{0}$ are in phase and related via:

$$
\mathbf{B}_{0} = \frac{1}{v} \hat{k} \times \mathbf{E}_{0}
$$

The speed of propagation of electromagnetic waves in a medium is:

$$
v = \frac{1}{\sqrt{\mu \epsilon}} = \frac{c}{\sqrt{\mu_{r} \epsilon_{r}}}
$$

We can define the refractive index of the medium as:

$$
n \equiv \sqrt{\mu_{r} \epsilon_{r}} \approx \sqrt{\epsilon_{r}}
$$

where the approximation is valid for most materials where $\mu_{r}$ is close to 1.

The energy density is:

$$
u = \frac{1}{2} \left( \epsilon E^{2} + \frac{1}{\mu} B^{2} \right) = \frac{1}{2} \left( \mathbf{E} \cdot \mathbf{D} + \mathbf{B} \cdot \mathbf{H} \right)
$$

Since we have $B^{2} = \mu^{2} \epsilon^{2} E^{2}$, the contribution from the magnetic field is the same as the contribution from the electric field. The energy density thus becomes:

$$
u = \epsilon E^{2} = \frac{1}{\mu} B^{2}
$$

The Poynting vector is:

$$
\mathbf{S} = \frac{1}{\mu} \mathbf{E} \times \mathbf{B} = \mathbf{E} \times \mathbf{H}
$$

with the momentum flux density:

$$
\mathbf{g} = \frac{\mathbf{S}}{c}
$$

We define the intensity of the wave as the time-averaged Poynting vector:

$$
I = \frac{1}{2} \left\lvert \mathbf{S} \right\rvert = \frac{1}{2} \left\lvert \mathbf{E} \times \mathbf{H} \right\rvert
$$

where the half factor arises from averaging the time dependence of the fields.

Similar to the vacuum case, the amplitude of the electric and magnetic fields are related by:

$$
E_{0} = v B_{0}
$$

When waves cross the boundary between two media, the boundary conditions are:

$$
\begin{split}
\epsilon_{1} E_{1}^{\perp} &= \epsilon_{2} E_{2}^{\perp} \\
B_{1}^{\perp} &= B_{2}^{\perp} \\
\mathbf{E}_{1}^{\parallel} &= \mathbf{E}_{2}^{\parallel} \\
\mu_{1} \mathbf{B}_{1}^{\parallel} &= \mu_{2} \mathbf{B}_{2}^{\parallel}
\end{split}
$$

For complex fields, the Poynting vector is defined as:

$$
\tilde{\mathbf{S}} = \frac{1}{2} \left( \mathbf{E} \times \mathbf{H}^{*} \right)
$$

whose real part is the time-averaged Poynting vector.

## Oblique Incidence

Consider a incident monochromatic plane wave:

$$
\begin{split}
\mathbf{E}_{I} &= \mathbf{E}_{I0} e^{i \left( \mathbf{k}_{I} \cdot \mathbf{r} - \omega t \right)} \\
\mathbf{B}_{I} &= \mathbf{B}_{I0} e^{i \left( \mathbf{k}_{I} \cdot \mathbf{r} - \omega t \right)}
\end{split}
$$

giving rise to a reflected wave:

$$
\begin{split}
\mathbf{E}_{R} &= \mathbf{E}_{R0} e^{i \left( \mathbf{k}_{R} \cdot \mathbf{r} - \omega t \right)} \\
\mathbf{B}_{R} &= \mathbf{B}_{R0} e^{i \left( \mathbf{k}_{R} \cdot \mathbf{r} - \omega t \right)}
\end{split}
$$

and a transmitted wave:

$$
\begin{split}
\mathbf{E}_{T} &= \mathbf{E}_{T0} e^{i \left( \mathbf{k}_{T} \cdot \mathbf{r} - \omega t \right)} \\
\mathbf{B}_{T} &= \mathbf{B}_{T0} e^{i \left( \mathbf{k}_{T} \cdot \mathbf{r} - \omega t \right)}
\end{split}
$$

For each set of waves, we have $\mathbf{B} = \hat{k} \times \mathbf{E}/v$.

### Snell's Law

Ignoring the wave amplitudes first, consider the boundary condition of the form:

$$
A e^{i \left( \mathbf{k}_{I} \cdot \mathbf{r} - \omega t \right)} + B e^{i \left( \mathbf{k}_{R} \cdot \mathbf{r} - \omega t \right)} = C e^{i \left( \mathbf{k}_{T} \cdot \mathbf{r} - \omega t \right)}
$$

The exponential terms must all agree when $z = 0$, i.e.:

$$
\mathbf{k}_{I} \cdot \mathbf{r} = \mathbf{k}_{R} \cdot \mathbf{r} = \mathbf{k}_{T} \cdot \mathbf{r}
$$

Writing each term explicitly and noting that $\mathbf{r} = (x, y, 0)^{T}$, we have:

$$
x k_{Ix} + y k_{Iy} = x k_{Rx} + y k_{Ry} = x k_{Tx} + y k_{Ty}
$$

which implies that terms associated with $x$ and $y$ must be all equal:

$$
\begin{split}
k_{Ix} &= k_{Rx} = k_{Tx} \\
k_{Iy} &= k_{Ry} = k_{Ty}
\end{split}
$$

We may as well demand that $\mathbf{k}_{I}$ be in the xz-plane so that $k_{Iy} = k_{Ry} = k_{Ty} = 0$. This implies that the three wave vectors are in the same plane, which we call the plane of incidence.

The first equation implies that:

$$
k_{I} \sin{\theta_{I}} = k_{R} \sin{\theta_{R}} = k_{T} \sin{\theta_{T}}
$$

Since the incident and reflected waves are in the same medium, we have $k_{I} = k_{R}$, and thus:

$$
\sin{\theta_{I}} = \sin{\theta_{R}}
$$

which is the law of reflection.

The second equality implies that:

$$
n_{I} \sin{\theta_{I}} = n_{T} \sin{\theta_{T}}
$$

which is the law of refraction or Snell's law.

### P-Polarisation (Parallel)

We have the boundary conditions on the field magnitudes:

$$
\begin{split}
\epsilon_{1} \left( E_{I0} + E_{R0} \right)_{z} &= \epsilon_{2} \left( E_{T0} \right)_{z} \\
\left( B_{I0} + B_{R0} \right)_{z} &= \left( B_{T0} \right)_{z} \\
\left( E_{I0} + E_{R0} \right)_{x, y} &= \left( E_{T0} \right)_{x, y} \\
\frac{1}{\mu_{1}} \left( B_{I0} + B_{R0} \right)_{x, y} &= \frac{1}{\mu_{2}} \left( B_{T0} \right)_{x, y}
\end{split}
$$

where the last two equations are the components of the fields that are parallel to the xy-plane.

Suppose the incident wave is polarised parallel to the plane of incidence. Noting that the polarisation vector is determined by the electric field, we have:

$$
\begin{split}
\epsilon_{1} \left( -E_{I0} \sin{\theta_{I}} + E_{R0} \sin{\theta_{R}} \right) &= \epsilon_{2} \left( -E_{T0} \sin{\theta_{T}} \right) \\
E_{I0} \cos{\theta_{I}} + E_{R0} \cos{\theta_{R}} &= E_{T0} \cos{\theta_{T}} \\
\end{split}
$$

where $\theta_{I} = \theta_{R}$.

The first equation, coupled with Snell's law, gives:

$$
E_{I0} - E_{R0} = \beta E_{T0}
$$

where we define:

$$
\beta \equiv \frac{\epsilon_{2} n_{1}}{\epsilon_{1} n_{2}} = \sqrt{\frac{\epsilon_{2}/\mu_{2}}{\epsilon_{1}/\mu_{1}}}
$$

The second equation gives:

$$
E_{I0} + E_{R0} = \alpha E_{T0}
$$

where $\alpha \equiv \cos{\theta_{T}} / \cos{\theta_{I}}$.

Solving $E_{T0}$ and $E_{R0}$ in terms of $E_{I0}$, we have:

$$
\boxed{
\begin{split}
E_{R0} &= \left( \frac{\alpha - \beta}{\alpha + \beta} \right) E_{I0} \\
E_{T0} &= \left( \frac{2 \alpha}{\alpha + \beta} \right) E_{I0}
\end{split}
}
$$

or, noting that $Z = \sqrt{\mu/\epsilon}$:

$$
\boxed{
\begin{split}
E_{R0} &= \left( \frac{Z_{2} \cos{\theta_{I}} - Z_{1} \cos{\theta_{T}}}{Z_{2} \cos{\theta_{I}} + Z_{1} \cos{\theta_{T}}} \right) E_{I0} \\
E_{T0} &= \left( \frac{2 Z_{1} \cos{\theta_{I}}}{Z_{2} \cos{\theta_{I}} + Z_{1} \cos{\theta_{T}}} \right) E_{I0}
\end{split}
}
$$

These are known as the Fresnel equations for P-polarisation. It is interesting to note that when $\alpha = \beta$, or:

$$
\sin^{2}{\theta_{I}} = \frac{1 - \beta^{2}}{(n_{1}/n_{2})^{2} - \beta^{2}}
$$

there is no reflected wave.

We call this angle the Brewster angle $\theta_{B}$.

The intensities of the incident, reflected, and transmitted waves striking the boundary are given by $\mathbf{S} \cdot \hat{z}$:

$$
\begin{split}
I_{I} &= \frac{1}{2} \epsilon_{1} v_{1} E_{I0}^{2} \cos{\theta_{I}} \\
I_{R} &= \frac{1}{2} \epsilon_{1} v_{1} E_{R0}^{2} \cos{\theta_{R}} \\
I_{T} &= \frac{1}{2} \epsilon_{2} v_{2} E_{T0}^{2} \cos{\theta_{T}}
\end{split}
$$

and the reflection and transmission coefficients are:

$$
\begin{split}
R_{P} &= \frac{I_{R}}{I_{I}} = \left( \frac{\alpha - \beta}{\alpha + \beta} \right)^{2} \\
T_{P} &= \frac{I_{T}}{I_{I}} = \frac{4 \alpha \beta}{\left( \alpha + \beta \right)^{2}}
\end{split}
$$

### S-Polarisation (Perpendicular)

Now suppose the incident wave is polarised perpendicular to the plane of incidence. Similarly we have:

$$
\begin{split}
E_{I0} + E_{R0} &= E_{T0} \\
\frac{1}{\mu_{1}} \left( -B_{I0} \cos{\theta_{I}} + B_{R0} \cos{\theta_{R}} \right) &= \frac{1}{\mu_{2}} \left( -B_{T0} \cos{\theta_{T}} \right)
\end{split}
$$

Noting that $B = E/v$, the second equation gives:

$$
E_{I0} - E_{R0} = \gamma E_{T0}
$$

where we define:

$$
\gamma \equiv \frac{\sqrt{\epsilon_{2}/\mu_{2}} \cos{\theta_{T}}}{\sqrt{\epsilon_{1}/\mu_{1}} \cos{\theta_{I}}} = \alpha \beta
$$

Solving $E_{I0}$ and $E_{R0}$ in terms of $E_{T0}$, we have:

$$
\boxed{
\begin{split}
E_{R0} &= \left( \frac{1 - \gamma}{1 + \gamma} \right) E_{I0} \\
E_{T0} &= \left( \frac{2}{1 + \gamma} \right) E_{I0}
\end{split}
}
$$

or:

$$
\boxed{
\begin{split}
E_{R0} &= \left( \frac{Z_{2} \cos{\theta_{I}} - Z_{1} \cos{\theta_{T}}}{Z_{2} \cos{\theta_{I}} + Z_{1} \cos{\theta_{T}}} \right) E_{I0} \\
E_{T0} &= \left( \frac{2 Z_{2} \cos{\theta_{I}}}{Z_{2} \cos{\theta_{I}} + Z_{1} \cos{\theta_{T}}} \right) E_{I0}
\end{split}
}
$$

These are known as the Fresnel equations for S-polarisation.

### Normal Incidence

Note that both P- and S-polarisation reduce to the same Fresnel equations when $\theta_{I} = \theta_{R} = \theta_{T} = 0$. In this case, we have $\alpha = 1$ and $\gamma = \beta$, and the Fresnel equations become:

$$
\begin{split}
E_{R0} &= \left( \frac{1 - \beta}{1 + \beta} \right) E_{I0} \\
E_{T0} &= \left( \frac{2}{1 + \beta} \right) E_{I0}
\end{split}
$$

or:

$$
\begin{split}
E_{R0} &= \left( \frac{Z_{2} - Z_{1}}{Z_{2} + Z_{1}} \right) E_{I0} \\
E_{T0} &= \left( \frac{2 Z_{2}}{Z_{2} + Z_{1}} \right) E_{I0}
\end{split}
$$

## Waves in Conductors

In a conductor, we have Maxwell's equations:

$$
\begin{split}
\nabla \cdot \mathbf{E} &= \frac{\rho_{f}}{\epsilon} \\
\nabla \cdot \mathbf{B} &= 0 \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{B} &= \mu \mathbf{J} + \mu \epsilon \frac{\partial \mathbf{E}}{\partial t}
\end{split}
$$

For a good conductor, any free charges are quickly distributed. Hence, $\rho_{f} = 0$. We also have $\mathbf{J} = \sigma \mathbf{E}$ for an Ohmic conductor. Taking the curl of the second last equation gives:

$$
\nabla^{2} \mathbf{E} = \mu \epsilon \frac{\partial^{2} \mathbf{E}}{\partial t^{2}} + \mu \sigma \frac{\partial \mathbf{E}}{\partial t}
$$

Similarly for $\mathbf{B}$:

$$
\nabla^{2} \mathbf{B} = \mu \epsilon \frac{\partial^{2} \mathbf{B}}{\partial t^{2}} + \mu \sigma \frac{\partial \mathbf{B}}{\partial t}
$$

These are modified wave equations that admit the plane wave solution:

$$
\begin{split}
\mathbf{E} &= \mathbf{E}_{0} e^{i(\kappa z - \omega t)} \\
\mathbf{B} &= \mathbf{B}_{0} e^{i(\kappa z - \omega t)}
\end{split}
$$

where the complex wave number $\kappa$ is given by:

$$
\kappa^{2} = \mu \epsilon \omega^{2} + i \mu_{0} \sigma \omega = \mu \epsilon \omega^{2} \left( 1 + i \frac{\sigma}{\epsilon \omega} \right)
$$

We can also write the wave number as $\kappa = k_{+} + ik_{-}$ where:

$$
k_{\pm} = \omega \sqrt{\frac{\mu \epsilon}{2}} \left( \sqrt{1 + \left( \frac{\sigma}{\epsilon \omega} \right)^{2}} \pm 1 \right)^{1/2} = \frac{k_{0}}{\sqrt{2}} \left( \sqrt{1 + \left( \frac{\sigma}{\epsilon \omega} \right)^{2}} \pm 1 \right)^{1/2}
$$

where $k_{0} = \omega \sqrt{\mu \epsilon}$ is the ordinary wave number.

The imaginary part of $\kappa$ leads to an exponential decay of the wave amplitudes:

$$
\begin{split}
\mathbf{E} &= \mathbf{E}_{0} e^{-k_{-} z} e^{i(k_{+} z - \omega t)} \\
\mathbf{B} &= \mathbf{B}_{0} e^{-k_{-} z} e^{i(k_{+} z - \omega t)}
\end{split}
$$

We define the skin depth $\delta$ as the distance over which the wave amplitude decays by a factor of $1/e$:

$$
\delta \equiv \frac{1}{k_{-}} = \frac{\sqrt{2}}{k_{0}} \left[ \sqrt{1 + \left( \frac{\sigma}{\epsilon \omega} \right)^{2}} - 1 \right]^{-1/2}
$$

For a very good conductor, we have $\sigma \gg \epsilon \omega$, and the approximation:

$$
\delta \approx \frac{\sqrt{2}}{k_{0}} \left( \frac{\sigma}{\epsilon \omega} \right)^{-1/2} = \sqrt{\frac{2}{\mu \omega \sigma}}
$$

On the other hand, for a very poor conductor, we have:

$$
\delta \approx \frac{2}{k_{0}} \frac{\epsilon \omega}{\sigma} = \frac{2}{\sigma} \sqrt{\frac{\epsilon}{\mu}}
$$

An important difference between waves in a conductor and waves in a vacuum is that the magnetic field is no longer in phase with the electric field. Consider the curl of the electric field:

$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
$$

which leads to $\mathbf{B}_{0} = (\kappa/\omega) \hat{k} \times \mathbf{E}_{0}$.

The fact that $\kappa$ is complex leads to a phase difference between $\mathbf{E}$ and $\mathbf{B}$. Taking $\kappa = Ke^{i\phi}$, we have:

$$
K = \omega \sqrt{\mu \epsilon} \left[ 1 + \left( \frac{\sigma}{\epsilon \omega} \right)^{2} \right]^{1/4}
$$

and:

$$
\phi = \tan^{-1}{\left( \frac{k_{-}}{k_{+}} \right)}
$$

The real amplitudes of the electric and magnetic fields are related by:

$$
\left\lvert \frac{\mathbf{B}_{0}}{\mathbf{E}_{0}} \right\rvert = \frac{K}{\omega}
$$

### Reflection and Transmission in a Conductor

In a conductor, the boundary conditions change due to possible surface charges and currents. The boundary conditions are:

$$
\begin{split}
\epsilon_{1} E_{1}^{\perp} - \epsilon_{2} E_{2}^{\perp} &= \sigma_{f} \\
B_{1}^{\perp} - B_{2}^{\perp} &= 0 \\
\mathbf{E}_{1}^{\parallel} - \mathbf{E}_{2}^{\parallel} &= 0 \\
\frac{1}{\mu_{1}} \mathbf{B}_{1}^{\parallel} - \frac{1}{\mu_{2}} \mathbf{B}_{2}^{\parallel} &= \mathbf{K}_{f} \times \hat{n}
\end{split}
$$

For ohmic conductors, there can be no free surface currents, i.e. $\mathbf{K}_{f} = 0$, as this would imply an infinite electric field at the surface. For simplicity, consider normal incidence. The boundary conditions yield exactly the same Fresnel equations as in the case of a dielectric:

$$
\begin{split}
E_{R0} &= \left( \frac{1 - \tilde{\beta}}{1 + \tilde{\beta}} \right) E_{T0} \\
E_{I0} &= \left( \frac{2}{1 + \tilde{\beta}} \right) E_{T0}
\end{split}
$$

where we define the complex version of $\beta$:

$$
\tilde{\beta} \equiv \frac{\mu_{1} v_{1}}{\mu_{2} \omega} \kappa_{2}
$$

For a perfect conductor, we have $\tilde{\beta} = 0$, and there is no reflected wave.
