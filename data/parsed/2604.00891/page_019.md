Input: \((d,G=(V,E),x,B_\mathrm{he},B_\mathrm{li},B_\mathrm{di},S_\pi)\) as specified in Lemma 8.<br>
Use Theorem 2 to compute a tree decomposition of width at most \(6\alpha_\pi d-1\)<br>
Use Lemma 5 to modify the tree decomposition into a binary tree decomposition T of<br>
width \(w\le 18\alpha_\pi d-1\) and depth O(log(n))<br>
\(D\leftarrow 4d^2\)<br>
/\* Build relevant instances and brute force solution for pairs of bags \*/<br>
foreach node u except the root of the tree decomposition do<br>
   Let \(u'\) be the parent of u in T<br>
\(Z_u\leftarrow X_u\backslash(B_\mathrm{li}\cup B_\mathrm{di})\)<br>
\(X'_u\leftarrow X_u\cup X_{u^\prime}\)<br>
\(Z'_u\leftarrow X'_u\backslash(B_\mathrm{li}\cup B_\mathrm{di})\)<br>
   \(I_u\leftarrow(D,G[Y_u],(Z_u,B_\mathrm{li}\cap X_u,B_\mathrm{di}\cap X_u),\infty,S_\pi[G[Y_u]])\)<br>
   \(I'_u\leftarrow(D,G[X'_u],(Z'_u,B_\mathrm{li}\cap X'_u,B_\mathrm{di}\cap X'_u),\infty,S_\pi[G[X'_u]])\)<br>
   \(\mathrm{res}'_u\leftarrow\) brute force solution for \(I'_u\)<br>
/\* Bottom-Up dynamic programming \*/<br>
foreach node u of the tree decomposition with at least one child from bottom to top do<br>
   Let v<sub>1</sub> be the first child of u in T<br>
\(I_u^1\leftarrow(D,G_1=G[X_u\cup Y_{v_1}],(B_\mathrm{he}[G_1]\cup Z_{v_1},B_\mathrm{li}[G_1],B_\mathrm{di}[G_1]),\infty,S_\pi[G_1])\)<br>
   Use Requirement R4 with separator \((Z_{v_1},B_\mathrm{li}\cap X_{v_1},B_\mathrm{di}\cap X_{v_1})\) and solutions \(\mathrm{res}'_{v_1}\) (for instance \(I'_{v_1}\)) and res<sub>v<sub>1</sub></sub> (for instance I<sub>v<sub>1</sub></sub>) to get solution \(\mathrm{res}_u^1\) for instance \(I_u^1\)<br>
   if u has only one child then<br>
\(\mathrm{res}_u\leftarrow\mathrm{res}_u^1\)<br>
   else<br>
   Let v<sub>2</sub> be the second child of u in T<br>
\(J_u\leftarrow(D,G'=G[X_u\cup Y_{v_2}],(B_\mathrm{he}[G']\cup Z_{v_2},B_\mathrm{li}[G'],B_\mathrm{di}[G']),\infty,S_\pi[G'])\)<br>
   \(I_u^2\leftarrow(D,G_2=G[Y_u],(B_\mathrm{he}[G_2]\cup Z_{v_2},B_\mathrm{li}[G_2],B_\mathrm{di}[G_2]),\infty,S_\pi[G_2])\)<br>
   Use Requirement R4 with separator \((Z_{v_2},B_\mathrm{li}\cap X_{v_2},B_\mathrm{di}\cap X_{v_w})\) and solutions \(\mathrm{res}'_{v_2}\)<br>
  (for instance \(I'_{v_2}\)) and res<sub>v<sub>2</sub></sub> (for instance I<sub>v<sub>2</sub></sub>) to get solution s<sub>u</sub> for instance J<sub>u</sub><br>
   Use Requirement R4 with separator \((Z_u,B_\mathrm{li}\cap X_u,B_\mathrm{di}\cap X_u)\) and solutions \(\mathrm{res}_u^1\) (for instance \(I_u^1\)) and s<sub>u</sub> (for instance J<sub>u</sub>) to get solution \(\mathrm{res}_u^2\) for instance \(I_u^2\)<br>
   \(\mathrm{res}_u\leftarrow\mathrm{res}_u^2\)<br>
/\* Removing Z<sub>p</sub> for root p from portal set \*/<br>
\(\mathrm{res}'_r\leftarrow\) brute force solution for<br>
instance \(I'_z=(D,G[X_p],(X_p\backslash(B_\mathrm{li}\cup B_\mathrm{di}),B_\mathrm{li}\cap X_p,B_\mathrm{di}\cap X_p),\infty,S_\pi[G[X_p]])\)<br>
Use Requirement R4 with separator \((X_p\backslash(B_\mathrm{li}\cup B_\mathrm{di}),\emptyset,\emptyset)\) and solutions \(\mathrm{res}'_p\) for<br>
instance \(I'_p\) and solution res<sub>p</sub> for \((D,G,(B_\mathrm{he}\cup(X_p\backslash(B_\mathrm{li}\cup B_\mathrm{di})),B_\mathrm{li},B_\mathrm{di}),\infty,S_\pi)\) to<br>
compute solution res<sup>∗</sup> for \((D,G,(B_\mathrm{he},B_\mathrm{li},B_\mathrm{di}),\infty,S_\pi)\)<br>
/\* Discarding solutions for too large pebble sets \*/<br>
foreach pebble set M for \((B,d,\alpha_\pi,x)\) do<br>
   Compute \(R=R_\pi(d,G,B,\mathcal{M},S_\pi)\) using Requirement R2<br>
   foreach \(r\in R\) do<br>
\(\mathrm{res}(r)\leftarrow\mathrm{res}^*(r)\)<br>
return res

**Algorithm 3: base-case**

