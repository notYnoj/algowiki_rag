1. it is already recorded by the bicliques contributing to _M_<sub>1</sub>;<tbc>

2. it belongs to a certified pair inside some subproblem \(T(m',n')\);<tbc>

3. it is an uncertain pair.

<tbc>By Lemma 5, the bicliques contributing to _M_<sub>2</sub> record at least one half of all certified pairs inside the subproblems. Therefore,<tbc>

\(M_2\ge\frac{|S\cap I|-M_1-N}{2}.\)

<tbc>Using _M=M_<sub>1</sub>+_M_<sub>2</sub>, we obtain<tbc>

\(M=M_1+M_2\ge M_1+\frac{|S\cap I|-M_1-N}{2}=\frac{M_1+|S\cap I|-N}{2}\ge\frac{|S\cap I|-N}{2}.\)

<tbc>Since \(N\le(c/c_1)|S\cap I|\),

\(M\ge\frac{1}{2}\left(1-\frac{c}{c_1}\right)|S\cap I|.\)

Choosing \(c_1\ge 5c\) yields \(M\ge 0.4|S\cap I|\). This proves (7). Together with the running-time and representation-size bounds established earlier, this completes the proof of Theorem 3.

## 5 Distance selection

In this section, we combine the quasi-decision theorem (Theorem 2) and the distance representation theorem (Theorem 3) to obtain a deterministic _O(n_<sup>4/3</sup>)-time algorithm for distance selection.

Recall that \(S=\{\|ab\|:a\in A,b\in B\}\). Given an integer _K_, our goal is to compute the _K_-th smallest distance in _S_, denoted by \(\delta^*\).

The algorithm proceeds in phases. Throughout the execution, we maintain an interval _I_ containing \(\delta^*\). For _i_=1,2_,...,O_(log<sup>∗</sup>_n_), the goal of the _i_-th phase is to transform an interval _I_ satisfying<tbc>

\(|S\cap I|=O\big(n^{4/3}(log^{(i-1)}n)^4\big)\)

<tbc>(and _O(n_<sup>2</sup>) when _i_=1) and containing \(\delta^*\) into a smaller interval \(I'\subseteq I\) such that

\(|S\cap I'|=O\big(n^{4/3}(log^{(i)}n)^4\big)\)

and \(\delta^*\in I'\).

Initially, we have \(I=(0,+\infty)\), and hence \(|S\cap I|=O(n^2)\). After _O_(log<sup>∗</sup>_n_) phases, we obtain an interval _I_ satisfying \(|S\cap I|=O(n^{4/3})\) and containing \(\delta^*\). A final _distance-reporting_ step then computes \(\delta^*\) from \(S\cap I\) in additional _O(n_<sup>4/3</sup>) time.

We will show that the _i_-th phase consists of _O_(log<sup>(_i_)</sup>_n_) iterations. Each iteration, which reduces the remaining candidate distances by a constant fraction, takes _O(n_<sup>4/3</sup>/log<sup>(_i_)</sup>_n_) time for _i_=1,2, and _O(n_<sup>4/3</sup>/(log<sup>(_i_)</sup>_n_)<sup>2</sup>) time for \(i\ge 3\). Consequently, each of the first two phases runs in _O(n_<sup>4/3</sup>) time, while the _i_-th phase for \(i\ge 3\) runs in _O(n_<sup>4/3</sup>/log<sup>(_i_)</sup>_n_) time. Therefore, the total time spent over all phases is

\(O(n^{4/3})\cdot\left(1+\sum_{i=3}^{O(log^*n)}\frac{1}{log^{(i)}n}\right),\)

which is _O(n_<sup>4/3</sup>). Including the final distance-reporting step, the overall running time remains _O(n_<sup>4/3</sup>).

In what follows, we first describe the algorithm in Section 5.1 and then prove its correctness in Section 5.2.

