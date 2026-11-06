**Definition 2.17.** _A_ thermodynamic circuit _is a circuit_ C _where each gate g computing a function with domain D is assigned a_ heat function \(Q_g:D\rightarrow\mathbb{R}_{\ge 0}\cup\{\infty\}\)_. On input_ \(x\in D\)_, the gate releases Q<sub>g</sub>(x_) _expected heat into the environment._

**Remark 2.18.** _As we are fixing the temperature, it is reasonable to view Q as expected heat release. A more generally accurate description of Q(x_) _would be the expected entropy flow out of the system on input x._

As we will see in Appendix D, it is important to note that _Q_ is only allowed to depend on the inputs to a gate. This represents the fact that a gate is modular and oblivious to the larger state of the circuit. Otherwise, these heat functions can in principle be an arbitrary function of _D_. A gate that releases \(\infty\) heat on some input _x_ can be thought of being designed so it is not physically possible to specify _x_. This conveys the notion of restricted reversibility in \[Fra17\], where Frank points out that some logically irreversible operations can become reversible with such restrictions on their domain. However, not all choices of heat functions are valid. The Second Law of Thermodynamics (or Landauer’s costs) places constraints on the possible heat functions that can be assigned to each gate.

**Definition 2.19** (Landauer cost, \[Lan61\])**.** _For any function_ \(f:D\rightarrow R\) _and distribution_ D _over D, we define the_ Landauer cost _function of f on_ D:

\(\mathcal{L}_f(\mathcal{D})=\mathcal{S}(\mathcal{D})-\mathcal{S}(f(\mathcal{D})).\)

The following is a corollary of the Second Law of Thermodynamics as applied to computation of functions. As a physical law, it cannot be proven in full generality, though it can be proven within specific models. We state it formally to motivate the subsequent Definition 2.21.

**Proposition 2.20** (Second law, \[Lan61, Sei05\])**.** _Let_ \(f:D\rightarrow R\) _be a function. Any physical process that maps every state_ \(x\in D\) _to the state f(x_) _must release at least_ L_<sub>f</sub>_(D) _expected heat when x is sampled from distribution_ D _over D._

X1
X1
0
0
0
X2
X2
0
0
0
X1, X2
X1, X2
0
0
X3
X3
0
0
X1, X2 X5
X1, X2 X5
0
X4
X1, X2 X5 X4
y

Figure 1: An example of a circuit that cleanly computes \(y=x_1\wedge x_2\wedge x_3\wedge x_4\) up to permutation of the wire indices. Here the red \(\wedge\) gates perform the mapping \((a,b,c)\rightarrow(a,b,a\wedge b)\) and the blue \(\emptyset\) erasure gates perform the mapping \(a\rightarrow 0\). Each gate overwrites its inputs (values on wires to the left of the gate) with its outputs (values on wires to the right of the gate).

