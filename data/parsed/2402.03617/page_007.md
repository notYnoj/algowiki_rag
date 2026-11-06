<tbc>that begins at _e_<sub>1</sub> is

\(g^1(L)=g_1g_2\cdots g_l=\left[\begin{array}{ c c }
R_{1,l} & \mathbf{p}_{1,l} \\
\mathbf{0} & 1
\end{array}\right]\)

where the superscript denotes the starting edge. However, the simple cycle may start at any edge \(e_k\in E(L)\).

**Proposition 1.** _The transformation matrix of a simple cycle_ \(L=e_1e_2\cdots e_l\) _with start edge e<sub>i</sub> is_

\(g^i(L)=\left(g_ig_{i+1}\cdots g_l\right)\left(g_1\cdots g_{i-1}\right)=\left[\begin{array}{ c c }
R^i & \mathbf{p}^i \\
\mathbf{0} & 1
\end{array}\right]\) (10)

_where the superscript denotes the starting edge. Two transformation matrices g<sup>i</sup>(L),g<sup>j</sup>(L_) _with starting edges e<sub>i</sub>,e<sub>j</sub> are related as_

\(R^i=R^j=R_{1,l}\mathbf{p}^i=R_{i,(j-1)}\mathbf{p}^j+\left(I-R_{1,l}\right)\mathbf{p}_{i,(j-1)}\) (11)

_Proof._ Rotations are commutative in _SE_(2), hence, \(\forall i,j\le l\) the rotation associated with simple cycle _L_ irrespective of the starting edge is _R<sup>i</sup>=R<sup>j</sup>=R_<sub>1_,l_</sub>. The two transformation matrices can be written as

\(g^i=\left(g_ig_{i+1}\cdots g_{j-1}\right)\left(g_jg_{j+1}\cdots g_lg_1\cdots g_{i-1}\right)\)<br>
\(g^j=\left(g_jg_{j+1}\cdots g_lg_1\cdots g_{i-1}\right)\left(g_ig_{i+1}\cdots g_{j-1}\right)\)

Hence,

\(g^ig_{i,j-1}=g_{i,j-1}g^j\)<br>
\(\left[\begin{array}{ c c }
R_{1,l} & \mathbf{p}^i \\
\mathbf{0} & 1
\end{array}\right]\left[\begin{array}{ c c }
R_{i,(j-1)} & \mathbf{p}_{i,(j-1)} \\
\mathbf{0} & 1
\end{array}\right]=\left[\begin{array}{ c c }
R_{i,(j-1)} & \mathbf{p}_{i,(j-1)} \\
\mathbf{0} & 1
\end{array}\right]\left[\begin{array}{ c c }
R_{1,l} & \mathbf{p}^j \\
\mathbf{0} & 1
\end{array}\right]\)<br>
\(\Rightarrow\mathbf{p}^i+R_{1,l}\mathbf{p}_{i,(j-1)}=\mathbf{p}_{i,(j-1)}+R_{i,(j-1)}\mathbf{p}^j\)<br>
\(\mathbf{p}^i=R_{i,(j-1)}\mathbf{p}^j+\left(I-R_{1,l}\right)\mathbf{p}_{i,(j-1)}\)

If the magnitude of the resultant translation or rotation for a gait depends on the starting vertex, the gait definition remains ambiguous. In context of the pMFC framework, this is resolved by ensuring that the resulting magnitude is independent of the starting vertex. Geometrically, **_p_**_<sup>i</sup>,**p**<sup>j</sup>_ denote the displacements of robot as it traverses the same simple cycle but with different start edges. However, they are expressed in different coordinate systems - in the initial vertices of their respective edges _e<sub>i</sub>,e<sub>j</sub>_. (11) provides the relationship where **_p_**_<sup>j</sup>_ is transformed to the same coordinate system as **_p_**_<sup>i</sup>_, i.e., the initial vertex _e<sub>i</sub>_.

**Definition.** _Locomotion gaits are defined as simple cycles that are transformation invariant. The principle of transformation invariance implies that the displacement and rotation of a simple cycle are preserved irrespective of starting vertex, i.e.,_

\(\mathbf{p}^i=R_{i,(j-1)}\mathbf{p}^j\text{and}R^i=R^j,\forall 1<i,j\le l\)

**Proposition 2.** _Only two fundamental types of locomotion gaits in SE_(2) _exist_<sup>3</sup>

1) _Translation gait: When the cumulative rotation of the simple cycle is zero, i.e.,_ \(\sum_{k=1}^l\theta_k=0\)<tbc>

_2)_ _Rotation gait: When the translation of all simple cycle motion primitives are zero, i.e.,_ \(\mathbf{p}_k=0\forall e_k\in E(L)\)

_Proof._ We have already seen that the resultant rotation of a simple cycle is the same irrespective of the starting vertex, i.e., _R<sup>i</sup>=R<sup>j</sup>_. Using (11), translation equivalence implies

\(\left(I-R_{1,l}\right)\mathbf{p}_{i,(j-1)}=0\)

This is possible only for two cases

1) \(\left(R_{1,l}-I\right)=0\Rightarrow\sum_{k=1}^l\theta_k=0\)<tbc>

2) \(\mathbf{p}_{i,(j-1)}=0\Rightarrow\sum_{k=i}^{j-1}R_{i,(k-1)}\mathbf{p}_k=0\forall 1<i,j\le l\). Hence, \(\mathbf{p}_k=0\forall e_k\in E(L)\).

## V. GAIT SYNTHESIS AND EXPLORATION

Gait synthesis is the process of determining a set of periodic sequences of motion primitives that satisfy the transformation invariance principle.

### A. Nonlinear Cost Functions

One approach to optimal gait synthesis would be to perform constrained optimization on nonlinear cost functions _J<sub>t,nl</sub>_ and \(J_{\theta,nl}\) that maximize a weighted sum of motion (translation or rotation, respectively) normalized by the length of the simple cycle: **z**<sup>T</sup>**z**.

\(J_{t,nl}(\mathbf{z})=\frac{\|\mathbf{p}(\mathbf{z})\|+\lambda_ts_p(\mathbf{z})}{\mathbf{z}^\mathsf{T}\mathbf{z}},J_{\theta,nl}(\mathbf{z})=\frac{|\Theta^\mathsf{T}\mathbf{z}|+\lambda_\theta s_\theta(\mathbf{z})}{\mathbf{z}^\mathsf{T}\mathbf{z}}\) (12)

where \(\lambda_t,\lambda_\theta\) are scalars, and \(s_p,s_\theta\) are the trace of the translation and rotation covariance matrices of the simple cycle. Here, the calculation of **_p_**(**z**) and the covariance matrix \(\Sigma(\mathbf{z})\) can be approximated on Euclidean motion groups \[42\]. Given the lack of a smooth expression for these cost functions, they need to be exhaustively calculated for each locomotion gait (constrained simple cycles).

A well-known algorithm for finding simple cycles has been proposed by Tarjan and later improved by Johnson \[43\]. However, the number of simple cycles _n<sub>z</sub>_ for a complete digraph increases exponentially with the size of the graph as defined by \(n_z=\sum_{i=1}^n\left(\begin{array}{ c }
n \\
n-i+1
\end{array}\right)(n-i)!\) Consequently, the associated time complexity O((_n+m_)(_n<sub>z</sub>_+1)) limits the usefulness of optimizing these cost functions. For example, this approach results in a very tractable lookup table for small graphs, e.g., _n<sub>z</sub>_=24 for the two-limb example robot. However, larger graphs quickly result in combinatorial explosion, e.g., \(n_z\approx 3.81\times 10^{12}\) for the four-limb experiment robot with _n_=16 vertex digraph. As a result, the nonlinear cost function for this combinatorial (discrete) problem is not tractable for robots with more than three actuators with traditional solvers.

<sup>3</sup>This definition is specific to the pMFC framework and results from the assumptions of quasi-static motion and transformation invariance. In other contexts, coupled rotation and translation cycles may be considered. In fact, some researchers think of the rotation gait as being the only possible type of gait; here, pure translation results from an infinite turning radius \[41\].

