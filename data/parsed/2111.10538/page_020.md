tuples (Lemma 3.7). Whenever this is the case, w.h.p. over the sub-sampling procedure, \(\mathsf{NF}_\lambda\) does not contain any undetected-constructive tuples (Claim 3.8).

The second part of the proof assumes by contradiction that \(\mathsf{NG}_\lambda\) is dense. It uses this assumption to conclude that \(\mathsf{NF}_\lambda\) is also dense (w.h.p. over the sub-sampling procedure, see Claim 3.9), and therefore by Turan’s Theorem contains a large bi-clique (Claim 3.11). Finally, we use the large bi-clique to show that \(\mathsf{NF}_\lambda\) does contain an undetected-constructive tuple (Lemma 3.12) - a contradiction!

## 3.1.1 Proof of Lemma 3.4, part 1: \(\mathsf{NF}_\lambda\) does not contain an undetected-constructive tuple

We first introduce the notion of "well-connected pairs".

**Definition 3.6** (well-connected pair)**.** We say that a pair of windows (_w<sub>i</sub>,w<sub>j</sub>_) is _well-connected_ if there are at least \(k^{2-\gamma}\) pairs of windows (_w<sub>a</sub>,w<sub>b</sub>_) such that \(\langle w_i,w_a,w_b,w_j\rangle\) is \((\epsilon,\lambda)\)-constructive.

We argue that well-connected pairs are detected in our algorithm with high probability.

**Lemma 3.7.** _Let_ \(\widehat{\mathsf{O}}_{\lambda^2}\in\{0,1\}^{k\times k}\) _denote the output of Algorithm 1. With probability at least_ 1-2_/k_<sup>3</sup>_, for all_ \((i,j)\in[k]\times[k]\) _such that_ (_w<sub>i</sub>,w<sub>j</sub>_) _is a well-connected pair (Definition 3.6), we have_ \(\widehat{\mathsf{O}}_{\lambda^2}[i][j]=1\).

_Proof._ We consider a fixed (_i,j_) such that pair (_w<sub>i</sub>,w<sub>j</sub>_) is well-connected. Let

\(Q_{i,j}=\left\{(a,b)\middle|\left\|\mathsf{opt}_{i,a}\cap\mathsf{opt}_{a,b}\cap\mathsf{opt}_{b,j}\right\|\ge(1-\epsilon)\lambda^3\right\}.\)

Conceptually, we divide the process of sampling _S_ into two phases: we sample \(20k^\gamma logk\) windows in the first phase, and then we sample \(20k^\gamma logk\) more windows in the second phase.

For each \(a\in[k]\), let \(Q_{i,j,a}=\{b:(a,b)\in Q_{i,j}\}\). Since \(\sum_{a\in[k]}|Q_{i,j,a}|=|Q_{i,j}|\ge k^{2-\gamma}\), there are at least \(\frac{k^{1-\gamma}}{2}\) different number _a_’s in \[_k_\] such that \(|Q_{i,j,a}|\ge\frac{k^{1-\gamma}}{2}\) . Hence, in the first phase, there is a sampled number _q_ such that \(|Q_{i,j,q}|\ge k^{1-\gamma}/2\) with probability at least<tbc>

\(1-\left(1-\frac{k^{1-\gamma}/2}{k}\right)^{20k^\gamma logk}>\frac{k^5-1}{k^5}.\)

<tbc>We fix such a _q_. In the second phase, there is a sampled number _r_ such that \(r\in Q_{i,j,q}\) with probability at least

\(1-\left(1-\frac{k^{1-\gamma}/2}{k}\right)^{20k^\gamma logk}>\frac{k^5-1}{k^5}.\)

Since the number of (_i,j_) pairs is at most _k_<sup>2</sup>, the lemma is obtained by a union bound on all the well-connected pairs (_w<sub>i</sub>,w<sub>j</sub>_).

We complete the first part of the proof by showing that with probability at least 0.99, \(\mathsf{NF}_\lambda\) does not have an undetected-constructive tuple.

**Claim 3.8** (\(\mathsf{NF}_\lambda\) has no undetected-constructive tuple)**.** _With probability at least_ 0.99_, there is no undetected-constructive tuple in_ \(\mathsf{NF}_\lambda\).

