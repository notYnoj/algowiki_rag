**Algorithm 1** Weighted padded bilinear algorithm for simultaneous contractions

Require:<br>
\(\mathcal{S}=\{(U_s,V_s,W_s)\}_{s=1}^m\subseteq B_{N,N,N},U_i\sqcup V_j\sqcup W_\ell=F\Longrightarrow i=j=\ell.\)<br>
Require:<br>
\(A^{(s)}\in(\mathbb{C}^n)^{\otimes 2N}\text{indexed by}F\backslash U_s,B^{(s)}\in(\mathbb{C}^n)^{\otimes 2N}\text{indexed by}F\backslash V_s.\)<br>
Ensure:<br>
\(C^{(s)}\in(\mathbb{C}^n)^{\otimes 2N}\text{indexed by}F\backslash W_s,\)<br>
with<br>
\(C_\alpha^{(s)}=\sum_{\mathbf{i}\in\unknown 0,n-1\unknown^d\mathbf{i}|_{W_s^c}=\alpha} A_{\mathbf{i}|_{U_s^c}^{(s)}}^{(s)}B_{\mathbf{i}|_{V_s^c}^{(s)}}.\)<br>
for all \(\mathbf{k}\in\unknown 0,n+1\unknown^d\) do<br>
   \(T_\mathbf{k}\leftarrow\left(\sum_{s=1}^m\Phi_{U_s,F}(A^{(s)})_\mathbf{k}\right)\left(\sum_{s=1}^m\Phi_{V_s,F}(B^{(s)})_\mathbf{k}\right).\)<br>
end for<br>
for s=1,...,m do<br>
   \(C^{(s)}\leftarrow\Phi_{W_s,F}^\star(T)\)<br>
end for<br>
return \(\{C^{(s)}\}_{s=1}^m\)

be indexed by F\\W<sub>s</sub>. By the definition of the transpose of \(\Phi_{S,F}\),

\(\sum_{s=1}^m\big\langle C^{(s)},Z^{(s)}\big\rangle=\sum_{\mathbf{k}\in\unknown 0,n+1\unknown^F}T_\mathbf{k}\sum_{s=1}^m\Phi_{W_s,F}(Z^{(s)})_\mathbf{k}\)<br>
\(=\sum_{\mathbf{k}\in\unknown 0,n+1\unknown^F}\left(\sum_{i=1}^m\Phi_{U_i,F}(A^{(i)})_\mathbf{k}\right)\left(\sum_{j=1}^m\Phi_{V_j,F}(B^{(j)})_\mathbf{k}\right)\left(\sum_{\ell=1}^m\Phi_{W_\ell,F}(Z^{(\ell)})_\mathbf{k}\right).\) (70)

Thus multiplying each output entry \(C_\alpha^{(s)}\) by an independent variable \(Z_\alpha^{(s)}\) and summing over s and \(\alpha\) gives exactly the weighted padded aggregated trilinear form.

Expanding (70) gives one term for each triple \((i,j,\ell)\). If

\(U_i\sqcup V_j\sqcup W_\ell\neq F,\) (71)

then, since all three sets have cardinality N and d=3N, the corresponding term is either linearly reducible or replicated in the sense of Definitions 4 and 3. By the filtering identities of Claim 1, namely

\(\sum_{q=0}^{n+1}w_q^2\nu(\mu(x))_q=0,\sum_{q=0}^{n+1}w_q^3=0,\) (72)

such terms vanish after centering, padding, and weighting.

The only remaining terms satisfy

\(U_i\sqcup V_j\sqcup W_\ell=F.\) (73)

By conflict-freeness, this forces \(i=j=\ell\). For these diagonal terms, every coordinate is retained by exactly two of the three tensors and weighted by the third, so Claim 1 gives, in each coordinate,

\(\sum_{q=0}^{n+1}w_q\nu(\mu(e_a))_q\nu(\mu(e_b))_q=\delta_{ab},\) (74)

