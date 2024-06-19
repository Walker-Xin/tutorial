# Classical Mechanics - Rigid Body

A rigid body can be defined as a system of particles such that the distances between particles remain constant. To describe such a system, two sets of coordinates are needed: an inertial system $O'$ and a moving system $O$. The rigid body is fixed in $O'$. The position of $O$ is system $O'$ is given by three components of the position vector $\mathbf{R}$ and its orientation is given by three independent angles $\alpha$, $\beta$ and $\gamma$. Thus, a rigid body in general has six degrees of freedom.

Let $\mathbf{r}$ be the position vector of an arbitrary particle in the rigid body in system $O$. Let $\mathbf{r}'$ be the position vector of the same particle in system $O'$. An infinitesimal displacement $\mathrm{d}\mathbf{r}'$ can be written as a sum of two parts: one due to the translation of $O$ and the other due to the rotation of $O$:

$$
\mathrm{d}\mathbf{r}' = \mathrm{d}\mathbf{R} + \mathrm{d}\mathbf{\phi} \times \mathbf{r}
$$

where $\mathrm{d}\mathbf{\phi}$ represents the infinitesimal rotation of angle $\mathrm{d}\phi$ about the line parallel to the vector.

We may take the time derivative of the above equation to obtain the velocity of the particle in system $O'$:

$$
\mathbf{v}' = \mathbf{V} + \mathbf{\omega} \times \mathbf{r}
$$

where we define the following quantities:

$$
\begin{split}
\mathbf{V} &\equiv \frac{\mathrm{d}\mathbf{R}}{\mathrm{d}t} \\
\mathbf{\omega} &\equiv \frac{\mathrm{d}\mathbf{\phi}}{\mathrm{d}t}
\end{split}
$$

From now on, we might as well drop the prime and take the system $O$ as the lab frame.

## Centre of Mass Frame

We define the centre of mass of the rigid body as the point $\mathbf{R}_{\mathrm{cm}}$ such that:

$$
\mathbf{R}_{\mathrm{cm}} = \frac{1}{M} \sum_{i} m_{i} \mathbf{r}_{i}
$$

## Kinetic Energy

The kinetic energy of the rigid body is given by the sum of the kinetic energies of all particles:

$$
\begin{split}
T &= \sum_{i} \frac{1}{2} m_{i} v_{i}^{2} \\
&= \sum_{i} \frac{1}{2} m_{i} (\mathbf{V} + \mathbf{\omega} \times \mathbf{r}_{i})^{2} \\
&= \sum_{i} \frac{1}{2} m_{i} V^{2} + \sum_{i} \frac{1}{2} m_{i} (\mathbf{\omega} \times \mathbf{r}_{i})^{2} + \sum_{i} m_{i} \mathbf{V} \cdot (\mathbf{\omega} \times \mathbf{r}_{i}) \\
\end{split}
$$

In the first term, $\mathbf{V}$ is constant so that the sum is simply $MV^{2}/2$ where $M$ is the total mass of the rigid body. In the third term, we have:

$$
\begin{split}
\sum_{i} m_{i} \mathbf{V} \cdot (\mathbf{\omega} \times \mathbf{r}_{i}) = \sum_{i} m_{i} \mathbf{r}_{i} \cdot (\mathbf{V} \times \mathbf{\omega}) = (\mathbf{V} \times \mathbf{\omega}) \cdot \sum_{i} m_{i} \mathbf{r}_{i} = 0
\end{split}
$$

where the last equality holds if we choose the centre of mass frame.

The second term can be expanded using tensor notation:

$$
\begin{split}
\sum_{i} \frac{1}{2} m_{i} (\mathbf{\omega} \times \mathbf{r}_{i})^{2} &= \sum_{i} \frac{1}{2} m_{i} (\mathbf{\omega} \times \mathbf{r}_{i}) \cdot (\mathbf{\omega} \times \mathbf{r}_{i}) \\
\end{split}
$$

$$
\begin{split}
(\mathbf{\omega} \times \mathbf{r}_{i}) \cdot (\mathbf{\omega} \times \mathbf{r}_{i}) &= \epsilon_{\alpha \beta \gamma} \omega_{\beta} (r_{i})_{\gamma} \epsilon_{\alpha \delta \epsilon} \omega_{\delta} (r_{i})_{\epsilon} \\
&= (\delta_{\beta \delta} \delta_{\gamma \epsilon} - \delta_{\beta \epsilon} \delta_{\gamma \delta}) \omega_{\beta} \omega_{\delta} (r_{i})_{\gamma} (r_{i})_{\epsilon} \\
&= \omega_{\beta} \omega_{\delta} ( \delta_{\beta \delta} r_{i}^{2} - (r_{i})_{\beta} (r_{i})_{\delta} )
\end{split}
$$

We may use the change of index $(\beta, \delta) \rightarrow (\alpha, \beta)$ to obtain:

$$
(\mathbf{\omega} \times \mathbf{r}_{i}) \cdot (\mathbf{\omega} \times \mathbf{r}_{i}) = \omega_{\alpha} \omega_{\beta} ( \delta_{\alpha \beta} r_{i}^{2} - (r_{i})_{\alpha} (r_{i})_{\beta} )
$$

Thus, we have the rotational kinetic energy:

$$
\begin{split}
T_{\mathrm{rot}} &= \frac{1}{2} \omega_{\alpha} \omega_{\beta} \sum_{i} m_{i} ( \delta_{\alpha \beta} r_{i}^{2} - (r_{i})_{\alpha} (r_{i})_{\beta} ) \\
&\equiv \frac{1}{2} \omega_{\alpha} \omega_{\beta} I_{\alpha \beta}
\end{split}
$$

where we have defined the inertia tensor $I_{\alpha \beta}$:

$$
I_{\alpha \beta} \equiv \sum_{i} m_{i} ( \delta_{\alpha \beta} r_{i}^{2} - (r_{i})_{\alpha} (r_{i})_{\beta} )
$$

The total kinetic energy is then given by:

$$
T = \frac{1}{2} \mu V^{2} + \frac{1}{2} \omega_{\alpha} \omega_{\beta} I_{\alpha \beta}
$$

where $\mu$ is the total mass of the rigid body.

We can therefore conclude that the Lagrangian of the rigid body is given by:

$$
\mathcal{L} = \frac{1}{2} \mu V^{2} + \frac{1}{2} \omega_{\alpha} \omega_{\beta} I_{\alpha \beta} - V
$$

where $V$ is some potential energy.

## Angular Momentum

Consider the sum of the angular momenta of all particles in the rigid body:

$$
\begin{split}
\mathbf{M} &\equiv \sum_{i} m_{i} \mathbf{r}_{i} \times \mathbf{v}_{i} \\
&= \sum_{i} m_{i} \mathbf{r}_{i} \times (\mathbf{V} + \mathbf{\omega} \times \mathbf{r}_{i}) \\
&= \sum_{i} m_{i} \mathbf{r}_{i} \times \mathbf{V} + \sum_{i} m_{i} \mathbf{r}_{i} \times (\mathbf{\omega} \times \mathbf{r}_{i}) \\
\end{split}
$$

In general, the angular momentum depends on the choice of reference frame. The natural choice here is the centre of mass frame. In this frame, the first term vanishes and the second term becomes:

$$
\begin{split}
\mathbf{M} &= \sum_{i} m_{i} \mathbf{r}_{i} \times (\mathbf{\omega} \times \mathbf{r}_{i}) \\
&= \sum_{i} m_{i} [\mathbf{r}_{i}^{2} \mathbf{\omega} - (\mathbf{r}_{i} \cdot \mathbf{\omega}) \mathbf{r}_{i}]
\end{split}
$$

Consider the $\alpha$ component of the angular momentum:

$$
\begin{split}
M_{\alpha} &= \sum_{i} m_{i} [\mathbf{r}_{i}^{2} \omega_{\alpha} - (\mathbf{r}_{i} \cdot \mathbf{\omega}) (r_{i})_{\alpha}] \\
&= \sum_{i} m_{i} [\delta_{\alpha \beta} r_{i}^{2} - (r_{i})_{\alpha} (r_{i})_{\beta}] \omega_{\beta} \\
&= I_{\alpha \beta} \omega_{\beta}
\end{split}
$$

This implies that $\mathbf{M} = I \mathbf{\omega}$ where $I$ is the inertia tensor. In general, $\mathbf{M}$ is not parallel to $\mathbf{\omega}$. However, if $\mathbf{\omega}$ is an eigenvector of $I$ such that $I \mathbf{\omega} = \lambda \mathbf{\omega}$, then $\mathbf{M}$ is parallel to $\mathbf{\omega}$.

The inertia tensor is real and symmetric with three eigenvectors $\mathbf{\omega}_{1}$, $\mathbf{\omega}_{2}$ and $\mathbf{\omega}_{3}$ corresponding to three eigenvalues $I_{1}$, $I_{2}$ and $I_{3}$. The eigenvectors are called the principal axes of the rigid body while the eigenvalues are called the principal moments of inertia. If we align the coordinate axes with the principal axes, then the inertia tensor becomes diagonal:

$$
I =
\begin{bmatrix}
I_{1} & 0 & 0 \\
0 & I_{2} & 0 \\
0 & 0 & I_{3}
\end{bmatrix}
$$

in which case the kinetic energy and angular momentum take much simpler forms:

$$
\begin{split}
T &= \frac{1}{2} \mu V^{2} + \frac{1}{2} \sum_{i} I_{i} \omega_{i}^{2} \\
\mathbf{M} &= \sum_{i} I_{i} \omega_{i} \mathbf{e}_{i}
\end{split}
$$

## Euler Angles

The orientation of a rigid body can be described by three angles that describe the relation of the axes (often taken to be the principal axes) $x_{i}$ and the axes $X_{i}$ of the lab frame. An often used set of angles are the Euler angles $(\theta, \phi, \psi)$. Suppose that initially the we have the fixed axes $X_{i}$ and another set $x_{i}^{(0)}$ that is identical to $X_{i}$. We rotate $x_{i}^{(0)}$ about the $x_{3}^{(0)}$ by an angle $\phi$. This is a rotation about the z-axis that can be described by the matrix:

$$
R_{1}(\phi) =
\begin{bmatrix}
\cos{\phi} & -\sin{\phi} & 0 \\
\sin{\phi} & \cos{\phi} & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

Next, we rotate the $x_{i}^{(1)}$ axes about $x_{1}^{(1)}$ by an angle $\theta$. This is a rotation about the x-axis that can be described by the matrix:

$$
R_{2}(\theta) =
\begin{bmatrix}
1 & 0 & 0 \\
0 & \cos{\theta} & -\sin{\theta} \\
0 & \sin{\theta} & \cos{\theta}
\end{bmatrix}
$$

Finally, we rotate $x_{i}^{(2)}$ about $x_{3}^{(2)}$ by an angle $\psi$. This is again a rotation about the z-axis described by the matrix:

$$
R_{3}(\psi) =
\begin{bmatrix}
\cos{\psi} & -\sin{\psi} & 0 \\
\sin{\psi} & \cos{\psi} & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

The eventual set of axes $x_{i}$ is obtained by applying the three rotations in the order $R_{3}(\psi) R_{2}(\theta) R_{1}(\phi)$ on the $X_{i}$ axes:

$$
\begin{split}
    \begin{bmatrix}
    x_{1} \\
    x_{2} \\
    x_{3}
    \end{bmatrix}
    &=
    R_{3}(\psi) R_{2}(\theta) R_{1}(\phi)
    \begin{bmatrix}
    X_{1} \\
    X_{2} \\
    X_{3}
    \end{bmatrix} \\
    &=
    \begin{bmatrix}
    \cos{\psi} \cos{\theta} \cos{\phi} - \sin{\psi} \sin{\phi} & -\cos{\psi} \cos{\theta} \sin{\phi} - \sin{\psi} \cos{\phi} & \cos{\psi} \sin{\theta} \\
    \sin{\psi} \cos{\theta} \cos{\phi} + \cos{\psi} \sin{\phi} & -\sin{\psi} \cos{\theta} \sin{\phi} + \cos{\psi} \cos{\phi} & \sin{\psi} \sin{\theta} \\
    -\sin{\theta} \cos{\phi} & \sin{\theta} \sin{\phi} & \cos{\theta}
    \end{bmatrix}
    \begin{bmatrix}
    X_{1} \\
    X_{2} \\
    X_{3}
    \end{bmatrix}
\end{split}
$$

which is a very unwieldy expression.

The angle $\theta$ varies from $0$ to $\pi$ while the angles $\phi$ and $\psi$ vary from $0$ to $2\pi$. Consider the angular velocity $\mathbf{\Omega}$ of the rigid body expressed in the moving frame $x_{i}$:

$$
\mathbf{\Omega} = \Omega_{1} \mathbf{e}_{1} + \Omega_{2} \mathbf{e}_{2} + \Omega_{3} \mathbf{e}_{3}
$$

By inspection, we can collect the contributions of the Euler angles to the angular velocity:

$$
\begin{split}
\Omega_{1} &= \dot{\phi} \sin{\theta} \sin{\psi} + \dot{\theta} \cos{\psi} \\
\Omega_{2} &= \dot{\phi} \sin{\theta} \cos{\psi} - \dot{\theta} \sin{\psi} \\
\Omega_{3} &= \dot{\phi} \cos{\theta} + \dot{\psi}
\end{split}
$$

## Equations of Motion

Since a rigid body has six degrees of freedom, we need six equations of motion to describe its motion. They can be derived by considering the time derivatives of the momentum and angular momentum of the rigid body. The total momentum of the rigid body is simply the sum of the momenta of all particles:

$$
\mathbf{P} = \sum_{i} m_{i} \mathbf{v}_{i} = \mu \mathbf{V}
$$

The time derivative of the total momentum is due to the external forces acting on the rigid body:

$$
\frac{\mathrm{d}\mathbf{P}}{\mathrm{d}t} = \mathbf{F}
$$

A similar argument can be made for the angular momentum. The time derivative of the angular momentum is due to the external torques acting on the rigid body:

$$
\frac{\mathrm{d}\mathbf{M}}{\mathrm{d}t} = \mathbf{\tau}
$$

## Euler's Equations

Consider the following statement. Let $\mathrm{d}\mathbf{A}/\mathrm{d}t$ be the time derivative of a vector $\mathbf{A}$ with respect to the fixed frame. If $\mathbf{A}$ is a constant vector in the moving frame, then its variation is solely due to the rotation of the moving frame, i.e., $\mathrm{d}\mathbf{A}/\mathrm{d}t = \mathbf{\Omega} \times \mathbf{A}$. If we allow $\mathbf{A}$ to change with time, we simply add the time derivative of $\mathbf{A}$ in the moving frame:

$$
\frac{\mathrm{d}\mathbf{A}}{\mathrm{d}t} = \frac{\mathrm{d}'\mathbf{A}}{\mathrm{d}t} + \mathbf{\Omega} \times \mathbf{A}
$$

where the prime indicates that the derivative is taken in the moving frame.

We can apply this to the equations of motion to obtain:

$$
\frac{\mathrm{d}'\mathbf{P}}{\mathrm{d}t} + \mathbf{\Omega} \times \mathbf{P} = \mathbf{F} \qquad \frac{\mathrm{d}'\mathbf{M}}{\mathrm{d}t} + \mathbf{\Omega} \times \mathbf{M} = \mathbf{\tau}
$$

Consider the components of the first equation taken in the moving $x_{i}$ frame. Replacing $\mathbf{P}$ with $\mu \mathbf{V}$, we have:

$$
\mu \left( \frac{\mathrm{d}V_{i}}{\mathrm{d}t} + \epsilon_{ijk} \Omega_{j} V_{k} \right) = F_{i}
$$

As an example, the first component of the equation gives:

$$
\mu \left( \frac{\mathrm{d}V_{1}}{\mathrm{d}t} + \Omega_{2} V_{3} - \Omega_{3} V_{2} \right) = F_{1}
$$

The second set of equations read:

$$
\frac{\mathrm{d}M_{i}}{\mathrm{d}t} + \epsilon_{ijk} \Omega_{j} M_{k} = \tau_{i}
$$

If $x_{i}$ are the principal axes, then we can substitute $M_{i} = I_{i} \Omega_{i}$ to obtain explicit equations for the angular velocity:

$$
\begin{split}
I_{1} \dot{\Omega}_{1} + (I_{3} - I_{2}) \Omega_{2} \Omega_{3} &= \tau_{1} \\
I_{2} \dot{\Omega}_{2} + (I_{1} - I_{3}) \Omega_{3} \Omega_{1} &= \tau_{2} \\
I_{3} \dot{\Omega}_{3} + (I_{2} - I_{1}) \Omega_{1} \Omega_{2} &= \tau_{3}
\end{split}
$$

which are called Euler's equations.
