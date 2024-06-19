# Error Analysis

Experimental measurements have uncertainties associated with them. A measurement is almost worthless unless accompanied by an estimate of their validity. There are three main types of errors:

- Mistakes
- Random errors that affect precision
- Systematic errors that affect accuracy

## Random errors

Much of experimental physics is concerned with reducing the random errors in repeated measurements. Given a set of $N$ measurements $x_{1}, x_{2}, \dots, x_{N}$, the mean $\bar{x}$ of the sample is given by:

$$
\bar{x} = \frac{1}{N} \sum_{i = 1}^{N} x_{i}
$$

The sample variance $S^{2}$ is given by:

$$
S^{2} = \frac{1}{N} \sum_{i = 1}^{N} (x_{i} - \bar{x})^{2}
$$

The unbiased estimate of population variance $\sigma^{2}$ is given by:

$$
s^{2} = \frac{N}{N - 1} S^{2}
$$

The standard error on the mean $\alpha^{2}$ is defined as:

$$
\alpha^{2} = \frac{s^{2}}{N} = \frac{1}{N(N - 1)} \sum_{i = 1}^{N} (x_{i} - \bar{x})^{2}
$$

When making several repeated measurements and taking their mean, the precision with which this mean is known is given by $\sigma_{m}$.

## Error Propagation

The aim of most experiments in the physical sciences is to combine several variables into a single quantity. The error on the combined value is a function of the errors on the constituent terms.

Consider a single variable function $Z = f(A)$. If $A$ is measured to have a mean $\bar{A}$ and standard error $\alpha_{A}$, then the best estimate for $Z$ is $\bar{Z} = f(\bar{A})$. The error in $\bar{Z}$ is given by:

$$
\alpha_{Z} = \left\lvert f(\bar{A} + \alpha_{A}) - f(\bar{A}) \right\rvert
$$

Or written in the differential form:

$$
\alpha_{Z} = \left\lvert \frac{\mathrm{d}Z}{\mathrm{d}A} \right\rvert \alpha_{A}
$$

Next consider a multi variable function $Z = f(x_{1}, x_{2}, \dots, x_{n})$. The error in $\bar{Z}$ is given by:

$$
\alpha_{Z}^{2} = \sum_{i = 1}^{n} \left( \frac{\partial Z}{\partial x_{i}} \right)^{2} \alpha_{x_{i}}^{2}
$$
