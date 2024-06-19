# Fourier Analysis

## Fourier Series

Sine and cosine functions can be used to express and decompose a complicated function. Suppose that a function $f(x)$ has a period of $L$. We wish to use a sum of sines and cosines of the same period to express the function. Naturally, $\sin{\frac{2 \pi k x}{L}}$ and $\cos{\frac{2 \pi k x}{L}}$ have the same period for any positive integer $k$. Thus we suppose:

$$
\boxed{
f(x) = \frac{a_0}{2} + \sum^{\infty}_{r=1} a_r \cos{\frac{2 \pi r x}{L}} + \sum^{\infty}_{r=1} b_r \sin{\frac{2 \pi r x}{L}}
}
$$

To obtain the coefficients $a_r$ and $b_r$, multiply both sides by $\cos{\frac{2 \pi p x}{L}}$ where $p$ is an arbitrary positive integer, then integrate over one full period. Then:

$$
\begin{split}
\int_{0}^{L} f(x) \cos{\frac{2 \pi p x}{L}} \, \mathrm{d}x = &\frac{a_0}{2} \int_{0}^{L} \cos{\frac{2 \pi p x}{L}} \, \mathrm{d}x \\
&+ \sum^{\infty}_{r=1} a_r \int_{0}^{L} \cos{\frac{2 \pi n x}{L}} \cos{\frac{2 \pi p x}{L}} \, \mathrm{d}x \\
&+ \sum^{\infty}_{r=1} b_r \int_{0}^{L} \sin{\frac{2 \pi n x}{L}} \cos{\frac{2 \pi p x}{L}} \, \mathrm{d}x
\end{split}
$$

Now let $p$ take different values to obtain the coefficients. For $p=0$:

$$
\int_{0}^{L} f(x) \, \mathrm{d}x = \frac{a_0}{2} L
$$

For any $p \ne 0$, the only term that does not vanish occurs when $r = p$ so that:

$$
\int_{0}^{L} f(x) \cos{\frac{2 \pi r x}{L}} \, \mathrm{d}x = \frac{a_r}{2} L
$$

Similarly for $b_r$, multiply both sides by $\sin{\frac{2 \pi p x}{L}}$ to yield:

$$
\int_{0}^{L} f(x) \sin{\frac{2 \pi r x}{L}} \, \mathrm{d}x = \frac{b_r}{2} L
$$

Hence:

$$
\boxed{
\begin{split}
a_r = \frac{2}{L} \int_{0}^{L} f(x) \cos{\frac{2 \pi r x}{L}} \, \mathrm{d}x \\
b_r = \frac{2}{L} \int_{0}^{L} f(x) \sin{\frac{2 \pi r x}{L}} \, \mathrm{d}x
\end{split}
}
$$

Note that for an odd function $f(x)$, the coefficients $a_r$ for the cosines (which are even) must be zero; conversely for an even function, the coefficients $b_r$ for the sines are zero.

Intuitively we can use exponential functions to replace the sines and cosines. Without loss of generality, we write:

$$
\boxed{
f(x) = \frac{1}{\sqrt{2\pi}} \sum^{+\infty}_{r = -\infty} c_r \exp(i\frac{ 2\pi r x}{L})
}
$$

The coefficients can be obtained by similar usage of orthogonality relations, leading to:

$$
c_r = \frac{\sqrt{2\pi}}{L} \int_{0}^{L} f(x) \exp(-\frac{2 \pi i r x}{L}) \, \mathrm{d}x
$$

Note that the integration can in fact start from any value of $x$ as long as the interval is of length $L$.

## Fourier Transform

We may wish to extend this sinusoidal representation of functions to an infinite interval to accommodate non-periodic functions. We can first rewrite the complex form of Fourier series using the substitution $k_r = 2\pi r/L$:

$$
f(x) = \frac{1}{\sqrt{2\pi}} \sum_{r = -\infty}^{\infty} c_r e^{i k_r x}
$$

The incremental change $\Delta k \equiv k_{r+1} - k_{r} = 2\pi/L$ in frequencies becomes increasingly small as the period tends to infinity. This motivates the usage of an integral. Note that the coefficients $c_r$ are given by:

$$
c_r = \frac{\sqrt{2\pi}}{L} \int_{-L/2}^{L/2} f(x) \exp(-\frac{2 \pi i r x}{L}) \, \mathrm{d}x = \frac{\Delta k}{\sqrt{2\pi}} \int_{-L/2}^{L/2} f(x) e^{-i k_r x} \, \mathrm{d}x
$$

Let us define a function $F(k)$ as:

$$
F(k) \equiv \frac{1}{\Delta k} c_r = \frac{1}{\sqrt{2\pi}} \int_{-L/2}^{L/2} f(x) e^{-i k x} \, \mathrm{d}x
$$

so that the original function can be expressed as:

$$
f(x) = \frac{1}{\sqrt{2\pi}} \sum_{k = -\infty}^{\infty} F(k) e^{i k x} \Delta k
$$

In the limit $L \rightarrow \infty$, $\Delta k \rightarrow 0$ and the summation becomes an integral. We can hence define the Fourier transform of $f(x)$ as:

$$
\boxed{
F[f](k) \equiv \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} f(x) e^{-i k x} \, \mathrm{d}x
}
$$

coupled with the inverse transform:

$$
\boxed{
F^{-1}[g](x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} g(k) e^{i k x} \mathrm{d}k
}
$$

Note that by construction, the inverse transform of a $F(k) = F[f](k)$ is the original function $f(x)$.

Consider for example the Fourier transform of a delta function $\delta(x)$:

$$
\begin{split}
\Delta(k) &= \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \delta(x) e^{-i k x} \, \mathrm{d}x \\
&= \frac{1}{\sqrt{2\pi}}
\end{split}
$$

where we have made use of the sampling property of the delta function.

This implies that the Fourier transform of a constant function is a delta function (up to a constant factor):

$$
\begin{split}
F[C](k) &= \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} C e^{-i k x} \, \mathrm{d}x \\
&= C \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{i k x} \, \mathrm{d}x \\
&= C F^{-1}[\Delta(k)](x) \\
&= C \delta(x)
\end{split}
$$

where the third line follows from the inverse transform of the delta function.

We can also work out the Fourier transforms of the sine and cosine functions:

$$
\begin{split}
F[\sin{(\omega x)}](k) &= \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \frac{e^{i\omega x} - e^{-i\omega x}}{2i} e^{-i k x} \, \mathrm{d}x \\
&= \frac{1}{2i\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{i(\omega - k)x} - e^{-i(\omega + k)x} \, \mathrm{d}x \\
&= \frac{1}{2i} \left[ \delta(\omega - k) - \delta(\omega + k) \right]
\end{split}
$$

and for the cosine function:

$$
\begin{split}
F[\cos{(\omega x)}](k) &= \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \frac{e^{i\omega x} + e^{-i\omega x}}{2} e^{-i k x} \, \mathrm{d}x \\
&= \frac{1}{2\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{i(\omega - k)x} + e^{-i(\omega + k)x} \, \mathrm{d}x \\
&= \frac{1}{2} \left[ \delta(\omega - k) + \delta(\omega + k) \right]
\end{split}
$$
