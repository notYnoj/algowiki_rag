_Lemma_ 6 (01\(\rightarrow\)10 shadowing under CNF)_. For any bitmask b with_ (_b_\[_i_<sub>0</sub>\]_,b_\[_i_<sub>1</sub>\])=(0,1) _there exists_ \(b'=\mathsf{canon}(b)\) _with_ (1,0) _such that_ \(\tilde{\sigma}(b)=\tilde{\sigma}(b')\) _and_ \(\chi(b)=\chi(b')\)_. Moreover, every aliased extension of b by any_ \(j\notin\{i_0,i_1\}\) _is aliased-equal to the corresponding extension of_ \(b'\).

_Proof._ Normalization replaces _x_<sub>1</sub> by _x_<sub>0</sub> at (_i_<sub>0</sub>_,i_<sub>1</sub>), which preserves \(\tilde{\sigma}\) and also \(\chi=b[i_1]\). Extensions by \(j\notin\{i_0,i_1\}\) add the same value to both sides.

_Lemma_ 7 (Successor preservation under CNF)_. Let b be any bitmask and_ \(j\notin\{i_0,i_1\}\)_. Then_

\(\tilde{\sigma}(b\cup\{j\})=\tilde{\sigma}(\mathsf{canon}(b)\cup\{j\}),\chi(b\cup\{j\})=\chi(\mathsf{canon}(b)\cup\{j\}).\)

_Proof._ Immediate from linearity of \(\tilde{\sigma}\) and the fact that `canon` only possibly flips \((0,1)\mapsto(1,0)\) at (_i_<sub>0</sub>_,i_<sub>1</sub>) with the same aliased contribution.

## State Space Reduction via Aliasing

_Lemma_ 8 (State Space Reduction via Aliasing)_. Let_ \(S'\subseteq\mathbb{Z}_{\ge 0}\) _be a set of k non-negative integers, and let_ \(x_0,x_1\in S'\) _be a designated alias pair with_ \(x_0\neq x_1\)_. If x_<sub>1</sub> _is treated as x_<sub>0</sub> _when present, the number of distinct_ aliased _subset sums is at most_ \(\frac{3}{4}\cdot 2^k\).

_Proof._ Fix \(P\subseteq S'\backslash\{x_0,x_1\}\). The four patterns _P_, \(P\cup\{x_0\}\), \(P\cup\{x_1\}\), \(P\cup\{x_0,x_1\}\) yield aliased values \(\sigma(P)\), \(\sigma(P)+x_0\), \(\sigma(P)+x_0\), \(\sigma(P)+2x_0\), i.e., at most three distinct values. There are 2<sup>_k_-2</sup> choices of _P_.

### Expansion Policy for Worst-Case Bound (count-based).

To tie running time to the number of _expanded_ states (not just distinct aliased values), we restrict which discovered states are enqueued when aliasing is enabled. Let<tbc>

\(c(b):=b[i_0]+b[i_1]\in\{0,1,2\},\chi(b):=b[i_1]\in\{0,1\}.\)

<tbc>A state with mask _b_ is _expandable_ iff

\(\mathrm{Expandable}(b):\Longleftrightarrow(c(b)=0)\vee(c(b)=2)\vee\big(c(b)=1\wedge\chi(b)=0\big).\)

Operationally, every discovered state is _inserted_ into its \((\tilde{\sigma},\chi)\) bucket (for correctness and witness recovery), but it is _enqueued for expansion_ iff Expandable(_b_) holds. In particular, \((c,\chi)=(1,1)\) ("_x_<sub>1</sub> only") states are recorded but marked `doNotExtend`.

_Lemma_ 9 (Expansion Accounting)_. Consider a half_ \(\ell\) _of size k with a fixed alias pair_ (_x_<sub>0</sub>_,x_<sub>1</sub>) _and the CNF expansion rule. For each base subset_ \(P\subseteq\ell\backslash\{x_0,x_1\}\)_, the four patterns on_ {_x_<sub>0</sub>_,x_<sub>1</sub>} _contribute at most three_ expanded _states. Consequently, the number of expanded states in the half is at most_ \(3\cdot 2^{k-2}=\frac{3}{4}\cdot 2^k\).

_Proof._ Partition subsets by their restriction to {_i_<sub>0</sub>_,i_<sub>1</sub>}. For each base \(P\subseteq\ell\backslash\{x_0,x_1\}\), we expand 00 and 11, and among {10,01} only 10. Thus at most three expanded states per base, giving \(3\cdot 2^{k-2}\).

_Lemma_ 10 (Policy Safety)_. The expansion policy preserves the lane invariant and completeness of the merge: forbidding expansion from_ \((c,\chi)=(1,1)\) _does not prevent the generation of any aliased sum nor the recovery of any witness._

_Proof sketch._ For _b_ with \((c,\chi)=(1,1)\), let _b<sup>⋆</sup>_ flip (_i_<sub>0</sub>_,i_<sub>1</sub>) to (1,0). For any \(J\subseteq\ell\backslash\{x_0,x_1\}\), \(\tilde{\sigma}(b\cup J)=\tilde{\sigma}(b^\star\cup J)\), so all descendants of _b_ are shadowed by descendants of the expandable _b<sup>⋆</sup>_. (1,1) states are still inserted into the \(\chi=1\) bucket, allowing the compensatory merge to return witnesses that include _x_<sub>1</sub>.

