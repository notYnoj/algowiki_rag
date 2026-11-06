### 6.3 Deletion stability

**Lemma 6.3.** _Suppose that a run executed on A has first t pivots f_<sub>1</sub>_,...,f<sub>t</sub>. If_

\(\{f_1,\dots,f_t\}\subseteq A'\subseteq A,\)

_then running on_ \(A'\) _with the same successive color choices produces the same first t pivots, thresholds, caps, and palette updates._

_Proof._ The main idea is that the choices of pivots and the cap palettes do not change. Induct on the rounds. The initial palettes are independent of the sample set. If the first _s_-1 rounds agree, the current palettes agree pointwise. The original pivot _f<sub>s</sub>_ remains a candidate in \(A'\), and every other candidate in \(A'\) was also a candidate in _A_. Thus its maximality and the fixed tie-breaking order are unchanged. The cap and update depend only on the current palettes, the pivot, and the chosen color. Since the original run completed _t_ rounds, the same pointwise equality also prevents the restricted run from stopping earlier.

## 7 Sampling upper bound

The container viewpoint makes the counting strategy explicit. For each _k_-colorable induced subgraph on _q_ vertices, the process selects pivots and their colors, which determine the relevant palette container when replayed on a suitable subset of the sample. The counting proof supplements this pivot fingerprint with a block choice and the ordered vertices in the selected blocks; this replay seed contains all pivots and, by deletion stability, reproduces the same container as the full-sample run. The remaining sample positions must lie inside that container. We count these descriptions and bound the probability of such a completion, then take a union bound over the descriptions.

For each \(t\in\{1,2,\dots,T\}\), partition the positions \[_q_\] deterministically into 2_t_ nonempty blocks whose sizes differ by at most one.

Our counting argument encodes each colorable sample by one of a small number of _descriptions_. We first record what such a description is.

**Definition 7.1** (Description)**.** A _description_ is a tuple

\((t,W,\mathbf{i},u_1,\dots,u_a,v_1,\dots,v_b)\) (9)

consisting of the following data:

1. an integer \(t\in\{1,\dots,T\}\);<tbc>

2. a _t_-element set \(W\subseteq[2t]\) of block indices of the deterministic partition of \[_q_\] into 2_t_ blocks used in the construction of _A_<sub>0</sub>;<tbc>

3. a color string \(\mathbf{i}=(i_1,\dots,i_t)\in[k]^t\);<tbc>

4. an ordered tuple (_u_<sub>1</sub>_,...,u<sub>a</sub>_) of distinct vertices of _G_, with _a_ equal to the total size of the blocks in _W_;<tbc>

5. an ordered tuple (_v_<sub>1</sub>_,...,v<sub>b</sub>_) of distinct vertices of _G_, with _b=q-a_.

The tuple is _retained_ if _u_<sub>1</sub>_,...,u<sub>a</sub>,v_<sub>1</sub>_,...,v<sub>b</sub>_ are pairwise distinct and, on replaying the process from _A_<sub>0</sub>:={_u_<sub>1</sub>_,...,u<sub>a</sub>_} with the color string **i**, the process completes _t_ rounds and its true cap _C_:=_U(P<sup>t</sup>_) satisfies<tbc>

\(\{u_1,\dots,u_a,v_1,\dots,v_b\}\subseteq C,|V(G)\backslash C|\ge\alpha tn.\) (10)

