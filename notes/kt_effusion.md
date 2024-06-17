# Kinetic Theory - Effusion and Collision

## Effusion

Consider a container of an ideal gas with a small hole on the wall. Taking z direction as perpendicular to the wall, the particle flux, i.e., the number of particles per unit time per unit area with velocities in the range $[\mathbf{v}, \mathbf{v} + \mathrm{d}^{3}\mathbf{v}]$ is given by:

$$
\mathrm{d}\Phi(\mathbf{v}) = n v_{z} g(\mathbf{v}) \mathrm{d}^{3}\mathbf{v} = n v^{3} g(v) \, \mathrm{d}v \cos{\theta} \sin{\theta} \, \mathrm{d}\theta \, \mathrm{d}\phi
$$

where we have used the isotropy of the velocity distribution and the fact that $v_{z} = v \cos{\theta}$.

This distribution is neither isotropic (due to the $\cos{\theta}$ factor) nor Maxwellian (due to the extra $v$ factor). Additionally, the speed part is in a higher order of $v$. This implise that collision happens more frequently for the particles with higher velocity, which naturally tends to impact a surface more.

We may integrate this to obtain the flux of particles with speeds between $v$ and $v + \mathrm{d}v$:

$$
\mathrm{d}\tilde{\Phi}(v) = \int_{0}^{\pi/2} \int_{0}^{2\pi} \mathrm{d}\Phi(\mathbf{v}) = \pi n v^{3} g(v) \, \mathrm{d}v = \frac{1}{4} n v f(v) \, \mathrm{d}v
$$

where the integration over $\theta$ is from $0$ to $\pi/2$ because we only consider the particles moving towards the hole (i.e., $v_{z} > 0$).

The total flux is thus given by:

$$
\boxed{
\tilde{\Phi} = \int_{0}^{\infty} \mathrm{d}\tilde{\Phi}(v) = \frac{1}{4} n \langle v \rangle
}
$$

This is gives the number of particles per unit time per unit area escaping through the hole. We can also relate this to the parameters ($P$, $T$, $n$) of the gas:

$$
\tilde{\Phi} = \frac{1}{4} n \left( \frac{8k_{B}T}{\pi m} \right)^{1/2} = \frac{P}{\sqrt{2\pi mk_{B}T}}
$$

## Collisions

Particles in an ideal gas can be treated as hard spheres of diameter $d$. They collide with each other if their centres are within a distance $d$ of each other. The collision cross-section of a particle is the area of the circle of radius $d$ centred at the particle:

$$
\sigma = \pi d^{2}
$$

A moving particle then sweeps out a volume $\sigma v t$ over time $t$ and any particle within this volume will collide with the moving particle. The average number of particles in this volume is just $\sigma n v t$. Setting this quantity to unity for one collision, we have:

$$
\tau_{c} = \frac{1}{\sigma n v}
$$

where $\tau_{c}$ is the mean time between collisions.

For $v$, we can use the average speed $\langle v \rangle$ , the thermal speed $v_{\text{th}} \equiv \sqrt{2k_{B}T/m}$, or the root-mean-square speed $\langle v^{2} \rangle^{1/2} = \sqrt{3k_{B}T/m}$. They are the same for approximations up to orders of unity and we will use the thermal speed $v_{\text{th}}$:

$$
\boxed{
\tau_{c} = \frac{1}{\sigma n v_{\text{th}}} = \frac{1}{\sigma n} \sqrt{\frac{m}{2k_{B}T}}
}
$$

and the typical distance a particle travels between collisions is:

$$
\boxed{
\lambda = v_{\text{th}} \tau_{c} = \frac{1}{\sigma n}
}
$$

which we call the mean free path.

Note that it would be more precise to use the relative speed $v_{\text{rel}} = 2\sqrt{2} v_{\text{th}}/\sqrt{\pi}$ instead of $v_{\text{th}}$ in the above expressions. However, the difference is still of order unity and can be neglected.
