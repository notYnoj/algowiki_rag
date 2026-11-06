To start, if all the strings _a_<sub>1</sub>_,...,a<sub>d</sub>_ begin with the same character, then the following inequality holds:

\(\mathbf{w}_\mathbf{n}[a_1,\dots,a_d]\ge\)<br>
\(1+\frac{1}{|\Sigma^d|}\sum_{(c_1,\dots,c_d)\in\Sigma^d}\mathbf{w}_{\mathbf{n}-\mathbf{d}}[T(a_1)c_1,\dots,T(a_d)c_d]\) (2.2)

This inequality states that if all the strings start with the same character, then the expected length of the LCS of all of them, permitting _n_ random extra characters, is at least 1 (the first character) plus the average of the expected length of the LCS of the strings obtained by removing the first character and adding _d_ of the _n_ random characters \[16\].

If all the strings do _not_ begin with the same character, then we must take a more complicated approach. For this purpose, we define a function _F<sub>z</sub>_ which computes the expected length of an LCS of the strings _A_=(_a_<sub>1</sub>_,...,a<sub>d</sub>_) when discarding the first character of all strings not beginning with _z_ and adding to their end a random character from \(\Sigma\).

Algorithm 2.1. Calculating _F<sub>z</sub>_

function _F<sub>z</sub>_(**v<sub>1</sub>**_,...,_**v<sub>d</sub>**_,A_)<br>
   \(r\leftarrow 0\)<br>
   \(N\leftarrow(j|j\in(1,\dots,d),h(s_j)\neq z)\)<br>
   for \((c_1,\dots,c_{|N|})\in\Sigma^{|N|}\)<br>
   \((s_1,\dots,s_d)\leftarrow(a_1,\dots,a_d)\)<br>
   for \(j\in\{1,\dots,|N|\}\)<br>
   \(s_{N[j]}\leftarrow T(s_{N[j]})c_j\)<br>
   \(r\leftarrow r+\mathbf{v}_{|\mathbf{N}|}[s_1,\dots,s_d]\)<br>
   return \(\sigma^{-|N|}\cdot r\)

Here, _N_ is an ordered set containing the positions of strings in the tuple (_a_<sub>1</sub>_,...,a<sub>d</sub>_) that do _not_ start with some character _z_. _F<sub>z</sub>_ removes the first character from all strings that do not start with _z_ and adds some new character to their ends, doing this for all possible combinations of new characters at the end of the strings. _F<sub>z</sub>_ then calculates the mean value of **v**<sub>|**N**|</sub> at the indices corresponding to all \(\sigma^{|N|}\) of the _d_-tuples created this way.

Using this, for all _d_-tuples of strings \(A\in(\Sigma^\ell)^d\), we have that

(2.3) \(\mathbf{w}_\mathbf{n}[A]\ge max_{z\in\Sigma} F_z(\mathbf{w}_{\mathbf{n}-\mathbf{d}},\dots,\mathbf{w}_{\mathbf{n}-\mathbf{1}},A).\)

If we let _b_ have value 1 if all strings in _A_ start with the same character and have value 0 otherwise, we can combine inequalities (2.2) and (2.3) into a single equation:

(2.4) \(\mathbf{w}_\mathbf{n}[A]\ge b+max_{z\in\Sigma} F_z(\mathbf{w}_{\mathbf{n}-\mathbf{1}},\dots,\mathbf{w}_{\mathbf{n}-\mathbf{d}},A).\)

For notational convenience, let \(F:(\mathbb{R}^{\sigma^{d\ell}})^d\rightarrow\mathbb{R}^{\sigma^{d\ell}}\) be the function that takes as input a collection of vectors **v<sub>n-1</sub>**_,...,_**v<sub>n-d</sub>** and outputs the vector whose coordinates are given by \(b+max_{z\in\Sigma} F_z(\mathbf{v}_{\mathbf{n}-\mathbf{1}},\dots,\mathbf{v}_{\mathbf{n}-\mathbf{d}},A)\) as _A_ varies over all string tuples in \((\Sigma^\ell)^d\). To turn (2.4) into a useful lower bound on \(\gamma_{\sigma,d}\), Kiwi and Soto prove the following pivotal lemma:

Lemma 2.1. _Suppose a function_ \(F:(\mathbb{R}^{\sigma^{d\ell}})^d\mapsto\mathbb{R}^{\sigma^{d\ell}}\) _satisfies the following three properties:_

1. **Monotonicity.** _Given two d-tuples of vectors_ \((\mathbf{v}_\mathbf{1},\dots\mathbf{v}_\mathbf{d})\le(\mathbf{u}_\mathbf{1},\dots,\mathbf{u}_\mathbf{d})\) _component-wise, then_ \(F(\mathbf{v}_\mathbf{1},\dots\mathbf{v}_\mathbf{d})\le F(\mathbf{u}_\mathbf{1},\dots,\mathbf{u}_\mathbf{d})\).<tbc>

2. **Translation Invariance.** _For all_ \(r\in\mathbb{R}\), _F_(**v<sub>1</sub>**+_r_**1**_,...,_**v<sub>d</sub>**+_r_**1**)=_F_(**v<sub>1</sub>**_,...,_**v<sub>d</sub>**)+_r_**1**.<tbc>

_3._ **Feasibility.** _There exists a **feasible triplet** for F. That is, there exists a 3-tuple_ \((\mathbf{u}\in\mathbb{R}^{\sigma^{d\ell}},r\in\mathbb{R},\epsilon\in[0,r])\) _such that_<tbc>

\(F(\mathbf{u}+(d-1)r\mathbf{1},\mathbf{u}+(d-2)r\mathbf{1},\dots,\mathbf{u})\ge\mathbf{u}+(dr-\epsilon)\mathbf{1}.\)

<tbc>_Then, for any sequence of_ \((\mathbf{v}_\mathbf{n})_{n\in\mathbb{N}}\) _of vectors in_ \(\mathbb{R}^{\sigma^{d\ell}}\) _such that_ \(\mathbf{v}_\mathbf{n}\ge F(\mathbf{v}_{\mathbf{n}-\mathbf{1}},\dots,\mathbf{v}_{\mathbf{n}-\mathbf{d}})\) _for all_ \(n\ge d\)_, there exists a vector_ \(\mathbf{u}_\mathbf{0}\in\mathbb{R}^{\sigma^{d\ell}}\) _such that for all_ \(n\ge 0\),

(2.5) \(\mathbf{v}_\mathbf{n}\ge\mathbf{u}_\mathbf{0}+n(r-\epsilon)\mathbf{1}.\)

It follows easily from _F_’s definition that _F_ is monotone and translation invariant. Thus, if we find a feasible triplet \((\mathbf{u},r,\epsilon)\) for _F_, then the sequence of vectors \((\mathbf{w}_\mathbf{n})_{n\in\mathbb{N}}\) must satisfy \(\mathbf{w}_\mathbf{n}\ge\mathbf{u}_\mathbf{0}+n(r-\epsilon)\mathbf{1}\) for all _n_ \[16\]. From (2.1) it follows that

(2.6) \(\gamma_{\sigma,d}\ge d(r-\epsilon).\)

Accordingly, to establish a good lower bound we need only find a feasible triplet where \((r-\epsilon)\) is as large as possible. Empirically, Kiwi and Soto observed that for any set of initial vectors **v<sub>1</sub>**_,...,_**v<sub>d</sub>**, if **v<sub>n+d</sub>** is set to _F_(**v<sub>n+d</sub>-1**_,...,_**v<sub>n</sub>**) for all \(n\in\mathbb{N}\), then there exists a real value _r_ such that **v<sub>n+1</sub>-v<sub>n</sub>**≈_r_**1** for all _n_ large enough. So, by definition of **v<sub>n+d</sub>**,

\(F(\mathbf{v}_\mathbf{n}+(d-1)r\mathbf{1},\mathbf{v}_\mathbf{n}+(d-2)r\mathbf{1},\dots,\mathbf{v}_\mathbf{n})\approx\mathbf{v}_\mathbf{n}+dr\mathbf{1}.\)

It follows that one way to find a feasible triplet for _F_ is to find _n_ large enough such that **v<sub>n+1</sub>-v<sub>n</sub>**≈_x_**1** for some real value _x_. Then, set **u**=**v<sub>n+1</sub>** and define _r_ as the maximum value where \(\mathbf{v}_{\mathbf{n}+\mathbf{1}}-\mathbf{v}_\mathbf{n}\ge r\mathbf{1}\) holds and \(\epsilon\) as the minimum value such that \((\mathbf{u},r,\epsilon)\) is a feasible triplet for _F_ \[16\]. This is exactly the approach taken by the Feasible Triplet Algorithm (Algorithm 2.2).

