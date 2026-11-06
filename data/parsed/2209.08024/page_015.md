**Lemma 4.2.** _For all n,_

\(\mathtt{cost}_{w_n}(C_n)=2^{\Delta+1}-1-(2^{\Delta+1}-2)\left(1-\frac{1}{2^\Delta}\right)^n.\) (4)

_Proof._ Denote _c<sub>n</sub>_=`cost`_<sub>w<sub>n</sub></sub>(C<sub>n</sub>_). Clearly _c_<sub>0</sub>=1 as required. Let _n\>_0. For each _i_, the subtree of all the descendants of _v<sub>i</sub>_ in _C<sub>n</sub>_ has weight 1/2<sup>_i_-1</sup>. Therefore

\(c_n=\sum_{i=1}^{\Delta+1}\frac{1}{2^{i-1}}+\sum_{i=1}^\Delta\frac{1}{2^i}c_{n-1}=2-\frac{1}{2^\Delta}+\left(1-\frac{1}{2^\Delta}\right)c_{n-1}.\)

It is straightforward to verify that the right hand side of Equation (4) is the solution to the recursive formula above.

In order to upper bound `OPT`(T_<sub>n</sub>,w<sub>n</sub>_) we construct recursively a search tree _T<sub>n</sub>_ on T_<sub>n</sub>_. For _n\>_0, _T<sub>n</sub>_ is constructed by setting \(v_{\Delta+1}\) as root and attaching to it \(\Delta\) copies of _T_<sub>_n_-1</sub>. The vertices \(v_1,\dots,v_\Delta\) are finally attached as leaves of _T<sub>n</sub>_, each at it’s unique valid place. See Figure 5 (right).

**Lemma 4.3.** _For all n,_

\(\mathtt{cost}_{w_n}(T_n)=2^\Delta-2^\Delta\left(1-\frac{1}{2^\Delta}\right)^{n+1}.\) (5)

_Proof._ Denote _t<sub>n</sub>_=`cost`_<sub>w<sub>n</sub></sub>(T<sub>n</sub>_). We have _t_<sub>0</sub>=1. For _n\>_0, _t<sub>n</sub>_ obeys the recursive relation

\(t_n=1+\sum_{i=1}^\Delta\frac{1}{2^i}t_{n-1}=1+\left(1-\frac{1}{2^\Delta}\right)t_{n-1},\)

of which the right hand side of Equation (5) is the solution.

_Proof of Theorem 1.4(i)._ Using Lemma 4.2 and Lemma 4.3,

\(\frac{\mathtt{cost}_{w_n}(C_n)}{\mathtt{OPT}(\mathcal{T}_n,w_n)}\ge\frac{\mathtt{cost}_{w_n}(C_n)}{\mathtt{cost}_{w_n}(T_n)}\rightarrow 2-\frac{1}{2^\Delta}.\)

Observe that, as discussed in Section 1, in the construction of Theorem 1.4(i), `OPT`(T_<sub>n</sub>,w<sub>n</sub>)/w<sub>n</sub>_(T_<sub>n</sub>_) is bounded.

## Part (ii).

To prove Theorem 1.4(ii), we repeat the recursive construction of Theorem 1.4(i) with a slight modification. As before, T<sub>0</sub> is a tree with a single vertex. For _n\>_0, (T_<sub>n</sub>,w<sub>n</sub>_) is constructed from \(\Delta\) weighted copies of (T<sub>_n_-1</sub>_,w_<sub>_n_-1</sub>) and \(\Delta-1\) additional vertices, \(v_1,\dots,v_{\Delta-1}\), each with weight 0, as shown in Figure 6 (left). We set \(\mathtt{root}(\mathcal{T}_n)=v_1\).

As before, the search tree _C<sub>n</sub>_ is defined by connecting the vertices \(v_1,\dots,v_{\Delta-1}\) to a path, setting _v_<sub>1</sub> as root and recursing on the remaining connected component. Observe that _C<sub>n</sub>_ is a centroid tree of (T_<sub>n</sub>,w<sub>n</sub>_). (See Figure 6 (middle).) The search tree _T<sub>n</sub>_ is defined by setting \(v_{\Delta-1}\) as root, attaching to it \(\Delta\) copies of _T_<sub>_n_-1</sub>, then adding the vertices \(v_1,\dots,v_{\Delta-2}\) as leaves, each at its unique valid place. See Figure 6 (right).

**Lemma 4.4.** _For all n,_

(_a)_ \(\mathtt{cost}_{w_n}(C_n)=\left(2-\frac{4}{2^\Delta}\right)\cdot n+1\),<tbc>

_(b)_ \(\mathtt{cost}_{w_n}(T_n)=n+1\).

The proof follows an analysis similar to that of Lemma 4.2 and Lemma 4.3.

