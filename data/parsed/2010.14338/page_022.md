input :<br>
MinGMConn instance (P,D) and a positive integer \(s\ge 2\)<br>
output:<br>
Feasible solution \(Q\subseteq\mathbb{R}^2\) for (P,D)<br>
if there is only one x-group then return \(\emptyset\);<br>
divide the plane R<sup>2</sup> into a collection S of s vertical strips each of which contains roughly<br>
the same number of x-groups;<br>
foreach strip \(S\in\mathcal{S}\) do<br>
   \(Q\leftarrow Q\cup\text{VerticalManhattan}(P\cap S,D\cap(S\times S),s)\);<br>
   \((P',D')\leftarrow\pi_\mathcal{S}(P,D)\);<br>
   \(Q\leftarrow Q\cup\text{HorizontalManhattan}(P',D')\);<br>
return \(Q\cup\pi_\mathcal{S}(P)\);

## E.2 Analysis

We now proceed to analyze the algorithm. Let us repeat the subadditivity property of vertically separable demands shown earlier, stating that the number of vertically separable demands is at least as much as that of the sum of corresponding numbers in the inter-strip instance and all intra- strip instances together, and in turn at least as much as the sum of numbers of vertically separable demands in all inter-strip instances created by the algorithm.

**Corollary 20.** _Let_ M _be the collection of inter-strip instances_ \((P',D')\) _created in line 5 over all recursive calls of the algorithm_ RecursiveManhattan _applied to an instance_ (_P,D_) _of Generalized Manhattan Connections. We have that_

\(\mathsf{VS}(P,D)\ge\sum_{(P^\prime,D^\prime)\in\mathcal{M}}\mathsf{VS}(P',D').\)

_Proof._ Apply Lemma 12 recursively.

### Bounding the Cost.

We are now ready to prove that Algorithm 3 yields the section’s main result (Theorem 3).

_Proof of Theorem 3._ The feasibility of the solution computed by VerticalManhattan follows by inductively applying Lemma 19 in line 7 and the fact that HorizontalManhattan actually computes a feasible solution to the inter-strip instance \((P',D')\) in line 6.

To bound the cost of the solution, consider the collection M of inter-strip instances \((P',D')\) created in line 5 over all recursive calls of the algorithm RecursiveManhattan applied to input (_P,D,s_). By Lemma 11 and Corollary 20, we can bound the total cost of points added to our solution in line 6 for solving the inter-strip instances by

\(\sum_{(P^\prime,D^\prime)\in\mathcal{M}}O(log(s))\cdot\mathsf{VS}(P',D')\le O(log(s))\cdot\mathsf{VS}(P,D)\le O(log(s))\cdot\mathsf{OPT}(P,D).\)

To bound the cost of points added in Line 7 via projection, note that there are _O_(log_n/_log_s_) levels of recursion. Since each point ends up in precisely one sub-instance upon the recursive calls in Line 4 each original input point contributes at most two points to the projection computed in Line 7 at each recursion level. Hence, the overall cost of this step is \(O(logn/logs)\cdot|P|=O(logn/logs)\cdot\mathsf{OPT}(P,D)\).

Adding these two cost components gives an overall cost of \(O(logs+logn/logs)\cdot\mathsf{OPT}(P,D)\). The theorem follows by setting \(s=2^{\sqrt{logn}}\).

**Algorithm 3:** VerticalManhattan(_P,D,s_)

