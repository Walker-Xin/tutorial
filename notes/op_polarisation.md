# Optics - Polarisation

Consider a light wave that is travelling in the $z$ direction. The electric field may have two components, one in the $x$ direction and one in the $y$ direction:

$$
\begin{split}
E_{x} &= E_{0x} \cos{(kz - \omega t)} \\
E_{y} &= E_{0y} \cos{(kz - \omega t + \phi(t))}
\end{split}
$$

where we could choose the time origin such that the phase factor is zero for x component.

The net electric field is then:

$$
\mathbf{E} = \begin{bmatrix} E_{x} \\ E_{y} \end{bmatrix} = \begin{bmatrix} E_{0x} \cos{(kz - \omega t)} \\ E_{0y} \cos{(kz - \omega t + \phi(t))} \end{bmatrix}
$$

## Polarisation States

### Linear Polarisation

If $\phi(t) = 0$, then the electric field is essentially fixed at an angle $\alpha$ measured from the positive $x$ axis:

$$
\tan{\alpha} = \frac{E_{0y}}{E_{0x}}
$$

This is called the polarisation angle.

### Elliptical Polarisation

In general, for some constant $\phi$, we can write the components of the electric field as:

$$
\begin{split}
E_{x} &= E_{0x} \cos{(kz - \omega t)} \\
E_{y} &= E_{0y} \cos{(kz - \omega t}) \cos{\phi} - E_{0y} \sin{(kz - \omega t}) \sin{\phi}
\end{split}
$$

Consider the special case where $\phi = \pi/2$. Then the electric field components are:

$$
\begin{split}
E_{x} &= E_{0x} \cos{(kz - \omega t)} \\
E_{y} &= E_{0y} \sin{(kz - \omega t})
\end{split}
$$

They satisfy the ellipse equation:

$$
\frac{E_{x}^2}{E_{0x}^2} + \frac{E_{y}^2}{E_{0y}^2} = 1
$$

which means that the vector $(E_{x}, E_{y})$ traces out an ellipse in the $xy$ plane.

For general $\phi$, the ellipse is tilted at some angle. To see this, suppose that in some rotated coordinate system, the electric field is given by $(E_{x}', E_{y}')$ and an ellipse is traced out such that:

$$
\frac{E_{x}'^2}{E_{0x}^2} + \frac{E_{y}'^2}{E_{0y}^2} = 1
$$

A rotation by some angle $\beta$ is given by the transformation:

$$
\begin{split}
E_{x}' &= E_{x} \cos{\beta} + E_{y} \sin{\beta} \\
E_{y}' &= -E_{x} \sin{\beta} + E_{y} \cos{\beta}
\end{split}
$$

Substituting into the ellipse equation eventually gives an expression for $\beta$:

$$
\tan{2\beta} = \frac{2E_{0x}E_{0y}}{E_{0x}^2 - E_{0y}^2}\cos{\phi}
$$

## Jones Formalism

The discussion of polarisation states can be generalised to a more abstract formalism. The electric field is represented by a 2D complex vector:

$$
\mathbf{E} = \Re \begin{bmatrix} E_{x} \\ E_{y} \end{bmatrix} = \Re \begin{bmatrix} E_{0x} e^{i(kz - \omega t)} \\ E_{0y} e^{i(kz - \omega t)} e^{i\phi(t)} \end{bmatrix}
$$

Assuming equal amplitudes $E_{0x} = E_{0y} = E_{0}$, the polarisation state of the electric field is completely determined by the vector:

$$
\begin{bmatrix} 1 \\ e^{i\phi} \end{bmatrix}
$$

Let us define the following sets of basis vectors:

$$
\begin{split}
\ket{H} &= \begin{bmatrix} 1 \\ 0 \end{bmatrix} \\
\ket{V} &= \begin{bmatrix} 0 \\ 1 \end{bmatrix}
\end{split}
$$

which represent the basis expressed in the $x$ and $y$ directions respectively.

$$
\begin{split}
\ket{+} &= \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ 1 \end{bmatrix} \\
\ket{-} &= \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ -1 \end{bmatrix}
\end{split}
$$

which represent the basis of the diagonals.

$$
\begin{split}
\ket{R} &= \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ i \end{bmatrix} \\
\ket{L} &= \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ -i \end{bmatrix}
\end{split}
$$

which represent the basis of the right and left circular polarisations.

Each of these basis sets are complete and orthonormal, so any arbitrary polarisation state can be expressed as a linear combination of these basis vectors. Consider for example a general elliptically polarised state represented by the vector:

$$
\begin{bmatrix} E_{x} \\ E_{y} \end{bmatrix} \propto \begin{bmatrix} 1 \\  e^{i\phi} \end{bmatrix}
$$

where $\phi$ is some constant that is not necessarily $\pi/2$.

This can be written as:

$$
\begin{bmatrix} 1 \\  e^{i\phi} \end{bmatrix} = \frac{1 + ie^{i\phi}}{\sqrt{2}} \ket{R} + \frac{1 - ie^{i\phi}}{\sqrt{2}} \ket{L}
$$

### Operations on Polarisation States

We can abstract polarisers as operators acting on the polarisation state. For example, a polariser that only allows light polarised in the $x$ can be written as:

$$
\hat{P}_{H} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}
$$

Similarly, a vertical polariser can be written as:

$$
\hat{P}_{V} = \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}
$$

We can also write sets of polarisers in other bases:

$$
\begin{split}
\hat{P}_{+} &= \ket{+}\bra{+} = \frac{1}{2} \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} \\
\hat{P}_{-} &= \ket{-}\bra{-} = \frac{1}{2} \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} \\
\end{split}
$$

and:

$$
\begin{split}
\hat{P}_{R} &= \ket{R}\bra{R} = \frac{1}{2} \begin{bmatrix} 1 & i \\ -i & 1 \end{bmatrix} \\
\hat{P}_{L} &= \ket{L}\bra{L} = \frac{1}{2} \begin{bmatrix} 1 & -i \\ i & 1 \end{bmatrix} \\
\end{split}
$$

## Birefringence

Birefringence is the property of a material to have different refractive indices for different polarisation states, i.e., different alignment of the electric field vector. It is characterised by the birefringence index $\Delta n = n_{e} - n_{o}$, where $n_{e}$ and $n_{o}$ are the refractive indices for the extraordinary and ordinary rays respectively. When some light is incident on a birefringent material, the difference in refractive indices induces a phase difference. The thickness of the material can be manipulated to produce wave plates.

A wave plate is a birefringent material with a thickness $d$ and refractive indices $n_{o}$ and $n_{e}$ for the ordinary and extraordinary rays respectively. On a mathematical level, the wave plate adds a phase shift $\phi$ to the extraordinary ray. Suppose that the wave plate is placed at an angle $\theta$ to the horizontal. In the angled basis, the wave plate is represented by the operator:

$$
\hat{W}(\phi) = e^{i\phi} \ket{\theta}\bra{\theta} + \ket{\theta + \pi/2}\bra{\theta + \pi/2} \equiv \begin{pmatrix} e^{i\phi} & 0 \\ 0 & 1 \end{pmatrix}
$$

Consider the transformation from angled to canonical basis:

$$
\begin{split}
    \ket{\theta} &= \cos{\theta}\ket{H} + \sin{\theta}\ket{V} \\
    \ket{\theta + \pi/2} &= \cos{\theta}\ket{V} - \sin{\theta}\ket{H}
\end{split}
$$

We can write this in a matrix form:

$$
\mathbf{\alpha} = \mathbf{R}(\theta) \mathbf{\alpha}_{\theta} = \begin{pmatrix} \cos{\theta} & -\sin{\theta} \\ \sin{\theta} & \cos{\theta} \end{pmatrix} \mathbf{\alpha}_{\theta}
$$

where the vectors $\mathbf{\alpha}$ and $\mathbf{\alpha}_{\theta}$ are representations of the state in the canonical and angled bases respectively and $\mathbf{R}(\theta)$ transforms a coordinate in the angled basis to the canonical basis.

The wave plate operator can be written in the canonical basis as:

$$
\hat{W}_{0}(\phi) = \mathbf{R} \hat{W}(\phi) \mathbf{R}^{-1} = \begin{pmatrix} e^{i\phi} & 0 \\ 0 & 1 \end{pmatrix} =
\begin{pmatrix}
    \sin^{2}{\theta} + \cos^{2}{\theta}e^{i\phi} & \sin{\theta}\cos{\theta}(e^{i\phi} - 1) \\
    \sin{\theta}\cos{\theta}(e^{i\phi} - 1) & \cos^{2}{\theta} + \sin^{2}{\theta}e^{i\phi}
\end{pmatrix}
$$

Wave plates of with different thicknesses and positioned at different angles can be combined to transform polarisation states. Consider the case where $\theta = \pi/8$ and $\phi = \pi$, i.e. a half-wave plate at 22.5 degrees. The matrix representation of the wave plate is:

$$
\hat{W}_{0}(\pi) = \frac{1}{\sqrt{2}} \begin{pmatrix} -1 & -1 \\ -1 & 1 \end{pmatrix}
$$

Let this act on a diagonal polarisation state:

$$
\begin{split}
    \hat{W}_{0}(\pi) \ket{+} = \frac{1}{\sqrt{2}} \begin{pmatrix} -1 & -1 \\ -1 & 1 \end{pmatrix} \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = -\ket{H} \\
    \hat{W}_{0}(\pi) \ket{-} = \frac{1}{\sqrt{2}} \begin{pmatrix} -1 & -1 \\ -1 & 1 \end{pmatrix} \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -1 \end{pmatrix} = -\ket{V}
\end{split}
$$

so this device transforms a diagonal polarisation state into canonical ones.

Further, consider the case where $\theta = 0$ and $\phi = \pi/2$, i.e. a quarter-wave plate at zero degree. The matrix representation of the wave plate is:

$$
\hat{W}_{0}(\pi/2) = \begin{pmatrix} i & 0 \\ 0 & 1 \end{pmatrix}
$$

Let this act on a diagonal polarisation state:

$$
\begin{split}
    \hat{W}_{0}(\pi/2) \ket{+} = \begin{pmatrix} i & 0 \\ 0 & 1 \end{pmatrix} \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \ket{R} \\
    \hat{W}_{0}(\pi/2) \ket{-} = \begin{pmatrix} i & 0 \\ 0 & 1 \end{pmatrix} \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -1 \end{pmatrix} = \ket{L}
\end{split}
$$

so this device transforms a diagonal polarisation state into circular ones.
