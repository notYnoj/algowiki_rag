\(\ell\leftarrow 0\text{and}r\leftarrow W_H\)<br>
while TRUE do `// Repeat loop until a value is returned`<br>
   If \(\ell=r\) return r<br>
   \(q\leftarrow\lfloor(\ell+r)/2\rfloor\)<br>
   Execute SPMonteCarlo(H<sup>+</sup>_q,s_).<br>
   if SPMonteCarlo returned an error then `// w.h.p H`<sup>+</sup>_q_ has a negative cycle<br>
   \(\ell\leftarrow q+1\)<br>
   else `// H`<sup>+</sup>_q_ does not contain a negative cycle<br>
   \(r\leftarrow q\)

<tbc>_Proof._ Consider a cycle _C_ in \(G_{\le n}\). We have \(w_{G_{\le n}}(C)\le n^2\) because every edge of \(G_{\le n}\) has weight \(\le n\). We now show that _C_ is a negative-weight cycle in \(G'\), which also implies that it is negative in _G<sub>in</sub>_. Observe that<tbc>

\(w_{(G^\prime)^{+B}}(C)=w_{((G^\prime)^{+B})_\phi}(C)=w_{G_{nonneg}}(C)=w_{G_{\le n}}(C),\)

<tbc>where the first equality is because price functions do not change weights of cycles, the second equality is because \(G_{nonneg}=((G')^{+B})_\phi\) and the last equality is because \(G_{\le n}\) is a subgraph of _G<sub>nonneg</sub>_ with the same edge weights. It follows that

\(w_{G^\prime}(C)=w_{(G^\prime)^{+B}}(C)-B|C|=w_{G_{\le n}}(C)-B|C|\le w_{G_{\le n}}(C)-2B\le n^2-2n^2<0,\)

as desired. (In the inequalities, we use the facts that every cycle has at least two edges and \(B\ge n^2\) by the previous lemmas.)

A union bound over the constant number of restart-lines now shows that w.h.p., no restart occurs. We conclude that w.h.p., SPLasVegas(_G<sub>in</sub>,s<sub>in</sub>_) runs in time _O(m_log<sup>8</sup>(_n_)).

## C.3 Proof of Lemma C.3 - FindThresh

In this section, we describe algorithm FindThresh from Lemma C.3. Recall the definition of _W<sub>H</sub>_ from the beginning of Section C. The algorithm (Algorithm 7) is a simple binary search.

**Runtime.** By a standard binary-search argument, the loop is executed _O_(log(_W<sub>H</sub>_)) times. Each iteration is dominated by the call to SPMonteCarlo, which takes time _O(m_log<sup>6</sup>(_n_)log(_W<sub>H</sub>_)). The total runtime of FindThresh is thus _O(m_log<sup>6</sup>(_n_)log<sup>2</sup>(_W<sub>H</sub>_)), as desired.

**Correctess.** We now show that w.h.p. FindThresh(_H,s_) returns a correct value of _B_. The only probabilistic component of FindThresh is SPMonteCarlo(_G,s_). Recall the guarantees of SPMonteCarlo(_G,s_) from Theorem C.1: if _G_ contains a negative-weight cycle then the algorithm _always_ returns an error message; if _G_ does not contain a negative-weight cycle then with high probability it does not. We say that an execution of SPMonteCarlo(_G,s_) is _bad_ if _G_ does not contain a negative-weight cycle, but the algorithm returns an error; otherwise we say the execution is _good_.

We know from Theorem C.1 that an execution of SPMonteCarlo is good w.h.p. Since FindThresh only executes SPMonteCarlo a total of log(_W<sub>H</sub>_) times, and we will only run FindThresh on a graph with weights polynomial in _n_, a union bound implies that _every_ execution of SPMonteCarlo is good.<tbc>

**Algorithm 7:** Algorithm for FindThresh(_H,s_)

