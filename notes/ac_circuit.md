# Circuit Analysis

## Circuit Theorems

### Thevenin's Theorem

Any linear circuit with voltage sources and resistances can be replaced by an equivalent circuit consisting of a voltage source $V_{\text{eq}}$ in series with a resistance $R_{\text{eq}}$. To determine the equivalent voltage, replace the load with an open circuit and calculate the voltage across the load. To determine the equivalent resistance, replace the load with a short circuit and calculate the effective resistance in the circuit.

### Norton's Theorem

The above theorem can be replaced by a current source $I_{\text{eq}}$ in parallel with a resistance $R_{\text{eq}}$. The effective resistance is the same, and the equivalent current is given by $I_{\text{eq}} = V_{\text{eq}} / R_{\text{eq}}$.

## Sinusoidal Input

Consider the response of a series LRC circuit to a sinusoidal current input of the form $I(t) = I_{0} \cos{\omega t}$. The voltage drop across $R$ is simply $IR = I_{0}R \cos{\omega t}$. The voltage drop across $C$ is given by:

$$
V_{C} = \frac{1}{C} \int_{0}^{t} I \, \mathrm{d}t = \frac{I_{0}}{\omega C} \cos{(\omega t - \pi/2)}
$$

This shows that the voltage drop across the capacitor lags the input current by $\pi/2$.

For the inductor, the voltage drop is given by:

$$
V_{L} = L \frac{\mathrm{d}I}{\mathrm{d}t} = I_{0} \omega L \cos{(\omega t + \pi/2)}
$$

This shows that the voltage drop across the inductor leads the input current by $\pi/2$.

The cumbersomeness of adding the voltages in terms of trigonometric functions can be overcome by introducing the complex impedance. Define the complex impedance $Z$ in the form $Z = A e^{i\phi}$, such that the (complex) voltage drop across the component is $V = IZ$. Then:

$$
Z =
\begin{cases}
R \text{ for a resistor} \\
\frac{1}{\omega C} e^{-\pi/2} = \frac{1}{i\omega C} \text{ for a capacitor} \\
\omega L e^{\pi/2} = i \omega L \text{ for an inductor}
\end{cases}
$$

Then the generalised Ohm's law states that the complex voltage $\tilde{V}$ and the complex current $\tilde{I}$ are related by:

$$
\tilde{V} = \tilde{I} Z
$$

The actual current and the voltage are given by the real parts of their complex counterparts. For components in series or in parallel, their effective impedance is computed the same way as in the normal resistance:

$$
Z_{\text{series}} = \sum_{i} Z_{i}
$$

$$
\frac{1}{Z_{\text{parallel}}} = \sum_{i} \frac{1}{Z_{i}}
$$
