Then:

\(T_k(A)=\sum_{z\in\mathbb{Z}}|\{(a_1,\dots,a_k)\in A^k:a_1+\cdots+a_k=z\}|^2\)<br>
\(\le\sum_{z\in\mathbb{Z}}\big(\sum_D2D\cdot|\{(a,x)\in A\times P_D:a+x=z\}|\big)^2\)<br>
\(=\sum_{D,D^\prime}\sum_{z\in\mathbb{Z}}2D\cdot|\{(a,x)\in A\times P_D:a+x=z\}|\cdot 2D'\cdot|\{(a',x')\in A\times P_{D^\prime}:a'+x'=z\}|\)<br>
\(\le\sum_{D,D^\prime}\big(\sum_{z\in\mathbb{Z}}4D^2\cdot|\{(a,x)\in A\times P_D:a+x=z\}|^2\big)^{1/2}\)<br>
\(\cdot\big(\sum_{z\in\mathbb{Z}}4(D')^2\cdot|\{(a',x')\in A\times P_{D^\prime}:a'+x'=z\}|^2\big)^{1/2}\)<br>
\(=\sum_{D,D^\prime}\big(4D^2\cdot E(A,P_D)\big)^{1/2}\big(4(D')^2\cdot E(A,P_{D^\prime})\big)^{1/2}.\)

We apply the dyadic pigeonhole principle: let _D_ denote the power of 2 maximizing \(D^2\cdot E(A,P_D)\). Then:

\(T_k(A)\le O((klog|A|)^2)\cdot D^2\cdot E(A,P_D).\)

Recall that \(T_k(A)\ge\Omega(|A|^{2k-1-c})\) by our initial assumption, and thus

\(D^2\cdot E(A,P_D)\ge|A|^{2k-1-c-o(1)}.\) (2)

Combined with the trivial bounds \(E(A,P_D)\le|A|^2|P_D|\) and \(|P_D|\le|A|^{k-1}/D\), it further follows that \(D\ge|A|^{k-2-c-o(1)}\) and thus \(|P_D|\le|A|^{1+c+o(1)}\). Moreover, we have that

\(|P_D|\cdot D^2\le T_{k-1}(A)\le|A|^{2(k-1)-1-c+\delta}.\) (3)

Combining (2) and (3), it follows that

\(E(A,P_D)\ge\frac{|A|^2|P_D|}{|A|^{\delta+o(1)}}.\)

In this situation the asymmetric BSG theorem applies. Specifically, we apply Theorem 2.4 to the sets _A_ and _P<sub>D</sub>_ with parameters \(\epsilon'=\epsilon/(4c)\) and \(\alpha=|A|^{-\delta-o(1)}\). It yields sets \(H,\Lambda\subseteq\mathbb{Z}\) such that

\(|H+H|\le K|H|,\) (4)

and

\(|H|\le|H||\Lambda|\le K|P_D|\le(K|A|^{o(1)})\cdot|A|^{1+c},\) (5)

