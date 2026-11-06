where all individual shifts are within \([0,w')\) so they stay inside word size \(w'\). Each output block depends on at most 2 input blocks, so the whole operation takes O(_c_) instructions.<tbc>

• _Comparing x_ with _y_ in _M_ can be implemented in \(M'\) by iteratively comparing \(x'_i\) with \(y'_i\). This takes at most _c_ steps.<tbc>

• _Branching_ between _x_ and _y_ in _M_ based on a condition can be implemented by a cascade of _c_ branches on each block of _x,y_, which can be done in at most _c_ steps.

Thus, we can simulate each instruction of _M_ with a constant number of instructions in \(M'\).

**Lemma 3** (Simplified Division Lemma)**.** _There exists a transformer block that, for any_ \(\phi(v)\) _present in the residual stream at position t for_ \(v\le t\)_, adds_ \(\phi(\lfloor v/2\rfloor)\) _and_ \(\phi(vmod2)\) _to the residual stream._

_Proof._ The idea is the same as in the more general proof of Merrill and Sabharwal (2024) for division by an arbitrary small value _m_. In their construction, each position _i_ computes \(\phi(i/m)\) and performs an equality test with \(\phi(j)\) computed at all prior positions _j\<i_ to determine if _i/m_ is an integer, i.e., _i_ is a multiple of _m_. Then position _t_ attends back to find the closest multiple of _m_ via rightmost hard attention to compute the mod and div values.

In our special use case, we can simplify this process as follows: each position _j\<t_ computes a key \(k_j=\phi(2j)\) and value \(\phi(j)\). Position _t_ uses query \(q_t=\phi(v-1)\), which can be computed via Prop. 2. It can be verified that the closest matching key is \(k_{\lceil(v-1)/2\rceil}\),<sup>7</sup> and the corresponding value is \(\phi(\lceil(v-1)/2\rceil)\). Observe that for all integer values _v_, \(\lceil(v-1)/2\rceil=\lfloor v/2\rfloor\). Thus the retrieved value is \(\phi(\lfloor v/2\rfloor)\), which we add to the residual stream. To obtain \(\phi(vmod2)\), we compute \(\phi(2\lfloor v/2\rfloor)\) via Prop. 2 and perform an equality test with \(\phi(v)\). If these are equal, \(\phi(vmod2)\) is 0, otherwise it is 1; we add this to the residual stream as well.

## C Proofs of Polylog-Width Transformer Results

### Serialization format.

Before stating the propositions, we fix the transcript format used throughout all four components.

<sup>7</sup>Suppose _v_ is odd, i.e., _v_=2_j_<sup>∗</sup>+1 for some integer _j_<sup>∗</sup>. Then (_v_-1)/2=_j_<sup>∗</sup> and we have an exact key-query match between _q<sub>t</sub>_ and _k_<sub>_j_<sup>∗</sup></sub>. When _v_ is even, say _v_=2_j_<sup>∗</sup>, then (_v_-1)/2=_j_<sup>∗</sup>-1/2. The two contenders for the closest match with \(q_t=\phi(2j^*-1)\) in this case are \(k_{j^*-1}=\phi(2j^*-2)\) and \(k_{j^*}=\phi(2j^*)\). Since these are unit norm vectors, the key-query inner product is the same as cosine distance, which is larger between \(\phi(2j^*-1)\) and \(\phi(2j^*)\) than between \(\phi(2j^*-1)\) and \(\phi(2j^*-2)\).

