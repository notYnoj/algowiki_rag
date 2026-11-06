Let \(G'\) be _G<sub>in</sub>_ with every edge weight multiplied by _n_<sup>3</sup><br>
\(B\leftarrow\) Find\(\text{Thresh}(G',s_{in})\)<br>
**if**<br>
_B_<br>
=<br>
0<br>
**then**<br>
**if**<br>
SPMonteCarlo<br>
(<br>
_G<sub>in</sub>,s<sub>in</sub>_<br>
)<br>
_returns error_<br>
**then**<br>
restart<br>
SPasVegas<br>
(<br>
_G<sub>in</sub>,s<sub>in</sub>_<br>
)<br>
;<br>
Let<br>
_T_<br>
be<br>
the<br>
tree<br>
output<br>
by<br>
SPMonteCarlo<br>
(<br>
_G<sub>in</sub>,s<sub>in</sub>_<br>
)<br>
**return**<br>
_T_<br>
**if**<br>
SPMonte\(\text{Carlo}((G')^{+B},s_{in})\)<br>
_returns error_<br>
**then**<br>
restart<br>
SPasVegas<br>
(<br>
_G<sub>in</sub>,s<sub>in</sub>_<br>
)<br>
;<br>
Let \(\phi(v)=\text{dist}_{(G^\prime)^{+B}}(s_{in},v)\) for all \(v\in V\) be obtained from the tree output by<br>
SPMonte\(\text{Carlo}((G')^{+B},s_{in})\)<br>
\(G_{nonneg}\leftarrow((G')^{+B})_\phi\) `// (Lemma 2.7) edge-weights in` _G<sub>nonneg</sub>_ `are non-negative`<br>
Obtain the subgraph \(G_{\le n}\) of _G<sub>nonneg</sub>_ consisting of edges of weight at most _n_<br>
**if** \(G_{\le n}\) _is acyclic_ **then** restart SPLasVegas(_G<sub>in</sub>,s<sub>in</sub>_);<br>
Let _C_ be an _arbitrary_ cycle of \(G_{\le n}\)<br>
**if** _C is not negative in G<sub>in</sub>_ **then** restart SPLasVegas(_G<sub>in</sub>,s<sub>in</sub>_);<br>
**return** _C_

**Lemma C.6.** _If Line 8 is reached and_ \((G')^{+(B-1)}\) _has a negative cycle then that cycle has weight less than n in G<sub>nonneg</sub>._

_Proof._ Edge-weights in \((G')^{+B}\) and \((G')^{+(B-1)}\) differ by at most 1, so if a cycle is negative in (_G_)<sup>+(_B_-1)</sup> it must have weight at most _n_ in \((G')^{+B}\). The Lemma then follows from the fact that _G<sub>nonneg</sub>_ and \((G')^{+B}\) are equivalent, so by Lemma 2.7, the weight of any cycle is the same in _G<sub>nonneg</sub>_ and in \((G')^{+B}\).

**Corollary C.7.** _If Line 8 is reached then every negative cycle in_ \((G')^{+(B-1)}\) _is a cycle in_ \(G_{\le n}\).

_Proof._ Consider any negative cycle _C_ in \((G')^{+(B-1)}\). By the preceding lemma, we know that _C_ has weight \(\le n\) in _G<sub>nonneg</sub>_. We also know that all edge-weights of _G<sub>nonneg</sub>_ are non-negative. This implies the corollary.

If a restart occurs in Line 11 then we simultaneously have that _B\>_0 and that \((G')^{+(B-1)}\) has no negative cycles by Corollary C.7, which means that the value of _B_ is not correct; Thus, by Lemma C.3, w.h.p. no restart occurs in Line 11.

Finally, Corollary C.9 below implies that w.h.p., no restart occurs in Line 13.

**Lemma C.8.** _If_ \(\text{FindThresh}(G',s_{in})\) _outputs a correct value B\>_0 _then_ \(B\ge n^2\).

_Proof._ Since we are assuming that _B\>_0 is correct, it must be the case that \(G'\) has some negative- weight cycle _C_, but \((G')^{+B}\) does not. Since all edge-weights in \(G'\) are integer multiples of _n_<sup>3</sup>, \(w_{G^\prime}(C)<0\) implies that \(w_{G^\prime}(C)\le-n^3\). We know that \(w_{(G^\prime)^{+B}}(C)\ge 0\), but also by definition of \((G')^{+B}\), we have that \(w_{(G^\prime)^{+B}}(C)=w_{G^\prime}(C)+B|C|\le w_{G^\prime}(C)+Bn\). Combining these inequalities yields \(Bn\ge n^3\), so \(B\ge n^2\).

**Corollary C.9.** _If_ \(\text{FindThresh}(G',s_{in})\) _outputs a correct value B\>_0_, every cycle in_ \(G_{\le n}\) _is a negative cycle in G<sub>in</sub>._

**Algorithm 6:** Algorithm SPLasVegas(_G<sub>in</sub>,s<sub>in</sub>_)

