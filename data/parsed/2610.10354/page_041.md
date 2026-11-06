Enumerate all shifts \(s,t\in S\). For each pair, construct the sequences \(A_s,B_t\in([0,N]\cup\{\perp\})^{[0,n]}\) defined by

\(A_s[i]=\left\{\begin{array}{ c c }
h(\phi(i,A[i])-s) & \text{if}\phi(i,A[i])\in Y+s, \\
\perp & \text{otherwise,}
\end{array}\right.\)<br>
\(B_t[j]=\left\{\begin{array}{ c c }
h(\phi(j,B[j])-t) & \text{if}\phi(j,B[j])\in Y+t, \\
\perp & \text{otherwise.}
\end{array}\right.\)

Note that both sequences are almost monotone: The sequence \(\phi(i,A[i])\) is increasing for _i_=0_,...,n_ (when restricted to the non-\(\perp\) entries), and hence, so are the images of \(\phi(i,A[i])-s\in Y\) under the order-preserving function _h_. To remove the \(\perp\) entries simply replace both sequences by their suffix-minima, i.e., replace _A<sub>s</sub>_ and _B<sub>t</sub>_ by

\(A'_s[i]=min_{i^\prime\ge i}A_s[i'],\)<br>
\(B'_t[j]=min_{j^\prime\ge j}B_t[j'].\)

We compute the Monotone Min-Plus Convolution \(A'_s*B'_t\) using the reduction provided by Lemma 5.6. Moreover, by Lemma 5.6, we know one witness _i_ per output \((A'_s*B'_t)[k]\); then update \(C[k]\leftarrow min\{C[k],A[i]+B[k-i]\}\).

## Correctness.

We argue that once the algorithm stops, we have correctly assigned _C_. Fix any witness _i_<sup>∗</sup> of (_A∗B_)\[_k_<sup>∗</sup>\], and let _j_<sup>∗</sup>=_k_<sup>∗</sup>-_i_<sup>∗</sup>. Since _H_ is a container of the index sets I(_A_) and I(_B_), we must have \((i^*,A[i^*]),(j^*,B[j^*])\in H\). Thus, by \(\phi(H)\subseteq Y+S\), there exist \(s,t\in S\) such that \(\phi(i^*,A[i^*])\in Y+s\) and \(\phi(j^*,B[j^*])\in Y+t\). Focus on the iteration associated with that pair _s,t_.

We first claim that any witness _i_ of (_A<sub>s</sub>∗B<sub>t</sub>_)\[_k_<sup>∗</sup>\] must also be a witness of (_A∗B_)\[_k_<sup>∗</sup>\]. Indeed, take any other pair _i+j=k_<sup>∗</sup> and assume that _i_ is not a witness of (_A∗B_)\[_k_<sup>∗</sup>\], i.e.,<tbc>

\(A[i^*]+B[j^*]<A[i]+B[j].\)

<tbc>Then clearly also<tbc>

\(\phi(i^*,A[i^*])+\phi(j^*,B[j^*])<\phi(i,A[i])+\phi(j,B[j]),\)

<tbc>and thus,<tbc>

\((\phi(i^*,A[i^*])-s)+(\phi(j^*,B[j^*])-t)<(\phi(i,A[i])-s)+(\phi(j,B[j])-t),\)

<tbc>But _h_ is sum-order-preserving and therefore,

\(A_s[i^*]+B_t[j^*]<A_s[i]+B_t[j],\)

for all non-\(\perp\) entries, so _i_ cannot be a witness of (_A<sub>s</sub>∗B<sub>t</sub>_)\[_k_<sup>∗</sup>\]. This proves that any witness _i_ of (_A<sub>s</sub>∗B<sub>t</sub>_)\[_k_<sup>∗</sup>\] is also a witness of (_A∗B_)\[_k_<sup>∗</sup>\] (though the converse is not necessarily true; notably, _i_<sup>∗</sup> is not necessarily a witness of (_A<sub>s</sub>∗B<sub>t</sub>_)\[_k_<sup>∗</sup>\]).

