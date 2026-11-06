## 3.2.1 \(\Omega(\lambda^3)\) Sparsification using lcs-cmp

We use a constant parameter \(\gamma\) in our algorithm, and in the end we adjust \(\gamma\) to minimize the total running time. Our algorithm repeats the following procedure \(O(k^\gamma logk)\) times: sample a window _w<sub>a</sub>_ uniformly at random and let _S_ be the set of all the other windows. Next, by setting \(\widetilde{\lambda}=\lambda^2/2\), we obtain \(\mathsf{lcs}\text{-}\mathsf{cmp}(w_a,S,\lambda^2/2)\) via running the preprocessing step. Finally, for each pair of windows \(w_i,w_j\in S\), we make a query to lcs-cmp to verify one of the following two possibilities:

• \(||\mathsf{lcs}_{w_a}(w_i,w_j)||<\lambda^2/2\);<tbc>

• \(||\mathsf{lcs}_{w_a}(w_i,w_j)||\ge\lambda^4/16\).

If the latter is verified we set \(\widehat{\mathsf{O}}_{\lambda^3}[i][j]\) and \(\widehat{\mathsf{O}}_{\lambda^3}[j][i]\) to 1 otherwise we take no action. In what follows, we prove that after the above sparsification, the number of edges in the remaining graph is truly subquadratic.

**Algorithm 2** Sparsification for arbitrary \(\lambda\) (Step 1 of Theorem 2.1)

procedure CubicSparsification\((w_1,w_2,\dots,w_k,\lambda)\triangleright\) Theorem 3.21<br>
  \(\widetilde{\lambda}\leftarrow\lambda^2/2\)<br>
   for counter \(=1\rightarrow 10k^\gamma logk\) do<br>
   Sample a∼[k] uniformly at random<br>
   \(S\leftarrow\emptyset\)<br>
   for \(i=1\rightarrow k\) do<br>
   if \(i\neq a\) then<br>
   \(S\leftarrow S\cup\{w_i\}\)<br>
   end if<br>
   end for<br>
   lcs-cmp.Initial\((w_a,S,\widetilde{\lambda})\triangleright\) Algorithm 3, Lemma 3.22<br>
   for \(w_i\in S\) do<br>
   for \(w_j\in S\) do<br>
   if lcs-cmp.Query(w<sub>i</sub>,w<sub>j</sub>) outputs accept then \(\triangleright\) Alg. 3, Lemma 3.23<br>
   \(\widehat{\mathsf{O}}_{\lambda^3}[i][j]\leftarrow 1\triangleright||\mathsf{lcs}_{w_a}(w_i,w_j)||\ge\widetilde{\lambda}^2/8\)<br>
   end if<br>
   end for<br>
   end for<br>
   end for<br>
   return \(\widehat{\mathsf{O}}_{\lambda^3}\)<br>
end procedure

Our goal for the rest of this section is to prove (Lemma 3.19) an upper bound on the number of edges that remain in the following graph:

**Definition 3.15** \((\mathsf{NG}_\lambda)\)**.** Define a graph \(\mathsf{NG}_\lambda\) with _k_ vertices and the following edges:

\(E(\mathsf{NG}_\lambda)=\left\{(i,j)\middle||\mathsf{lcs}(w_i,w_j)||\ge\lambda\text{and}\widehat{\mathsf{O}}_{\lambda^3}[i][j]=0\right\}.\)

We define a notation called "close" which is similar to the notion of "well-connected" vertices in Section 3.1.

