**4. The ordering of the positions.** First come all the violating positions \(C_1^*,C_2^*,\dots,C_m^*\), using the same priority order as the clauses (with _C_<sub>1</sub> having the highest priority). Then come the 15_m_ non-violating positions, in some arbitrary order.

Consider a string \(\vec{v}\) in the orbit, meaning \(\vec{v}=\vec{s}\circ\sigma\) for some \(\sigma\in\langle G\rangle\). Then for each clause _C_, exactly one of the sixteen positions _C<sub>b</sub>_ has a 1 in \(\vec{v}\); this corresponds to some truth assignment to the variables in _C_. Those assignments agree globally and define an assignment \(\alpha_v:V\rightarrow\{0,1\}\).

**Proposition 7.** _Let_ \(1\le j\le m\) _and let_ \(\vec{v}\) _be in the orbit. Then v<sub>j</sub> is_ 1 _if and only if the corresponding assignment_ \(\alpha_v\) _violates C<sub>j</sub>._

Thus, if \(\alpha_v\) can be improved by flipping some variable _x_, then \(\vec{v}\circ\pi_x\) decreases the string lexicographically; Thus, a locally minimal string in the orbit corresponds to an assignment that cannot be improved by 1-flips i.e., a local optimum for LocalLexMax-4-SAT. This concludes the proof of Theorem 4.

## 4 Max 4-SAT with lexicographic costs - proof of Theorem 3

This is the main technical contribution of the paper. We will proceed in three steps.

**1.** In Section 4.1, we present a proof by Krentel[15, 16] that LocalMax-4-SAT is PLS- complete; we will make sure that the clause weights are "almost lexicographic", meaning that each clause weight is a power of two, and each weight appears for at most two clauses.

**2.** In Section 4.2 we modify this construction to achieve fully lexicographic weights; this requires a new idea and comes at the cost that we need to allow "double flips" for PLS-completeness, that is, the neighborhood relation is defined by flipping up to two variables.

**3.** In Section 4.3 we show how to simulate double flips by a sequence of single flips. This will then prove Theorem 3.

## 4.1 Krentel’s Construction: Reducing Flip to LocalMax-4-SAT With Almost Lexicographic Clause Weights

Let \(C'\) be an instance of Flip: a Boolean circuit with _n_ inputs and _m_ outputs. We can transform this into a new circuit _C_ with _n_ inputs and _m+n_ outputs that also computes the best neighbor of the current input. We can assume without loss of generality that _C_ uses only NAND-gates. We create two copies of _C_, called TOP and BOTTOM. For every input \(1\le i\le n\) of _C_ we create two variables \(x_i^T\) and \(x_i^B\), giving a total of 2_n_ input variables. For every gate _j_ of _C_ we create variables \(g_j^T\) and \(g_j^B\). Of those, 2(_m+n_) correspond to the outputs of TOP and BOTTOM. It is advantageous to give them synonyms: we denote the _m+n_ output variables of TOP \(v_1^T,\dots,v_m^T,z_1^T,\dots,z_n^T\) and those of BOTTOM \(v_1^B,\dots,v_m^B,z_1^B,\dots,z_n^B\). Altogether, if \(C'\) has _s_ NAND-gates, we get 2_s_ gate variables, thus a total of 2(_n+s_) variables.

**Feeding output back to the inputs.** The variables represent a partial evaluation of the two circuits. NAND-gates can temporarily be incorrect, for example if \(g_j^T\) is a gate variable with inputs \(y_1^T\) and \(y_2^T\) (those being either gate variables or input variables), but all three variables are set to 1, because the correct output of the gate would be 0. Also, we connect the last _n_ output bits (the "successor output") of TOP to the input of BOTTOM and vice versa. The intuition is that we can (1) flip gate variables in TOP to make every gate

