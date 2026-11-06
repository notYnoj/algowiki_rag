Finally, before we end the sub-routine, we update _U_ to include every vertex _x_ in the set _W_ returned by \(\text{FinDPIVOTS}\) with \(\widehat{d}[x]<B'\).

**Algorithm 2** Base Case of BMSSP

function BaseCase(_B,S_)<br>
• requirement 1: S={x} is a singleton, and x is complete<br>
• requirement 2: for every incomplete vertex v with d(v)\<B, the shortest path to v visits x<br>
• returns 1: a boundary \(B'\le B\)<br>
• returns 2: a set U<br>
   \(U_0\leftarrow S\)<br>
   initialize a binary heap H with a single element \(\langle x,\widehat{d}[x]\rangle\) \[Wil64\]<br>
   while H is non-empty and |U<sub>0</sub>|\<k+1 do<br>
   \(\langle u,\widehat{d}[u]\rangle\leftarrow\mathcal{H}.\text{ExtractMin}()\)<br>
   \(U_0\leftarrow U_0\cup\{u\}\)<br>
   for edge e=(u,v) do<br>
   if \(\widehat{d}[u]+w_{uv}\le\widehat{d}[v]\) and \(\widehat{d}[u]+w_{uv}<B\) then<br>
   \(\widehat{d}[v]\leftarrow\widehat{d}[u]+w_{uv}\)<br>
   if v is not in H then<br>
\(\mathcal{H}.\text{Insert}(\langle v,\widehat{d}[v]\rangle)\)<br>
   else<br>
\(\mathcal{H}.\text{DecreaseKey}(\langle v,\widehat{d}[v]\rangle)\)<br>
   if \(|U_0|\le k\) then<br>
\(\text{return}B'\leftarrow B,U\leftarrow U_0\)<br>
   else<br>
\(\text{return}B'\leftarrow max_{v\in U_0}\widehat{d}[v],U\leftarrow\{v\in U_0:\widehat{d}[v]<B'\}\)

**Remark 3.4.** Note that on Line 7 of Algorithm 1, Line 8 of Algorithm 2 and Line 15 of Algorithm 3, the conditions are "\(\widehat{d}[u]+w_{uv}\le\widehat{d}[v]\)". The equality is required so that an edge relaxed on a lower level can be re-used on upper levels.

**Remark 3.5.** Using methods in Lemma 3.3 to implement data structure D in Algorithm 3 at level _l_, where _M_=2<sup>(_l_-1)_t_</sup>, and \(|S|\le 2^{lt}\), the total number of insertions _N_ is _O(k_2<sup>_lt_</sup>), because of the fact that |_U_|=_O(k_2<sup>_lt_</sup>), the constant-degree property, and the disjointness of _U<sub>i</sub>_’s (as established later in Remark 3.8). Also, size of _K_ each time is bounded by _O_(|_U<sub>i</sub>_|)=_O(k_2<sup>(_l_-1)_t_</sup>). Thus, insertion to D takes _O_(log_k+t_)=_O(t_) time, and Batch Prepend takes _O_(log_k_)=_O_(loglog_n_) time per vertex in _K_.

## 3.2 Observations and Discussions on the Algorithm

We first give some informal explanations on the algorithm, and then in the next subsections, we will formally prove the correctness and running time of the algorithm.

### What can we get from the recursion?

Let’s look at the recursion tree T of Algorithm 3 where each node _x_ denotes a call of the BMSSP procedure. Let _l<sub>x</sub>_ , _B<sub>x</sub>_, and _S<sub>x</sub>_ denote the parameters _l_, _B_, and _S_ at node _x_, \(B'_x\) and _U<sub>x</sub>_ denote the returned values \(B'\) and _U_ at node _x_, _P<sub>x</sub>_ and _W<sub>x</sub>_ denote _P_ and _W_ (on Line 4) returned by the \(\text{FinDPIVOTS}\) procedure at node _x_, respectively, and \(W'_x\) denote the set of vertices \(v\in W_x\) satisfying \(d(v)<B'_x\). Then we expect:

1. Since we assume that all vertices are reachable from _s_, in the root _r_ of T , we have _U<sub>r</sub>=V_ ;<tbc>

