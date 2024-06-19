# Optics - Interference

From the Maxwell equations, we can derive the wave equation for the electric field $\mathbf{E}$ and the magnetic field $\mathbf{B}$:

$$
\begin{split}
\nabla^{2} \mathbf{E} - \frac{1}{v^{2}} \frac{\partial^{2} \mathbf{E}}{\partial t^{2}} &= 0 \\
\nabla^{2} \mathbf{B} - \frac{1}{v^{2}} \frac{\partial^{2} \mathbf{B}}{\partial t^{2}} &= 0
\end{split}
$$

where $v$ is the speed of light in the medium given by:

$$
v = \frac{1}{\sqrt{\mu \epsilon}}
$$

A possible solution to the wave equation is a spherical wave:

$$
\begin{split}
\mathbf{E} &= \mathbf{E}_{0} e^{i(\mathbf{k} \cdot \mathbf{r} - \omega t)} \\
\mathbf{B} &= \mathbf{B}_{0} e^{i(\mathbf{k} \cdot \mathbf{r} - \omega t)}
\end{split}
$$

where the amplitudes are related via:

$$
\mathbf{B}_{0} = \frac{\mathbf{k}}{\omega} \times \mathbf{E}_{0}
$$

The energy densities of the electric and magnetic fields are the same:

$$
\begin{split}
u_{E} &= \frac{1}{2} \epsilon \mathbf{E} \cdot \mathbf{E}^{*} \\
u_{B} &= \frac{1}{2\mu} \mathbf{B} \cdot \mathbf{B}^{*}
\end{split}
$$

## Fraunhofer Diffraction

Under Fraunhofer condition, the phase difference between a point with coordinates $(x, y)$ on the aperture plane and the point $(X, Y)$ on the screen is approximately linear in the aperture coordinates:

$$
\delta = k(xX + yY)
$$

The amplitude at a point $(X, Y)$ on the screen is given by:

$$
u(X, Y) = \iint_{\text{aperture}} u_{0}(x, y) e^{i\delta} \, \mathrm{d}x \mathrm{d}y
$$

Note that this is just the Fourier transform of the aperture function $u_{0}(x, y)$. For example, consider a square aperture of size $a \times b$ illuminated by a plane wave. The integral becomes:

$$
\begin{split}
u(X, Y) &= \iint_{\text{aperture}} u_{0}(x, y) e^{i\delta} \, \mathrm{d}x \mathrm{d}y \\
&\propto \int_{-a/2}^{a/2} \int_{-b/2}^{b/2} e^{i k (xX + yY)} \, \mathrm{d}x \mathrm{d}y \\
&= (ab) \operatorname{sinc}\left(\frac{aX}{2}\right) \operatorname{sinc}\left(\frac{bY}{2}\right)
\end{split}
$$

so that the intensity is given by:

$$
I(X, Y) = I_{0} \operatorname{sinc}^{2}\left(\frac{aX}{2}\right) \operatorname{sinc}^{2}\left(\frac{bY}{2}\right)
$$

This is a simplification of the Huygens-Fresnel diffraction integral, which asserts that the amplitude at some point $P$ due a point source is given by:

$$
u(P) = -\frac{i}{\lambda} \int_{S} \frac{u_{\rho}}{r} \eta(\mathbf{n}, \mathbf{r}) e^{i k r} \, \mathrm{d}S
$$

where the integral is done over some wavefront $S$.

The factor $\eta(\mathbf{n}, \mathbf{r})$ is the obliquity factor, which accounts for the fact that the wavefront is not perpendicular to the line joining the source and the point $P$. The $1/r$ dependence is due to a spherical wavefront. Under the Fraunhofer condition, the obliquity factor is approximately unity and the $1/r$ dependence can be ignored so that the integral becomes a Fourier transform.

### Fraunhofer Condition

The Fraunhofer condition is satisfied when the aperture is illuminated by a plane wave and the screen is far away from the aperture. Specifically, the condition is satisfied when the distance $L$ from the aperture to the screen is much larger than the dimensions of the aperture:

$$
F \equiv \frac{a^{2}}{L \lambda} \ll 1
$$

where we define the Fresnel number $F$ which has to be much smaller than unity for the Fraunhofer condition to be satisfied.

For near unity Fresnel numbers, the Huygens-Fresnel integral must be used and the regime is known as Fresnel diffraction.
