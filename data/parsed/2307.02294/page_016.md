which does not contain \(\sigma\). We therefore need to argue that neither \(\sigma\) nor \(\sigma'\) can arise in _U(i,j_) in the _shuffling_ operation.

If \(\sigma\) or \(\sigma'\) arose during shuffling, then Lemma 4.2 implies that for any \(a,b\in\{1,2,3\}\) with \(a\in\Sigma(U_\mathrm{top})\) and \(b\in\Sigma(U_\mathrm{bot}^*)\), that _a\<b_. It cannot be that {1} or \(\{1,2\}\subset\Sigma(U_\mathrm{top})\) while {2,3} or \(\{3\}\subset\Sigma(U_\mathrm{bot}^*)\) since 3’s copy of _S_<sub>bot</sub> only receives _one_ copy of any symbol during shuffling, but both \(\sigma,\sigma'\) have two 1s between the first and last 3.

**Remark 4.4.** The distinction between _live_ and _dead_ blocks is critical for constructing order- 3 (_ababa_-free) Davenport-Schinzel sequences \[HS86, Niv10, Pet15a\], and generalized DS sequences with length \(O(n\mathrm{poly}(\alpha(n)))\) \[Pet11b, Pet15b\]. However, all constructions of DS sequences at order- 4 and above \[ASS89, Niv10, Pet15a\] (having length \(\Omega(n2^{\alpha(n)})\)) only use live blocks. In Lemma 4.3, it is very important that _first_ occurrences lie exclusively in dead blocks, and are never shuffled into the middle of a copy of _U_<sub>bot</sub>. If the first block in _U_(1_,j_) were redefined to be live, then we would see instances of 41213 in _U(i,j_). It could be that 12121 appears in a copy of _U_<sub>bot</sub>, and the first occurrences of {3,4} lie in a common live block in _U_<sub>top</sub>. The restriction of _U_<sub>top</sub> to {3,4} contains (34)3. After shuffling the block (34) into the _U_<sub>bot</sub> containing 1,2 we can see 12341213. Lemma 4.2(2) rules out this possibility when first occurrences appear in _dead_ blocks.

**Theorem 4.5.** \(\mathrm{Ex}(W,n,m)=\Theta(m+n2^{\alpha(n,m)})\)_, where_

\(W=\left(\begin{array}{ c c c c }
\bullet &  &  &  \\
 &  &  & \bullet \\
 &  & \bullet &  \\
 &  & \bullet &  \\
 &  & \bullet & 
\end{array}\right)\)

_Proof._ By Lemma 4.1, the sequence _U=U(i,j_) has _n=N(i,j_) symbols, _m\<_2_L(i,j_) blocks, and length \(|U|=\Theta(n2^i)=\Theta(n2^{\alpha(n,m)})\). We convert _U_ to an \(n\times m\) 0-1 matrix _A<sub>U</sub>_. Number the rows of _A<sub>U</sub>_ from bottom-to-top, and the columns from left-to-right, and let _A<sub>U</sub>(i,j_)=1 iff symbol _i_ appears in block _j_. _U_ does not contain subsequences order-isomorphic to 41213, which implies that _A<sub>U</sub>_ is _W_-free, and hence \(\mathrm{Ex}(W,n,m)=\Omega(n2^{\alpha(n,m)})\). The matching upper bound is obtained as in \[Pet11b, Thm. 3.4\].

## 5 Additional Upper Bounds

### 5.1 Proof of Theorem 1.5

Recall that _I<sub>k</sub>_ is the \(k\times k\) identity matrix. For example, when _k_=3, we have the following.

\(I_k=\left(\begin{array}{ c c c c }
\bullet &  &  &  \\
 &  & \bullet &  \\
 &  &  & \bullet
\end{array}\right)I_k\otimes(\bullet)=\left(\begin{array}{ c c c c }
\bullet &  &  &  \\
\bullet &  & \bullet &  &  \\
 &  &  & \bullet &  \\
 &  &  &  & \bullet
\end{array}\right)\)

Theorem 1.5 follows from Keszegh’s \[Kes09\] _joining_ operation and and Pettie’s upper bound on order-3 Davenport-Schinzel sequences \[Pet15a\]; cf. \[HS86, Niv10\]. Keszegh \[Kes09\] proved that if _R_ has a 1 in its southeast corner and _S_ has a 1 in its northwest corner, that \(\mathrm{Ex}(R\oplus S,n,m)\le\)<tbc>

