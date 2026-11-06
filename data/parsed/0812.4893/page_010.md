### Red turn.

Each red node \(r\in R\) completes the following read-compute- write cycle. Initially, _C(r_) consists of all adjacent blue nodes, in order of decreasing preference, most preferred first; \(c(r)=\perp\); \(p(r)=\perp\).

1. If \(c(r)\neq\perp\):<tbc>

(a) Receive a message _m_ from _c(r_).<tbc>

(b) If \(m=\text{‘accept’ then}p(r)\leftarrow c(r)\).<tbc>

(c) If \(m=\text{‘reject’ then remove}c(r)\) from _C(r_).<tbc>

(d) \(c(r)\leftarrow\perp\).<tbc>

2. If \(p(r)\neq\perp\):<tbc>

(a) Receive a message _m_ from _p(r_), if any.<tbc>

(b) If \(m=\text{‘break’ then remove}p(r)\) from _C(r_), and set \(p(r)\leftarrow\perp\).<tbc>

3. If \(p(r)=\perp\) and _C(r_) is not empty:<tbc>

(a) Let _c(r_) be the first element of _C(r_).<tbc>

(b) Send the message ‘propose’ to _c(r_).

## 5 Analysis

We adopt the convention of using a subscript _i_=1,2_,..._ to denote the state of the algorithm at the end of round _i_. For example, _p<sub>i</sub>(r_) denotes the value of the variable _p(r_) in the local state of _r_ at the end of round _i_.

At the end of round _i_=1,2_,..._, the local state variables \(p_i(\cdot)\) define a matching

\(M_i=\{\{r,p_i(r)\}:r\in R,p_i(r)\neq\perp\}\)<br>
\(=\{\{b,p_i(b)\}:b\in B,p_i(b)\neq\perp\}\subseteq E.\)

### 5.1 Lost edges and convergence to stability

We start from a restatement, in our terms, of the fact that as the Gale- Shapley algorithm progresses, women only improve their match and men only get worse.

**Lemma 1.** _An edge_ \(\{r,b\}\in E\backslash M_i\) _with_ \(r\in R\) _and_ \(b\in B\) _is unstable in M<sub>i</sub> only if b is present in C<sub>i</sub>(r_) _and r is unmatched at the end of round i._

_Proof._ If _b_ is not in _C<sub>i</sub>(r_), then either _b_ rejected _r_ or broke up with _r_ earlier, which means that _b_ prefers its current match to _r_. If _b_ is in _C<sub>i</sub>(r_) and _r_ is matched, then _r_ has not proposed to _b_ yet, which means that _r_ prefers its current match to _b_.

