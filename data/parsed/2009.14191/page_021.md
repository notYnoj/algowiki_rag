\(a_2:\{a_1,a_3\}\succ\{a_1,a_4\}\succ\{a_3,a_4\},\)<br>
\(a_3:\{a_1,a_2\}\succ\{a_1,a_4\}\succ\{a_2,a_4\},\)<br>
\(a_4:\{a_1,a_2\}\succ\{a_1,a_3\}\succ\{a_2,a_3\}.\)

The instance \(\mathcal{I}'\) arising from I by adding a cut-off gadget for _a_:=_a_<sub>2</sub> and _p<sub>a</sub>_:={_a_<sub>1</sub>_,a_<sub>4</sub>} has the following preferences (where for \(z_a^r\) all 2-sets containing \(z_a^r\) shall be deleted):

\(a_1:\{a_2,a_3\}\succ\{a_2,a_4\}\succ\{a_3,a_4\}\dots\succ\dots^{(\text{rest})},\)<br>
\(a_2:\{a_1,a_3\}\succ\{a_1,a_4\}\succ\{z_a^1,z_a^4\}\succ\{z_a^2,z_a^3\}\succ\{z_a^1,z_a^5\}\succ\{z_a^2,z_a^4\}\succ\{z_a^1,z_a^3\}\succ\{z_a^3,z_a^4\},\)<br>
\(\succ\{z_a^1,z_a^2\}\succ\{z_a^2,z_a^5\}\succ\{z_a^3,z_a^5\}\succ\{z_a^4,z_a^5\}\succ\{a,z_a^6\}\succ\{z_a^1,z_a^6\}\succ\{z_a^2,z_a^6\}\succ\{z_a^3,z_a^6\},\)<br>
\(\succ\{z_a^4,z_a^6\}\succ\{z_a^5,z_a^6\}\succ\{a_3,a_4\},\)<br>
\(a_3:\{\{z_a^r,z_a^{r^\prime}\}:r,r'\in[6],r\neq r'\}\succ\{a_1,a_2\}\succ\{a_1,a_4\}\succ\{a_2,a_4\}\succ\dots^{(\text{rest})},\)<br>
\(a_4:\{\{z_a^r,z_a^{r^\prime}\}:r,r'\in[6],r\neq r'\}\succ\{a_1,a_2\}\succ\{a_1,a_3\}\succ\{a_2,a_3\}\succ\dots^{(\text{rest})},\)<br>
\(z_a^r:\{a,z_a^1\}\succ\{a,z_a^2\}\succ\{a,z_a^3\}\succ\{a,z_a^5\}\succ\{z_a^1,z_a^4\}\succ\{z_a^2,z_a^3\}\succ\{a,z_a^4\}\succ\{z_a^1,z_a^5\}\)<br>
\(\succ\{z_a^2,z_a^4\}\succ\{z_a^1,z_a^3\}\succ\{z_a^3,z_a^4\}\succ\{z_a^1,z_a^2\}\succ\{z_a^2,z_a^5\}\succ\{z_a^3,z_a^5\}\succ\{z_a^4,z_a^5\}\)<br>
\(\succ\{a,z_a^6\}\succ\{z_a^1,z_a^6\}\succ\{z_a^2,z_a^6\}\succ\{z_a^3,z_a^6\}\succ\{z_a^4,z_a^6\}\succ\{z_a^5,z_a^6\}\succ\dots^{(\text{rest})}.\)

We now show that adding for every agent _a_ a cut-off gadget for _a_ and a 2-set _p<sub>a</sub>_ enforces that _a_ is matched at least as good as _p<sub>a</sub>_ in every stable matching.

**Lemma 4.7.** _Let_ I<sub>0</sub> _be an_ MDSR-Poset_-instance with set A of agents, and for each_ \(a\in A\)_, let p<sub>a</sub> be a 2-set not containing a. Let A_={_a_<sub>1</sub>_,...,a<sub>n</sub>_} _with_ \(a_i\succ a_j\) _or_ \(a_i\perp a_j\) _for all i\<j. Let_ I_<sub>s</sub> arise from_ I<sub>_s_-1</sub> _by adding a cut-off gadget for agent a<sub>s</sub> and 2-set p<sub>a<sub>s</sub></sub>. Let_ M_<sub>s</sub> be the set of stable matchings M in_ I<sub>0</sub> _with_ \(M(a)\succ_ap_a\) _for all_ \(a\in\{a_1,\dots,a_s\}\).

_Then, for any matching_ \(M\in\mathcal{M}_s\)_, the matching_ \(M_s:=M\cup\{\{z_a^1,z_a^2,z_a^3\},\{z_a^4,z_a^5,z_a^6\}:a\in\{a_1,\dots,a_s\}\}\) _is stable in_ I_<sub>s</sub>. Furthermore, for every matching_ \(M'\) _which is stable in_ I_<sub>s</sub>, we have that_ \(M'\cap\genfrac(){pt}{2}{A}{3}\in\mathcal{M}_s\).

_Proof._ We prove the lemma by induction on _s_. For _s_=0, there is nothing to show. Fix _s\>_0.

First, we show that for any stable matching \(M\in\mathcal{I}_0\) with \(M(a)\unknown_ap_a\) for all \(a\in\{a_1,\dots,a_s\}\), it holds that \(M_s:=M\cup\{\{z_b^1,z_b^2,z_b^3\},\{z_b^4,z_b^5,z_b^6\}:b\in\{a_1,\dots,a_s\}\}\) is a stable matching in I_<sub>s</sub>_. Let _a_:=_a<sub>s</sub>_. No blocking 3-set consists solely of agents from \(\{z_a^r:r\in[6]\}\); this can be seen by checking all 20 such 3-sets. Any blocking 3-set needs to contain at least one agent \(z_a^r\) (else it would already be a blocking 3-set in I<sub>_s_-1</sub>, contradicting the induction hypothesis). Agent _a_ is not part of such a blocking 3-set, as it ranks all 2-sets containing an agent \(z_a^r\) after \(M(a)\unknown_ap_a\). All other 2-sets preferred by agent \(z_a^r\) contain an agent \(a'\) or \(z_{a^\prime}^q\) with \(a'\succ_\text{ML}a\). However, \(a'\) is matched to a 2-set \(M(a')\) it prefers to \(p_{a^\prime}\), and therefore \(a'\) does not prefer any 2-set containing \(z_a^r\) to \(M(a')\). Thus, \(a'\) is not part of a blocking 3-set. Consequently, the blocking 3-set contains solely agents from cut-off gadgets for agents \(a'\) with \(a'\succ_\text{ML}a\). However, no agent \(z_{a_i}^r\) prefers any pair \(\{z_{a_{i^\prime}}^{i^\prime},z_{a_{i^\prime}^{i^{\prime\prime}}}^{i^{\prime\prime}}\}\) with \(i'\ge i\) and \(i''>i\). Thus, the blocking 3-set cannot contain agents from different cut-off gadgets, a contradiction.

To see the second part of the lemma, let _M<sub>s</sub>_ be a stable matching in I_<sub>s</sub>_. Let _M_ be the matching arising from _M<sub>s</sub>_ by deleting all 3-sets containing an agent \(z_{a_i}^r\). We need to show that _M_ is stable and \(M(a)\unknown_ap_a\) for all \(a\in\{a_1,\dots,a_s\}\). If there exists some \(a\in\{a_1,\dots,a_s\}\) such that \(M(a)\unknown_ap\) does not hold, then let _a<sub>i</sub>_ be the agent of minimal index for which \(p_{a_i}\succ M(a_i)\). Then for all _j\<i_, matching _M_ matches the agents from \(\{z_{a_j}^r:r\in[6]\}\) in two 3-sets: These agents are not matched to \(a_{j^\prime}\) with \(j'\le j\) since \(a_{j^\prime}\) is matched at least as good as \(p_{a_{j^\prime}}\), and if \(z_{a_j}^r\)<tbc>

