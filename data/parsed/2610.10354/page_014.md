_Moreover, given A and K, we can compute_ \(A'\) _in time_ \(\widetilde{O}(K^{12}|A|)\) _by a randomized algorithm._

The Asymmetric BSG Theorem was proved in the textbook by Tao and Vu \[TV06, Section 2.6\]. We need an algorithmic version of this theorem stated below, which we prove in Section 7.

**Theorem 2.4** (Asymmetric BSG Theorem)**.** _Let_ \(\epsilon>0\) _and_ \(0<\alpha\le 1\)_. Let_ \(A,B\subseteq\mathbb{Z}\) _be sets with energy_ \(E(A,B)\ge\alpha|A|^2|B|\)_. Then there are sets_ \(H,\Lambda\subseteq\mathbb{Z}\) _and some_ \(K\le O_\epsilon(\alpha^{-O_\epsilon(1)}(1+|B|/|A|)^\epsilon)\) _such that:_

• \(|H+H|\le K|H|\),<tbc>

• \(|H||\Lambda|\le K|B|\),<tbc>

• \(|A\cap H|\ge|A|/K\) _and_ \(|B\cap(H+\Lambda)|\ge|B|/K\).

_Moreover, there is a randomized algorithm to compute_ \(H,\Lambda\) _in time_ \(\widetilde{O}((|A|+|B|)K)\).

Related to these tools, we will also need to compute approximations of sumset multiplicities.

**Lemma 2.5** (Approximating Sumset Multiplicities)**.** _There is a randomized algorithm that, given sets A,B,C and_ \(\epsilon>0\)_, computes approximations_ \(\tilde{r}(x)\)_, for all_ \(x\in C\)_, with additive error_

\(|r_{A+B}(x)-\tilde{r}(x)|\le\epsilon|A|.\)

_The algorithm runs in time_ \(\widetilde{O}(|A|+|B|/\epsilon+|C|)\).

A proof of Lemma 2.5 can be found in \[FJX25,  6\]. See \[FJX25, Corollary 3.1\] for a derandomization of this algorithm.

## 2.2 Problem Definitions

As is common in fine-grained complexity, hardness hypotheses and reductions implicitly allow Monte-Carlo randomization (though there has been some interest in derandomizing 3SUM-related reductions \[CH20, FKP24\]).

**Definition 2.6** (3SUM)**.** Given three sets of integers _A,B,C_, determine whether there exists \(a\in A,b\in B,c\in C\) such that _a+b=c_. In its All-Integer version we need to determine for every number in the input, whether it participates in a solution _a+b=c_.

We use 3SUM(_n_) to denote the running time of 3SUM instances with size-_n_ inputs. We also use \(3SUM(n|r\le R)\) to denote the running time of 3SUM instances where the rank (Definition 1.3) of one of the sets is at most _R_, and such a rank decomposition is given. A subinstance of a 3SUM instance with input (_A,B,C_) is another 3SUM instance with input \((A',B',C')\) where \(A'\subseteq A,B'\subseteq B,C'\subseteq C\).

**Definition 2.7** (Min-Plus Convolution)**.** Given two sequences \(A,B\in\mathbb{Z}^{[0,n]}\), compute a sequence \(C=A*B\in\mathbb{Z}^{[0,2n]}\), where _C_\[_k_\]=min<sub>_i+j=k_</sub>{_A_\[_i_\]+_B_\[_j_\]}.

We use MPConv(_n_) to denote the running time of Min-Plus Convolution instances with size-_n_ inputs. We also use \(MPConv(n|u\le U)\) to denote the running time of Min-Plus Convolution instances where the entries are from \[_U_\].

