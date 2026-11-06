The algorithm outputs \(\perp\) if any of _i_, \(\ell\), or _j_ are out-of-bounds.<sup>9</sup><tbc>

• \(S_\ell^{gates}\): the number of gates in layer \(\ell\) of _C_.

This is defined analogously for boolean circuits.

**Definition 2.7** (Succinctly-uniform boolean circuits)**.** We say that boolean family {_C<sub>n</sub>_} is **succinctly- uniform** if there is a poly(log_n_)-time, _O_(log_n_)-space algorithm such that, given \((i,j,\ell)\) in binary (where \(i,j,\ell\in[\text{poly}(n)]\)), the algorithm outputs:

• The following information about the _i_<sup>th</sup> gate residing in the \(\ell^\mathrm{th}\) layer of _C_, denoted \(g_{i,\ell}\):<tbc>

– \(\text{gate}\text{type}(i,\ell)\): encodes which type of gate (e.g. `AND`, `OR`, `NOT`, `THR`, etc) \(g_{i,\ell}\) is.<tbc>

– \(\text{incoming}(i,\ell,j)\): encodes the index _k_ of the gate in layer \(\ell-1\) corresponding to the _j_<sup>th</sup> incoming wire to \(g_{i,\ell}\), as well as the binary value of incoming gate \(g_{k,\ell}\) if it is a fixed constant.<tbc>

– \(\text{in}\text{degree}(i,\ell)\): The in-degree of gate \(g_{i,\ell}\).

The algorithm outputs \(\perp\) if any of _i_, \(\ell\), or _j_ are out-of-bounds.

• \(S_\ell^{gates}\): the number of gates in layer \(\ell\) of _C_.

## 3 Evaluating Low-Depth Circuits of Symmetric Gates

In this section, we give a fast and simple version of the circuit evaluation algorithm from \[BCKLS14\], and note several algorithmic applications of fast circuit evaluation.

### 3.1 Fast SYM Circuit Evaluation

**Theorem 1.1.** There exists a catalytic algorithm using _O_(log(_w_)+_d_) clean workspace and \(\widetilde{O}\left(w2^d\right)\) time, which takes in a _d_-layer, _w_-wire circuit of symmetric gates, and an input to the circuit, and computes the circuit’s output.

_Proof._ By increasing the number of wires by at most a factor of _d_, we can assume that the circuit is _layered_, in that all gates only read the outputs of gates on the previous layer. We also assume without loss of generality that _w_, and all gate fan-ins, are powers of two. (Otherwise, simply add dummy gates and wires to the circuit to make this the case.) We divide the catalytic space into "registers", each of which stores a value from \[_w_\].

For each gate _g_ of the circuit, we assign an associated "output register", and _f<sub>g</sub>_ associated "helper registers", where _f<sub>g</sub>_ is _g_’s fan-in. We will use _R<sub>g</sub>_ and \(R_g^{(1)},\dots,R_g^{(f_g)}\) to refer to the values held by these registers, respectively, at a given point in time. Let \(\tau_g\) and \(\tau_g^{(1)},\dots,\tau_g^{(f_g)}\) denote the initial values of these registers prior to any computation.

Our goal will be to set every gate’s output register to \(\tau_g+b_i\text{mod}w\), where _b<sub>i</sub>_ is the value (0 or 1) outputted by the gate when the circuit reads its input<sup>10</sup>. We say a gate is "computed" if \(R_g=\tau_g+b_i\text{mod}w\), and "reset" if \(R_g=\tau_g\). (Note that it could also be in neither of these states.)

As in \[BCKLS14\], we do this computation recursively. That is, we assume we have a reversible algorithm \(A_\ell\) that computes all of the output registers on level \(\ell\), and use this algorithm as a subroutine to yield a reversible algorithm \(A_{\ell+1}\) that computes all of the output registers on level \(\ell+1\). In order to keep the space usage small, we ensure that we always completely erase the clean space before each<tbc>

<sup>9</sup>Therefore, by convention, input gates always have all incoming wires be \(\perp\). <sup>10</sup>Observe that, if we can do so, then we can also write the answer onto an XOR-only output tape while resetting the catalytic space: First, XOR the least-significant bits of all of the final layer’s output registers into the output. Then, run our algorithm. Then, do this XOR again. Finally, run our algorithm in reverse to reset all of the gates.

