# Slide by Slide Script

## Slide 2

What do you think is the greatest achievement of science? People may say its mechanics, quantum physics. But in my opinion, the single most important result from science is that science has bestowed upon us the ability to predict the future.

## Slide 3

Consideration of the future is a very human trait. We as a species worries about survival. Individual members worry about their own future, their job prospects, health, and whether they can graduate. We humans are so mesmerised by the idea of looking beyond the present, that we have developed a whole field of science to theorise how our physical world evolves.

This is especially true in mechanics, where Newton's laws dictate the evolution of all physical systems, at least within the realm of classical mechanics. While the laws have the beauty of simplicity, extracting information from them is an involved process.

## Slide 4

In this talk, let us embark on a journey that starts with classical mechanics and the art of solving differential equations. We will see how the study of everyday objects can enable us to model some of the most exotic heavenly objects in the universe.

## Slide 5

Here I give you a quote from the renowned physicists Laudau and Lifshitz in their mechanics book.

Let us consider the significance of this statement. It is saying that, within classical mechanics, our universe evolves in such a way that we only need to know the position and velocity of an object at **some time**, and we would in principle be able to determine its complete past, present, and future. This is a very powerful statement.

## Slide 6

What is the 'principle' we are talking about? Newton's laws of motion. Let us think of $F = ma$. Apart from some philosophical interpretations, such as what force and mass are, this equation tells us how an object moves given some other information.

## Slide 7

Let us consider a very simple example.

Imagine a rocket moving through space under the influence of gravity. Its motion is determined by the vector containing its position and velocity. In a very small time interval, the rocket will update its position via its current velocity $\delta x = v\delta t$. It will also update its velocity via the force acting on it $\delta v = F\delta t/m$. This force, of course, is a function of the current position. 

## Slide 8

This is the idea of the Euler method. I put here a picture of him for fun. It is a very simple method that is not very accurate.

## Slide 9

Consider the Euler method used in solving the following equation. We know the theorectical solution, which is just an exponential decay. Let us see how Euler's method performs

## Slide 10

Here I have used Python to simulte the solutions with different step sizes. The red line shows the actual solution.

Unsurprisingly, choosing $dt = 0.01$ gives us the best solution that closely follows the theroretical one. If we increase the step size however, the solution gets very funky.

If we choose a step size of $1/8$, the computed solution becomes very oscillatory. This is because the error of the Euler method is of the order of the step size, which is often too large for practical purposes. Therefore we run into the problem of overshooting at every step, and the result is a mess.

## Slide 11

We see that the naive Euler method has two contradicting drawbacks: It is very inaccurate when the step size is large, but becomes very slow if step size is small. We can improve on both of these by using the Runge-Kutta methods coupled with adaptive step size.

## Slide 12

A apparent flaw of Euler's method is that it is in some way too 'naive' or too 'local'. An immediate improvement is to go forward one step and see what the force is there, and then use the average of the next force and the current force. Simply doing this yields a good improvement to the accuracy.

## Slide 13

We can 'scout' ahead even further and use an weighted average of the forces at each step. By adjusting carefully the weights of the forces, we can get a fourth order method called the Runge-Kutta method.

## Slide 14

Another problem of the method is that it is too 'dumb' because it only knows a fixed step size. This is very inefficient. For example, consider this extreme potential.

At large distances, the potential is almost uniform so the force does not vary a lot. This is when we want to increase our step size. When the potential (and thus the force) varies a lot, we better use a small step size to capture the features of the force. This is the idea of adaptive step size. 

## Slide 15

To implement an algorithm, we would need a criterion, often an error estimate, to determine when to change the step size by how much. In practice, when using the 4th order Runge-Kutta method, we can use the difference between the 4th order and 5th order Runge-Kutta methods as an error estimate. This is a very good estimate, as the 5th order method is very accurate. There are a variety of other methods to estimate the error, but the idea is the same.

## Slide 16

I promised at the start that the methods we have just discussed can be applied to exotic heavenly objects, such as black holes. To apply our knowledge, we will have to simulate how photons move around BHs. But before we jump into calculation, let us first understand what a black hole is.

## Slide 17

The idea of a physical entity with a gravity so strong that light cannot escape from it was proposed as early as 1783 by John Michell. The idea was that the escape velocity from such an object is only dependent on its mass and radius. There is nothing stopping us to increase the escape velocity to the speed of light.

However, there was little interest in the idea as physicists of that time lacked the mathematical machinery to deal with such an object. In fact, the idea was so far ahead of its time that only more than a century later did scientists start to understand the implications of such an object.

## Slide 18

In 1915, Einstein published his theory of general relativity along with the Einstein field equations. In the subsequent year, Karl Schwarzschild found the first exact solution to the field equations, known as the Schwarzschild metric. From the structure of the metric, the idea of a black hole naturally emerged. 

## Slide 19

It was soon realised that despite the lengthy development of such a complex theory, black holes are very simple objects characterised by only three parameters: mass, charge, and spin. This is known as the no-hair theorem. It is then theorised that black holes should have negligible charge as our universe is electrically neutral, and that they should be spinning due to conservation of angular momentum.

## Slide 20

Often, black holes are found in binary systems consisting of a BH and another object which is often a star. The star's mass can be 'sucked' into the BH in a process call accretion. Due to angular momentum conservation, the matter does not fall directly into the BH, but instead forms a disk around it and gradually spirals in. The immense gravitational potential energy gets converted to heat and the disk material gets so hot ($\sim 10^{7}K$) that it emits some of the most energetic radiation in the universe in the form of X-rays. In fact, the efficiency of this energy radiation is about ten times that of nuclear fusion. This is how we can 'see' black holes.

## Slide 21

Going back to our central theme, the natural question to ask is: how do we model the motion of photons around a black hole? If we can simulate the full motion of photons, we can then find out how photons from a accretion disk would travel to an observer at a distant location. This will then tell us how this observer would 'see' the black hole.

We know from popular science that mass can deform spacetime. To quantify this, we use the metric tensor. In flat spacetime, the metric tensor is simply the Minkowski metric. In curved spacetime, however, the terms in the tensor become functions of the coordinates. The Schwarzschild metric, for example, describes how spacetime is deformed by a non-rotating, spherically symmetric mass.

## Slide 22

Given some metric, the motion of a photon is described by the geodesic equation:

$$
\frac{d^2x^\mu}{d\lambda^2} + \Gamma^\mu_{\nu\sigma}\frac{dx^\nu}{d\lambda}\frac{dx^\sigma}{d\lambda} = 0
$$

Let us explain this equation in lay man's terms. Here $\lambda$ is called an affine parameter that 'plays the role of time' so that we can track the evolution of the coordinates. The $\Gamma$ terms are a set of very complicated functions that depend on the metric. I will show you how complicated they are later.

The equation then says that the second derivative of one coordinate is determined by the first derivatives of the other coordinates. Compare this to Newton's second law, we see that GR is a much more complicated theory.

Still, this a set of coupled second order differential equations. In principle, this is a problem that can be solved by a computer. However, several other pieces of information are needed to solve this equation, such as the initial position and energy of the photon. Such information is actually not within the scope of GR, but is determined by the accretion disk model that eventually boils down to atomic physics of the disk material.

## Slide 23

What comes next is technically all computation and zero physics. To simulate the look of a black hole, or really its accretion disk, we need to solve the geodesic equation for photons emitted by the disk. Simulating all of the photons emitted by the disk wastes a lot of resource, as not all of them will reach the observer. Instead, we trace photons backwards from the observer to the disk. If we are only interested in the shape of the image, we can imagine a uniform disk emitting photons of the same energy. The observer can be treated as a plane at a large distance away that is perpendicular to the vector pointing from the observer to the black hole. We then fire photons from different locations on the plane and see if they hit the disk. By collecting the photons that hit the disk, we can then form an image of the disk.

## Slide 24

But you ask what is the point of all this? Beside the coolness of simulating a literal black hole on your personal computer, there are a lot of scientific value in modelling space time and ray tracing photons. Instead of visualising the BH, we could generate a simulated spectrum of the photons and compare this with what we observe from telescopes. The shape of the spectrum is affected by the gravitational redshift, which ultimately depends on the parameters of the BH. The spectrum hence serves as a tool to measure the properties of the BH.

## Slide 25

We have undergone a journey that started with the simple Newton's laws and Euler methods and progressed all the way to simulating some of the most extreme objects in the universe. There are two key messages that unpin this journey. The first one, being the more philosophical, is that physical theories often share common features where similar mathematical structures are observed. The second one, being more practical, is the interplay between the power of computation and the power of human wisdom. While the computer can solve some of the immediate problems by brute force, ingenuity of us scientists is often what prevails in solving the most difficult problems. We have seen ChatGPTs excelling in casual conversation, but it scientific reasoning is still lackluster. Perhaps what we discussed today is a good example of how human wisdom is still essential, and it is certainly my hope that this will remain true for a long time to come.