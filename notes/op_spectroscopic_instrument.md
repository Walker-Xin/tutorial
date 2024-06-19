# Optics - Spectroscopic Instruments

## Michelson Interferometer

A Michelson interferometer is an optical instrument that produces interference between two beams of light via division of amplitude. It consists of a beam splitter and two mirrors to produce two beams arriving at the output with an optical path difference given by:

$$
x = 2\Delta d = 2(d_{2} - d_{1})
$$

The amplitude at the output due to a monochromatic source is given by:

$$
I = I_{0} \cos^{2}{\left( \frac{kx}{2} \right)} = \frac{I_{0}}{2} \left( 1 + \cos{kx} \right)
$$

### Application as a Spectrometer

Consider an input beam of light with two wavelengths, $\lambda_{1}$ and $\lambda_{2}$. Since the light from different wavelengths do not interfere, the output intensity is given by:

$$
\begin{split}
I &= \frac{I_{0}}{2} \left( 1 + \cos{k_{1} x} \right) + \frac{I_{0}}{2} \left( 1 + \cos{k_{2} x} \right) \\
&= I_{0} \left( 1 + \cos{[(k_{1} + k_{2})x]} \cos{[(k_{1} - k_{2})x]} \right)
\end{split}
$$

The resulting intensity displays a beat pattern with a spatial beat frequency given by:

$$
f_{b} = \frac{k_{1} - k_{2}}{2\pi}
$$

Given the light with $\lambda_{1}$, it is possible to detect the existence of $\lambda_{2}$ if the range in $x$ can at least cover half a period of the beat pattern:
$$
(k_{1} - k_{2})x_{\text{max}} \ge \pi
$$

which means that the separation between the two wavelengths must satisfy:

$$
\Delta k = \frac{\pi}{x_{\text{max}}} = \frac{\pi}{2 \Delta d_{\text{max}}}
$$

The resolving power of the Michelson interferometer is given by:

$$
RP = \frac{\lambda}{\Delta \lambda} = \frac{k}{\Delta k} = \frac{x_{\text{max}}/2}{\lambda} = \frac{\Delta d_{\text{max}}}{\lambda}
$$

## Fabry-Perot Interferometer

A Fabry-Perot interferometer, also known as an etalon, is an optical instrument that produces interference via multiple reflections between two parallel mirrors. If the emerging rays are brought to focus, the total amplitude of the emerging light is given by:

$$
u = u_{0}t_{1}t_{2} \sum_{n=0}^{\infty} (r_{1}r_{2} e^{i\delta})^{n} = u_{0} \frac{t_{1}t_{2}}{1 - r_{1}r_{2} e^{i\delta}}
$$

where $\delta$ is the phase difference caused by the thickness of the etalon:

$$
\delta = 2kd\cos{\theta}
$$

The intensity is given by:

$$
\begin{split}
    I &= I_{0} \frac{(t_{1} t_{2})^{2}}{1 - 2r_{1}r_{2}\cos{\delta} + r_{1}^{2}r_{2}^{2}} \\
    &= I_{0} \left[ \frac{(t_{1} t_{2})^{2}}{1 - R} \right]^{2} \frac{1}{1 + \Phi \sin^{2}{(\delta/2)}}
\end{split}
$$

where we define the finesse coefficient as:

$$
\Phi \equiv \frac{4r_{1}r_{2}}{(1 - r_{1}r_{2})^{2}}
$$

Let us define the finesse of the Fabry-Perot interferometer as:

$$
\boxed{
\mathcal{F} \equiv \frac{\pi \sqrt{R}}{1 - R} = \frac{\pi}{2} \sqrt{\Phi}
}
$$

so that the intensity can be written as:

$$
\boxed{
I = I_{\text{max}} \frac{1}{1 + (2\mathcal{F}/\pi)^{2} \sin^{2}{(\delta/2)}}
}
$$

This is known as the Airy function. The finesse is a parameter that controls the sharpness of the interference pattern, that is, the width of the bright circular fringes in the interference pattern. A higher finesse means a sharper interference pattern.

### Resolving Power

Let us consider the location of half the maximum intensity, which occurs when:

$$
\sin^{2}{(\delta/2)} = \frac{\pi^{2}}{4\mathcal{F}^{2}}
$$

This is a small angle, so that we have:

$$
\delta_{1/2} = \frac{\pi}{\mathcal{F}}
$$

The full width at half maximum (FWHM) is just twice this value:

$$
\text{FWHM} = \frac{2\pi}{\mathcal{F}}
$$

This also implies that the sharpness of the interference pattern is completely determined by the reflectivities of the mirrors. From the FWHM, we change to $k$ space and define the instrumental width:

$$
\Delta k_{\text{inst}} = \frac{\text{FWHM}}{2d} = \frac{\pi}{\mathcal{F}d}
$$

Two monochromatic lines differing by $\Delta k$ are just resolved if they are separated by the instrumental width:

$$
\Delta k \ge \Delta k_{\text{inst}} = \frac{\pi}{\mathcal{F}d}
$$

The resolving power of the Fabry-Perot interferometer is thus given by:

$$
RP = \frac{k}{\Delta k_{\text{inst}}} = \frac{k\mathcal{F}d}{\pi}
$$

For values of $k$ that gives the qth order of interference, we have $k_{n} = q\pi/d$, so that the resolving power is given by:

$$
\boxed{
RP = q\mathcal{F}
}
$$
