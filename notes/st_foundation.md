# Statistical Mechanics - Foundation

Thermodynamics is about flows of energy:

$$
\mathrm{d}U = \delta Q - \delta W = T \mathrm{d}S - P \mathrm{d}V
$$

coupled with two further pieces of relations:

$$
\begin{split}
&\text{equation of state: } P = P(T, V) \\
&\text{energy: } U = U(T, V)
\end{split}
$$

The free energy $F(T, V)$ satisfies:

$$
\mathrm{d}F = -S \mathrm{d}T - P \mathrm{d}V
$$

Once $F$ is known, the equation of state $P(T, V)$ and the energy $U(T, V)$, along with other thermodynamic properties can be known. Therefore the formal programme is to seek an expression for $F(T, V)$ for systems in equilibrium.

## Systems and states

Any physical system is a quantum-mechanical one that can be in a number of quantum states called microstates, enumerated by $\alpha$:

$$
\alpha = 1, 2, 3, \dots, \Omega
$$

where the total number of possible microstates $\Omega$ is a huge number.

For each state $\alpha$, there is a certain probability $p_{\alpha}$ for the system to be in it:

$$
\sum_{\alpha = 1}^{\Omega} p_{\alpha} = 1
$$

Each state also has an energy $E_{\alpha}$ so that the mean energy of the system is:

$$
U = \langle E_{\alpha} \rangle = \sum_{\alpha = 1}^{\Omega} p_{\alpha} E_{\alpha}
$$

### Pressure

The concept of pressure is connected to changes in the system's volume, here called the external parameter $V$. In general the properties of the states of the system, e.g., $p_{\alpha}$ and $E_{\alpha}$, depend on $V$.

From quantum mechanics, if an external parameter is changed slowly in an otherwise isolated system, the system will stay in the same eigenstate with its energy changing slowly. This is called an adiabatic process. Since the system's microstates $\{\alpha\}$ do not change in an adiabatic process, neither do there probabilities $\{p_{\alpha}\}$. Therefore, we only consider change in the state energy $E_{\alpha}$ due to a change in volume $V$.

Keeping the probabilities constant, the change in the mean energy due to a change in volume is:

$$
\mathrm{d}U = \left(\frac{\partial U}{\partial V} \right)_{p_{\alpha}} \mathrm{d}V = \sum_{\alpha} p_{\alpha} \frac{\partial E_{\alpha}}{\partial V} \, \mathrm{d}V
$$

However, a change of energy in a system due exclusively to a change in volume can be related to the work done on the system:

$$
\mathrm{d}U = -P \mathrm{d}V
$$

Hence, the external parameter called pressure can be defined as:

$$
P \equiv -\sum_{\alpha} p_{\alpha} \frac{\partial E_{\alpha}}{\partial V} = - \left\langle \frac{\partial E_{\alpha}}{\partial V} \right\rangle
$$

In fact, if $\{p_{\alpha}\}$ and $\{E_{\alpha}\}$ are known, any external parameters can be derived. However, determining $\{E_{\alpha}\}$ is in general a difficult quantum mechanical problem that involves knowing the exact microscropic structure of the system.

## Principle of Maximum Entropy

If nothing is known about the system in interest, then the **equal a priori probabilities postulate** states that probabilities of microstates should be assumed to be all equal:

$$
p_{\alpha} = \frac{1}{\Omega}
$$

However, typically there is information already known about the system, e.g., the mean energy $U$. An algorithm must be constructed to assign values to $\{p_{\alpha}\}$ ('a distribution'), subject to $\sum_{\alpha}p_{\alpha} = 1$ and taking into consideration the known information as constraints, such that the 'uncertainty' of the system is maximised.

Therefore, given a distribution $\{p_{\alpha}\}$, we seek a function $H(p_{1}, \dots, p_{\Omega})$ that would measure the uncertainty associated with this distribution. A suitable $H$ should satisfy certain basic properties:

1. $H$ should be a continuous function of $p_{\alpha}$;
2. $H$ should not change if the order of listing of $p_{\alpha}$ is changed;
3. for any set of $\{p_{\alpha}\}$ that are not all equal, $H(p_{1}, \dots, p_{\Omega}) < H (1/\Omega, \dots, 1/\Omega) \equiv H_{\Omega}$ (the distribution with equal probabilities corresponds to maximum uncertainty);
4. if $\Omega' > \Omega$, $H_{\Omega'} > H_{\Omega}$ (more equiprobable microstates lead to more uncertainty);
5. H should be additive and independent of how the microstates are counted.

Under these conditions, it can be proven that the only suitable function takes the form:

$$
H(p_{1}, \dots, p_{\Omega}) = -k \sum_{\alpha} p_{\alpha} \ln{p_{\alpha}}
$$

for some real constant $k > 0$. Choosing $k = 1$ yields the Gibbs entropy $S_{G}$:

$$
\boxed{
S_{G} \equiv - \sum_{\alpha} p_{\alpha} \ln{p_{\alpha}}
}
$$

Choosing $k = k_{B}$ gives the conventional thermodynamic entropy $S$:

$$
\boxed{
S \equiv - k_{B} \sum_{\alpha} p_{\alpha} \ln{p_{\alpha}}
}
$$

## Canonical Distribution

A typical physical constraint on a system is a constant mean energy $U$:

$$
\sum_{\alpha} p_{\alpha} E_{\alpha} = U
$$

We seek a set of probabilities $\{p_{\alpha}\}$ that maximises $S_{G}(p_{1}, \dots, p_{\Omega})$ given the conditions $\sum_{\alpha}p_{\alpha} = 1$ and $\sum_{\alpha}p_{\alpha} E_{\alpha} = U$. Using the technique of Lagrange multipliers, it can be shown that $p_{\alpha}$ follows the Gibbs (canonical) distribution given by:

$$
\boxed{
p_{\alpha} = \frac{e^{-\beta E_{\alpha}}}{Z(\beta)}
}
$$

where the partition function $Z$ is the normalisation constant defined by:

$$
\boxed{
Z(\beta) \equiv \sum_{\alpha} e^{-\beta E_{\alpha}}
}
$$

and $\beta$ is determined by the equation:

$$
\boxed{
-\frac{\partial \ln{Z}}{\partial \beta} = U
}
$$

Now the Gibbs entropy can be rewritten using the Gibbs distribution:

$$
S_{G} = - \sum_{\alpha} p_{\alpha} \ln{p_{\alpha}} = - \sum_{\alpha} p_{\alpha} (-\beta E_{\alpha} - \ln{Z}) = \beta U + \ln{Z}
$$

Then:

$$
\begin{split}
\mathrm{d}S_{G} &= \beta \mathrm{d}U + U \mathrm{d}\beta + \frac{\mathrm{d}Z}{Z} \\
                &= \beta \mathrm{d}U + U \mathrm{d}\beta + \sum_{\alpha} \frac{e^{-\beta E_{\alpha}}}{Z}(-\beta \mathrm{d}E_{\alpha} - E_{\alpha} \mathrm{d}\beta) \\
                &= \beta \left( \mathrm{d}U - \sum_{\alpha} p_{\alpha} \mathrm{d}E_{\alpha} \right)
\end{split}
$$

Holding the total number of particles $N$ constant, $E_{\alpha} = E_{\alpha}(V)$ so $\mathrm{d}E_{\alpha} = (\partial E_{\alpha}/\partial V) \mathrm{d}V$. Recalling the definition of pressure $P$:

$$
\mathrm{d}S_{G} = \beta(\mathrm{d}U + P \mathrm{d}V) = \beta \mathrm{d}Q_{\text{rev}}
$$

where $\mathrm{d}Q_{\text{rev}} = \mathrm{d}U + P \mathrm{d}V$ is the definition of reversible heat. Thus $S_{G}$ is clearly a function of state, and $\beta$ is found to be an integrating factor of heat in thermal equilibrium, i.e., Kelvin's definition of thermodynamic temperature:

$$
\beta = \frac{1}{k_{B}T}
$$

where $k_{B}$ is chosen to fit degrees Kelvin.

The conventional thermodynamic entropy $S$ is thus:

$$
S = k_{B} S_{G}
$$

and the fundamental equation of thermodynamics results:

$$
T \mathrm{d}S = \mathrm{d}U + P \mathrm{d}V
$$

Introducing the free energy $F = U - TS$, simplification using the above results leads to:

$$
\boxed{
F = -k_{B}T \ln{Z}
}
$$

where $Z = \sum_{\alpha} \exp{(-E_{\alpha}/k_{B}T)}$.

This implies that once the partition function $Z$ is known, everything about the equilibrium thermodynamics of the system is known, since we can calculate the relevant thermodynamic quantities according to:

$$
\begin{split}
P &= - \left( \frac{\partial F}{\partial V} \right)_{T} \\
U &= F + TS \\
S &= - \left( \frac{\partial F}{\partial T} \right)_{V}
\end{split}
$$

## Grand Canonical Distribution

In the aforementioned derivation of the canonical distribution, the information already known (measured) about the system is the mean energy $U$. However, the system could well depend on other parameters such as the total volume $V$ and the number of particles $N$. Consider the case where $N$ is now a measurable mean quantity rather than a fixed external parameter. Suppose that each microstate $\alpha$ has a certain energy $E_{\alpha}$ and a certain number $N_{\alpha}$ of particles associated with it. The known information about the system (the constraints) is:

$$
\begin{split}
&\sum_{\alpha} p_{\alpha} = 1 \\
&\sum_{\alpha} p_{\alpha} E_{\alpha} = U \\
&\sum_{\alpha} p_{\alpha} N_{\alpha} = \bar{N}
\end{split}
$$

Maximisation of the Gibbs entropy $S_{G}$ under these constraints lead to the grand canonical distribution:

$$
\boxed{
p_{\alpha} = \frac{e^{-\beta(E_{\alpha} - \mu N_{\alpha})}}{\mathcal{Z}(\beta, \mu)}
}
$$

where the grand partition function $\mathcal{Z}$ is defined by:

$$
\boxed{
\mathcal{Z}(\beta, \mu) \equiv \sum_{\alpha} e^{-\beta(E_{\alpha} - \mu N_{\alpha})}
}
$$

where $\beta$ and $\mu$ are determined by the equalities:

$$
\boxed{
\begin{split}
&\bar{N} = \frac{1}{\beta} \frac{\partial \ln{\mathcal{Z}}}{\partial \mu} \\
&U = -\frac{\partial \ln{\mathcal{Z}}}{\partial \beta} + \mu \bar{N}
\end{split}
}
$$

Then in terms of the grand canonical distribution, the Gibbs entropy can be rewritten as:

$$
S_{G} = \beta(U - \mu \bar{N}) + \ln{\mathcal{Z}}
$$

Taking the total differential with $\mathrm{d}N_{\alpha} = 0$ (varying the single external parameter $V$):

$$
\begin{split}
\mathrm{d}S_{G} &= \beta(\mathrm{d}U - \bar{N} \mathrm{d}\mu - \mu \mathrm{d}\bar{N}) + (U - \mu \bar{N})\mathrm{d}\beta + \frac{\mathrm{d}\mathcal{Z}}{\mathcal{Z}} \\
                &= \beta \left( \mathrm{d}U - \mu \mathrm{d}\bar{N} - \sum_{\alpha} p_{\alpha} \mathrm{d}E_{\alpha} \right) \\
                &= \beta (\mathrm{d}U + P \mathrm{d}V - \mu \mathrm{d}\bar{N}) = \beta \mathrm{d}Q_{\text{rev}}
\end{split}
$$

The identification of $\beta \mathrm{d}Q_{\text{rev}}$ has to be made so as to keep the correspondence between $S_{G}$ and the thermodynamic entropy $S$, as well as that between $\beta$ and the thermodynamic temperature. This implies that $-\mu$ represents the amount of heat generated during a reversible process where $U$ and $V$ are constant but $\bar{N}$ changes:

$$
\mu = -T \left( \frac{\partial S}{\partial \bar{N}} \right)_{U, V}
$$

Therefore, the fundamental equation of thermodynamics of open systems results:

$$
\boxed{
\mathrm{d}U = T \mathrm{d}S - P \mathrm{d}V + \mu \mathrm{d}\bar{N}
}
$$

This highlights another interpretation of the chemical potential $\mu$:

$$
\mu = \left( \frac{\partial U}{\partial \bar{N}} \right)_{S, V}
$$

which we interpret as the energy cost of adding a particle to a system at constant volume and entropy.

Introducing the **grand potential** $\Phi$, a similar concept to the free energy $F$:

$$
\boxed{
\Phi = -k_{B}T \ln{\mathcal{Z}} = U - TS - \mu \bar{N} = F - \mu \bar{N}
}
$$

Its differential is:

$$
\mathrm{d}\Phi = -S \mathrm{d}T - P \mathrm{d}V - \bar{N} \mathrm{d}\mu
$$

which means that all thermodynamic properties of the system can be derived from $\Phi$:

$$
\begin{split}
S &= - \left( \frac{\partial \Phi}{\partial T} \right)_{V, \bar{N}} \\
P &= - \left( \frac{\partial \Phi}{\partial V} \right)_{T, \bar{N}} \\
\bar{N} &= - \left( \frac{\partial \Phi}{\partial \mu} \right)_{T, V} \\
U &= \Phi + TS + \mu \bar{N}
\end{split}
$$

### Other Thermodynamic Potentials

We can write the free energy $F$ explicitly:

$$
\mathrm{d}F = -S \mathrm{d}T - P \mathrm{d}V + \mu \mathrm{d}\bar{N}
$$

so that:

$$
\mu = \left( \frac{\partial F}{\partial \bar{N}} \right)_{T, V}
$$

By the same token, the Gibbs free energy $G$ is:

$$
\mathrm{d}G = -S \mathrm{d}T + V \mathrm{d}P + \mu \mathrm{d}\bar{N}
$$

so that:

$$
\mu = \left( \frac{\partial G}{\partial \bar{N}} \right)_{T, P}
$$

However, consider the fact that $G(T, P, \bar{N})$ is a function of two intensive variables $T$ and $P$, and one extensive variable $\bar{N}$. Suppose that we scale the system such that $\bar{N} \to \lambda \bar{N}$ while $T$ and $P$ are not affected. Then, we expect $G$ to scale as $G \to \lambda G$:

$$
G(T, P, \lambda \bar{N}) = \lambda G(T, P, \bar{N})
$$

Differentiating both sides with respect to $\lambda$ and setting $\lambda = 1$:

$$
\bar{N} \left( \frac{\partial G}{\partial \bar{N}} \right)_{T, P} = G
$$

which means that we could just write:

$$
\boxed{
\mu = \frac{G}{\bar{N}}
}
$$

in place of the differential expression, indicating that the chemical potential is the Gibbs free energy per particle.

This also confirms that $\mu$ is an intensive variable:

$$
\mu(T, P, \lambda \bar{N}) = \mu(T, P, \bar{N})
$$

We could extend this argument to the grand potential $\Phi(T, V, \mu)$, which is also a function of two intensive variables $T$ and $V$, and one extensive variable $\mu$. Then we could derive a similar simplification:

$$
\boxed{
P = -\frac{\Phi}{V}
}
$$

which is a simpler equation of state compared to the differential form.
