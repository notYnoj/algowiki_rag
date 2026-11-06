that we can uniquely associate a unique \(\pi\)-avoiding \(n\times n\) permutation matrix to each \(\pi\)-avoiding permutation sequence of length _k_. Then we can use the upper bound on the number of \(\pi\)-avoiding permutation matrices by Cibulka \[Cib09\] to see that the number of non-order-isomorphic \(\pi\)-avoiding permutation sequences of length _k_ is at most \((2.88c_\pi^2)^n\).

Similarly, each general \(\pi\)-avoiding sequence corresponds to a unique \(\pi\)-avoiding \(n\times m\) matrix where \(m\le n\), each column contains exactly one 1-entry and each row contains at least one 1- entry. We show that the number of such matrices is bounded in a similar way. In fact, we prove a stronger claim by bounding the number of all \(\pi\)-avoiding \(n\times n\) matrices with exactly _n_ 1-entries. Let \(T_\pi(m,n)\) denote the set of all \(\pi\)-avoiding \(m\times m\) matrices with exactly _n_ 1-entries.

Cibulka \[Cib09\] claims that arguments similar to his proof relating together the Stanley-Wilf and Füredi-Hajnal limits can be used to show that \(\vee^n\sqrt{|T_\pi(n,n)|}\in O(c_\pi^2)\). Unfortunately, he does not provide any further justification. Therefore, we include a self-contained proof of this fact.

**Theorem 4.5.** _For every pattern_ \(\pi\) _and every_ \(n\in\mathbb{N}\)_, we have_ \(|T_\pi(n,n)|\le(240c_\pi^2)^n\).

_Proof._ We assume that \(c_\pi\ge 1\), since otherwise \(\pi\) is the singleton permutation and \(T_\pi(n,n)=\emptyset\) for every \(n\ge 1\).

The first part of the argument follows the reduction of Klazar \[Kla00\]. Let \(T_\pi(n)\) denote the set of all \(\pi\)-avoiding \(n\times n\) matrices, regardless of the number of 1-entries. We show by induction that for every _i_, we have \(|T_\pi(2^i)|\le 15^{c_\pi\cdot 2^i}\). This clearly holds for _i_=0, so let \(i\ge 1\). Observe that every matrix \(M\in T_\pi(2^i)\) can be obtained from some matrix \(M'\in T_\pi(2^{i-1})\) by replacing each entry \(\alpha\) with a \(2\times 2\) block that is all-zero if and only if \(\alpha=0\). Moreover, by the Marcus-Tardos theorem\[MT04\] there are at most \(c_\pi\cdot 2^{i-1}\) 1-entries in \(M'\) and for each of them, there are exactly 15 possible \(2\times 2\) blocks to choose from. Thus, we get

\(|T_\pi(2^i)|\le 15^{c_\pi\cdot 2^{i-1}}\cdot|T_\pi(2^{i-1})|\le 15^{c_\pi\cdot 2^{i-1}}\cdot 15^{c_\pi\cdot 2^{i-1}}\le 15^{c_\pi\cdot 2^i}\)

Set \(a=\lfloor log(n/c_\pi)\rfloor\) and observe that \(\frac{n}{2c_\pi}\le 2^a\le\frac{n}{c_\pi}\). In order to simplify the arguments, we bound \(|T_\pi(m,n)|\) where \(m=2^{a+1}\cdot c_\pi\). The desired bound on \(|T_\pi(n,n)|\) follows since \(m\ge n\) and \(|T_\pi(\cdot,n)|\) is a non-decreasing function. Similarly to before, every matrix \(M\in T_\pi(m,n)\) can be obtained from some \(M'\in T_\pi(2^a)\) by replacing each entry \(\alpha\) with a \(2c_\pi\times 2c_\pi\) block that is all-zero if and only if \(\alpha=0\).

We encode _M_ from \(M'\) in two steps. First, we distribute all _n_ 1-entries of _M_ among the blocks obtained from the 1-entries of \(M'\). This is the standard problem of counting the number of ways to distribute indistinguishable balls into bins. By the Marcus-Tardos theorem\[MT04\], the matrix \(M'\) contains at most \(c_\pi\cdot 2^a\le n\) 1-entries. Therefore, the number of ways to distribute the 1-entries of _M_ into the blocks obtained from the 1-entries of \(M'\) is at most \(\genfrac(){pt}{2}{2n-1}{n}\le 4^n\).

At this point, we know how the _n_ 1-entries of _M_ are distributed among the \(2c_\pi\times 2c_\pi\) blocks. It remains to encode the specific location of each 1-entry within its assigned block. There are \((2c_\pi)^2\) possibilities for each 1-entry, making a total of \((2c_\pi)^{2n}\). Putting everything together, we obtain

\(|T_\pi(n,n)|\le|T_\pi(m,n)|\le|T_\pi(2^a)|\cdot 4^n\cdot(2c_\pi)^{2n}\le 15^{c_\pi\cdot\frac{n}{c_\pi}}\cdot 16^n(c_\pi^2)^n\le(240c_\pi^2)^n.\)

This wraps up the proof of Theorem 4.1.

## 5 The algorithm

We can finally assemble the asymptotically optimal algorithm by combining the merging algorithm obtained in Section 3 and the algorithm for sorting many short sequences obtained in Section 4.

