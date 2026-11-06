_Proof._ Let \((P',D')=\pi_\mathcal{S}(P,D)\) be the inter-strip instance. Let \(D''\subseteq D'\) be a vertically separable demand subset of size \(\mathsf{VS}(P',D')\). Let \(D_\mathsf{I}=\{(p,q)\in D|(\pi_\mathcal{S}(p),\pi_\mathcal{S}(q))\in D''\}\) be the demand subset of _D_ corresponding to \(D''\). For any \(S\in\mathcal{S}\), let _D_<sub>S</sub> be a vertically separable demand subset of \(D\cap(S\times S)\) of cardinality \(\mathsf{VS}(P\cap S,D\cap(S\times S))\). We claim that \(D_\mathsf{I}\cup\bigcup_{S\in\mathcal{S}}D_S\) is a vertically separable demand subset of _D_. Obviously, its size is equal to the right side of the inequality that we want to prove.

Since \(D''\) is vertically separable, we can sequentially cut it via vertical line segments. W.l.o.g. we may assume that these segments lie on strip boundaries. Observe also that any vertical line segment _z_ on some strip boundary cuts (intersects) some rectangle \(R(\pi_\mathcal{S}(p),\pi_\mathcal{S}(q))\) with \((\pi_\mathcal{S}(p),\pi_\mathcal{S}(q))\in D''\) if and only if cuts (intersects) _R(p,q_) where \((p,q)\in D_\mathsf{I}\). Hence, the same sequence of vertical line segments on the strip boundaries that cuts \(D''\) also cuts _D_<sub>I</sub>.

After cutting _D_<sub>I</sub>, process the strips \(S\in\mathcal{S}\) in an arbitrary order and cut the demand set _D<sub>S</sub>_ with segments contained in the interior of _S_. Obviously, there is no interference between cutting within different strips and none of the segments we used for cutting _D_<sub>I</sub> intersects any rectangle in _D<sub>S</sub>_ because they lie on the strip boundaries.

**Divide-and-conquer.** Choose the strips S so that \(s=|\mathcal{S}|=2^{\sqrt{logn}}\). Thus the inter-strip instance admits an approximation of ratio \(O(logs)=O(\sqrt{logn})\); in fact, we obtain a solution of cost \(O(\sqrt{logn})\mathsf{VS}(\pi_\mathcal{S}(P,D))\). We recursively solve each intra-strip instance (_P<sub>i</sub>,D<sub>i</sub>_), and combine the solutions from these _s_+1 sub-instances. (Details on how the solution can be combined are deferred to Appendix E.)

We show by induction on the number of points that for any instance (_P,D_) the cost of the computed solution is \(O(\sqrt{logn})\mathsf{VS}(P,D)\). (Here, we do not take into account the cost incurred by combining the solutions to the sub-instances.) By induction hypothesis, we have for each (_P<sub>i</sub>,D<sub>i</sub>_) a solution of cost \(O(\sqrt{logn})\mathsf{VS}(P_i,D_i)\) since |_P<sub>i</sub>|\<|P_|. Note that we cannot use the induction hypothesis for the inter-strip instance since \(|P'|=|P|\), which is why we need the _O_(log_s_)-approximation algorithm. Using sub-additivity we obtain:

\(O(\sqrt{logn})\left(\mathsf{VS}(\pi_\mathcal{S}(P,D))+\sum_{S\in\mathcal{S}}\mathsf{VS}(P\cap S,D\cap(S\times S))\right)=O(\sqrt{logn})\mathsf{VS}(P,D).\)

There is an additional cost incurred by combining the solutions of the sub-instances to a feasible solution of the current instance. In Appendix E we argue that this can be done at a cost of _O_(OPT) for each of the \(logn/logs=\sqrt{logn}\) many levels of the recursion. (This prevents us from further improving the approximation factor by picking \(s=2^{o(\sqrt{logn})}\).)

S1
S2
S3
S4

Figure 4: An illustration of the inter-strip instance. Each strip _S<sub>i</sub>_ is collapsed into one column. The red demands are demands between pairs of points lying inside different strips. The black demands are demands that are handled by intra-strip instances.

