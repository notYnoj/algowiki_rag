**Algorithm 1** Sparsification for constant \(\lambda\) (Step 1 of Theorem 2.2)

procedure QuadraticSparsification\((w_1,w_2,\dots,w_k,\lambda,\epsilon)\triangleright\) Theorem 3.13<br>
   \(S\leftarrow 40k^\gamma logk\) i.i.d. samples of \[k\]<br>
   \(\widehat{\mathsf{O}}_{\lambda^2}\leftarrow\{0\}^{k\times k}\)<br>
   for \(w_i\in S\) do \(\triangleright\) Takes \(k|S|\mathsf{w}_\mathsf{max}^2\) time<br>
   for \(j\leftarrow 1\) to k do<br>
   \(\mathsf{opt}_{i,j},\mathsf{opt}_{j,i}\leftarrow\mathsf{lcs}(w_i,w_j)\)<br>
   end for<br>
   end for<br>
   for \(w_i\in S\) do \(\triangleright\) Takes \(k|S|\mathsf{w}_\mathsf{max}\) time<br>
   for \(j\leftarrow 1\) to k do<br>
   if \(||\mathsf{opt}_{i,j}||\ge\lambda\) then<br>
   \(\widehat{\mathsf{O}}_{\lambda^2}[i][j]\leftarrow 1\)<br>
   \(\widehat{\mathsf{O}}_{\lambda^2}[j][i]\leftarrow 1\)<br>
   end if<br>
   end for<br>
   end for<br>
   for \(i\leftarrow 1\) to k do \(\triangleright\) Takes \(k^2|S|^2\mathsf{w}_\mathsf{max}\) time<br>
   for \(j\leftarrow 1\) to k do<br>
   for \(w_a\in S\) do<br>
   for \(w_b\in S\) do<br>
   if \(\left\|\left(\mathsf{opt}_{i,a}\cap\mathsf{opt}_{a,b}\cap\mathsf{opt}_{b,j}\right)\right\|\ge(1-\epsilon)\lambda^3\) then<br>
   \(\widehat{\mathsf{O}}_{\lambda^2}[i][j]\leftarrow 1\)<br>
   \(\widehat{\mathsf{O}}_{\lambda^2}[j][i]\leftarrow 1\)<br>
   end if<br>
   end for<br>
   end for<br>
   return \(\widehat{\mathsf{O}}_{\lambda^2}\)<br>
end procedure

**Lemma 3.4.** _With probability at least_ 1-2_/k_<sup>3</sup>, \(\mathsf{NG}_\lambda\) _has at most_ \(k^{2-\gamma\epsilon\lambda^3/(80\mathsf{w}_\mathsf{layers}\mathsf{w}_\mathsf{gap})}\) _edges._

Instead of arguing directly about \(\mathsf{NG}_\lambda\), our proof uses another graph \(\mathsf{NF}_\lambda\), which is sub-sampled from \(\mathsf{NG}_\lambda\):

**Definition 3.5** \((\mathsf{NF}_\lambda)\)**.** Let \(\mathsf{NF}_\lambda\) be the graph constructed in the following way: for each node \(v\in\mathsf{NG}_\lambda\) we keep _v_ in \(\mathsf{NF}_\lambda\) with probability

\(p:=k^{-1+\gamma/4}/4.\)

For each \(u,v\in\mathsf{NF}_\lambda\), if \((u,v)\in\mathsf{NG}_\lambda\) then we also draw an edge _u,v_ in \(\mathsf{NF}_\lambda\). We identify between the vertices and edges of \(\mathsf{NF}_\lambda\) and the corresponding vertices and edges of \(\mathsf{NG}_\lambda\), i.e. \(V(\mathsf{NF}_\lambda)\subseteq V(\mathsf{NG}_\lambda)\) and \(E(\mathsf{NF}_\lambda)\subseteq E(\mathsf{NG}_\lambda)\).

The proof has two main ingredients. The first part of the proof uses the details of our algorithm to show that, w.h.p. over the algorithm’s randomness, \(\mathsf{NG}_\lambda\) contains few undetected-constructive<tbc>

