We also get improved results for the Hamming distance, which is a more basic measure trivially computable in _O(N_) time. Here, we present an \(O(n\sqrt{N})\)-time algorithm which improves upon the _O(n_<sup>1.41</sup>_N_<sup>0.593</sup>) bound of \[ABBK17\]. Additionally, we note that natural generalizations to multiple strings (including the median Hamming distance) can be computed in _O(nN_<sup>1-1_/k_</sup>) time.

## 2 Preliminaries

For two integers \(i\le j\), we write \[_i...j_\] to denote the set {_i,...,j_} and \[_i...j_) to denote {_i,...,j_-1}. The notions (_i...j_\] and (_i...j_) are defined analogously.

A _string_ is a sequence of characters from a fixed alphabet \(\Sigma\). We write \(\Sigma^*\) to denote the set of all strings over \(\Sigma\), and we define \(\Sigma^+=\Sigma^*\backslash\{\gamma\}\), where \(\gamma\) denotes the empty string. The length of a string _X_ is denoted by |_X_| and, for a position \(i\in[1..|X|]\) in _X_, the character of _X_ at position _i_ is denoted by _X_\[_i_\]. For an integer \(N\ge 0\), the set of length-_N_ strings over \(\Sigma\) is denoted by \(\Sigma^N\).

For two positions \(i\le j\) in _X_, we write _X_\[_i...j_\] to denote the fragment of _X_ starting at positions _i_ and ending at position _j_; this fragment is an occurrence of \(X[i]\cdots X[j]\) as a substring of _X_. The fragments _X_\[_i...j_\], _X(i...j_\], and _X(i...j_) are defined similarly.

A morphism is a function \(f:\Sigma_1^*\rightarrow\Sigma_2^*\) such that \(f(X)=\circlearrowleft_{i=1}^{|X|}f(X[i])\), where \(\circlearrowleft\) denotes the concatenation operator. Note that every function mapping \(\Sigma_1\) to \(\Sigma_2^*\) can be uniquely extended to a morphism.

### 2.1 Straight-Line Programs

A straight-line program is a tuple \(\mathbf{G}=(\mathbf{S},\Sigma,\text{rhs},S)\), where **S** is a finite sequence of _symbols_, \(\Sigma\subseteq\mathbf{S}\) is a set of _terminal symbols_, \(\text{rhs}:(\mathbf{S}\backslash\Sigma)\rightarrow\mathbf{S}^*\) is the _production_ (or _right-hand side_) function, and \(S\in\mathbf{S}\) is the start symbol, and the symbols in **S** are ordered so that _B_ precedes _A_ if _B_ occurs in rhs(_A_). We also write \(A\rightarrow B_1\cdots B_k\) instead of \(\text{rhs}(A)=B_1\cdots B_k\).

The set \(\mathbf{S}\backslash\Sigma\) of _non-terminals_ is denoted by **N**. The size of **G** is \(|\mathbf{G}|:=|\mathbf{S}|+\sum_{A\in\mathbf{N}}|\text{rhs}(A)|\): the number of symbols plus the total length of productions. The _expansion_ function \(\mathrm{exp}:\mathbf{S}\rightarrow\Sigma^+\) is defined recursively:

\(\mathrm{exp}(A)=\left\{\begin{array}{ c c }
A & \text{if}A\in\Sigma, \\
\circlearrowleft_{i=1}^k\mathrm{exp}(B_i) & \text{if}A\rightarrow\circlearrowleft_{i=1}^kB_i.
\end{array}\right.\)

We say that **G** is a _grammar-compressed representation_ of exp(_S_). The exp function naturally extends to a morphism \(\mathrm{exp}:\mathbf{S}^*\rightarrow\Sigma^*\) with \(\mathrm{exp}(\circlearrowleft_{i=1}^mA_i)=\circlearrowleft_{i=1}^m\mathrm{exp}(A_i)\).

For a symbol \(A\in\mathbf{S}\), we denote |_A_|=|exp(_A_)|. In this work, we assume a word RAM machine with machine words of \(\Omega(\mathrm{log}|S|)\) bits. In this setting, one can compute |_A_| for all \(A\in\mathbf{S}\) in _O_(|**G**|) time. Consequently, we assume that |_A_| is stored along with _A_ in the straight-line programs given to our algorithms.

A straight-line program **G** is in _Chomsky normal form_ if |rhs(_A_)|=2 for all \(A\in\mathbf{N}\). Given an arbitrary straight-line program **G**, an equivalent straight-line program \(\mathbf{G}'\) in Chomsky normal form can be constructed in _O_(|**G**|) time; moreover, \(|\mathbf{G}|=O(|\mathbf{G}'|)\). Thus, without loss of generality, we assume that all straight-line programs given to our algorithms are already in the Chomsky normal form.

## 3 FPTAS for Compressed Edit Distance of Two Strings

The edit distance \(\delta_E(X,Y)\) of two strings \(X,Y\in\Sigma^*\) is defined as the minimum number of character insertions, deletions, and substitutions needed to transform _X_ into _Y_ .

In this section, we prove the following result.

**Theorem 3.1.** _Given a straight-line program_ **G**_<sub>X</sub> of size n generating a string X of length N\>_0_, a straight-line program_ **G**_<sub>Y</sub> of size m generating a string Y of length M\>_0_, and a parameter_ \(\epsilon\in(0,1]\)_, an integer between_ \(\delta_E(X,Y)\) _and_ \((1+\epsilon)\delta_E(X,Y)\) _can be computed in_ \(\bar{O}\left((nm(N+M))^{2/3}\epsilon^{-1/3}\right)\) _time._

Let \(\$\notin\Sigma\) and let \(\cdot^\$:\Sigma^*\rightarrow(\Sigma\cup\{\$\})^*\) be a morphism defined with _a_<sup>$</sup>=_a_$ for \(a\in\Sigma\). Then, \(\delta_E(X,Y)=\frac{1}{2}\delta_D(X^\$,Y^\$)\) \[Tis15\]. Moreover, if _X_ is represented by a straight line program **G**, then _X_<sup>$</sup> can be represented using a straight-line program of size 2|**G**|+1. This reduction allows computing \(\delta_D\) instead of \(\delta_E\).

