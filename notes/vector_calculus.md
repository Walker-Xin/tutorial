# Vector Calculus

- [Multivariate Calculus](#multivariate-calculus)
    - [Partial Derivatives](#partial-derivatives)
    - [Change of Variables](#change-of-variables)
    - [Taylor's Theorem and Stationary Points](#taylors-theorem-and-stationary-points)
- [Multiple Integrals](#multiple-integrals)
    - [Double Integrals](#double-integrals)
    - [Triple Integrals](#triple-integrals)
    - [Chain Rule](#chain-rule)
- [Curvilinear Coordinates](#curvilinear-coordinates)
    - [Polar Coordinates](#polar-coordinates)
    - [Cylindrical Coordinates](#cylindrical-coordinates)
    - [Spherical Coordinates](#spherical-coordinates)
- [Vector Calculus Operations](#vector-calculus-operations)
    - [Gradient](#gradient)
    - [Divergence](#divergence)
    - [Laplacian](#laplacian)
    - [Curl](#curl)
- [Line and Surface Integrals](#line-and-surface-integrals)
    - [Line Integrals](#line-integrals)
    - [Surface Integrals](#surface-integrals)
- [Vector Calculus Theorems](#vector-calculus-theorems)
    - [Divergence Theorem](#divergence-theorem)
    - [Stokes' Theorem](#stokes-theorem)

## Multivariate Calculus

### Partial Derivatives

Consider a function $f(x, y)$ of two variables. The partial derivative of $f$ with respect to $x$ is defined as:

$$
\frac{\partial f}{\partial x} \equiv \lim_{\Delta x \to 0} \frac{f(x + \Delta x, y) - f(x, y)}{\Delta x}
$$

provided the limit exists.

Similarly, the partial derivative of $f$ with respect to $y$ is defined as:

$$
\frac{\partial f}{\partial y} \equiv \lim_{\Delta y \to 0} \frac{f(x, y + \Delta y) - f(x, y)}{\Delta y}
$$

There can be higher order partial derivatives. Particularly, note the identity:

$$
\frac{\partial^{2} f}{\partial x \partial y} = \frac{\partial^{2} f}{\partial y \partial x}
$$

The total differential of $f$ is defined as:

$$
\mathrm{d}f = \frac{\partial f}{\partial x} \, \mathrm{d}x + \frac{\partial f}{\partial y} \, \mathrm{d}y
$$

### Change of Variables

Suppose that for $f(x, y)$, $x = x(t)$ and $y = y(t)$ are functions of $t$. Then the chain rule gives the derivative of $f$ with respect to $t$ as:

$$
\frac{\mathrm{d}f}{\mathrm{d}t} = \frac{\partial f}{\partial x} \frac{\mathrm{d}x}{\mathrm{d}t} + \frac{\partial f}{\partial y} \frac{\mathrm{d}y}{\mathrm{d}t}
$$

In general, if $f(x_{1}, x_{2}, \ldots, x_{n})$ is a function of $n$ variables that are each functions of $t$, then the chain rule gives:

$$
\frac{\mathrm{d}f}{\mathrm{d}t} = \sum_{i = 1}^{n} \frac{\partial f}{\partial x_{i}} \frac{\mathrm{d}x_{i}}{\mathrm{d}t}
$$

Consider the general case of a function $f(x_{1}, x_{2}, \ldots, x_{n})$ of $n$ variables. Suppose that $x_{i}$ are in turn functions of $m$ other variables $u_{1}, u_{2}, \ldots, u_{m}$. Then the chain rule gives:

$$
\frac{\partial f}{\partial u_{j}} = \sum_{i = 1}^{n} \frac{\partial f}{\partial x_{i}} \frac{\partial x_{i}}{\partial u_{j}}
$$

### Taylor's Theorem and Stationary Points

Consider a function $f(x, y)$ of two variables. The Taylor series expansion of $f$ about the point $(x_{0}, y_{0})$ is given by:

$$
f(x, y) = f(x_{0}, y_{0}) + \frac{\partial f}{\partial x} \Delta x + \frac{\partial f}{\partial y} \Delta y + \frac{1}{2!} \left( \frac{\partial^{2} f}{\partial x^{2}} \Delta x^{2} + 2 \frac{\partial^{2} f}{\partial x \partial y} \Delta x \Delta y + \frac{\partial^{2} f}{\partial y^{2}} \Delta y^{2} \right) + \ldots
$$

where $\Delta x = x - x_{0}$ and $\Delta y = y - y_{0}$ and the derivatives are evaluated at $(x_{0}, y_{0})$.

In general, the stationary points of a multivariate function are the points where the first derivatives of $f$ are zero. The second derivatives of $f$ can be used to classify the stationary points. For a function $f$ of two variables, consider the second order variation in $f$ about a stationary point $(x_{0}, y_{0})$:

$$
\begin{split}
f(x, y) - f(x_{0}, y_{0}) &\approx \frac{1}{2} \left( f_{xx} \Delta x^{2} + 2 f_{xy} \Delta x \Delta y + f_{yy} \Delta y^{2} \right) \\
&= \frac{1}{2} \left[ f_{xx} \left( \Delta x + \frac{f_{xy} \Delta y}{f_{xx}} \right)^{2} + \left( f_{yy} - \frac{f_{xy}^{2}}{f_{xx}} \right) \Delta y^{2} \right]
\end{split}
$$

For a minimum, we require this to be positive for all $\Delta x$ and $\Delta y$. This requires $f_{xx} > 0$ and $f_{yy} f_{yy} > f_{xy}^{2}$. By symmetry, we also require $f_{yy} > 0$.

For a maximum, we require $f_{xx} < 0$, $f_{yy} < 0$ and $f_{yy} f_{yy} > f_{xy}^{2}$.

For a saddle point, we require $f_{xx} f_{yy} < 0$ (they have opposite signs) or $f_{yy} f_{yy} < f_{xy}^{2}$.

## Multiple Integrals

### Double Integrals

Consider a rectangular domain $D = [a, b] \times [c, d] \sub \mathbb{R}^{2}$ in the $xy$ plane and a continuous function $f(x, y)$ defined on $D$. The volume $V$ contained by the surfaces $z = 0$ and $z = f(x, y)$ is given by the double integral:

$$
V = \int_{a}^{b} \left( \int_{c}^{d} f(x, y) \, \mathrm{d}y \right) \, \mathrm{d}x = \iint_{D} f(x, y) \, \mathrm{d}x \, \mathrm{d}y
$$

It can be shown that the above integral is defined if $D \in \mathbb{R}^{2}$ is a regular domain and $f(x, y)$ is continuous on $D$. There are, of course, more complex domains. A domain is called x-simple if horizontal lines alway intersect the domain into a single line segment and y-simple if vertical lines always intersect the domain into a single line segment. Formally, a set $D \sub \mathbb{R}^{2}$ is x-simple if:

$$
D = \left\{ (x, y) \in \mathbb{R}^{2} | x \in [a, b], g_{1}(x) \le y \le g_{2}(x) \right\}
$$

where $g_{1}(x)$ and $g_{2}(x)$ are some continuous functions on $[a, b]$.

Similarly, $D$ is y-simple if:

$$
D = \left\{ (x, y) \in \mathbb{R}^{2} | y \in [c, d], h_{1}(y) \le x \le h_{2}(y) \right\}
$$

where $h_{1}(y)$ and $h_{2}(y)$ are some continuous functions on $[c, d]$.

Given a, say, x-simple domain $D$, we compute the double integral as follows:

$$
V = \int_{a}^{b} \left( \int_{h_{1}(y)}^{h_{2}(y)} f(x, y) \, \mathrm{d}x \right) \, \mathrm{d}y
$$

For a y-simple domain:

$$
V = \int_{c}^{d} \left( \int_{g_{1}(x)}^{g_{2}(x)} f(x, y) \, \mathrm{d}y \right) \, \mathrm{d}x
$$

A domain is called simple if it is both x-simple and y-simple. For such a domain, the order of integration does not matter. For more complicated domains, it is usually the case that it can be decomposed into a finite number of simple domains so that the double integral can be carried out.

### Triple Integrals

Extending the above argument to a domain $D \sub \mathbb{R}^{3}$, we have two types of triple integrals: integration by layers and by lines. For integration by layers, let $\Omega$ be a domain in $\mathbb{R}^{3}$ defined by:

$$
\Omega = \left\{ (x, y, z) \in \mathbb{R}^{3} | h_{1} \le z \le h_{2} \in \Omega(z) \right\}
$$

where for every $z \in [h_{1}, h_{2}]$, $\Omega(z)$ is a simple domain in $\mathbb{R}^{2}$. Then if $f(x, y, z)$ is continuous on $\Omega$, $f$ is integrable on $\Omega$ and the integral is defined as:

$$
\iiint_{\Omega} f(x, y, z) \, \mathrm{d}x \, \mathrm{d}y \, \mathrm{d}z = \int_{h_{1}}^{h_{2}} \left( \iint_{\Omega(z)} f(x, y, z) \, \mathrm{d}x \, \mathrm{d}y \right) \, \mathrm{d}z
$$

For integration by lines, let $\Omega$ be a domain in $\mathbb{R}^{3}$ defined by:

$$
\Omega = \left\{ (x, y, z) \in \mathbb{R}^{3} | g_{1}(x, y) \le z \le g_{2}(x, y), (x, y) \in D \right\}
$$

where $D$ is a regular domain in the $xy$ plane and $g_{1}$ and $g_{2}$ are continuous functions on $D$. Then if $f(x, y, z)$ is continuous on $\Omega$, $f$ is integrable on $\Omega$ and the integral is defined as:

$$
\iiint_{\Omega} f(x, y, z) \, \mathrm{d}x \, \mathrm{d}y \, \mathrm{d}z = \iint_{D} \left( \int_{g_{1}(x, y)}^{g_{2}(x, y)} f(x, y, z) \, \mathrm{d}z \right) \, \mathrm{d}x \, \mathrm{d}y
$$

### Chain Rule

Consider the double integral:

$$
\iint_{D} f(x, y) \, \mathrm{d}x \, \mathrm{d}y
$$

Suppose that the original coordinates $(x, y)$ can be changed to some new set of coordinates $(u, v)$ via a transformation $T:D' \to D$:

$$
(x, y) = T(u, v)
$$

or explicitly:

$$
\begin{split}
x &= x(u, v) \\
y &= y(u, v)
\end{split}
$$

so that the integrand $f(x, y)$ can be written $f(x, y) \equiv f'(u, v)$.

To carry out the change of variables, we need to express the infinitesimal area $\mathrm{d}x \, \mathrm{d}y$ in terms of $\mathrm{d}u \, \mathrm{d}v$. We have:

$$
\mathrm{d}x \, \mathrm{d}y = (x_{u}y_{v} - x_{v}y_{u}) \, \mathrm{d}u \, \mathrm{d}v = J(u, v) \, \mathrm{d}u \, \mathrm{d}v
$$

where $J(u, v)$ is the determinant of the Jacobian matrix associated with the transformation $T$:

$$
J(u, v) = \det \begin{pmatrix} x_{u} & x_{v} \\ y_{u} & y_{v} \end{pmatrix} \equiv \left\lvert \frac{\partial (x, y)}{\partial (u, v)} \right\rvert
$$

Then, the double integral becomes:

$$
\iint_{D} f(x, y) \, \mathrm{d}x \, \mathrm{d}y = \iint_{D'} f'(u, v) \, \left\lvert \frac{\partial (x, y)}{\partial (u, v)} \right\rvert \, \mathrm{d}u \, \mathrm{d}v
$$

Generalising the result to three dimensions, a change of coordinates in an n-dimensional integral from $(x, y, z)$ to $(u, v, w)$ is given by:

$$
\mathrm{d}x \, \mathrm{d}y \, \mathrm{d}z = J(u, v, w) \, \mathrm{d}u \, \mathrm{d}v \, \mathrm{d}w
$$

where $J(u, v, w)$ has the form:

$$
J(u, v, w) = \det \begin{pmatrix} x_{u} & x_{v} & x_{w} \\ y_{u} & y_{v} & y_{w} \\ z_{u} & z_{v} & z_{w} \end{pmatrix} \equiv \left\lvert \frac{\partial (x, y, z)}{\partial (u, v, w)} \right\rvert
$$

Note that since we are taking the determinant, the actual matrix can be transposed and the determinant will still be the same.

A rough proof of the Jacobian determinant in the two-dimensional case proceeds as follows. Let $T$ be a transformation from $(x, y)$ to $(u, v)$. An infinitesimal rectangle $R$ in the domain $D$ expressed in $(x, y)$ is mapped to another shape $R'$ (in general not rectangular) in the domain $D'$ expressed in $(u, v)$. Consider a point $P = (x_{0}, y_{0})^{\intercal}$ in $R$ and its image $P'$ in $R'$. In the vicinity of $P$, the transformation $T$ can be approximated as a series expansion:

$$
T(x, y) \approx T(x_{0}, y_{0}) + \frac{\partial T}{\partial x}(x_{0}, y_{0}) (x - x_{0}) + \frac{\partial T}{\partial y}(x_{0}, y_{0}) (y - y_{0})
$$

Let us denote $\delta x = x - x_{0}$ and $\delta y = y - y_{0}$. This means that we can approximate $R'$ as a parallelogram with vertices $P'$, $P' + \delta u \hat{u}$, $P' + \delta u \hat{u}+ \delta v \hat{v}$ and $P' + \delta v\hat{v}$ where $\delta u = \frac{\partial T}{\partial x}(x_{0}, y_{0}) \, \delta x$ and $\delta v = \frac{\partial T}{\partial y}(x_{0}, y_{0}) \, \delta y$. Then the area of $R$ is given by:

$$
\delta A = \delta x \, \delta y
$$

The area of $R'$ is given by:

$$
\delta A' = \left\lvert \delta u \hat{u} \times \delta v \hat{v} \right\rvert
$$

## Curvilinear Coordinates

### Polar Coordinates

Consider the transformation from Cartesian coordinates $(x, y)$ to polar coordinates $(r, \theta)$ given by:

$$
\begin{split}
x &= r \cos{\theta} \\
y &= r \sin{\theta}
\end{split}
$$

so that the basis vectors in polar coordinates are given by:

$$
\begin{split}
\hat{r}  &= \cos{\theta} \hat{x} + \sin{\theta} \hat{y} \\
\hat{\theta} &= -\sin{\theta} \hat{x} + \cos{\theta} \hat{y}
\end{split}
$$

The Jacobian is given by:

$$
J(r, \theta) = \left\lvert \frac{\partial (x, y)}{\partial (r, \theta)} \right\rvert = r
$$

so that:

$$
\mathrm{d}A = \mathrm{d}x \, \mathrm{d}y = r \, \mathrm{d}r \, \mathrm{d}\theta
$$

### Cylindrical Coordinates

Next we consider the cylindrical coordinates $(r, \theta, z)$ given by:

$$
\begin{split}
x &= r \cos{\theta} \\
y &= r \sin{\theta} \\
z &= z
\end{split}
$$

so that the basis vectors in cylindrical coordinates are given by:

$$
\begin{split}
\hat{r}  &= \cos{\theta} \hat{x} + \sin{\theta} \hat{y} \\
\hat{\theta} &= -\sin{\theta} \hat{x} + \cos{\theta} \hat{y} \\
\hat{z} &= \hat{z}
\end{split}
$$

The Jacobian is given by:

$$
J(r, \theta, z) = \left\lvert \frac{\partial (x, y, z)}{\partial (r, \theta, z)} \right\rvert = r
$$

so that:

$$
\mathrm{d}V = \mathrm{d}x \, \mathrm{d}y \, \mathrm{d}z = r \, \mathrm{d}r \, \mathrm{d}\theta \, \mathrm{d}z
$$

### Spherical Coordinates

Finally, we consider the spherical coordinates $(r, \theta, \phi)$ given by:

$$
\begin{split}
x &= r \sin{\theta} \cos{\phi} \\
y &= r \sin{\theta} \sin{\phi} \\
z &= r \cos{\theta}
\end{split}
$$

where $\theta \in [0, \pi]$ is the polar angle and $\phi \in [0, 2\pi]$ is the azimuthal angle.

The basis vectors in spherical coordinates are given by:

$$
\begin{split}
\hat{r}  &= \sin{\theta} \cos{\phi} \hat{x} + \sin{\theta} \sin{\phi} \hat{y} + \cos{\theta} \hat{z} \\
\hat{\theta} &= \cos{\theta} \cos{\phi} \hat{x} + \cos{\theta} \sin{\phi} \hat{y} - \sin{\theta} \hat{z} \\
\hat{\phi} &= -\sin{\phi} \hat{x} + \cos{\phi} \hat{y}
\end{split}
$$

The Jacobian is given by:

$$
J(r, \theta, \phi) = \left\lvert \frac{\partial (x, y, z)}{\partial (r, \theta, \phi)} \right\rvert = r^{2} \sin{\theta}
$$

so that:

$$
\mathrm{d}V = \mathrm{d}x \, \mathrm{d}y \, \mathrm{d}z = r^{2} \sin{\theta} \, \mathrm{d}r \, \mathrm{d}\theta \, \mathrm{d}\phi
$$

## Vector Calculus Operations

### Gradient

The gradient of a scalar field $\phi$ is defined as:

$$
\nabla \phi \equiv \left( \frac{\partial \phi}{\partial x}, \frac{\partial \phi}{\partial y}, \frac{\partial \phi}{\partial z} \right)^{\intercal}
$$

In fact, the gradient can be defined via the directional derivative. Consider an infinitesimal displacement $\mathrm{d}\mathbf{r}$ in the direction $\hat{v}$. The directional derivative of $\phi$ at $\mathbf{r}_{0}$ in the direction $\hat{v}$ is given by:

$$
\frac{\partial \phi}{\partial x_{v}} \equiv \lim_{\epsilon \rightarrow 0} \frac{\phi(\mathbf{r}_{0} + \epsilon \hat{v}) - \phi(\mathbf{r}_{0})}{\epsilon}
$$

Then the gradient of $\phi$ at $\mathbf{r}_{0}$ is just a linear combination of the directional derivatives:

$$
\frac{\partial \phi}{\partial x_{v}} = \nabla \phi \cdot \hat{v}
$$

There are several interpretations of the gradient. $\nabla \phi \cdot \hat{v}$ is a scalar that will be maximized when $\hat{v}$ is parallel to $\nabla \phi$. This is the same as the direction of steepest ascent in the value of $\phi$. For a surface characterised by $f(x, y, z) = 0$, the gradient at any point gives the direction of the normal to the surface. That is, the unit normal vector is given by:

$$
\hat{n} = \frac{\nabla f}{\left\lvert \nabla f \right\rvert}
$$

### Divergence

The divergence of a vector field $\mathbf{F}$ is defined as:

$$
\nabla \cdot \mathbf{F} \equiv \left( \frac{\partial F_{x}}{\partial x} + \frac{\partial F_{y}}{\partial y} + \frac{\partial F_{z}}{\partial z} \right)
$$

A vector field with a zero divergence is called solenoidal or incompressible.

### Laplacian

The Laplacian of a scalar field $vec{F}$ is defined as:

$$
\nabla^{2} \phi \equiv \left( \frac{\partial^{2} \phi}{\partial x^{2}} + \frac{\partial^{2} \phi}{\partial y^{2}} + \frac{\partial^{2} \phi}{\partial z^{2}} \right)
$$

### Curl

The curl of a vector field $\mathbf{F}$ is defined as:

$$
\nabla \times \mathbf{F} \equiv \left( \frac{\partial F_{z}}{\partial y} - \frac{\partial F_{y}}{\partial z}, \frac{\partial F_{x}}{\partial z} - \frac{\partial F_{z}}{\partial x}, \frac{\partial F_{y}}{\partial x} - \frac{\partial F_{x}}{\partial y} \right)^{\intercal}
$$

Formally, the components of the curl are defined via the line integrals:

$$
(\nabla \times \mathbf{F}) \cdot \hat{n} = \lim_{A \to 0} \frac{1}{A} \int_{\partial A} \mathbf{F} \cdot \mathrm{d}\mathbf{r}
$$

where $\partial A$ is the boundary of a small area $A$ and $\hat{n}$ is the unit normal vector to $\partial A$.

Taking $\mathbf{n}$ as the standard unit vectors, we can recover the original formula of the curl as a cross product.

A vector field with a zero curl is called irrotational.

## Line and Surface Integrals

### Line Integrals

Consider a curve $\mathbf{r}$ on $\mathbb{R}^{m}$ be a regular curve with trace $C$. Let $f$ be a real-valued scalar function defined on a subset of $\mathbb{R}^{m}$ that contains $C$. The line integral of $f$ along the curve is defined as:

$$
\int_{C} f \, \mathrm{d}s \equiv \int_{C} f(\mathbf{r}) \, \left\lvert \frac{\mathrm{d}\mathbf{r}}{\mathrm{d}s} \right\rvert \, \mathrm{d}s
$$

This integration can also be done with respect to the infinitesimal vector displacement $\mathrm{d}\mathbf{r}$:

$$
\int_{C} f \, \mathrm{d}\mathbf{r} \equiv \int_{C} f(\mathbf{r}) \, (\hat{i} \mathrm{d}x + \hat{j} \mathrm{d}y + \hat{k} \mathrm{d}z)
$$

Consider further a vector function or field $\mathbf{A}$ defined on a subset of $\mathbb{R}^{m}$ that contains $C$. The line integral of $\mathbf{A}$ along the curve is defined as:

$$
\int_{C} \mathbf{A} \cdot \, \mathrm{d}\mathbf{r} \equiv \int_{C} A_{x} \, \mathrm{d}x + A_{y} \, \mathrm{d}y + A_{z} \, \mathrm{d}z
$$

Given a vector field $\mathbf{A}$, the line integral of $\mathbf{A}$ along a curve $C$ is generally dependent on the path taken. If, however, there exists a scalar field $\phi$ such that $\mathbf{A} = \nabla \phi$, then the line integral of $\mathbf{A}$ is path independent. Such a vector field is said to be conservative. The line integral of a conservative vector field around a closed curve is zero.

Let $C$ be a simple closed curve on $\mathbb{R}^{2}$ and let $D$ be the region bounded by $C$. Consider two functions $P(x, y)$ and $Q(x, y)$ defined on $D$ with continuous partial derivatives. Green's theorem states that:

$$
\oint_{C} P \, \mathrm{d}x + Q \, \mathrm{d}y = \iint_{D} \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) \, \mathrm{d}x \mathrm{d}y
$$

where the path of integration is anticlockwise around $C$.

### Surface Integrals

As in the case line integrals, a surface integral can have several forms. For a scalar function $f$ and some surface $S$, the simplest form of the surface integral is:

$$
\iint_{S} f \, \mathrm{d}S
$$

which can be viewed as a simple double integral over the surface.

Some other forms of the surface integral are:

$$
\iint_{S} f \, \mathrm{d}\mathbf{S}, \quad \iint_{S} \mathbf{A}  \cdot \, \mathrm{d}\mathbf{S}, \quad \iint_{S} \mathbf{A} \times \, \mathrm{d}\mathbf{S}
$$

where vector differential $\mathrm{d}\mathbf{S}$ is defined as the product of the infinitesimal area $\mathrm{d}S$ and the unit normal vector $\hat{n}$.

To evaluate a surface integral over some general surface, the area element $\mathrm{d}S$ must be expressed in terms of a chosen coordinate system. In some cases, the case can be simplified greatly due to certain symmetries, but for a general surface, it is often required to work in Cartesian coordinates by projecting the infinitesimal area element onto the xy-plane. At any given point on $S$, the area element $\mathrm{d}S$ satisfies:

$$
\mathrm{d}S = \frac{\mathrm{d}A}{\left\lvert \cos{\alpha} \right\rvert} = \frac{\mathrm{d}A}{\left\lvert \hat{n} \cdot \hat{k} \right\rvert}
$$

where $\mathrm{d}A = \mathrm{d}x \, \mathrm{d}y$ is the infinitesimal area element in the xy-plane and $\alpha$ is the angle between the normal vector $\hat{n}$ and the z-axis.

If the surface is given by the equation $g(x, y, z) = 0$, then the normal vector is given by:

$$
\hat{n} = \frac{\nabla g}{\left\lvert \nabla g \right\rvert}
$$

so that the infinitesimal vector area element can be expressed as:

$$
\mathrm{d}\mathbf{S} = \hat{n} \mathrm{d}S =\frac{\nabla g}{\partial g/\partial z} \, \mathrm{d}A
$$

On the other hand, if the surface is given in parametric form $\mathbf{r}(u, v) = (x(u, v), y(u, v), z(u, v))$, then the normal vector is given by:

$$
\hat{n} = \frac{\frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v}}{\left\lvert \frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v} \right\rvert}
$$

Since the size of the infinitesimal area element $\mathrm{d}S$ is related to $\mathrm{d}u \mathrm{d}v$ through the Jacobian:

$$
\mathrm{d}S = \left\lvert \frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v} \right\rvert \, \mathrm{d}u \mathrm{d}v
$$

the infinitesimal vector area element can be expressed as:

$$
\mathrm{d}\mathbf{S} = \left( \frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v} \right) \, \mathrm{d}u \mathrm{d}v
$$

## Vector Calculus Theorems

### Divergence Theorem

The divergence theorem, also known as Gauss' theorem, states that the surface integral of a vector field $\mathbf{F}$ with continuous first derivatives over a closed surface $S$ is equal to the volume integral of the divergence of $\mathbf{F}$ over the volume $V$ bounded by $S$:

$$
\oiint_{S} \mathbf{F} \cdot \mathrm{d}\mathbf{S} = \iiint_{V} \nabla \cdot \mathbf{F} \, \mathrm{d}V
$$

### Stokes' Theorem

Stokes' theorem states that the surface integral of the curl of a differentiable vector field $\mathbf{F}$ over a regular and oriented surface $S$ is equal to the line integral of $\mathbf{F}$ around the boundary $C$ of $S$:

$$
\iint_{S} (\nabla \times \mathbf{F}) \cdot \mathrm{d}\mathbf{S} = \oint_{C} \mathbf{F} \cdot \mathrm{d}\mathbf{r}
$$

In two dimensions, this is reduced to Green's theorem:

$$
\iint_{S} \left( \frac{\partial F_{y}}{\partial x} - \frac{\partial F_{x}}{\partial y} \right) \mathrm{d}\mathbf{S} = \oint_{C} \left( F_{x} \, \mathrm{d}x + F_{y} \, \mathrm{d}y \right)
$$
