# Linear Algebra Summary

- [Index Notation](#index-notation)
- [Vector Spaces](#vector-spaces)
- [Linear Maps](#linear-maps)
- [Change of Basis](#change-of-basis)
- [Scalar Product](#scalar-product)
    - [Adjoint Map](#adjoint-map)
    - [Orthogonal and Unitary Maps](#orthogonal-and-unitary-maps)
- [Determinants](#determinants)
- [Rotation Matrices](#rotation-matrices)

## Index Notation

Given a set of orthonormal basis vectors $e_{i}$, any vector can be expressed as a linear combination of them:

$$
\mathbf{a} = \sum_{i = 1}^{n} \alpha_{i} \mathbf{e}_{i}
$$

The Einstein summation convention says that if any index is repeated once, then a sum is performed over this index, effectively removing the need for the summation sign.

The dot product between two vectors can be expressed as:

$$
\mathbf{a} \cdot \mathbf{b} = \delta_{ij} a_{i} b_{j}
$$

The components of the cross product between two vectors can be expressed as:

$$
(\mathbf{a} \times \mathbf{b})_{i} = \epsilon_{ijk}a_{j}b_{k}
$$

A triple product of vectors $\mathbf{a}$, $\mathbf{b}$ and $\mathbf{c}$ is given by:

$$
\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c})
$$

Note that the triple product is invariant under cyclic permutation:

$$
\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c}) = \mathbf{b} \cdot (\mathbf{c} \times \mathbf{a}) = \mathbf{c} \cdot (\mathbf{a} \times \mathbf{b})
$$

Further note **an important identity**:

$$
\epsilon_{ijk} \epsilon_{imn} = \delta_{jm} \delta_{kn} - \delta_{jn} \delta_{km}
$$

A $n \times m$ matrix can be similarly defined using the summation convention:

$$
A \equiv \sum_{i, j = 1}^{n, m} A_{ij}
$$

The matrix product between two matrices $A$ and $B$ is:

$$
(AB)_{ij} = A_{ik} B_{kj}
$$

## Vector Spaces

Formally, a vector space consists of a set $V$ of elements called vectors, a field $\mathbb{F}$ and two operations vector addition $+$ and scalar multiplication $\cdot$.

A non-empty subset $W \sub V$ is a vector (sub)space if for all $\mathbf{w}_{1}, \mathbf{w}_{2} \in W$, we have $\alpha \mathbf{w}_{1} + \beta \mathbf{w}_{2} \in W$ for $\alpha, \beta \in \mathbb{F}$.

The span of a set of vectors $\mathbf{v}_{i} \in V$ is the set of all linear combinations of these vectors:

$$
\text{span}(\mathbf{v}_{i}) \equiv \left\{ \sum_{i = 1}^{n} \alpha_{i} \mathbf{v}_{i} \right\}
$$

A set of vectors $\mathbf{v}_{i} \in V$ are called linearly independent if the equation:

$$
\sum_{i = 1}^{n} \alpha_{i} \mathbf{v}_{i} = \mathbf{0}
$$

only has the trivial solution $\alpha_{i} = 0$ for all $i$.

The set of vectors is called a basis of $V$ if it is linearly independent and spans $V$. While the particular choice of basis is arbitrary, the number of vectors in the basis is unique and is called the **dimension** of $V$.

It can be deduced that for any set of vectors $\mathbf{w}_{i}$ for $i = 1, \dots, k$, the set does not span $V$ if $k < \dim{V}$ and is linearly dependent if $k > \dim{V}$. If $k =\dim{V}$ and the set is linearly independent, then it must be a basis of $V$.

## Linear Maps

A map $f: V \to W$ is called a linear map if for all $\mathbf{v}_{1}, \mathbf{v}_{2} \in V$ and $\alpha, \beta \in \mathbb{F}$, we have:

$$
f(\alpha \mathbf{v}_{1} + \beta \mathbf{v}_{2}) = \alpha f(\mathbf{v}_{1}) + \beta f(\mathbf{v}_{2})
$$

Let $f$ act on the basis $\mathbf{v}_{j}$ of $V$ and represent the resulting vector in terms of the basis $\mathbf{w}_{i}$ of $W$:

$$
f(\mathbf{v}_{j}) = \sum_{i = 1}^{n} A_{ij} \mathbf{w}_{i}
$$

For a general vector $\mathbf{v} = \sum v_{j}\mathbf{v}_{j} \in V$, $f(\mathbf{v})$ can be written as a linear combination of the basis $\mathbf{w}_{i}$ of $W$. We can thus write:

$$
f(\mathbf{v}) = \sum_{i = 1}^{m} \sum_{j = 1}^{n} A_{ij} v_{j} \mathbf{w}_{i} = \sum_{i = 1}^{n} w_{i} \mathbf{w}_{i}
$$

This implies that a linear map can be represented by a matrix $A$ with $m$ rows and $n$ columns, whose elements are $A_{ij}$. The matrix $A$ is called the **representation matrix** of $f$. Note that to determine the jth of $A$, simply work out the action of $f$ on the basis $\mathbf{v}_{j}$ of $V$.

The kernel of a linear map $f: V \to W$ is the set of vectors $\mathbf{v} \in V$ such that $f(\mathbf{v}) = \mathbf{0}$. The dimension of the kernel is called the **nullity** of $f$. The rank of $f$ is the dimension of the image of $f$, i.e., the dimension of $W$. The **rank-nullity theorem** states that the rank of $f$ plus the nullity of $f$ is the dimension of $V$:

$$
\text{rank}(f) + \text{null}(f) = \dim{V}
$$

## Change of Basis

Let $A$ be the representation matrix of a linear map $f: V \to W$ relative to a choice of bases $\mathbf{v}_{i}$ and $\mathbf{w}_{i}$. Let these bases have the coordinate maps $\phi$ and $\psi$ respectively. The matrix representation can be written as:

$$
A = \psi^{-1} \cdot f \cdot \phi
$$

Suppose now that we have another choice of bases $\mathbf{v}'_{i}$ and $\mathbf{w}'_{i}$ with a new set of coordinate maps $\phi'$ and $\psi'$ respectively. The new representation matrix $A'$ of the same linear map is:

$$
A' = \psi'^{-1} \cdot A \cdot \phi' = \psi'^{-1} \cdot \psi \cdot \psi^{-1} \cdot A \cdot \phi \cdot \phi^{-1} \cdot \phi' = QAP^{-1}
$$

where $Q \equiv \psi'^{-1} \cdot \psi$ and $P \equiv \phi'^{-1} \cdot \phi$ transform coordinate vectors from the old bases to the new ones:

$$
\mathbf{\alpha}' = P \mathbf{\alpha}, \quad \mathbf{\beta}' = Q \mathbf{\beta}
$$

provided that $\phi(\mathbf{\alpha}) = \phi'(\mathbf{\alpha}') \in V$ and $\psi(\mathbf{\beta}) = \psi'(\mathbf{\beta}') \in W$.

To determine the elements of $P$, consider the equation $P \mathbf{e}_{j} = (\phi'^{-1} \cdot \phi) \mathbf{e}_{j} = \sum_{i} P_{ij} \mathbf{e}_{i}$ where $\mathbf{e}_{j}$ is the jth standard basis vector. Applying $\phi'$ to both sides, we get:

$$
\mathbf{v}_{j} = \sum_{i} P_{ij} \mathbf{v}_{i}'
$$

Conversely, we have the inverse relation:

$$
\mathbf{v}_{j}' = \sum_{i} (P^{-1})_{ij} \mathbf{v}_{i}
$$

Elements of Q are determined similarly.

In the particular case where the domain is the same as codomain, $f: V \to V$, $P = Q$ and $A' = PAP^{-1}$, where $\mathbf{v}_{j} = \sum_{i} P_{ij} \mathbf{v}_{i}'$.

In the even more special case where the old basis the standard basis $\mathbf{e}_{i}$, matrix $A$ is the one canonically associated with the linear map $f$. Then we have:

$$
\mathbf{v}_{j}' = \sum_{i} (P^{-1})_{ij} \mathbf{e}_{i}
$$

so that the new basis $\mathbf{v}_{j}'$ just form the columns of $P^{-1}$:

$$
P^{-1} = (\mathbf{v}_{1}', \dots, \mathbf{v}_{n}')
$$

## Scalar Product

A real (hermitian) scalar product on a vector space $V$ over $\mathbb{F} = \mathbb{R}$ ($\mathbb{F} = \mathbb{C}$) is a map $\left\langle \cdot, \cdot \right\rangle: V \times V \to \mathbb{F}$ satisfying:

- $\left\langle \mathbf{v}, \mathbf{w} \right\rangle = \left\langle \mathbf{w}, \mathbf{v} \right\rangle$ for a real scalar product and $\left\langle \mathbf{v}, \mathbf{w} \right\rangle = \left\langle \mathbf{w}, \mathbf{v} \right\rangle^{*}$ for a hermitian scalar product
- $\left\langle \mathbf{v}, \alpha \mathbf{u} + \beta \mathbf{w} \right\rangle = \alpha \left\langle \mathbf{v} , \mathbf{u} \right\rangle + \beta \left\langle \mathbf{v}, \mathbf{w} \right\rangle$
- $\left\langle \mathbf{v}, \mathbf{v} \right\rangle > 0$ if $\mathbf{v} \ne 0$

If the first argument of a hermitian scalar product is a linear combination, we have:

$$
\left\langle \alpha \mathbf{v} + \beta \mathbf{u}, \mathbf{w} \right\rangle = \left\langle \mathbf{w}, \alpha \mathbf{v} + \beta \mathbf{u} \right\rangle^{*} = \alpha^{*} \left\langle \mathbf{v}, \mathbf{w} \right\rangle + \beta^{*} \left\langle \mathbf{u}, \mathbf{w} \right\rangle
$$

Thus the first argument is linear only if $\alpha$ and $\beta$ are real.

The case for a real scalar product is similarly shown, and the first argument of a real scalar product is always linear.

Under a scalar product, the norm of a vector is defined as:

$$
\left\lvert \mathbf{v} \right\rvert = \left\langle \mathbf{v}, \mathbf{v} \right\rangle
$$

A set of vectors $\mathbf{v}_{i}$ is said to be orthogonal if $\left\langle \mathbf{v}_{i}, \mathbf{v}_{j} \right\rangle = k \delta_{ij}$ for some $k$. If $k$ equals zero for all pairs of vectors, then the vectors are said to be orthonormal.

The **Gram-Schmidt procedure** is a method to construct an orthonormal basis $\mathbf{\epsilon}_{i}$ from a given basis $\mathbf{v}_{i}$:

$$
\mathbf{\epsilon}_{i} = \frac{\mathbf{v}_{i}'}{\left\lvert \mathbf{v}_{i}' \right\rvert} \\
$$

where

$$
\mathbf{v}_{i}' = \mathbf{v}_{i} - \sum_{j=1}^{i-1} \left\langle \mathbf{v}_{i}, \mathbf{\epsilon}_{j} \right\rangle \mathbf{\epsilon}_{j}
$$

The usefulness of an orthonormal basis manifests in the following properties. To express a vector $\mathbf{v}$ in an orthonormal basis $\mathbf{\epsilon}_{i}$:

$$
\mathbf{v} = \sum_{i=1}^{n} \alpha_{i} \mathbf{\epsilon}_{i} = \sum_{i=1}^{n} \left\langle \mathbf{v}, \mathbf{\epsilon}_{i} \right\rangle \mathbf{\epsilon}_{i} \\
$$

Then the inner product of two vectors $\mathbf{v}$ and $\mathbf{u}$ can be expressed as:

$$
\left\langle \mathbf{v}, \mathbf{w} \right\rangle = \sum_{i=1}^{n} \left\langle \mathbf{v}, \mathbf{\epsilon}_{i} \right\rangle \left\langle \mathbf{\epsilon}_{i}, \mathbf{w} \right\rangle = \sum_{i=1}^{n} \alpha_{i}^{*} \beta_{i}
$$

Since the representing matrix $A$ of a linear map $f : V \to W$ is given by $f(\mathbf{v}_{j}) = \sum A_{ij} \mathbf{w}_{i}$, taking the inner product of both sides with $\mathbf{w}_{i}$ gives:

$$
A_{ij} = \left\langle \mathbf{w}_{i}, f(\mathbf{v}_{j}) \right\rangle
$$

For the special case of a linear map $f : V \to V$, the representing matrix can therefore be expressed as:

$$
A_{ij} = \left\langle \mathbf{e}_{i}, f(\mathbf{e}_{j}) \right\rangle
$$

### Adjoint Map

Given a linear map $f:V \to V$, the adjoint map $f^{\dagger}:V \to V$ is defined to satisfy:

$$
\left\langle f^{\dagger}(\mathbf{u}), \mathbf{v} \right\rangle = \left\langle \mathbf{u}, f(\mathbf{v}) \right\rangle
$$

Suppose that A is the representing matrix of a linear map $f:V \to V$. Let the adjoint map $f^{\dagger}$ be represented by the matrix $B$ such that:

$$
A_{ij} = \left\langle \mathbf{e}_{i}, f(\mathbf{e}_{j}) \right\rangle \quad B_{ij} = \left\langle \mathbf{e}_{i}, f^{\dagger}(\mathbf{e}_{j}) \right\rangle
$$

By definition of the adjoint map, we have $B_{ji}^{*} = A_{ij}$, that is, the matrix representing the adjoint map is the hermitian of the matrix representing the original map.

A Hermitian operator is a linear map that is self-adjoint, that is, $f^{\dagger} = f$ and the corresponding matrices satisfy $A^{\dagger} = A$.

### Orthogonal and Unitary Maps

An operator $f$ that satisfies:

$$
\left\langle f(\mathbf{u}), f(\mathbf{v}) \right\rangle = \left\langle \mathbf{u}, \mathbf{v} \right\rangle
$$

is called orthogonal if the scalar product is real, or unitary if the scalar product is hermitian.

A unitary map $f$ must satisfy $f f^{\dagger} = f^{\dagger} f = I$. The corresponding matrices satisfy $A A^{\dagger} = A^{\dagger} A = I$. An orthogonal map satisfies similar relations by replacing $A^{\dagger}$ with $A^{\intercal}$.

It can be deduced that $\left\lvert \det(A) \right\rvert = 1$. For an orthogonal map, if $\det(A) = 1$, then $A$ and $f$ represent a pure rotation; if $\det(A) = -1$, then $A$ and $f$ represent a rotation with a reflection.

Hermitian and unitary maps are also called normal maps satisfying the condition:

$$
\left[ f, f^{\dagger} \right] \equiv f f^{\dagger} - f^{\dagger} f = 0
$$

## Determinants

The determinant of a $n \times n$ matrix is defined as a mapping of the $n$ column vectors $\mathbf{A}^{i}$ to a scalar, denoted as $\det(\mathbf{A}^{1}, \dots, \mathbf{A}^{n})$, that is multilinear and alternating and satisfies the condition $\det(\mathbf{e}_{1}, \dots, \mathbf{e}_{n}) = 1$. This means that the determinant is linear in each of its argument and switching any two of its arguments changes its sign.

It can be shown that the function that satisfies these properties takes the form:

$$
\det(A) = \det(\mathbf{A}^{1}, \dots, \mathbf{A}^{n}) = \sum_{\sigma \in S_{n}} \operatorname{sgn}(\sigma) A_{\sigma(1) 1} \dots A_{\sigma(n) n}
$$

where $S_{n}$ is the set of all possible permutations of $\{ 1, 2, \dots, n \}$ and the sign function is defined as $\operatorname{sgn}(\sigma) = (-1)^{k}$ where $k$ is the number of transpositions (switching the elements).

Under this definition, the determinant can also be written as:

$$
\det(A) = \epsilon_{i_{1} \dots i_{n}} A_{i_{1} 1} \dots A_{i_{n}n}
$$

where the Levi-Civita tensor is defined as:

$$
\epsilon_{i_{1} \dots i_{n}} =
\begin{cases}
    +1 \text{ if } i_{1} \dots i_{n} \text{ is an even permutation of } 1 \dots n \\
    -1 \text{ if } i_{1} \dots i_{n} \text{ is an odd permutation of } 1 \dots n \\
    0 \text{ otherwise ,i.e., one or more of the indices are repeated}
\end{cases}
$$

The determinant of a matrix is closely linked to its trace. It can be easily proven that $\operatorname{tr}A = \operatorname{tr}(PAP^{-1})$ where $P$ is an invertible matrix. This shows that the trace of a matrix that represent a linear map is independent of the coordinate basis. Thus, define the trace of a linear map $f:V \to V$ as:

$$
\operatorname{tr}f \equiv \operatorname{tr}A
$$

where $A$ is a representation of $f$ in any basis.

## Rotation Matrices

A rotation matrix is a matrix $A$ that satisfies $\det{A} = 1$ and $A^{\intercal}A = I$. This represents the linear map that rotates a vector. In two-dimensional space, it can be shown that an anti-clockwise rotation measured from +x-axis can be represented by the matrix:

$$
R =
\begin{pmatrix}
\cos{\theta} & \sin{\theta} \\
-\sin{\theta} & \cos{\theta}
\end{pmatrix}
$$

where $\theta$ is the angle of rotation.

In three-dimensional space, a rotation around the +z-axis is written as:

$$
R_{z} =
\begin{pmatrix}
\cos{\theta} & \sin{\theta} & 0 \\
-\sin{\theta} & \cos{\theta} & 0 \\
0 & 0 & 1
\end{pmatrix}
$$

Any orthogonal matrix with unity determinant represents a rotation, with its direction not necessarily clear from the form of the matrix. An arbitrary rotation matrix can be viewed as an ordinary z-axis rotation being expressed in another set of bases, so that $R = PR_{z}P^{-1}$ for some $P$. Since the trace is basis-independent, we have $\operatorname{tr}R = \operatorname{tr}R_{z} = 2\cos{\theta} + 1$. This provides a way to determine the angle of rotation. To determine the direction of rotation, consider the equation $R \mathbf{v} = \mathbf{v}$. Solving for $\mathbf{v}$ leads to an expression for the direction of rotation.

## Normed Vector Spaces

## Inner Product Spaces
