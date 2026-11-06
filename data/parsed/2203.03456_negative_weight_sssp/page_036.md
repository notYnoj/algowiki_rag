• We define _G<sub>i</sub>_:=_G<sub>i</sub>(R_<sub>1</sub>_...R_<sub>_i_-1</sub>) as follows. If _s<sub>i</sub>_ is already removed from _G_ when it is considered by the while loop in Line 11 then we define _G<sub>i</sub>_ as the empty set. Else, we define _G<sub>i</sub>_ to be the graph after _every_ \(s_j\in\{s_1,s_2,\dots s_{i-1}\}\) has either been processed by the while loop (i.e. a ball was grown from this _s<sub>j</sub>_) or removed from _G_ by the algorithm. Note that _G<sub>i</sub>_ is a random variable whose value depends on _R_<sub>1</sub>_,...,R_<sub>_i_-1</sub>.<tbc>

• Define \(B_i:=\mathrm{Ball}_{G_i}^*(s_i,R_i)\), where the ∗ refers to the direction (in or out) uniquely determined by the choice of _s<sub>i</sub>_. _B<sub>i</sub>_ is a random variable whose value depends on _R_<sub>1</sub>_,...,R<sub>i</sub>_. Note that if _G<sub>i</sub>_ is empty then so is _B<sub>i</sub>_.<tbc>

• Define _I<sub>i</sub>_ to be the event that \(u,v\notin B_1,\dots,B_{i-1}\) AND \(u\in B_i\) if the algorithm grows an out-ball \(B_i=\mathrm{Ball}_\mathrm{G}^\mathrm{out}(s_i,R_i)\); otherwise (if the algorithm grows an in-ball \(B_i=\mathrm{Ball}_\mathrm{G}^\mathrm{in}(s_i,R_i)\)), _I<sub>i</sub>_ is defined to be the event that \(u,v\notin B_1,\dots,B_{i-1}\) AND \(v\in B_i\). (I stands for "included".)<tbc>

• Define _X<sub>i</sub>_ to be the event \(v\notin B_i\) if the algorithm grows an out-ball \(B_i=\mathrm{Ball}_\mathrm{G}^\mathrm{out}(s_i,R_i)\); otherwise (if the algorithm grows an in-ball \(B_i=\mathrm{Ball}_\mathrm{G}^\mathrm{in}(s_i,R_i)\)), _X<sub>i</sub>_ is defined to be the event \(u\notin B_i\). (X stand for "excluded".)

**Observation D.1.**<tbc>

• _I<sub>i</sub> and X<sub>i</sub> are independent from R<sub>j</sub> for j\>i; in other words, I<sub>i</sub> and X<sub>i</sub> only depend on R_<sub>1</sub>_,...,R_<sub>_i_-1</sub>_,R<sub>i</sub>._<tbc>

• _The events I<sub>i</sub> are disjoint and thus_ \(\sum\mathrm{Pr}[I_i]\le 1\).<tbc>

• \(\mathrm{Pr}[(u,v)\in E^{boundary}]=\sum_{i\ge 0}Pr_{R_1,\dots,R_i}[I_i\wedge X_i]\).

_Proof._ The first property is clear. For the second property, note that if _I<sub>i</sub>_ is true then \(u\in B_i\), so _u_ will be removed from the graph (Line 18) and not be present in any _G<sub>j</sub>_, _j\>i_, so all _I<sub>j</sub>_, _j\>i_ are false. For the third property, note that (_u,v_) is added to _E<sup>boundary</sup>_ if and only if for some _i_, both _u_ and _v_ are present in _G<sub>i</sub>_ and (_u,v_) is in the boundary of ball _B<sub>i</sub>_ (Line 14), which is precisely captured by \(I_i\wedge X_i\).

Before proceeding with the proof, we will state a common assumption about probabilistic notation that greatly simplifies the presentation

**Assumption D.2.** Given probabilistic events _A,B_, we define Pr\[_A|B_\]=0 if Pr\[_B_\]=0.

This leads to significantly simpler notation because it allows us to write \(\mathrm{Pr}[A\wedge B]=\mathrm{Pr}[B]\cdot\mathrm{Pr}[A|B]\) and separately bound Pr\[_A|B_\] without worrying about undefined conditional probabilities when Pr\[_B_\]=0. This notational simplification is commonly used to state the following law of total probability (which we will use later): If {_B_<sub>1</sub>_,B_<sub>2</sub>_,..._} is a finite or countably infinite partition of a sample space (i.e. it is a set of pairwise disjoint events whose union is the entire sample space) and _A_ is another event, then

\(\mathrm{Pr}[A]=\sum_i\mathrm{Pr}[A\wedge B_i]=\sum_i\mathrm{Pr}[A|B_i]\mathrm{Pr}[B_i].\) (13)

(Without Assumption D.2 the sum on the right-hand side and its applications below must be only over _i_ such that Pr\[_B<sub>i</sub>_\]_\>_0.) The assumption is justified because we are dealing with a finite probability space, so all zero-probability events combined still have zero probability mass.<sup>23</sup>

This notational assumption allows us to state the following lemma.

<sup>23</sup>By contrast, in an infinite space one would have to be more careful about such an assumption: it is possible for _every_ individual instantiation of the random variables to have probability 0, but all infinity of them combined to have probability mass 1.

