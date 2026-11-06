Specifically, the ring requirements are as follows, following \[BCKLS14, Section 4.1\] but with a further time constraint:

**Definition 4.2** (\[BCKLS14\], Section 4.1)**.** Let K=K_<sub>n</sub>_ be a family of rings. We say K is **(_S,T)-uniform_** if there exists a bijection _e<sub>n</sub>_ mapping K_<sub>n</sub>_ to the lexicographically first |K| strings of \(\{0,1\}^{\lceil log|\mathcal{K}_n|\rceil}\), such that there exist _S(n_)-space, _T(n_)-time algorithms for the following operations:

• On read-only input (1_<sup>n</sup>,e(u),e(v_)), output (each bit of) \(e(u\circ v)\), for operation \(\circ\in\{+,-,\times\}\).<tbc>

• On read-only input (1_<sup>n</sup>,e(v_)) and _e(u_) on a read-write tape, transform _e(u_) in place into _e(u+v_).<tbc>

• On input (1_<sup>n</sup>_), output (each bit of) _e_(-1)_,e_(0)_,e_(1) and |K_<sub>n</sub>_|.

Note that, for instance, \(\{\mathbb{Z}/m_n\mathbb{Z}\}_{n\in\mathbb{N}}\) is \((O(loglogm),\mathsf{polylog}(m))\)-uniform for any uniform sequence \(\{m_n\}_{n\in\mathbb{N}}\). We have the following:

**Theorem 4.3.** Let K be an (_S,T_)-uniform ring. There exists a catalytic algorithm using time \(\widetilde{O}\left(w3^dT\right)\), clean space _O_(log(_w_)+_d_+log(_T_)+_S_), and dirty space \(\widetilde{O}\left(wlog|\mathcal{K}_n|\right)\), which takes in a #NC(K_<sub>n</sub>_) circuit with _w_ wires and multiplicative depth _d_, and a setting of all of the input wires to the circuit, and computes the value of all of the circuit’s output wires.

_Proof._ The proof is essentially identical to that of \[BCKLS14\], except that we make a distinction between different types of multiplication gates (linear and non-linear) and adjust accordingly. We think of the dirty space as consisting of a sequence of "registers", each holding a value over K_<sub>n</sub>_. Note that, if |K_<sub>n</sub>_| is a power of 2, this is trivial to do, but otherwise it is non-obvious one can treat the dirty space this way. Nonetheless, \[CDKMR26\] shows how, at polylogarithmic overhead in time and dirty space, one can assume without loss of generality that one has access to such registers over K_<sub>n</sub>_. (This follows by compressing the dirty space whenever a large block of tape cells contains no value in the appropriate range -- see their Appendix A. Their algorithm requires a pre-processing and post-processing phase, so we assume our entire procedure below happens between these.)

Let \(\tau_i\in\mathcal{K}_n\) denote the initial contents of the _i_th register, and _R<sub>i</sub>_ denote the value currently held at a given point in the algorithm. As in Theorem 1.1, we say that the _i_th gate’s value is "reset" if \(R_i=\tau_i\), and "computed" if \(R_i=\tau_i+v_i\), where _v<sub>i</sub>_ is that gate’s output in the arithmetic circuit. Assume we have a reversible algorithm \(A_\ell\) that results in all of the gates up to and including the \(\ell\)th multiplicative layer being converted from "reset" to "computed", and leaves the clean space empty except for a single global time counter. We give a reversible algorithm \(A_{\ell+1}\) which makes 3 calls to \(A_\ell\) and takes \(\widetilde{O}\left(wT\right)\) time. This algorithm will require further helper registers \(R_i^{(1)}\) and \(R_i^{(2)}\) for every _i_ corresponding to a product gate.

The algorithm proceeds as follows (erasing the clean space after each step):

i) For each gate _i_ (in order of layers, from the output layer backwards):<tbc>

• If _i_ is an addition gate in-between the \(\ell\)th and \(\ell+1\)st multiplicative layers, set \(R_i\leftarrow R_i-R_j-R_k\), where _j_ and _k_ are the two input gates.<tbc>

• If _i_ is a \(\times x\) gate in-between the \(\ell\)th and \(\ell+1\)st multiplicative layers, set \(R_i\leftarrow R_i-R_j\times x\), where _j_ is the input gate.<tbc>

• If _i_ is a +_x_ gate in-between the \(\ell\)th and \(\ell+1\)st multiplicative layers, set \(R_i\leftarrow R_i-R_j\), where _j_ is the input gate.<tbc>

• If _i_ is a product gate on the \(\ell+1\)st layer of the circuit, set \(R_i\leftarrow R_i+R_jR_k+R_jR_i^{(1)}+R_i^{(2)}R_k\), where _j_ and _k_ are the two input gates.<tbc>

ii) Run \(A_\ell\).<tbc>

iii) For each gate _i_ (in order of layers, from the input layer forwards):<tbc>

• If _i_ is an addition gate in-between the \(\ell\)th and \(\ell+1\)st multiplicative layers, set \(R_i\leftarrow R_i+R_j+R_k\), where _j_ and _k_ are the two input gates.<tbc>

