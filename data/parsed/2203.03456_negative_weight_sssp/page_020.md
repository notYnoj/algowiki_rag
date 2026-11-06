<tbc>at this level of recursion each vertex participates in at most one ball. Each ball is computed via Dijkstra’s algorithm, which requires _O_(log(_n_)) time per vertex explored and _O_(1) time per edge explored.<sup>20</sup> So, the total time to execute the while loop is _O_(|_V(G_)|log(_n_)+|_E(G_)|).

Finally, checking the diameter in Line 20 only requires a single execution of Dijkstra’s algorithm. Thus the overall non-recursive work is _O_(|_V(G_)|log<sup>2</sup>(_n_)+|_E(G_)|log(_n_)). By Observation 6.4, each vertex (and thus each edge) participates in _O_(log(_n_)) calls, completing the lemma.

## 6.3 Bounding termination probabilities

We now show that it is extremely unlikely for the algorithm to terminate in Lines 15 or 20. When we discuss some call LDD(_G,D_) in this subsection, we will use _G_<sub>0</sub> to the denote the initial input to LDD(_G,D_), in order to differentiate it from the graph _G_ from which vertices can be deleted over the course of the algorithm (Line 18). Note that we always have \(G\subseteq G_0\).

We start with a useful auxiliary claim.

**Claim 6.7.** _Consider a single call_ LDD(_G,D_) _(ignoring all future recursive calls). Then, with probability_ \(\ge 1-O(1/n^{19})\)_, the following holds:_

• _For any vertex v marked in-light we have_ \(|\mathrm{Ball}_{\mathrm{G}_0}^\mathrm{in}(v,D/4)|\le.7|V(G_0)|\)<tbc>

• _For any vertex v marked out-light we have_ \(|\mathrm{Ball}_{\mathrm{G}_0}^\mathrm{out}(v,D/4)|\le.7|V(G_0)|\)<tbc>

• _For any vertex v marked heavy we have_ \(|\mathrm{Ball}_{\mathrm{G}_0}^\mathrm{in}(v,D/4)|>.5|V(G_0)|AND|\mathrm{Ball}_{\mathrm{G}_0}^\mathrm{out}(v,D/4)|>.5|V(G_0)|\)

_Proof._ Consider any single instance of a vertex _v_ being marked during the recursive call. We will show that for this vertex the claim holds with probability \(\ge 1-O(1/n^{20})\). A union bound over all \(|V(G_0)|\le n\) vertices completes the lemma.

We first show that for any vertex _v_ such that \(|\mathrm{Ball}_{\mathrm{G}_0}^\mathrm{in}(v,D/4)|>.7|V(G_0)|\), we have Pr\[_v_ is marked in-light \(]\le 1/n^{20}\) : Since \(|\mathrm{Ball}_{\mathrm{G}_0}^\mathrm{in}(v,D/4)|>.7|V(G_0)|\) and since the _k=c_log(_n_) vertices from _S_ are sampled randomly, we know that \(\unknown[|\mathrm{Ball}_{\mathrm{G}_0}^\mathrm{in}(v,D/4)\cap S|]>.7k\). But for _v_ to be marked in-light we must have \(|\mathrm{Ball}_{\mathrm{G}_0}^\mathrm{in}(v,D/4)\cap S|\le.6k\); a Chernoff bounds shows such a high deviation from expectation to be extremely unlikely.<sup>21</sup>

By similar proofs, it also holds that (a) for any vertex _v_ such that \(|\mathrm{Ball}_{\mathrm{G}_0}^\mathrm{out}(v,D/4)|>.7|V(G_0)|\), we have Pr\[_v_ is marked out-light \(]\le 1/n^{20}\) and (b) for any vertex _v_ such that \(|\mathrm{Ball}_{\mathrm{G}_0}^\mathrm{in}(v,D/4)|\le.5|V(G_0)|\) or \(|\mathrm{Ball}_{\mathrm{G}_0}^\mathrm{out}(v,D/4)|\le.5|V(G_0)|\), we have Pr\[_v_ is marked heavy\(]\le 1/n^{20}\).

**Claim 6.8.** _Consider a single call_ LDD(_G,D_) _(ignoring all future recursive calls). With probability_ \(\ge 1-O(1/n^{19})\), LDD(_G,D_) _does not terminate in Lines 15 or 20._

_Proof._ Let us assume that the statement of Claim 6.7 holds. Under this assumption the algorithm clearly cannot terminate in the second condition in Line 15 (i.e. \(\mathrm{Ball}_\mathrm{G}^*(v,R_v)\) being too large), because \(\mathrm{Ball}_\mathrm{G}^*(v,R_v)\subseteq\mathrm{Ball}_{\mathrm{G}_0}^*(v,R_v)\). We now show that the algorithm also cannot terminate in<tbc>

<sup>20</sup>A standard Dijkstra’s implementation requires _O_(|_V(G_)|) time to initialize the priority queue and vertices’ labels (e.g. \[CLRS09\]). This can be easily modified to avoid the initialization time (e.g. \[TZ05\]). One way to do this is to initialize the priority queue and labels _once_ in the beginning of Phase 2. After we use them to compute each ball \(\mathrm{Ball}_\mathrm{G}^*(v,R_v)\) on Line 13, we reinitialize them at the cost of the number of explored vertices. <sup>21</sup>We use the following Chernoff’s bound. For any independent 0/1 random variables _X_<sub>1</sub>_,...,X<sub>k</sub>_, if \(X_{avg}:=(1/k)\sum_{i=1}^kX_i\), then \(Pr[X_{avg}<\unknown[X_{avg}]-\epsilon]\le e^{-2k\epsilon^2}\). Here, we use \(\epsilon=0.1\) and define _X<sub>i</sub>_=1 iff \(s_i\in\mathrm{Ball}_{\mathrm{G}_0}^*(v,D/4)\) (so, \(\unknown[X_{avg}]=\frac{|\mathrm{Ball}_{\mathrm{G}_0}^*(v,R_v)|}{|V(G_0)|}>0.7\)).

