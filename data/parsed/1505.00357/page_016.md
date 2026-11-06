<tbc>**Lemma 13 (\[11, Lemma 2\]).** _For any node N in an optimal_ `gbst`_, N’s equality key is a least-frequent key among those in I<sub>N</sub> that aren’t equality keys in any of N’s subtrees: if e<sub>N</sub>=K<sub>i</sub>, then_ \(\beta_i=min\{\beta_j:K_j\in D_N\}\).

The proof is the same exchange argument that shows our Assumption 1(ii).

\[11\] claims (incorrectly) that, by Lemma 13, the desired value \(\mathsf{opt}(\mathcal{Q},\emptyset)\) can be computed as follows. For any key interval _I_={_K_<sub>_i_+1</sub>_,...,K<sub>j</sub>_} and \(d\le n\), let

\(p[i,j,d]=min\{\mathsf{opt}(I\backslash D):D\subseteq I,|D|=d\}\) (1)

be the minimum cost of any `gbst` for any query set _I_\\_D_ consisting of _I_ minus any _d_ deleted keys. Let _t_\[_i,j,d_\] be a corresponding subtree of cost _p_\[_i,j,d_\], and let _w_\[_i,j,d_\] be the weight of the root of _t_\[_i,j,d_\].

Their algorithm uses the following (incorrect) recurrence (their Lemma 4):

\(p[i,j,d]=min(w[i,j,d]+p[i,k-1,m]+p[k-1,j,d-m-1])\)

_where the minimum is taken over all legal combinations of k’s and m’s \[and\]_

\(w[i,j,d]=w[i,k-1,m]+w[k-1,j,d-m-1]+\beta_x\)

_where x is the index of the key of minimum frequency among those in range_ {_K_<sub>_i_+1</sub>_,...,K<sub>j</sub>_} _but outside t_\[_i,k_-1_,m_\] _and t_\[_k_-1_,j,d-m_+1\]_..."_

Next we describe their error. Recall that _p_\[_i,j,d_\] chooses a subtree of _minimum cost_ (among trees with any _d_ keys deleted). But this choice might not lead to minimum overall cost! The reason is that the subtree’s cost does not suffice to determine the contribution to the overall cost: the _weight_ of the subtree, and the weights of the deleted keys and their eventual locations, also matter.

For example, consider _p_\[_i,j,d_\] for the subproblem where _d_=2 and interval _I_ consists of the nine keys _I_={_A_1_,A_2_,A_3_,B_0_,B_4_,C_0_,D_0_,D_1_,E_0}, with the following weights:

\begin{tabular}{cccccccccc}
key: & _A_1 & _A_2 & _A_3 & _B_0 & _B_4 & _C_0 & _D_0 & _D_1 & _E_0 \\
weight: & 20 & 20 & 20 & 10 & 20 & 5 & 10 & 22 & 10 \\
\end{tabular}

B4 20
DI 22
(a)
A3 20
(b)
A3 20
T
A2 20
T
A2 20
A1 20
DI 22
A1 20
B4 20
B0 10
C0 5
DO 10
EO 10
BO 10
DO 10
EO 10
C0 5

**Fig.11.** Trees _T_, \(T'\) for 9-key interval _I_ with _d_=2. (Split keys not shown.)

