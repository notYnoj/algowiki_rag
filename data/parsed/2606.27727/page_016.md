## 8:16 Beating Trivial Time for Tricky Triangle Tasks

To do this, repeat the hashed color _h<sub>c</sub>(c(i,j_)) in the lower \(\ell\) bits of each of the \(2\ell\)-length chunks. Take the XOR of this value with every word in the packed lists \(N(i)\cap S_v\) and \(N(j)\cap S_v\). Then, produce an indicator mask using Claim 16 with chunk size \(\ell\) to indicate edges with the appropriate color. We can then zero out ones in the mask corresponding to even chunk locations, as these correspond to a subset of the potential triangles and are taken care of by the earlier mask. We then shift the entire mask \(\ell\) bits to the left, so that our ones are aligned along the length \(2\ell\) chunks, as desired. Finally, we can AND this mask with the one created above, producing a mask that indicates all potential monochromatic triangles (but will have false positives corresponding to collisions under _h<sub>v</sub>_ and under _h<sub>c</sub>_).

We now need to check false positives, as in the All-Edges version. We note that the probability that any two length-\(2\ell\) entries collide (either under _h<sub>v</sub>_ or _h<sub>c</sub>_) is upper bounded by 2_/k_<sup>3</sup> by union bound. As a result, by the same argument as above, we expect _O_(1_/k_) collisions per color class per query in expectation. For each one, we look up both the original vertex name and also the true label, and verify that both preimages match. The expected preimage size is _O_(1_/k_<sup>2</sup>), so with high probability, we will only need to check a constant number of values here. Thus, the expected cost of checking all of these collisions is still _O_(1_/k_). As before, we simply allot ourselves a "budget" of false positives to check, and return "don’t know" on any queries for which we cannot check them all. By the same analysis, we obtain an expected running time of \(O(n^{1+2\delta} logw/w)\) for this problem.

## 5.2 A Faster Algorithm for Exact Triangle

We now consider Exact Triangle, which, unlike the problems mentioned above, can be sped up even in the dense case. The problem is known to require _n_<sup>3-_o_(1)</sup> time under both the 3SUM hypothesis [38] and the APSP hypothesis [37], but it admits a log-factor speedup using an equality product based approach similar to the one in Section 4.1.

\(\blacktriangleright\) **Definition 24** (Exact Triangle)**.** _This problem asks, given a target T and an n node graph with edge weights in_ {-_n<sup>c</sup>,...,n<sup>c</sup>_} _for some integer c\>_0_, does there exist a triple of vertices p,q,r such that w(p,q_)+_w(q,r_)+_w(r,p_)=_T?_

**Reminder of Theorem 4.** There is a Las Vegas algorithm that solves Exact Triangle on _n_-node graphs in expected _O(n_<sup>3</sup>log_w/w_<sup>3/2</sup>) time.

**Proof of Theorem 4.** Without loss of generality, we may assume the graph _G_=(_V,E_) is tripartite with parts _I_, _J_, and _K_, where each part has _n/_3 nodes. Given a target weight _T_, and weight function \(w':E\rightarrow\mathbb{Z}\), we want to determine if there are \(i\in I\), \(j\in J\), and \(k\in K\) such that _i,j,k_ is a triangle and \(w'(i,j)+w'(j,k)+w'(k,i)=T\). For simplicity, we assume that all weights are in [-2_<sup>w</sup>,_2_<sup>w</sup>_] where _w_ is the word size.

Let \(t=\sqrt{w}/(6\sqrt{logw})\). We split the nodes of _I_, _J_, and _K_ into at most _n/t_+1 _groups_ of _t_ nodes each. Our idea is to check each triple of groups (containing 3_t_ nodes and _O(t_<sup>2</sup>) edges) for an exact triangle, using a constant number of word operations.

To this end, we let \(\ell:=10logw\), and we will hash all edge weights modulo a random prime _p_ from the integer interval \(\big[2,2^\ell\big]\). (To be clear, we replace each edge weight with the corresponding residue in {0,1_,...,p_-1}.) By the Prime Number Theorem, a random integer in this range is prime with probability \(\Omega(1/\ell)\). We can efficiently find such a prime by picking integers at random and primality testing. Note that this process costs only an (additive) poly(log_w_) factor.

\(\blacktriangleleft\)

