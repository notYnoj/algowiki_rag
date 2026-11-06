We will show that as long as this holds, FindThresh returns a correct value of _B_. So from now on we assume that every execution of SPMMonteCarlo is good.

We now show that if FindThresh(_H,s_) returns _B_, then _G_<sup>+_B_</sup> does not contain a negative-weight cycle, as desired. To see this, note that the algorithm guarantees the invariant that _H_<sup>+_r_</sup> contains no negative-weight cycles: this is true initially because we start with _r=W<sub>H</sub>_, so by definition of _W<sub>H</sub>_, all edges in _H_<sup>+_r_</sup> are non-negative; it remains true because the algorithm only changes _r_ in Line 9, where the else-condition guarantees that _H_<sup>+_r_</sup> contains no negative-weight cycle. Since in the end the algorithm returns _B=r_, we know that _G_<sup>+_B_</sup> does not contain a negative-weight cycle.

Next, we show that if _H_ does contain a negative cycle, then FindThresh(_H,s_) returns _B_=0. This is because _H_<sup>+_q_</sup> will also never contain a negative-weight cycle (because _q_ is always positive), so the algorithm will repeatedly execute the else-statement in Line 9, eventually returning \(B=\ell=r=0\).

Finally, we need to show that if _H_ does contain a negative-weight cycle, then _H_<sup>+(_B_-1)</sup> contains a negative-weight cycle. Note that whenever the algorithm changes \(\ell\) in Line 7, the preceding if- condition guarantees that \(H^{+(\ell-1)}\) contains a negative cycle. The desired claim then follows from the fact that upon termination the algorithm returns \(B=\ell=r\).

## Appendix D Proof of Lemma 6.9

We start with some notation that sets up the main argument.

**Notation:**

• Throughout the proof we fix edge (_u,v_) and bound \(Pr[(u,v)\in E^{boundary}]\).<tbc>

• Whenever the algorithm executes the While loop in Line 11, it picks some light vertex. We will assume it chooses the next vertex to process according to some arbitrary ordering _s_<sub>1</sub>_,s_<sub>2</sub>_,..._. That is, there is some ordering _s_<sub>1</sub>_,s_<sub>2</sub>_,..._, of the vertices that are marked in-light or out-light (Line 7), such that every time the algorithm executes the while loop in Line 11, it does so by picking the first _s<sub>i</sub>_ in this ordering that has not yet been removed from _G_. Note that the ordering can be adversarially chosen; our analysis works with any ordering. Note also that once _s<sub>i</sub>_ is chosen, the direction of the ball (in-ball or out-ball) is uniquely determined because every vertex only receives one marking (see loop in Line 7).<tbc>

• When the algorithm picks _s<sub>i</sub>_, it grows the ball up to radius _R<sub>i</sub>_:=_R<sub>s<sub>i</sub></sub>_ from _s<sub>i</sub>_, where _R<sub>i</sub>∼Geo(p_) is a random variable. (See Line 12). (Note: _R_<sub>1</sub>_,...R<sub>n</sub>_ are the _only_ source of randomness in this proof.)<tbc>

• We now make a small technical change that does not affect the algorithm but simplifies the analysis. Let _W<sub>max</sub>_ be the heaviest edge weight in the graph and note that all shortest distances are \(\le(n-1)W_{max}\). Define _R<sub>max</sub>=nW<sub>max</sub>_. Note that if \(R_i\ge R_{max}\) then \(\text{Ball}_\text{G}^*(s_i,R_i)=\text{Ball}_\text{G}^*(s_i,R_{max})\). Thus, whenever _R<sub>i</sub>\>R<sub>max</sub>_, we instead set _R<sub>i</sub>=R<sub>max</sub>_. This has zero effect on the behaviour of the algorithm or the set _E<sup>boundary</sup>_ but will be convenient for the analysis because it ensures that we are now working with a _finite_ probabilistic space: there are a finite number of variables _R<sub>i</sub>_ and each one is an integer in the bounded set \[1_,R<sub>max</sub>_\].<tbc>

• Recall that _R<sub>i</sub>_∼Geo(_p_) where _p_=min{1,40log(_n)/D_} (Line 12). We will use this variable _p_ in our analysis.<tbc>

