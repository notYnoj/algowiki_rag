We omit the proof of Lemma 2.14 here since it is standard. We refer readers to \[Fis26, Section 5.1\] for a proof in the analogous setting of Min-Plus Matrix Product, which can be adapted to Min- Plus Convolution in a straightforward manner. The same proof strategy also applies to Min-Max Convolution and Min-Equality Convolution.<sup>8</sup>

The same sampling strategy together with FFT yields the following more well-known lemma for listing witnesses of Boolean Convolution:

**Lemma 2.15.** _Given two sequences_ \(A,B\in\{0,1\}^{[0,n]}\) _and a threshold_ \(t\ge 1\)_, one can compute their Boolean Convolution_ \(C\in\{0,1\}^{[0,2n]}\) _defined as_ \(C[k]=\vee_{i+j=k}(A[i]\wedge B[j])\)_, and additionally, for each k, list up to t witnesses i such that A_\[_i_\]=_B_\[_k-i_\]=1_, in_ \(\widetilde{O}(tn)\) _time._

## 3 Popular _k_-Sum Structure

The goal of this section is to prove Theorem 1.2. We start with some basic definitions and facts.

**Definition 3.1** (Popular _k_-Sums)**.** Let \(A_1,\dots,A_k\subseteq\mathbb{Z}\), and _p\>_0. The set Pop(_A_<sub>1</sub>_,...,A<sub>k</sub>;p_) consists of all integers _x_ that can be expressed in at least _p_ distinct ways as

\(x=a_1+\cdots+a_k\)

for \((a_1,\dots,a_k)\in A_1\times\cdots\times A_k\); we call these the _p-popular k-sums_. When \(A=A_1=\cdots=A_k\), we simply write Pop_<sup>k</sup>(A;p_).

The following simple observation will be useful later.

**Observation 3.2.** _If_ \(\mathrm{Pop}(A_1,\dots,A_k;p)\neq\emptyset\) _then_ \(\mathrm{Pop}(A_2,\dots,A_k;p/|A_1|)\neq\emptyset\).

**Theorem 1.2** (Popular _k_-Sums Imply Low-Doubling Structure)**.** _For every c\>_0 _and_ \(\epsilon>0\)_, there is some_ \(k=k(c,\epsilon)\) _such that the following holds. Let_ \(A\subseteq\mathbb{Z}\) _and assume that_ \(\mathrm{Pop}^k(A;p)\neq\emptyset\) _for some_ \(p=\Omega(|A|^{k-1-c})\)_. Then there exists a set_ \(H\subseteq\mathbb{Z}\) _and some_ \(K=O_{c,\epsilon}(|A|^\epsilon)\) _such that:_

• \(|H|\le K|A|^{1+c}\),<tbc>

• \(|H+H|\le K|H|\),<tbc>

• \(|A\cap H|\ge|A|/K\).

The following lemma is based on simple random sampling. Its version for _k_=2 has been considered before (e.g., \[JX23\]).

**Lemma 3.3** (Approximating Popular Sums)**.** _There is a randomized algorithm that, given sets_ \(A_1,\dots,A_k\subseteq\mathbb{Z}\) _and an integer threshold_ \(p\ge 1\)_, computes a set P such that_

\(\mathrm{Pop}(A_1,\dots,A_k;2p)\subseteq P\subseteq\mathrm{Pop}(A_1,\dots,A_k;p)\)

<sup>8</sup>En route we rely on a sampling-based approach, which requires setting some input values to \(\perp\), so that they cannot be used in any solution (see \[Fis26, Section 5.1\]). In the problems we consider, \(\perp\) can be replaced with actual numbers without heavily affecting the problem sizes. In Min-Plus Convolution with universe \[_u_\], we can simply set \(\perp\) to 2_u_+1, so they can never participate in a solution with value less than or equal to 2_u_, while all the solutions obtained from non-\(\perp\) values have value at most 2_u_. Similarly, in Min-Max Convolution with universe \[_u_\], we can simply set \(\perp\) to _u_+1. In Min-Equality Convolution, we can set \(\perp\) in _A_ and in _B_ to be two different special values that do not occur in the non-\(\perp\) values of _A,B_.

