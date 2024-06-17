# Electromagnetism - Electrodynamics

## Motional Electromotive Force

We define the electromotive force (emf) in a circuit as the path integral:

$$
\varepsilon = \oint \mathbf{f} \cdot \mathrm{d}\mathbf{l}
$$

where $\mathbf{f}$ is force per unit charge exerted on the charges in the circuit.

The source of $\mathbf{f}$ can be of any nature. For a conductor in a magnetic field, $\mathbf{f}$ is the Lorentz force defined as $\mathbf{f} = \mathbf{v} \times \mathbf{B}$. This implies that there would be a motional emf in a conductor moving in a magnetic field. Define the magnetic flux through a surface $\mathcal{S}$ as the surface integral:

$$
\Phi = \int_{\mathcal{S}} \mathbf{B} \cdot \mathrm{d}\mathbf{A}
$$

It can be shown that the motional emf created in a conductor loop moving in a magnetic field is given by:

$$
\varepsilon = -\frac{d\Phi}{dt}
$$

## Faraday's Law

Faraday's experimental work implied that a changing magnetic field induces an electric field. Faraday's law states that the induced electric field is such that an electromotive force is created:

$$
\varepsilon = \oint \mathbf{E}_{\text{ind}} \cdot \mathrm{d}\mathbf{l} = -\frac{\mathrm{d}\Phi}{\mathrm{d}t}
$$

Note carefully that this although this has the same expression as the motional emf, the underlying physical principles are different. The motional emf is due to the Lorentz force, while the induced emf is due to the induced electric field by a changing magnetic field.

Further insight in the induced electric field can applying the Stoke's theorem on the path integral:

$$
\oint \mathbf{E}_{\text{ind}} \cdot \mathrm{d}\mathbf{l} = \int_{S} (\nabla \times \mathbf{E}_{\text{ind}}) \cdot \mathrm{d}\mathbf{A} = -\int_{\mathcal{S}} \mathbf{B} \cdot \mathrm{d}\mathbf{A}
$$

so that the induced electric field is satisfies:

$$
\nabla \times \mathbf{E}_{\text{ind}} = -\frac{\partial \mathbf{B}}{\partial t}
$$

Note that this induced electric field is different from the one given by Coulomb's law, which has been shown to be curl-less. In fact, the induced electric field satisfies the exact same mathematical structure in magnetostatics. It follows that the Biot-Savart law can be used to calculate the induced electric field:

$$
\mathbf{E}_{\text{ind}} = -\frac{1}{4\pi} \frac{\partial}{\partial t} \int \frac{\mathbf{B} \times \mathbf{r}'}{r'^{2}} \, \mathrm{d}V
$$

and Faraday's law is just the corresponding Ampere's law.

## Maxwell's Equations

Consider the Ampere's law $\nabla \times B = \mu_{0} \mathbf{J}$. The divergence of this is supposed to be zero, but the divergence of $\mathbf{J}$ is in fact:

$$
\nabla \cdot \mathbf{J} = -\frac{\partial \rho}{\partial t} = -\epsilon_{0} \frac{\partial}{\partial t} \nabla \cdot \mathbf{E}
$$

from the continuity equation.

This implies that the original formulation of Ampere's law is flawed, as we must use $\mathbf{J} + \epsilon_{0} \partial \mathbf{E}/\partial t$ in place of $\mathbf{J}$ to make the divergence zero. The modified Ampere's law is:

$$
\nabla \times \mathbf{B} = \mu_{0} (\mathbf{J} + \epsilon_{0} \frac{\partial \mathbf{E}}{\partial t})
$$

which implies that a changing electric field induces a magnetic field.

The term $\epsilon_{0} \partial \mathbf{E}/\partial t$ is called the displacement current (density).

Now we can write down the full set of Maxwell's equations:

$$
\begin{split}
\nabla \cdot \mathbf{E} &= \frac{\rho}{\epsilon_{0}} \\
\nabla \cdot \mathbf{B} &= 0 \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{B} &= \mu_{0} (\mathbf{J} + \epsilon_{0} \frac{\partial \mathbf{E}}{\partial t})
\end{split}
$$

In integral form, we have:

$$
\begin{split}
\int_{S} \mathbf{E} \cdot \mathrm{d}\mathbf{A} &= \frac{1}{\epsilon_{0}} Q_{\text{encl}} \\
\int_{S} \mathbf{B} \cdot \mathrm{d}\mathbf{A} &= 0 \\
\oint \mathbf{E} \cdot \mathrm{d}\mathbf{l} &= -\int_{S} \frac{\partial \mathbf{B}}{\partial t} \cdot \mathrm{d}\mathbf{A} \\
\oint \mathbf{B} \cdot \mathrm{d}\mathbf{l} &= \mu_{0} I_{\text{encl}} + \int_{S} \mu_{0} \frac{\partial \mathbf{E}}{\partial t} \cdot \mathrm{d}\mathbf{A}
\end{split}
$$

## Electromagnetic Waves

In vacuum, $\mathbf{J} = 0$ and $\rho = 0$, so that the equations reduce to:

$$
\begin{split}
\nabla \cdot \mathbf{E} &= 0 \\
\nabla \cdot \mathbf{B} &= 0 \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{B} &= \mu_{0} \epsilon_{0} \frac{\partial \mathbf{E}}{\partial t}
\end{split}
$$

Consider the curl of the curl of $\mathbf{E}$:

$$
\nabla \times (\nabla \times \mathbf{E}) = \nabla (\nabla \cdot \mathbf{E}) - \nabla^{2} \mathbf{E} = -\nabla^{2} \mathbf{E}
$$

as $\nabla \cdot \mathbf{E} = 0$.

This implies that:

$$
\nabla^{2} \mathbf{E} = \frac{\partial}{\partial t} (\nabla \times \mathbf{B}) = \mu_{0} \epsilon_{0} \frac{\partial^{2} \mathbf{E}}{\partial t^{2}}
$$

which is the wave equation.

A similar derivation can be done for $\mathbf{B}$, and this implies that in vacuum, electric and magnetic fields can propagate as waves with speed:

$$
c \equiv \frac{1}{\sqrt{\mu_{0} \epsilon_{0}}}
$$

A solution to the wave equation is the plane wave of the form:

$$
\begin{split}
\tilde{\mathbf{E}} &= \tilde{\mathbf{E}}_{0} e^{i(\mathbf{k} \cdot \mathbf{r} - \omega t)} \\
\tilde{\mathbf{B}} &= \tilde{\mathbf{B}}_{0} e^{i(\mathbf{k} \cdot \mathbf{r} - \omega t)}
\end{split}
$$

where $\mathbf{k}$ is the wave vector that points in the direction of propagation and we have used a complex notation to simplify the equations.

It can be shown with Maxwell's equations that $\tilde{\mathbf{E}}_{0} \cdot \mathbf{k} = \tilde{\mathbf{B}}_{0} \cdot \mathbf{k} = 0$ and $\tilde{\mathbf{E}}_{0} \cdot \tilde{\mathbf{B}}_{0} = 0$. This means that the electric and magnetic fields are perpendicular to each other and to the direction of propagation. The magnitude of the electric and magnetic fields are related by:

$$
\left\lvert \tilde{\mathbf{E}}_{0} \right\rvert = c\left\lvert \tilde{\mathbf{B}}_{0} \right\rvert
$$

so that numerically, the electric field is much stronger than the magnetic field.

Consider the energy density in an electromagnetic wave:

$$
u = \frac{1}{2} \epsilon_{0} \left\lvert \tilde{\mathbf{E}} \right\rvert^{2} + \frac{1}{2\mu_{0}} \left\lvert \tilde{\mathbf{B}} \right\rvert^{2} = \epsilon_{0} \left\lvert \tilde{\mathbf{E}} \right\rvert^{2} = \frac{1}{\mu_{0}} \left\lvert \tilde{\mathbf{B}} \right\rvert^{2}
$$

The energy density is the same for the electric and magnetic fields. By convention, we define the energy density to be the electric field energy density, so that for a monochromatic wave, the energy density is:

$$
u = \epsilon_{0} \left\lvert \tilde{\mathbf{E}} \right\rvert^{2} = \epsilon_{0} E_{0}^{2} \cos^{2}(\mathbf{k} \cdot \mathbf{r} - \omega t)
$$

We can define a vector $\mathbf{S} \equiv \mathbf{E} \times \mathbf{B}/\mu_{0}$ called the Poynting vector. This vector points in the direction of propagation and has magnitude $c\epsilon_{0} \left\lvert \tilde{\mathbf{E}}_{0} \right\rvert^{2}$. This is the energy flux of the wave:

$$
\mathbf{S} = cu \hat{\mathbf{k}}
$$

and the average intensity of the wave is just the time average of the Poynting vector.

### Poynting Theorem

Consider a volume $V$ bounded by a surface $S$ where no charges or currents are present in the volume. The total energy in the volume is given by the integral

$$
U = \int_{V} \left( \frac{1}{2} \epsilon_{0} E^{2} + \frac{1}{2\mu_{0}} B^{2} \right) \, \mathrm{d}V
$$

Consider the time derivative of this integral:

$$
\begin{split}
\frac{\mathrm{d}U}{\mathrm{d}t} &= \int_{V} \frac{\partial}{\partial t} \left( \frac{1}{2} \epsilon_{0} E^{2} + \frac{1}{2\mu_{0}} B^{2} \right) \, \mathrm{d}V \\
&= \int_{V} \left( \epsilon_{0} \mathbf{E} \cdot \frac{\partial \mathbf{E}}{\partial t} + \frac{1}{\mu_{0}} \mathbf{B} \cdot \frac{\partial \mathbf{B}}{\partial t} \right) \, \mathrm{d}V \\
&= \int_{V} \frac{1}{\mu_{0}} \left[ \mathbf{E} \cdot \left( \nabla \times \mathbf{B} \right) - \mathbf{B} \cdot \left( \nabla \times \mathbf{E} \right) \right] \, \mathrm{d}V \\
&= \int_{V} \frac{1}{\mu_{0}} \nabla \cdot \left( \mathbf{B} \times \mathbf{E} \right) \, \mathrm{d}V \\
&= -\frac{1}{\mu_{0}} \int_{S} \left( \mathbf{E} \times \mathbf{B} \right) \cdot \mathrm{d}\mathbf{S} \\
\end{split}
$$

where the divergence theorem has been used in the last step.

This is the Poynting theorem, which states that the rate of decrease of energy in a volume is equal to the flux of energy through the surface of the volume given by the Poynting vector.
