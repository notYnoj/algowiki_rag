iii) An output tape, initialized to all zeros, with the following write pattern: _k_ passes of a one-way XOR head. One pass to the output tape consists of a one-way (XOR) head, starting at the leftmost cell and moving right by one cell, that is capable of XORing any value \(b\in\{0,1\}\) to the current cell. To conclude one pass, the head position is reset to the leftmost cell -- this resetting is only done (at most) _k_-1 times. Once the machine halts, the output is defined as all the bits up to the _rightmost_ accessed head position over the entire computation. (The tape is at most 2<sup>_O(s_)</sup> bits long.)

Note this definition does not allow for overwriting bits of the output tape. As XORing _b_=0 into any bit keeps that bit the same and XORing by _b_=1 flips it, we can equivalently think of Definition 2.3 as allowing the machine to flip bits of the output tape in a multi-pass fashion. As bit-flips (XORs) can be undone by simply flipping (XORing) again, any machine in the above model will only modify the output tape _reversibly_ -- run the machine again to undo.

Observe that for _k_=1 the _k_-output-pass model (Definition 2.3) is, in fact, equivalent in power to the transducer model (Definition 2.1), so the transducer is a special case of the _k_-pass model.<sup>7</sup>

**Hash functions.** We define perfect hash families and note small such families can be constructed efficiently. These are used to obtain _k_-path and _k_-cycle algorithms in Section 4.3.

**Definition 2.4** (Perfect Hashing)**.** Fix a universe _U_. A _k_-perfect hash family H_<sub>U,m</sub>_ is a set of functions of the form \(h:U\rightarrow[m]\) with the following property. For any set \(S\subseteq U\) with |_S_|=_k_ there exists an \(h\in\mathcal{H}_{U,m}\) such that _h_ maps _S_ injectively onto \[_m_\].

**Lemma 2.5** (Uniform perfect hash, full table)**.** \[SS90; FKS84\] Let _n,k_ be positive integers. There exists a _k_-perfect hash family mapping from universe \[_n_\] to \[_m_\] with the following properties.

• Each function in the family is specified using _b=O(k_+loglog_n_) bits.<tbc>

• We can iterate through all functions in the family in 2<sup>_O(k_)</sup>poly(log_n_) time and _O_(log_n+k_) space.<tbc>

• For input \(x\in[n]\) and function _h_ in the family, we can compute _h(x_) in _O_(log(_n+k_)) space and poly(log(_n+k_)) time.

**Uniformity.** We define a natural notion of uniform arithmetic circuits and boolean circuits that will be useful for our catalytic algorithm applications. In short, a circuit family {_C<sub>n</sub>_} is uniform in our sense if the gate and wire information can be computed in polylog time and logspace, and (when arithmetic) every bit of every scalar on every wire can be determined in polylog time and logspace. <sup>8</sup>

Let {_C<sub>n</sub>_} be a polynomial-size arithmetic circuit family, and fix a ring K. Let _S<sup>gates</sup>(n_), \(S_\ell^{wires}(n)\), and _S<sup>wires</sup>(n_) be the total number of gates in _C<sub>n</sub>_, the total number of wires in layer \(\ell\) of _C<sub>n</sub>_, and the total number of wires in _C<sub>n</sub>_, respectively.

**Definition 2.6** (Succinctly-uniform arithmetic circuits)**.** We say that arithmetic family {_C<sub>n</sub>_} is **succinctly- uniform** if there is a poly(log_n_)-time, _O_(log_n_)-space algorithm such that, given \((i,j,\ell)\) in binary (where \(i,j,\ell\in[\text{poly}(n)]\)) and \(m\in[\lceil log|\mathcal{K}|\rceil]\) in binary, the algorithm outputs:

• The following information about the _i_<sup>th</sup> gate residing in the \(\ell^\mathrm{th}\) layer of _C_, denoted \(g_{i,\ell}\):<tbc>

– \(\text{incoming}(i,\ell,j)\): encodes the index _k_ of the gate in layer \(\ell-1\) corresponding to the _j_<sup>th</sup> incoming wire to \(g_{i,\ell}\), as well as the _m_<sup>th</sup> low-order bit of the scalar \(\alpha_j\in\mathcal{K}\) attached to the wire if \(g_{i,\ell}\) is linear.<tbc>

**–** \(\text{in.degree}(i,\ell)\): The in-degree of gate \(g_{i,\ell}\).<tbc>

<sup>7</sup>Indeed, on an output tape initialized to zeros, XORing bit \(b\in\{0,1\}\) once onto the tape is equivalent to overwriting by _b_. <sup>8</sup>For circuits, this is distinct from standard logspace uniformity in that the usual definition imposes no restriction on the runtime (aside from the polynomial bound implied by any logspace algorithm). Our definition ensures we can simulate the circuits with little unnecessary time overhead.

