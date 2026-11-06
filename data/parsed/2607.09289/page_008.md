(_Z_<sub>1</sub>\\_Z_<sub>2</sub>_,Z_<sub>2</sub>\\_Z_<sub>1</sub>) is an ESS solution for \(S'\). Since \(A'\cup B'\) contains exactly one of _e_<sub>2_i_-1</sub> and _e_<sub>2_i_</sub> for every \(i\in[k]\), the set _Z_ also contains exactly one of _e_<sub>2_i_-1</sub> and _e_<sub>2_i_</sub> for every \(i\in[k]\). Thus, by Lemma 3.1, this ESS solution for \(S'\) can be converted into an ESS solution for the original set _S_ by increasing its size by at most _k_. Its size is at most \(|Z|+k=n-\ell+2k\), which is strictly smaller than \(\ell\) because \(\ell-k>n/2\). This contradicts the assumption that the minimum solution size for _S_ is \(\ell\). Therefore, all subset sums of _Z_ are distinct, and hence \(|\{\sum(Z')|Z'\subseteq Z\}|=2^{|Z|}=2^{n-(\ell-k)}\), which gives the desired lower bound in this case.

Second, consider the remaining case. Let \(j=\left\lfloor\frac{\ell-k-1}{2}\right\rfloor\). We claim that all subsets of _Z_ of size _j_ have distinct sums. Suppose, for contradiction, that there exist distinct subsets \(Z_1,Z_2\subseteq Z\) such that |_Z_<sub>1</sub>|=|_Z_<sub>2</sub>|=_j_ and \(\sum(Z_1)=\sum(Z_2)\). Then \((Z_1\backslash Z_2,Z_2\backslash Z_1)\) is an ESS solution for \(S'\). Again, by Lemma 3.1, this solution can be converted into an ESS solution for _S_ by increasing its size by at most _k_. The resulting solution has size at most \(2j+k<\ell\), contradicting the minimality of \(\ell\). Therefore, all subsets of _Z_ of size _j_ have distinct sums, and hence \(|\{\sum(Z')|Z'\subseteq Z\}|\ge\genfrac(){pt}{2}{|Z|}{j}\), which gives the desired lower bound.

**Lemma 3.4.** _Assume that_ \(0\le 2k\le\ell\) _and_ \(\epsilon n\le\ell\le(1-\epsilon)n\) _for some constant_ \(\epsilon>0\) _(say,_ \(\epsilon=1/100\)_). Set the prime-bound parameter p_<sub>max</sub> _in Algorithm 2 to_ \(2^{n-(\ell-k)}\) _if_ \(\ell-k>n/2\)_, and to_ \(\genfrac(){pt}{2}{n-(\ell-k)}{\lfloor(\ell-k-1)/2\rfloor}\) _otherwise. Then, with probability at least_ \(\Omega^*\left(\genfrac(){pt}{2}{\ell}{2k}/\genfrac(){pt}{2}{n}{2k}\right)\)_, Algorithm 2 outputs a solution._

_Proof._ Let F denote the event that the solution described in Lemma 3.2 exists. We analyze the conditional probability of success given that F occurs. By Lemma 3.2, we have \(\mathbb{P}[\mathcal{F}]\ge\genfrac(){pt}{2}{\ell}{2k}/\genfrac(){pt}{2}{n}{2k}\). It remains to show that, conditioned on F, Algorithm 2 outputs a solution with probability \(\Omega^*(1)\).

Let G denote the event that Algorithm 2 does not halt in Line 3, i.e., the event that \(|C|\le n^d\frac{2^n}{p_\mathrm{max}}\) occurs, where _d\>_2 is the fixed constant used in Line 3 of Algorithm 2. When G occurs, the algorithm reaches Line 5.

Let H denote the event that there exist \((X,v_X),(Y,v_Y)\in C'\) satisfying \(\sum(X)=\sum(Y)\) and _v<sub>X</sub>+v<sub>Y</sub>_=**1**. When H occurs, the algorithm finds such a pair in Line 5.

Therefore, the conditional probability that Algorithm 2 outputs a solution can be expressed as \(\mathbb{P}[(\mathcal{G}\cap\mathcal{H})|\mathcal{F}]\). To lower-bound P\[H|F\], it suffices to lower-bound the probability that there exists an \(a\in\Phi\) such that \(a\equiv_pr\), where \(\Phi\) is defined in (1) and _r_ is the random residue chosen in Line 2 of Algorithm 2.

**Claim 3.5.** _Suppose that_ \(|\Phi|\ge p_\mathrm{max}\) _and_ \(p_\mathrm{max}=2^{\Theta(n)}\)_. Then, with constant probability, we have_ \(|\{a\mathrm{mod}p|a\in\Phi\}|\ge\Omega(p/n^2)\).

_Proof._ The proof is identical to that of \[25, Lemma 3.6\]. For completeness, we provide the details in Appendix B.1.

By Lemma 3.3, conditioned on F, we have \(|\Phi|\ge p_\mathrm{max}\). Moreover, from the assumptions on \(\ell\) and _k_, we have \(\ell-k=\Theta(n)\) and \(n-(\ell-k)=\Theta(n)\). Thus, in either case of the definition of _p_<sub>max</sub>, we have \(p_\mathrm{max}=2^{\Theta(n)}\). Hence, by Claim 3.5, with constant probability, \(|\{a\mathrm{mod}p|a\in\Phi\}|\ge\Omega(p/n^2)\). Conditioned on this event, since _r_ is chosen uniformly at random from \[0_,p_-1\], the probability that \(r\in\{a\mathrm{mod}p|a\in\Phi\}\) is \(\Omega(1/n^2)\). Therefore,

\(\mathbb{P}[\mathcal{H}|\mathcal{F}]\ge\Omega(1/n^2).\) (2)

We next upper-bound the expected value of |_C_|.

**Claim 3.6.** _For any fixed_ \(S'\)_, we have_ \(\mathbb{E}[|C|]\le 2^n/p_\mathrm{max}\).

