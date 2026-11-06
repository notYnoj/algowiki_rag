## 1.4 Structure of the paper

Section 2 describes a _rotation_ and related concepts in smi that will be used later in the paper. Sections 3 and 4 describe Algorithm REDI and Algorithm MRS respectively, giving in each case pseudocode, correctness proofs and time complexity calculations. An experimental evaluation is given in Section 5. Finally, future work is presented in Section 6.

## 2 Structure of stable matchings

For some stable matching _M_ in an instance _I_ of smi, let _s(mi,M_) denote the next woman on _mi_’s preference list (starting from _M(mi_)) who prefers _mi_ to _M(s(mi,M_)) (their partner in _M_). A _rotation_ \(\rho\) is then a sequence of man-woman pairs {(_m_<sub>1</sub>_,w_<sub>1</sub>),(_m_<sub>2</sub>_,w_<sub>2</sub>)_,...,(m<sub>q</sub>,w<sub>q</sub>_)} in _M_, such that _m_<sub>_i_+1</sub>=_M(s(mi,M_)) for \(1\le i\le q\) where addition is taken modulo _q_ [12]. We say rotation \(\rho\) is _exposed_ on _M_ if \(\{(m_1,w_1),(m_2,w_2),\dots,(m_q,w_q)\}\subseteq M\). If \(\rho\) is exposed on _M_, we may _eliminate_ \(\rho\) on _M_, that is, remove all pairs of \(\rho\) from _M_ and add pairs (_mi,w_<sub>_i_+1</sub>) for \(1\le i\le q\), where addition is taken modulo _q_, in order to produce another stable matching \(M'\) of _I_. The _rotation poset R<sub>p</sub>(I_) of _I_ indicates the order in which rotations may be eliminated. Rotation \(\rho\) is said to _precede_ rotation \(\tau\) if \(\tau\) is not exposed until \(\rho\) has been eliminated. There is a one-to-one correspondence between the set of stable matchings and the set of closed subsets of _R<sub>p</sub>(I_) [12, Theorem 3.1]. Gusfield and Irving [9] describe a graphical structure known as the _rotation digraph R<sub>d</sub>(I_) of _I_ which is based on _R<sub>p</sub>(I_) and allows for the enumeration of all stable matchings in _O(m+n_|M|) time.

Let _R_ be the set of rotations of _I_. Then _R<sub>j</sub>(M_) is the set of rotations that contain a women of rank _j_ in _M_, that is, \(R_j(M)=\{\sigma\in R:(m,w)\in\sigma\wedge\text{rank}(w,M(w))=j)\}\). Let _M<sub>z</sub>_ be the woman-optimal stable matching [5]. For any stable pair \((mi,w_j)\notin M_z\), let \(\phi(mi,w_j)\) denote the unique rotation containing pair (_mi,w<sub>j</sub>_). Finally, denote by \(c(\rho)\) the closure of rotation \(\rho\) and similarly denote by \(c(R')\) the closure of set of rotations \(R'\). We say that the closure of an undefined rotation or an empty set of rotations is the empty set.

## 3 Algorithm to find a regret-equal stable matching in SMI

### 3.1 Description of the Algorithm

Algorithm REDI, which finds a regret-equal stable matching in a given instance _I_ of smi, is presented as Algorithm 1. For an instance _I_ of smi, Algorithm REDI begins with operations to find the man-optimal and woman-optimal stable matchings, _M_<sub>0</sub> and _M<sub>z</sub>_, found using the Man-oriented and Women-oriented Gale-Shapley Algorithm [5]. The set of rotations _R_ is also found using the Minimal Differences Algorithm [12].

Let _d(M_<sub>0</sub>)=(_a_<sub>0</sub>_,b_<sub>0</sub>). If _a_<sub>0</sub>=_b_<sub>0</sub> then we must have an optimal stable matching and so we output _M_<sub>0</sub> on Line 5. If _a_<sub>0</sub>_\>b_<sub>0</sub> then any other matching \(M'\), where \(d(M')=(a',b')\), must have \(a'\ge a_0\) and \(b'\le b_0\) since any rotation (or combination of rotations) eliminated on the man-optimal matching _M_<sub>0</sub> will make men no better off and women no worse off. Therefore _M_<sub>0</sub> is optimal and so it is returned on Line 5. Now suppose _a_<sub>0</sub>_\<b_<sub>0</sub>. Throughout the algorithm we save the best matching found so far to the variable _M<sub>opt</sub>_ starting with _M_<sub>0</sub>. We know that a matching exists with _d_<sub>0</sub>=_b_<sub>0</sub>-_a_<sub>0</sub> and so we try to improve on this, by finding a matching _M_ with _r(M)\<d_<sub>0</sub>.

We create several ‘columns’ of possible degree pairs of a regret-equal matching as follows. The top-most pairs for columns \(k\ge 1\) are given by the sequence

\(\big((a_0,b_0),(a_0+1,b_0),(a_0+2,b_0),\dots,(min\{n,2b_0-a_0-1\},b_0)\big).\)

