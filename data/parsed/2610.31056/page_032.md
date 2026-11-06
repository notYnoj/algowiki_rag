_Proof._ refer Section D.4.

In Proposition 6.0.1, we give an upper bound for the size of the set _B_<sub>_t_<sub>1</sub>_,t_<sub>2</sub>_,t_<sub>3</sub></sub>. In the next proposition, using a sophisticated combinatorial technique, we give another upper bound for the same when the vectors satisfy a specific relation.

**Proposition 6.0.3.** _For some_ \(m\in\mathbb{Z}^{\ge 1}\)_, let_

\(\mathsf{T}_\mathsf{m}:=\left\{\left(\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3,\mathbf{v}_4\right)\middle|\begin{array}{ c }
\mathbf{v}_1\neq\mathbf{v}_2,\mathbf{v}_3\neq\mathbf{v}_4, \\
\mathbf{v}_1-\mathbf{v}_2=\mathbf{v}_3-\mathbf{v}_4
\end{array}\right\},\)

_where_ \(\mathbf{v}_i\in\{0,1\}^m\backslash\{0^m\}\), \(\forall 1\le i\le 4\)_. Then,_ |T<sub>m</sub>|_\<_6_<sup>m</sup>._

_Proof._ Let **w** be any vector of the set \(\{0,\pm 1\}^m\backslash\{0^m\}\). We say that the vector **w** splits iff \(\exists\mathbf{u}\neq\mathbf{v}\in\{0,1\}^m\backslash\{0^m\}\) such that **w**=**u**-**v**. Let S<sub>_m_<sub>0</sub></sub> be the set of all the \(\mathbf{w}\in\{0,\pm 1\}^m\backslash\{0^m\}\) such that they contain _m_<sub>0</sub> zeroes. Then, we can say that<tbc>

\(|\mathsf{S}_{m_0}|=\genfrac(){pt}{2}{m}{m_0}2^{m-m_0}.\)

<tbc>Since the split vectors belong to {0,1}_<sup>m</sup>_, any non-zero bit in **w** fixes the corresponding bit in the split vectors. Hence, for any **w** with _m_<sub>0</sub> zeroes, the number of possible splits is 2_<sup>m_<sub>0</sub></sup>. Then, we have

\(|\mathsf{T}_\mathsf{m}|<\sum_{m_0=0}^{m-1}|\mathsf{S}_{m_0}|\genfrac(){pt}{2}{2^{m_0}}{2},\)<br>
\(<\sum_{m_0=0}^{m-1}\genfrac(){pt}{2}{m}{m_0}2^{m-m_0}2^{2m_0},\)<br>
\(=2^m\sum_{m_0=0}^{m-1}\genfrac(){pt}{2}{m}{m_0}2^{m_0},\)<br>
\(<6^m.\)

Now, we have all the desired tools to upper bound the terms _S_<sub>1</sub> and _S_<sub>2</sub>.

**Upper bound of** _S_<sub>1</sub>**.** Let us recall the expression of the sum _S_<sub>1</sub>

\(S_1=\frac{1}{r}.\sum_{i<j,l<k(i,j)\neq(l,k)\mathbf{u}_i-\mathbf{u}_j=\pm(\mathbf{u}_l-\mathbf{u}_k)}\mathbb{P}_{\mathbf{a}^{(pq)}}\left(\mathcal{D}_{ij}=1\wedge\mathcal{D}_{lk}=1\right),\)

where D_<sub>ij</sub>_ is a binary random variable equal to 1 if and only if events \(\mathsf{E}_{\mathsf{LS},p^\prime}^{(i)}\mathsf{E}_{\mathsf{RS},p^\prime}^{(i)}\mathsf{E}_{\mathsf{LS},p^\prime}^{(j)}\mathsf{E}_{\mathsf{RS},p^\prime}^{(j)}\mathsf{E}_{\mathsf{TS},q^\prime}^{(i)}\) and \(\mathsf{E}_{\mathsf{TS},q}^{(j)}\) occur simultaneously.

**Claim 6.0.2.** _Let_ **u**, **v**, **w**, \(\mathbf{x}\in\{0,1\}^n\backslash\{0^n\}\) _such that all of them are distinct vectors. Consider the following matrix over the field_ Z_<sub>s</sub>, where s is a prime_

\(\mathbf{M}=[\mathbf{u}\mathbf{v}\mathbf{w}\mathbf{x}].\)

_Here, all the vectors are considered as column vectors. Then_ \(3\le\mathsf{rank}(\mathbf{M})\le 4\).

