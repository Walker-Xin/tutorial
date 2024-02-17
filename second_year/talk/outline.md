# Second Year Talk Outline

Tentative title: *From Newton's Laws to Modelling Black Holes - The Power of Numerical Methods*

This talk aims to explore the power of computational methods in physical modelling, through examples drawn from both classical mechanics and general relativity.

We start with the classical mechanics idea that, to determine the past, present and future of a particle's motion, we only need to know its position and velocity at some time. The rest can be determined by integrating Newton's laws of motion, which are second order differential equations.

Computers do a good job in solving DEs, but designing a good algorithm is the task of scientists. We will discuss the trivial Euler method and move on to Runge-Kutta methods and discuss the issue of adaptive step size. An illustration of the importance of adaptive step size can be made by considering a chaos system (three-body system). Some simulation results may be shown.

We then move to general relativity and briefly introduce the notion of geodesics, which in our case are the trajectories of photons. We will only focus on its mathematical structure of being a set of coupled second order DEs. We will discuss the Schwarzschild metric and the geodesic equation (a generalisation of Newton's second law in curved spacetime). We will briefly discuss the accretion disk and how photons emitted by them allow us to 'see' black holes.

A short demonstration of the ray-tracing code will be given. A simple simulated image of a black hole will be shown. Finish with some scientific value of visualising BHs (determining BH spin, testing GR, etc.)

## Introduction

One of the greatest achievements of science is the ability to 'predict the future'. This is especially true in mechanics, where the Newton's laws set out the evolution of all physical systems, at least within the realm of classical mechanics. While the laws demonstrate the simplicity of physics, solving for useful information from them is often a very involved process. In this talk, we will embark on a journey that starts with classical mechanics and the art of solving differential equations. We will see how the study of lowly everyday objects can enable us to model and simulate some of the most exotic heavenly objects in universe.

## Newton's Laws

'If all the co-ordinates and velocities (of a system) are simultaneously specified, it is known from experience that the state of the system is completely determined and that its subsequent motion can, in principle, be calculated.' - Laudau and Lifshitz

Let us consider the significance of this statement. It is saying that, within the framework of classical mechanics, the working of our universe is such that we only need to know the position and velocity of an object at some time, and we would in principle be able to determine its complete past, present, and future. This is a very powerful statement.

What is the 'principle' we are talking about? Newton's laws of motion. Let us think of $F = ma$. Apart from some philosophical interpretations, such as what force and mass are, this equation tells us how an object moves given some other information.

### Euler's Method and Error

## Numerical Methods

We see that the naive Euler method has at least two drawbacks: its error is of the order of the step size, and it is not very stable. We can improve on both of these by using the Runge-Kutta methods coupled with adaptive step size.

### Higher Order Methods

### Adaptive Step Size

## Black Hole, Accretion, and Photon Trajectories

### Idea of Black Hole

The question now becomes: how does a black hole deform spacetime, and how does this affect the motion of photons? To answer this, we first need to understand what a black hole is.

The idea of a physical entity with a gravity so strong that light cannot escape from it was proposed as early as 1783 by John Michell. The idea was that the escape velocity from such an object is only dependent on its mass and radius, and there is nothing stopping us to extend the escape velocity to the speed of light. However, there was little interest in the idea as physicists of that time lacked the mathematical machinery to deal with such an object. In fact, the idea was so far ahead of its time that only more than a century later did scientists start to understand the implications of such an object.

In 1915, Einstein published his theory of general relativity along with the Einstein field equations. In the subsequent year, Karl Schwarzschild found the first exact solution to the field equations, known as the Schwarzschild metric. From the structure of the metric, the idea of a black hole naturally emerged. It was soon realised that despite the lengthy development of such a complex theory, black holes are very simple objects characterised by only three parameters: mass, charge, and spin. This is known as the no-hair theorem. It is then theorised that black holes should have negligible charge as our universe is electrically neutral, and that they should be spinning due to conservation of angular momentum.

### Accretion Disk

Often, black holes are found in binary systems consisting of a BH and another object which is often a star. The star's mass can be 'sucked' into the BH in a process call accretion. Due to angular momentum conservation, the matter does not fall directly into the BH, but instead forms a disk around it and gradually spirals in. The immense gravitational potential energy gets converted to heat and the disk material gets so hot ($\sim 10^{7}K$) that it emits some of the most energetic radiation in the universe in the form of X-rays. In fact, the efficiency of this energy radiation is about ten times that of nuclear fusion. This is how we can 'see' black holes.

## Numerical Modelling of Photon Trajectories

Going back to our central theme, the natural question to ask is: how do we model the motion of photons around a black hole? If we can simulate the full motion of photons, we can then find out how photons from a accretion disk would travel to an observer at a distant location. This will then tell us how this observer would 'see' the black hole.

### Spacetime Metric

We know from popular science that mass can deform spacetime. To quantify this, we use the metric tensor. In flat spacetime, the metric tensor is simply the Minkowski metric:

$$
\eta_{\mu\nu} = \begin{pmatrix} -1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}
$$

In curved spacetime, however, the terms in the tensor become functions of the coordinates. The Schwarzschild metric, for example, describes how spacetime is deformed by a non-rotating, spherically symmetric mass:

$$
ds^2 = -\left(1 - \frac{2GM}{c^2r}\right)c^2dt^2 + \left(1 - \frac{2GM}{c^2r}\right)^{-1}dr^2 + r^2d\theta^2 + r^2\sin^2\theta d\phi^2
$$

Given some metric, the motion of a photon is described by the geodesic equation:

$$
\frac{d^2x^\mu}{d\lambda^2} + \Gamma^\mu_{\nu\sigma}\frac{dx^\nu}{d\lambda}\frac{dx^\sigma}{d\lambda} = 0
$$

Let us explain this equation in lay man's terms. Here $\lambda$ is called an affine parameter that 'plays the role of time'. The $\Gamma$ terms are a set of very complicated functions that depend on the metric. The equation then says that the second derivative of one coordinate is determined by the first derivatives of the other coordinates. Compare this to Newton's second law, we see that GR is a much more complicated theory.

That is, the trajectory of a photon some spacetime is determined by the a set of coupled second order differential equations. This is then, in principle, a problem that can be solved by a computer. However, several other pieces of information are needed to solve this equation, such as the initial position and energy of the photon. Such information is actually not within the scope of GR, but is determined by the accretion disk model that eventually boils down to atomic physics of the disk material.
