## 3 Select-Plus Rank

In this section, we recap the central definition of select-plus rank, establish some basic facts (Section 3.1), and develop a refined notion of rank decompositions that will be crucial later on (Section 3.2).

**Definition 1.17** (Select-Plus Rank)**.** _The_ select-plus rank _of a matrix_ \(A\in(\mathbb{Z}\cup\{\perp\})^{n\times m}\)_, denoted by r(A), is the smallest integer_ \(r\ge 0\) _such that there are integer matrices_ \(U\in\mathbb{Z}^{n\times r}\) _and_ \(V\in\mathbb{Z}^{r\times m}\) _satisfying for all_ \((i,j)\in[n]\times[m]\):

\(A[i,j]\in\{U[i,1]+V[1,j],\dots,U[i,r]+V[r,j]\}\cup\{\perp\}.\)

We reiterate that this alternative rank notion is reminiscent of the standard matrix rank, which can be characterized as the smallest number _r_ such that _A_ can be written as _UV_ for matrices _U_ of size \(n\times r\) and _V_ of size \(r\times m\), respectively. In the following we will often refer to the select-plus rank simply as the "rank" of a matrix.

### 3.1 Basic Facts

We gather some basic facts concerning the select-plus rank. The first two involve trivial upper bounds on the rank based on the size and maximum entry.

**Fact 3.1.** \(r(A)\le min\{n,m\}\) _for all matrices_ \(A\in(\mathbb{Z}\cup\{\perp\})^{n\times m}\).

**Proof.** Take _U_ to be all-zero and _V=A_, or vice versa.

**Fact 3.2.** \(r(A)\le u\) _for all matrices_ \(A\in([u]\cup\{\perp\})^{n\times m}\).

**Proof.** Take _U_ to be all-zero and define _V_ by _V_\[_k,j_\]=_k_.

**Fact 3.3** (Submultiplicativity)**.** \(r(A_1+A_2)\le r(A_1)\cdot r(A_2)\) _for all matrices_ \(A_1,A_2\in(\mathbb{Z}\cup\{\perp\})^{n\times m}\).

**Proof.** Let _U_<sub>1</sub>_,V_<sub>1</sub> be matrices witnessing _r(A_<sub>1</sub>) and let _U_<sub>2</sub>_,V_<sub>2</sub> be matrices witnessing _r(A_<sub>2</sub>). Consider the following matrices _U,V_ , where we index the rows of _U_ and columns of _V_ by pairs \((k_1,k_2)\in[r(A_1)]\times[r(A_2)]\):

\(U[i,(k_1,k_2)]=U_1[i,k_1]+U_2[i,k_2],\)<br>
\(V[(k_1,k_2),j]=V_1[k_1,j]+V_2[k_2,j].\)

Each entry in _A_<sub>1</sub>+_A_<sub>2</sub> can be expressed as

\(A_1[i,j]+A_2[i,j]=U_1[i,k_1]+V_1[k_1,j]+U_2[i,k_2]+V_2[k_2,j]=U[i,(k_1,k_2)]+V[(k_1,k_2),j],\)

for some pair \((k_1,k_2)\in[r(A_1)]\times[r(A_2)]\). Thus, _U,V_ witnesses that \(r(A_1+A_2)\le r(A_1)\cdot r(A_2)\).

### 3.2 Regular Rank Decompositions

We will now make the concept of a select-plus rank decomposition formal.

**Definition 3.4** (Rank Decomposition)**.** _Let A,U,V and r be as in Definition 1.17. Let_ \(S\in([r]\cup\{\perp\})^{n\times m}\) _be a matrix such that_

\(A[i,j]=\left\{\begin{array}{ c c }
U[i,S[i,j]]+V[S[i,j],j] & \text{\textit{if}}S[i,j]\neq\perp, \\
\perp & \text{\textit{if}}S[i,j]=\perp.
\end{array}\right.\)

_Then we call_ (_U,V,S_) _a_ select-plus rank-_r_ decomposition _of A._

