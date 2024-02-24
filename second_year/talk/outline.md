# Second Year Talk Outline

Tentative title: *From Newton's Laws to Modelling Black Holes - The Power of Numerical Methods*

This talk aims to explore the power of computational methods in physical modelling, through examples drawn from both classical mechanics and general relativity.

We start with the classical mechanics idea that, to determine the past, present and future of a particle's motion, we only need to know its position and velocity at some time. The rest can be determined by integrating Newton's laws of motion, which are second order differential equations.

Computers do a good job in solving DEs, but designing a good algorithm is the task of scientists. We will discuss the trivial Euler method and move on to Runge-Kutta methods and discuss the issue of adaptive step size. An illustration of the importance of adaptive step size can be made by considering a chaos system (three-body system). Some simulation results may be shown.

We then move to general relativity and briefly introduce the notion of geodesics, which in our case are the trajectories of photons. We will only focus on its mathematical structure of being a set of coupled second order DEs. We will discuss the Schwarzschild metric and the geodesic equation (a generalisation of Newton's second law in curved spacetime). We will briefly discuss the accretion disk and how photons emitted by them allow us to 'see' black holes.

A short demonstration of the ray-tracing code will be given. A simple simulated image of a black hole will be shown. Finish with some scientific value of visualising BHs (determining BH spin, testing GR, etc.)

## Introduction

One of the greatest achievements of science is the ability to 'predict the future'. Consideration of the future, or in psychology terms, foresight, is a very human trait. We as a species worries about survival, and individual members worry about their own future, such as job prospects, health, and being able to graduate. We are mesmerised by the idea of looking beyond the present, that we have developed a whole field of science to theorise how our physical world evolves.

This is especially true in mechanics, where the Newton's laws set out the evolution of all physical systems, at least within the realm of classical mechanics. While the laws demonstrate the simplicity of physics, solving for useful information from them is often a very involved process.

In this talk, we will embark on a journey that starts with prediction using classical mechanics and the art of solving differential equations. We will see how the study of ordinary everyday objects can enable us to model and simulate some of the most exotic heavenly objects in universe.

## Newton's Laws

'If all the co-ordinates and velocities (of a system) are simultaneously specified, it is known from experience that the state of the system is completely determined and that its subsequent motion can, in principle, be calculated.' - Laudau and Lifshitz

Let us consider the significance of this statement. It is saying that, within the framework of classical mechanics, the working of our universe is such that we only need to know the position and velocity of an object at some time, and we would in principle be able to determine its complete past, present, and future. This is a very powerful statement.

What is the 'principle' we are talking about? Newton's laws of motion. Let us think of $F = ma$. Apart from some philosophical interpretations, such as what force and mass are, this equation tells us how an object moves given some other information.

### Euler's Method and Error

Imagine a rocket moving through space under the influence of gravity. It state of motion is determined by the vector containing its position and velocity. In a very small time interval, the rocket will update its position via its current velocity $\delta x = v\delta t$. It will also update its velocity via the force acting on it $\delta v = F\delta t/m$. This force, of course, is a function of the current position. This is the idea of the Euler method. It is a very simple method, and it is not very accurate. Consider the Euler method used in solving the following equation:

$$
y' = -15y \quad y(0) = 1
$$

We know the theorectical solution is $y = e^{-15x}$. If we choose a step size of $1/8$, the computed solution becomes oscillatory. This is because the error of the Euler method is of the order of the step size, which is often too large for practical purposes.

## Numerical Methods

We see that the naive Euler method has at least two drawbacks: its error is of the order of the step size, and it is not very stable. We can improve on both of these by using the Runge-Kutta methods coupled with adaptive step size.

### Higher Order Methods

A apparent flaw of Euler's method is that it is in some way too 'naive' or too 'local'.

An immediate improvement is to go forward one step and see what the force is there, and then use the average of the next force and the current force. This is the second order method. We can then 'scout' ahead even further and use the average of the forces at each step. By adjusting carefully the weights of the forces, we can get a fourth order method called the Runge-Kutta method.

### Adaptive Step Size

Another issue with the Euler method is that the step size is fixed. This is not very efficient. For example, we do not want to use a very small step size when the rocket is far away from the Earth, but we do want to use a small step size when the rocket is near the Earth. When the force varies a lot, we want to use a small step size to capture the features of the force. This is the idea of adaptive step size. To implement an algorithm, we would need a criterion, often an error estimate, to determine when to change the step size by how much.

In practice, when using the 4th order Runge-Kutta method, we can use the difference between the 4th order and 5th order Runge-Kutta methods as an error estimate. This is a very good estimate, as the 5th order method is very accurate. There are a variety of other methods to estimate the error, but the idea is the same.

## Black Hole, Accretion, and Photon Trajectories

### Idea of Black Hole

The question now becomes: how does a black hole deform spacetime, and how does this affect the motion of photons? To answer this, we first need to take a detour to understand what a black hole is.

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

### Ray Tracing

What comes next is technically all computation and zero physics. To simulate the look of a black hole, or really its accretion disk, we need to solve the geodesic equation for photons emitted by the disk. Simulating all of the photons emitted by the disk wastes a lot of resource, as not all of them will reach the observer. Instead, we trace photons backwards from the observer to the disk. If we are only interested in the shape of the image, we can imagine a uniform disk emitting photons of the same energy. The observer can be treated as a plane at a large distance away that is perpendicular to the vector pointing from the observer to the black hole. We then fire photons from different locations on the plane and see if they hit the disk. By collecting the photons that hit the disk, we can then form an image of the disk.

## Scientific Value

But you ask what is the point of all this? Beside the coolness of simulating a literal black hole on your personal computer, there are a lot of scientific value in modelling space time and ray tracing photons. Instead of visualising the BH, we could generate a simulated spectrum of the photons and compare this with what we observe from telescopes. The shape of the spectrum is affected by the gravitational redshift, which ultimately depends on the parameters of the BH. The spectrum hence serves as a tool to measure the properties of the BH.

## Concluding Remarks

We have undergone a journey that started with the simple Newton's laws and Euler methods and progressed all the way to simulating some of the most extreme objects in the universe. There are two key messages that unpin this journey. The first one, being the more philosophical, is that physical theories often share common features where similar mathematical structures are observed. The second one, being more practical, is the interplay between the power of computation and the power of human wisdom. While the computer can solve some of the immediate problems by brute force, ingenuity of us scientists is often what prevails in solving the most difficult problems. We have seen ChatGPTs excelling in casual conversation, but it scientific reasoning is still lackluster. Perhaps what we discussed today is a good example of how human wisdom is still essential, and it is certainly my hope that this will remain true for a long time to come.
