**Lemma 5.4** (\[1, Section 3.1\])**.** _Let_ \(\prec\) _be the relation on_ \(\{I|I\subseteq[n]\}\) _defined as follows: for all_ \(I_1,I_2\subseteq[n]\)_, we have_ \(I_1\prec I_2\) _if and only if_ \(max\{i|i\in I_1\Delta I_2\}\in I_2\)_. Then_ \(\prec\) _is a strict total order. Let S_={_w_<sub>1</sub>_,...,w<sub>n</sub>_} _be an input set, and let_ \(C_\mathrm{idx}=\{I\subseteq[n]|\sum_{i\in I}w_i\equiv_pr\}\)_. In O(np_) _time and space, we can construct a data structure that, given an index_ \(J\in[|C_\mathrm{idx}|]\)_, returns the J-th subset in C_<sub>idx</sub> _with respect to_ \(\prec\) _in O(n_) _time. The data structure also stores the value_ |_C_<sub>idx</sub>|.

Since the input _S_ is a set, we identify each index set \(I\subseteq[n]\) with the corresponding subset \(\{w_i|i\in I\}\) of _S_. Under this identification, Lemma 5.4 provides random access to \(C=\{X\subseteq S|\sum(X)\equiv_pr\}\). The success-probability analysis of Algorithm 3 is essentially the same as that of Algorithm 2 with replacement count _k_=0.

**Lemma 5.5.** _Assume that_ \(\epsilon n\le\ell\le(1-\epsilon)n\) _for some constant_ \(\epsilon>0\)_, and let_ \(\alpha\in(0,1/2]\) _be a constant. Then Algorithm 3 returns a solution with probability at least_ \(\Omega(1/n^2)\).

_Proof._ We follow the same argument as in the proof of Lemma 3.4, except that we do not modify the input set using Algorithm 1. We first state the special cases of the claims used there corresponding to _k_=0, where no input modification is performed.

**Claim 5.6.** _Let_<tbc>

\(\Phi=\left\{\sum(X)|X\subseteq S,\exists Y\subseteq S\text{\textit{such that}}X\neq Y\text{\textit{and}}\sum(X)=\sum(Y)\right\}.\)

<tbc>_Then_

\(|\Phi|\ge\left\{\begin{array}{ c c }
2^{n-\ell} & \text{\textit{if}}\ell>n/2, \\
\genfrac(){pt}{2}{n-\ell}{\lfloor(\ell-1)/2\rfloor} & \text{\textit{otherwise.}}
\end{array}\right.\)

_Proof._ The claim follows by applying the proof of Lemma 3.3 with _k_=0.

**Claim 5.7.** _Suppose that_ \(|\Phi|\ge p_\mathrm{max}\) _and_ \(p_\mathrm{max}=2^{\Theta(n)}\)_. Then, with constant probability, we have_ \(|\{a\mathrm{mod}p|a\in\Phi\}|\ge\Omega(p/n^2)\).

_Proof._ The claim follows from the proof of Claim 3.5.

**Claim 5.8.** _We have_ \(\mathbb{E}[|C|]\le 2^n/p_\mathrm{max}\).

_Proof._ The claim follows from the proof of Claim 3.6.

Let G denote the event that Algorithm 3 does not halt in Line 2, i.e., the event that \(|C|\le n^d\frac{2^n}{p_\mathrm{max}}\) occurs, where _d\>_2 is the fixed constant used in Line 2. When G occurs, the algorithm reaches Line 3. Let H denote the event that there exist \(X,Y\in C\) satisfying \(\sum(X)=\sum(Y)\). When H occurs, Lemma 5.3 finds such a pair in Line 3 with constant probability. Therefore, the probability that Algorithm 3 outputs a solution is at least a constant factor times \(\mathbb{P}[\mathcal{G}\cap\mathcal{H}]\).

By Line 1 of Algorithm 3 and Claim 5.6, we have \(p_\mathrm{max}\le|\Phi|\). From the assumptions on \(\ell\) and \(\alpha\), we also have \(p_\mathrm{max}=2^{\Theta(n)}\). Therefore, by Claim 5.7, with constant probability, \(|\{a\mathrm{mod}p|a\in\Phi\}|\ge\Omega(p/n^2)\). Conditioned on this event, the residue _r_ chosen in Line 1 of Algorithm 3 belongs to \(\{a\mathrm{mod}p|a\in\Phi\}\) with probability at least \(\Omega(1/n^2)\). Thus, we have<tbc>

\(\mathbb{P}[\mathcal{H}]\ge\Omega(1/n^2).\) (9)

<tbc>Let G_<sup>c</sup>_ denote the complement of G, namely the event that \(|C|>n^d\frac{2^n}{p_\mathrm{max}}\) occurs. By Claim 5.8 and Markov’s inequality, we have<tbc>

\(\mathbb{P}[\mathcal{G}^c]\le\frac{\mathbb{E}[|C|]}{n^d\cdot 2^n/p_\mathrm{max}}\le\frac{1}{n^d}.\) (10)

