**Algorithm 3** Bounded Multi-Source Shortest Path

function BMSSP(l,B,S)<br>
• requirement 1: \(|S|\le 2^{lt}\)<br>
• requirement 2: for every incomplete vertex x with d(x)\<B, the shortest path to x visits some<br>
complete vertex \(y\in S\)<br>
• returns 1: a boundary \(B'\le B\)<br>
• returns 2: a set U<br>
   if l=0 then<br>
   return \(B',U\leftarrow\mathrm{BASECASE}(B,S)\)<br>
  \(P,W\leftarrow\mathrm{FINDPIVOTS}(B,S)\)<br>
   D.Initialize(M,B) with \(M=2^{(l-1)t}\triangleright\mathcal{D}\) is an instance of Lemma 3.3<br>
  \(\mathcal{D}.\mathrm{INSERT}(\langle x,\widehat{d}[x]\rangle)\) for \(x\in P\)<br>
   \(i\leftarrow 0\); \(B'_0\leftarrow\mathrm{min}_{x\in P}\widehat{d}[x]\); \(U\leftarrow\emptyset\triangleright\) If \(P=\emptyset\) set \(B'_0\leftarrow B\)<br>
   while |U|\<k2<sup>lt</sup> and D is non-empty do<br>
   \(i\leftarrow i+1\)<br>
   \(B_i,S_i\leftarrow\mathcal{D}.\mathrm{PULL}()\)<br>
   \(B'_i,U_i\leftarrow\mathrm{BMSSP}(l-1,B_i,S_i)\)<br>
   \(U\leftarrow U\cup U_i\)<br>
   \(K\leftarrow\emptyset\)<br>
   for edge e=(u,v) where \(u\in U_i\) do<br>
   if \(\widehat{d}[u]+w_{uv}\le\widehat{d}[v]\) then<br>
\(\widehat{d}[v]\leftarrow\widehat{d}[u]+w_{uv}\)<br>
   if \(\widehat{d}[u]+w_{uv}\in[B_i,B)\) then<br>
\(\mathcal{D}.\mathrm{INSERT}(\langle v,\widehat{d}[u]+w_{uv}\rangle)\)<br>
   else if \(\widehat{d}[u]+w_{uv}\in[B'_i,B_i)\) then<br>
\(K\leftarrow K\cup\{\langle v,\widehat{d}[u]+w_{uv}\rangle\}\)<br>
   D.BATCHREPEND(\(K\cup\{\langle x,\widehat{d}[x]\rangle:x\in S_i\) and \(\widehat{d}[x]\in[B'_i,B_i)\}\))<br>
   return \(B'\leftarrow\mathrm{min}\{B'_i,B\}\); \(U\leftarrow U\cup\{x\in W:\widehat{d}[x]<B'\}\)

2. \(|S_x|\le 2^{l_xt}\), so the depth of T is at most (logn)/t=O(log<sup>1/3</sup>_n_);<tbc>

3. We break when \(|U_x|\ge k2^{l_xt}>|S_x|\). Intuitively, the size of _U<sub>x</sub>_ increases slowly enough so we should still have |_U<sub>x</sub>_|=_O(k_2<sup>_l<sub>x</sub>t_</sup>) (formally shown in Lemma 3.9);<tbc>

4. If node _x_ is a successful execution, in the execution of FINDPIVOTS, \(\widetilde{U}\) in Lemma 3.2 is equal to _U<sub>x</sub>_, so \(|P_x|\le|U_x|/k\) by Lemma 3.2;<tbc>

5. If node _x_ is a partial execution, \(|U_x|\ge k2^{l_xt}\ge k|S_x|\), so \(|P_x|\le|S_x|\le|U_x|/k\);<tbc>

6. For each node _x_ of T and its children \(y_1,\cdots,y_q\) in the order of the calls, we have:

• \(U_{y_1},\cdots,U_{y_q}\) are disjoint. For _i\<j_, distances to vertices in _U<sub>y<sub>i</sub></sub>_ are smaller than distances to vertices in _U<sub>y<sub>j</sub></sub>_;<tbc>

• \(U_x=W'_x\cup U_{y_1}\cup\cdots\cup U_{y_q}\);<tbc>

• Consequently, the _U<sub>x</sub>_’s for all nodes _x_ at the same depth in T are disjoint, and total sum of |_U<sub>x</sub>_| for all nodes _x_ in T is _O(n_(log_n)/t_).<tbc>

