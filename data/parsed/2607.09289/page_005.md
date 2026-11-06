We may also use the following fact to remove floors and ceilings in the \(O^*(\cdot)\) notation.

**Fact 2.2** (\[32, eq.(4)\])**.** _For any_ \(x,y\in[0,1]\)_, we have_ \(|H(x)-H(y)|\le H(|x-y|)\)_. Consequently, if_ \(x,y\in[0,1]\) _satisfy_ \(|x-y|\le O(1/n)\)_, then_ \(|H(x)-H(y)|\le O((logn)/n)\).

We adopt the input assumptions from \[25\]: the input set _S_ consists of positive integers and satisfies \(\sum(S)\le 2^{O(n)}\). We enforce these assumptions using the following preprocessing lemma, which is based on \[25, Appendix A of the full version\]. For completeness, we provide a proof in Appendix A of this paper.

**Lemma 2.3.** _Given a set S of n integers satisfying_ \(|s|\le 2^m\) _for all_ \(s\in S\)_, the following holds. If_ \(0\in S\) _or_ \(m\ge 2^n\)_, then ESS on S can be solved in O_(poly(_n,m_)) _time. Otherwise, with probability at least_ 1-_O_(2<sup>-_n_</sup>)_, we can construct, in O_(poly(_n,m_)) _time, a set_ \(S'\) _of_ \(n+\lceil logn\rceil\) _positive integers satisfying_ \(0<s'\le 2^{O(n)}\) _for all_ \(s'\in S'\)_, and satisfying the following properties: if_ \(S'\) _has no ESS solution, then neither does S; conversely, from any ESS solution of_ \(S'\)_, we can reconstruct a corresponding ESS solution of S in O_(poly(_n,m_)) _time._

Lemma 2.3 increases the input size by only _O_(log_n_). Thus, a running time of the form \(O^*(2^{\Theta(n)})\) changes only by a factor of 2<sup>_O_(log_n_)</sup>=poly(_n_), which is absorbed in the \(O^*(\cdot)\) notation.

For simplicity, we also assume that _n_ is divisible by 12. This can be achieved by setting \(M=\sum(S)+1\) and adding _O_(1) elements of the form _M,_2_M,_4_M,_8_M,..._ to _S_. We define a minimum solution as follows.

**Definition 2.4** (Minimum solution)**.** For an ESS instance with input set _S_, a solution \(A,B\subseteq S\) is called a minimum solution if |_A_|+|_B_| is minimized. We refer to the value |_A_|+|_B_| as the minimum solution size, denoted by \(\ell\), and define the minimum solution ratio as \(\ell'=\ell/n\).

By trying all possible values \(\ell\in[n]\), we incur only a polynomial overhead. If no execution finds a solution, then the algorithm reports that the instance is a No instance. Thus, in the following, we may assume that the minimum solution size \(\ell\) is given in advance.

When analyzing the bounds in terms of the minimum solution ratio \(\ell'\), we may upper-bound the running time and space usage by maximizing over the continuous interval (0,1\], instead of the discrete set {1_/n,_2_/n,...,(n_-1)_/n,_1} of possible values of \(\ell'\).

## 3 Faster Exponential-Space Algorithm

We first describe a modification of the input instance that may reduce the number of integers required to represent a solution. The algorithm randomly selects a subset of the input integers, partitions them into disjoint pairs, and replaces each pair with its sum and difference, as shown in Algorithm 1. In Lemma 3.1, we show that an ESS solution for the modified instance can be transformed into a valid ESS solution for the original instance under a certain condition.

\(\text{\textbf{Algorithm 1:} RandomReplace
\textbf{Input:} Input set S and replacement count k
\textbf{Output:} Modified set}S'\text{and the set of new elements}E=\{e_1,\dots,e_{2k}\}\text{Randomly select a subset}D\subseteq S\text{consisting of}2k\text{elements, and partition it arbitrarily into}k\text{disjoint pairs. Denote the}i\text{-th pair by}(x_i,y_i)\text{, where we relabel the elements so that}x_i>y_i\text{for each}i\in[k]\text{. \textbf{2 For each}}i\in[k]\text{, define}e_{2i-1}=x_i+y_i\text{, and}e_{2i}=x_i-y_i\text{. Let}E=\{e_1,\dots,e_{2k}\}\text{. \textbf{3 Construct the modified set}}S'=(S\backslash D)\cup E\text{.}\)

