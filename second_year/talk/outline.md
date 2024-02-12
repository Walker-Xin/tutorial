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

## Forage into General Relativity

Instead of a spacecraft travelling under the influence of a sun, let us consider a photon travelling under the influence of a black hole. The entities we consider now are beyond the scope of classical mechanics, and we need to use the machinery of general relativity.

### Spacetime Metric

We know from popular science that mass can deform spacetime. To quantify this, we use the metric tensor. In flat spacetime, the metric tensor is simply the Minkowski metric:

$$
\eta_{\mu\nu} = \begin{pmatrix} -1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}
$$

In curved spacetime, however, the terms in the tensor become functions of the coordinates. The Schwarzschild metric, for example, describes how spacetime is deformed by a non-rotating, spherically symmetric mass:

$$
ds^2 = -\left(1 - \frac{2GM}{c^2r}\right)c^2dt^2 + \left(1 - \frac{2GM}{c^2r}\right)^{-1}dr^2 + r^2d\theta^2 + r^2\sin^2\theta d\phi^2
$$

Given some metric,

## Black Hole, Accretion, and Photon Trajectories
