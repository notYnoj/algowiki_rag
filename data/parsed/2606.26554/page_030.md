1. If \(R-L\le 2\), compute reach(_s,v_) for all \(s\in S_\mathrm{in}\) and \(L<v\le R\).<tbc>

2. Set \(M\leftarrow\lfloor(L+R)/2\rfloor\) and run `complete`(_G,S_<sub>in</sub>_,L,M_).<tbc>

3. Construct \(S_\mathrm{in}\times[L,M]\) matrix _X_ and \([L,M]\times[M,R]\) matrix _Y_ with entries

\(X[s,u]=\mathrm{reach}(s,u),Y[u,v]=\unknown[(u,v)\in E].\)

Compute _XY_ and update \(\mathrm{reach}(s,v)\leftarrow^\vee(XY)[s,v]\) for all \(s\in S_\mathrm{in},v\in V\) .<tbc>

4. Run `complete`(_G,S_<sub>in</sub>_,M,R_).

Our algorithm for Multiple-Source Reachability computes `complete`(_G,S_<sub>in</sub>,0,|_V_|). We prove the correctness of our algorithm via the following inductive claim.

**Claim 6.2.** _Suppose_ reach(_s,v_) _is computed for all_ (_s,v_) _such that_ \(s\in S_\mathrm{in}\) _and_ \(v\le L\) _or_ \(\mathrm{pred}(s,v)\le L\) _before the execution of `complete`(G,S_<sub>in</sub>_,L,R). Then, after the execution of `complete`(G,S_<sub>in</sub>_,L,R),_ reach(_s,v_) _is computed for all_ (_s,v_) _with_ \(s\in S_\mathrm{in}\) _and_ \(v\le R\).

First, we argue that the claim suffices to compute reach(_s,v_) for all \(s\in S_\mathrm{in}\) and \(v\in V\) . When _L_=0, there is exactly one vertex \(\le L\), say _s_<sup>∗</sup> in _L_. If \(s^*\unknown\in S_\mathrm{in}\), then we set reach(_s,v_)=0 for all _s,v_. If \(s^*\in S_\mathrm{in}\), we note \(\mathrm{pred}(s,v)\le 0\) if and only if \(v\in N^+(s^*)\) is an out-neighbor of _s_<sup>∗</sup>. In this case, we update reach(_s_<sup>∗</sup>_,v_)=1 for all \(v\in N^+(s^*)\) in _O(n_) time. In either case, the assumption of Claim 6.2 is satisfied. Thus, the claim ensures that reach(_s,v_) is computed for all \(s\in S_\mathrm{in}\) and \(v\in V\) . It remains to prove Claim 6.2.

_Proof of Claim 6.2._ We begin by describing how to compute `complete` in the base case (i.e. \(R-L\le 2\)). Note that in _O_(1) time, we can compute reach(_a,b_) for all \(a,b\in[L,R]\). Then, for all \(s\in S_\mathrm{in}\) and \(v\in[L,R]\), we set

\(\mathrm{reach}(s,v)\leftarrow^\vee\vee_{L\le u<v}(\mathrm{reach}(s,u)\wedge\mathrm{reach}(u,v)).\) (4)

This completes the description of our algorithm.

To prove correctness, we first observe that whenever reach(_s,v_)=1, there exists a path from _s_ to _v_. Thus, it suffices to show that we set reach(_s,v_)=1 if there exists a path from _s_ to _v_. Fix \(s\in S_\mathrm{in}\) and \(v\le R\) such that there is a path from _s_ to _v_. We may assume _v\>L_ and pred(_s,v)\>L_. Otherwise, we already have reach(_s,v_)=1 by the input assumption, and observe that our algorithm never decreases (i.e. flip from 1 to 0) reach(_s,v_).

We then proceed by induction, beginning with the base case. In the base case, we need to compute reach(_s,v_) for \(s\in S_\mathrm{in}\) and \(L<v\le R\le L+2\). Since we compute the transitive closure of \[_L,R_\], we compute reachability following the update rule of Equation (4) if \(s\le L\) and from the transitive closure of \[_L,R_\] if \(L\le s\le R\).

We now conclude the proof of correctness with the inductive case. We may assume _v\>M_, as otherwise the first recursive call `complete`(_G,S_<sub>in</sub>_,L,M_) computes reach(_s,v_). We consider two cases.

## Case 1: \(\mathrm{pred}(s,v)\le M\).

We have \(L<\mathrm{pred}(s,v)\le M\), or there exists \(L<u\le M\) such that reach(_s,u_)=1 and \((u,v)\in E\). In this case, since \(u\le M\), we have _X_\[_s,u_\]=reach(_s,u_)=1 and _Y_\[_u,v_\]=1. In particular, (_XY_)\[_s,v_\]=1 so we set \(\mathrm{reach}(s,v)\leftarrow 1\) as desired.

## Case 2: pred(_s,v)\>M_.

From the previous case, when we call `complete`(_G,S_<sub>in</sub>_,M,R_), we have computed reach(_s,v_) for all \(s\in S_\mathrm{in}\) and \(v\le M\) (handled by first recursive call) or \(\mathrm{pred}(s,v)\le M\) (handled by Case 1). Thus, we satisfy the input assumption of Claim 6.2, and obtain reach(_s,v_) for all \(v\le R\) by induction.

Finally, we bound the running time. Note that an invocation of the base case requires _O_(|_S_<sub>in</sub>|) time. In the base case, we compute the transitive closure of \[_L,R_\] in _O_(1) time as the graph is sorted in topological<tbc>

