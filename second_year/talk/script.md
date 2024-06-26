# Slide by Slide Script

\newpage

## Slide 1

Good afternoon everyone. Welcome to my talk, titled "From Newton's Laws to Modelling Black Holes". While my aim today is to show you how powerful numerical methods can be, I would like to start with a more philosophical question.

\newpage

## Slide 2

What do you think is the greatest achievement of science? People may say its mechanics, quantum physics. But in my opinion, the single most important result from science is that science has bestowed upon us the ability to predict the future.

\newpage

## Slide 3

Consideration of the future is a very human trait. We as a species worries about survival. Individual members worry about their own future, their job prospects, health, and whether they can graduate. We humans are so mesmerised by the idea of looking beyond the present, that we have developed a whole field of science to theorise how our physical world evolves.

This is especially true in mechanics, where Newton's laws dictate the evolution of all physical systems, at least within the realm of classical mechanics. While the laws have the beauty of simplicity, extracting information from them is an involved process. This is where numerical methods come in.

\newpage

## Slide 4

In this talk, let us embark on a journey that starts with classical mechanics and the art of solving differential equations. We will see how the study of everyday objects can enable us to model some of the most exotic heavenly objects in the universe. Finally, I will demonstrate how our discussion today can be applied to study some of the most extreme phenomena in the universe. Before that, let us start from Newton's laws.

\newpage

## Slide 5

Here I give you a quote from the renowned physicists Laudau and Lifshitz in their mechanics book.

Let us consider the significance of this statement. It is saying that, within classical mechanics, our universe evolves in such a way that we only need to know the position and velocity of an object at **some time**, and we would in principle be able to determine its complete past, present, and future. This is a very powerful statement, as it allows us to not only predict the future, but also to understand the past.

\newpage

## Slide 6

What is the 'principle' we are talking about? Newton's laws of motion. Let us think of $F = ma$. Apart from some philosophical interpretations, such as what force and mass are, this equation tells us how an object moves given some other information.

\newpage

## Slide 7

Let us consider a very simple example.

Imagine a rocket moving through space under the influence of gravity. Its motion is determined by the vector containing its position and velocity. In a very small time interval, the rocket will update its position via its current velocity $\delta x = v\delta t$. It will also update its velocity via the force acting on it $\delta v = F\delta t/m$. This force, of course, is a function of the current position.

\newpage

## Slide 8

This is the idea of the Euler method. I put here a picture of Euler for fun. This is perhaps the simplest method that every physics student learns. It is simple, but it is not very accurate.

\newpage

## Slide 9

To see how Euler's method is flawed, consider the following equation. We know the theoretical solution, which is just an exponential decay. Let us see how Euler's method performs.

\newpage

## Slide 10

Here I have used Python to simulate the solutions with different step sizes. The red line shows the actual solution.

Unsurprisingly, choosing $dt = 0.01$ gives us the best solution that closely follows the theoretical one. If we increase the step size however, the solution gets very funky.

If we choose a step size of $1/8$, the computed solution becomes very oscillatory. This is because the error of the Euler method is of the order of the step size, which is often too large for practical purposes. Therefore we run into the problem of overshooting at every step, and the result is a mess.

\newpage

## Slide 11

We see that the naive Euler method has two contradicting drawbacks: It is very inaccurate when the step size is large, but becomes very slow if step size is small. We can improve on both of these by using the Runge-Kutta methods coupled with adaptive step size. I will now explain them in detail.

\newpage

## Slide 12

A apparent flaw of Euler's method is that it is in some way too 'naive' or too 'local'. An immediate improvement is to go forward one step and see what the force is there, and then use the average of the next force and the current force. Simply doing this yields a good improvement to the accuracy.

\newpage

## Slide 13

We can 'scout' ahead even further and use an weighted average of the forces at each step. By adjusting carefully the weights of the forces, we can get a fourth order method called the Runge-Kutta 4 method. Here I also include a picture of Runge, who was a German mathematician.

\newpage

## Slide 14

Another problem of the method is that it is too 'dumb' because it only knows a fixed step size. This is very inefficient. For example, consider this extreme potential.

At large distances, the potential is almost uniform so the force does not vary a lot. This is when we want to increase our step size. When the potential (and thus the force) varies a lot, we better use a small step size to capture the features of the force.

Therefore, using a fixed step size is dumb in two ways: it is too slow when the force is smooth, and too inaccurate when the force is not smooth. We should therefore consider how we should change the step size at each iteration.

\newpage

## Slide 15

To implement an algorithm, we would need a criterion, often an error estimate, to determine when to change the step size by how much. In practice, when using the 4th order Runge-Kutta method, we can use the difference between the 4th order and 5th order Runge-Kutta methods as an error estimate. This is a very good estimate, as the 5th order method is very accurate. There are a variety of other methods to estimate the error, but the idea is the same. Then, at each step, if the error is too large, we decrease the step size and redo the step. If the error is too small, we increase the step size.

\newpage

## Slide 16

I promised at the start that the methods we have just discussed can be applied to exotic heavenly objects, such as black holes. To apply our knowledge, we will have to simulate how photons move around BHs. But before we jump into calculation, let us first understand what a black hole is.

\newpage

## Slide 17

A black hole can be thought of as a body with such extreme mass and spacetime deformation around it that not even light can escape from it.
The idea of a black hole was proposed in the 18th century by the British scientist John Michell. But it was not until a century later that the idea was taken seriously by the scientific community. Einstein's groundbreaking theory of General Relativity (GR) did not immediately predict black holes. Karl Schwarzschild found the first exact solution to the Einstein's field equations and from the solution, the concept of a black hole naturally emerged.

\newpage

## Slide 18

A black hole in GR really is just a spherical object with an extreme amount of mass. They are very simple objects in the sense that they are completely characterised by just three parameters: mass, charge, and angular momentum. Charge of a black hole is usually zero since the universe is electrically neutral.

\newpage

## Slide 19

Going back to our central theme, the natural question to ask is: how do we model the motion of photons around a black hole? The answer is the geodesic equation. This is a generalisation of Newton's second law to curved spacetime.

$$
\frac{d^2x^\alpha}{d\lambda^2} + \Gamma^{\alpha}_{\beta\gamma}\frac{dx^\beta}{d\lambda}\frac{dx^\gamma}{d\lambda} = 0
$$

Let us explain this equation in lay man's terms. Here $\lambda$ is called an affine parameter that 'plays the role of time' so that we can track the evolution of the coordinates. The $\Gamma$ terms are a set of very complicated functions that depend on the the local curvature of spacetime.

The equation then says that the second derivative of one coordinate is determined by the first derivatives of the other coordinates. Compare this to Newton's second law, we see that GR is a much more complicated theory.

Still, this a set of coupled second order differential equations. In principle, this is a problem that can be solved by a computer.

\newpage

## Slide 20

What comes next is technically all computation and zero physics. To simulate the look of a black hole, or really its accretion disk, we need to solve the geodesic equation for photons emitted by the disk.

Simulating all of the photons emitted by the disk wastes a lot of resource, as not all of them will reach the observer. Instead, we trace photons backwards from the observer to the disk.

If we are only interested in the shape of the image, we can imagine a uniform disk emitting photons of the same energy. The observer can be treated as a plane at a large distance away. We then fire photons from different locations on the plane and see if they hit the disk. By collecting the photons that hit the disk, we can then form an image of the disk.

Here, I used C++ to simulate the look of a black hole with a high spin at a low inclination angle. The spin of the black hole leads to a asymmetry in the image. Just to show you how computationally expensive this is, this simulation took 20 minutes on my personal computer with some fairly optimised code.

\newpage

## Slide 21

But you ask what is the point of all this? Beside the coolness of simulating a literal black hole on your personal computer, there are a lot of scientific value in modelling space time and ray tracing photons. Instead of visualising the BH, we could generate a simulated spectrum of the photons and compare this with what we observe from telescopes. The shape of the spectrum is affected by the gravitational redshift, which ultimately depends on the parameters of the BH. The spectrum hence serves as a tool to measure the properties of the BH.

Before we have powerful enough telescopes to directly image a BH, this is probably the best we can do to understand directly the properties of a BH.

\newpage

## Slide 22

We have undergone a journey that started with the simple Newton's laws and Euler methods and progressed all the way to simulating some of the most extreme objects in the universe. Beyond the details of my talk, I hope you can take away two important points.

\newpage

## Slide 23

The first one is that physical theories often share common features where similar mathematical structures are observed. We have seen how ODEs apply to all sorts of physical systems, and how the same numerical methods can be used to simulate vastly different objects. However, numerical simulation does not necessarily imply understanding of the science. The interplay between the two is what makes physics so fascinating.

\newpage

## Slide 24

The second one, is the dynamics between the power of computation and the power of human wisdom. While the computer can solve some of the immediate problems by brute force, ingenuity of us scientists is often what prevails in solving the most difficult problems. While Euler's method can be used to solve some problem with enough computational power, it certainly would not suffice to solve the problem of simulating a black hole. For that, we need to use our wisdom to develop more sophisticated methods that outperform the naive ones in the long run.

In recent years, we have seen ChatGPTs excelling in casual conversation, but it scientific reasoning is still lacklustre. Perhaps what we discussed today is a good example of how human wisdom is still essential, and it is certainly my hope that this will remain true for a long time to come.
