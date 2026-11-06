An endomorphism \(\sigma\) is _idempotent_ if \(\sigma(\sigma(a))=\sigma(a)\) for every \(a\in D\). Choose an endomorphism with minimum image. Its restriction to its image is a permutation, since applying the map again cannot make the image smaller. A suitable power is therefore the identity on its image and is idempotent. We fix such an idempotent endomorphism \(\sigma\) and write \(C=\sigma(D)\). We define

\(\mathrm{core}(R)=\sigma(R)=R\cap C^k,\)

and call _C_ its _core domain_. We fix one such choice throughout the paper. The equality holds because an idempotent map fixes every value in its image. The relation core(_R_) is a core relation because every one of its endomorphisms is an automorphism. Indeed, a non-bijective endomorphism composed with \(\sigma\) would give an endomorphism of _R_ with image smaller than _C_. We call _R_ itself a _core relation_ when every endomorphism of _R_ is an automorphism.

**Example 3.4.** For CUT, every endomorphism must send 0 and 1 to different values. Hence its only endomorphisms are the identity and the map that swaps 0 and 1. Both are automorphisms, so CUT is a core relation.

For a relation that is not a core, let _D_={0,1,2} and let

\(R_\mathrm{star}=\{(0,1),(1,0),(0,2),(2,0)\}.\)

The map that fixes 0 and 1 and sends 2 to 1 is a non-bijective endomorphism of _R_<sub>star</sub>. Therefore _R_<sub>star</sub> is not a core relation. Its image is {0,1}, and restricting the relation to this image gives CUT. Hence core(_R_<sub>star</sub>)=CUT on the core domain {0,1}.

The automorphisms of a core relation are the only unavoidable ambiguity when we try to force variables to chosen values. Let _X_ be a set of variables and let \(s:X\rightarrow D\) be a fixed assignment. We say that an _R_-instance _P<sub>s</sub> hard-pins s up to one common automorphism_ if it may use additional variables and

\(\{\alpha|_X:\alpha\in\mathrm{Sat}(P_s)\}=\{\sigma\circ s:\sigma\in\mathrm{Aut}(R)\}.\)

**Example 3.5.** For CUT, introduce two variables _y_<sub>0</sub>_,y_<sub>1</sub> and require CUT(_y_<sub>0</sub>_,y_<sub>1</sub>). If _s(x_)=0, add CUT(_x,y_<sub>1</sub>). If _s(x_)=1, add CUT(_x,y_<sub>0</sub>). These constraints force every \(x\in X\) to agree with _s_ after either the identity or the common swap of 0 and 1.

The relation _R_<sub>star</sub> above explains why we first reduce to a core. Its non-bijective endomorphism replaces the value 2 by 1. Applying this map to any satisfying assignment gives another satisfying assignment, so constraints over _R_<sub>star</sub> cannot in general distinguish these two values. After reducing _R_<sub>star</sub> to its core CUT, the construction above applies.

In Section 4.2, we prove that every core relation admits the same kind of construction.

## 3.5 Finite-domain degree

The parameter for Exact-CSP is the degree of the indicator function of the core relation. We define degree for any function \(f:D^k\rightarrow\mathbb{R}\). The domain _D_ need not contain a value already called 0. We choose any value of _D_ and call it 0. This choice only fixes the notation, and the reader may think of it as the usual value 0. For each coordinate \(i\in[k]\) and each \(a\in D\backslash\{0\}\), define _Z<sub>i,a</sub>(z_)=**1**\[_z<sub>i</sub>=a_\].

Every function \(f:D^k\rightarrow\mathbb{R}\) has a unique expansion<tbc>

\(f(z)=\sum_{T\subseteq[k]}\sum_{b\in(D\backslash\{0\})^T}\widehat{f}(T,b)\prod_{i\in T}Z_{i,b_i}(z),\)

