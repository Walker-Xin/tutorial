# Wave Optics

## Interference

Consider the complex description of a wave:

$$
\Psi = A e^{i(\omega t - kx + \phi_{0})}
$$

In a young's double slit experiment, it can be shown that the path difference between the two slits is given by:

$$
\delta_{1} - \delta_{2} \approx \frac{nay}{D}
$$

where $n$ is the refractive index of the medium, $a$ is the slit separation, $y$ is the distance from the centre of the slits to the screen, and $D$ is the distance from the slits to the screen.

In complex notation, the total wave displacement at the point $M$ of interest is given by:

$$
\Psi(M) = \Psi_{1}(M) + \Psi_{2}(M) = A e^{i(\omega t + \phi_{0})} \left( e^{-ik\delta_{1}} + e^{-ik\delta_{2}} \right)
$$

The intensity of the wave at the point $M$ is given by:

$$
I = \frac{1}{2} \left\lvert \Psi \right\rvert^{2} = \frac{1}{2} \Psi \Psi^{*} = \frac{1}{2} A^{2} \left[ 2 + e^{-ik(\delta_{1} - \delta_{2})} + e^{-ik(\delta_{2} - \delta_{1})} \right] = A^{2} \left[ 1 + \cos{k(\delta_{1} - \delta_{2})} \right]
$$

We define the intensity at the centre of the slits to be $I_{0} = A^{2}/2$, so that $A^{2} = 2I_{0}$. Substituting the expression for $\delta_{1} - \delta_{2}$ and $k = 2\pi/\lambda$ gives:

$$
I(y) = 2I_{0} \left[ 1 + \cos{\left( 2\pi \frac{nay}{\lambda D} \right)} \right]
$$

which has a spacing of $\lambda D/na$ between the maxima and minima of the intensity.

## Diffraction

### Rectangular Aperture

Consider a rectangular aperture of width $\alpha$ and height $\beta$. Let the centre of the aperture be at the origin and let the screen be a plane at $z = D$. For a point on the screen at $(x, y, D)$, consider the path difference between the origin and the point $(X, Y, 0)$:

$$
\delta_{p} - \delta_{o} = n\sqrt{D^{2} + (x - X)^{2} + (y - Y)^{2}} - n\sqrt{D^{2} + x^{2} + y^{2}}
$$

The small slit approximation demands $X \ll x$ and $Y \ll y$, while the Fraunhofer approximation demands $x, y \ll D$. Under these conditions, a binomial expansion of the above equation yields:

$$
\delta_{p} - \delta_{o} \approx \frac{nD}{2} \left[ \left( \frac{X}{D} \right)^{2} + \left( \frac{Y}{D} \right)^{2}  - \frac{2Xx}{D^{2}} - \frac{2Yy}{D^{2}} \right]
$$

$X$ and $Y$ are much smaller than $x$ and $y$, which are in turn much smaller than $D$. We may thus ignore the first two terms on the right hand side and write:

$$
\delta_{p} - \delta_{o} \approx -\frac{n}{D} \left( Xx + Yy \right)
$$

The wave displacement at the point $(x, y, D)$ is given by:

$$
\Psi = \int \sigma e^{i(\omega t - k_{0}\delta_{p})} \, \mathrm{d}X \mathrm{d}Y = \sigma e^{i(\omega t - k_{0}\delta_{o})} \int e^{-ik_{0}(\delta_{p} - \delta_{o})} \, \mathrm{d}X \mathrm{d}Y
$$

where a 'change of variable' has been done so that we can make use of the previous approximation in path difference.

The integral becomes:

$$
\int_{-\beta/2}^{\beta/2} \int_{-\alpha/2}^{\alpha/2} e^{ik_{0}n(Xx + Yy)/D} \, \mathrm{d}X \mathrm{d}Y = \alpha \beta \operatorname{sinc} \left( \frac{\pi x \alpha}{\lambda D} \right) \operatorname{sinc} \left( \frac{\pi y \beta}{\lambda D} \right)
$$

where $\operatorname{sinc}(x) \equiv \sin(x)/x$.

The intensity at the point $(x, y, D)$ is given by:

$$
I = \frac{1}{2} \left| \Psi \right|^{2} = \frac{1}{2} \sigma^{2} \alpha^{2} \beta^{2} \operatorname{sinc}^{2} \left( \frac{\pi x \alpha}{\lambda D} \right) \operatorname{sinc}^{2} \left( \frac{\pi y \beta}{\lambda D} \right)
$$

We define $I_{0} = \sigma^{2}/2$ at the centre of the aperture, which gives:

$$
I = I_{0} \alpha^{2} \beta^{2} \operatorname{sinc}^{2} \left( \frac{\pi x \alpha}{\lambda D} \right) \operatorname{sinc}^{2} \left( \frac{\pi y \beta}{\lambda D} \right)
$$

Maximum of the intensity occurs when the two $\operatorname{sinc}$ functions have their maximum values of unity. The maximum value of the intensity is thus:

$$
I_{\mathrm{max}} = I_{0} \alpha^{2} \beta^{2}
$$

Differentiating the expression for $I$ with respect to $x$ and $y$ gives the spacing between the minima:

$$
\Delta x = \frac{\lambda D}{a} \quad \Delta y = \frac{\lambda D}{b}
$$

### Thin-Slit Diffraction

Now let the width $\alpha$ of the aperture be very small. The terms involving $\alpha$ becomes:

$$
\alpha^{2} \operatorname{sinc}^{2} \left( \frac{\pi x \alpha}{\lambda D} \right) \approx \alpha^{2}
$$

But we might as well absorb the $\alpha^{2}$ into the definition of $I_{0}$, so that for a thin slit of width $\beta$:

$$
I = I_{0} \beta^{2} \operatorname{sinc}^{2} \left( \frac{\pi x \beta}{\lambda D} \right)
$$

### Circular Aperture

It can be shown that the intensity distribution for a circular aperture is given by:

$$
I = I_{0} \left[ \frac{J_{1}(\pi \rho/\lambda D)}{\pi \rho/\lambda D} \right]^{2}
$$

where $J_{1}(x)$ is the first order Bessel function of the first kind and $\rho = \sqrt{x^{2} + y^{2}}$ is the distance from the centre of the aperture.

The first minimum occurs at $\rho =1.22 \lambda D/\alpha$.
