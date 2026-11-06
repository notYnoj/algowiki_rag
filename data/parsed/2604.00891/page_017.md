Input: \((d,G=(V,E),x,B_\mathrm{he},B_\mathrm{li},B_\mathrm{di},S_\pi)\) as specified in Lemma 8.<br>
if \(|V|<2^{7\alpha_\pi}\) then<br>
   return brute force solution for instance \((d,G,B,x,S_\pi)\)<br>
   if \(d<2^{7\alpha_\pi}\) then<br>
   return base-case(d,G,x,B<br>
he<br>
,<br>
B<br>
li<br>
,<br>
B<br>
di<br>
,<br>
\(S_\pi\))<br>
   if \(x\ge 40\mathrm{log}^7(d)\) then<br>
   return red-portals(d,G,x,0,B<br>
he<br>
,<br>
\(\emptyset,B_\mathrm{li},\emptyset,B_\mathrm{di},\emptyset,S_\pi)\)<br>
   \(\mathrm{res}\leftarrow\overrightarrow{\infty}\)<br>
   Use Lemma 2 to compute a set \(\Delta\) of edges such that \(G^\Delta=G+\Delta\) is triangulated<br>
and \((\alpha_\pi d+1)\)-outerplanar<br>
   Use Corollary 1 to find a 3/4-balanced cycle separator C with a vertex set V<sub>C</sub> of at<br>
most \(2\alpha_\pi d+3\) vertices in \(G^\Delta\) for the weight functions that assigns 1/|<sub>V</sub>| to each \(v\in V\)<br>
/\* case where C contains at most \(20\sqrt{d}\mathrm{log}(d)\) vertices of the solution \*/<br>
Compute \(S_\pi[C_\mathrm{in}]\) and \(S_\pi[C_\mathrm{in}]\) using Requirement R3<br>
\(\mathrm{res}_1\leftarrow\text{solve-}\pi\text{-}\text{\textbf{r}}(d,C_\mathrm{in}-\Delta,x+1,B_\mathrm{he}[C_\mathrm{in}],(B_\mathrm{li}\cup C)[C_\mathrm{in}],B_\mathrm{di}[C_\mathrm{in}],S_\pi[C_\mathrm{in}])\)<br>
\(\mathrm{res}_2\leftarrow\text{solve-}\pi\text{-}\text{\textbf{r}}(d,C_\mathrm{ex}-\Delta,x+1,B_\mathrm{he}[C_\mathrm{ex}],(B_\mathrm{li}\cup C)[C_\mathrm{ex}],B_\mathrm{di}[C_\mathrm{ex}],S_\pi[C_\mathrm{ex}])\)<br>
foreach pebble set M for \((B,d,\alpha_\pi,x)\) do<br>
   Compute \(R_\pi(d,G,B,\mathcal{M},S_\pi)\) using Requirement R2<br>
   Use Requirement R4 to compute a solution s(r) for each \(r\in R_\pi(d,G,B,\mathcal{M},S_\pi)\) based<br>
on res<sub>1</sub> and res<sub>2</sub><br>
res(r)=max(res(r),s(r))<br>
/\* case where C contains more than \(20\sqrt{d}\mathrm{log}(d)\) vertices of the solution \*/<br>
Use Lemma 6 with input \(G^\Delta\) and C to compute a set S of separators<br>
\(d'=\lfloor d-3\sqrt{d}\rfloor\)<br>
foreach \(C'\in\mathcal{S}\) with partition \((C'_\mathrm{he},C'_\mathrm{li},C'_\mathrm{di})\) do<br>
   Use Lemma 1 with \(\alpha_\pi d'\) on the interior of \(C'\) to compute sets \(A_\mathrm{in}^1,A_\mathrm{in}^2,\dots,A_\mathrm{in}^{\alpha_\pi d^\prime+1}\)<br>
   Use Lemma 1 with \(\alpha_\pi d'\) on the exterior of \(C'\) to compute sets \(A_\mathrm{ex}^1,A_\mathrm{ex}^2,\dots,A_\mathrm{ex}^{\alpha_\pi d^\prime+1}\)<br>
foreach A<sub>in</sub>, A<sub>ex</sub> do<br>
   \(\mathrm{res}_1\leftarrow\text{solve-}\pi\text{-}\text{\textbf{r}}(d',C'_\mathrm{in}-A_\mathrm{in}-\Delta,2x+2,(B_\mathrm{he}\cup C'_\mathrm{he})[C'_\mathrm{in}],(B_\mathrm{li}\cup C'_\mathrm{li})[C'_\mathrm{in}],\)<br>
   \((B_\mathrm{di}\cup C')[C'_\mathrm{in}],S_\pi[C'_\mathrm{in}])\)<br>
   \(\mathrm{res}_2\leftarrow\text{solve-}\pi\text{-}\text{\textbf{r}}(d',C'_\mathrm{ex}-A_\mathrm{ex}-\Delta,2x+2,(B_\mathrm{he}\cup C'_\mathrm{he})[C'_\mathrm{ex}],(B_\mathrm{li}\cup C'_\mathrm{li})[C'_\mathrm{ex}],\)<br>
   \((B_\mathrm{di}\cup C')[C'_\mathrm{ex}],S_\pi[C'_\mathrm{ex}])\)<br>
foreach pebble set M for \((B,d,\alpha_\pi,x)\) do<br>
   Compute \(R_\pi(d,G,B,\mathcal{M},S_\pi)\) using Requirement R2<br>
   Use Requirement R4 to compute a solution s(r) for each \(r\in R_\pi(d,G,B,\mathcal{M},S_\pi)\) based<br>
based on res<sub>1</sub> and res<sub>2</sub><br>
res(r)=max(res(r),s(r))<br>
\(d'=\lfloor d-3\sqrt{d}\rfloor\)<br>
return res

**Algorithm 1:** `solve-`\(\pi\)**-r` (maximization)

