## Running Time.

The initial call to Lemma 3.3 takes time \(\widetilde{O}(|X||Y_1|\dots|Y_k||A|/p')\). In the un popular case, the construction of _Y_ takes time \(O(|Y|)=O(|Y_1|\dots|Y_k|\cdot R/p)\) (which will turn out to be negligible). The meet-in-the-middle algorithm takes time _O_(|_A_||_X_|) to prepare the hash table, plus time _O_(|_B_||_Y_|) to enumerate all pairs (_a,x_). To bound the total time of listing all 4-tuples (_a,b,x,y_), note that each unpopular item _b_ can be represented in at most \(2p'\) ways as

\(b=x+y_1+\cdots+y_k-a.\)

For each such representation, the tuple (_y_<sub>1</sub>_,...,y<sub>k</sub>_) is part of _Y_ only with probability _R/p_, and thus the total number of solutions _a=x+y-b_ is at most \(O(p'\cdot R/p)=O(|A|/s\cdot R)\) (in expectation and with high probability) for any unpopular _b_. In particular, the algorithm lists at most \(O(|B||A|/s\cdot R)\) such solutions overall. The popular case runs in linear time.

We are finally ready to prove Lemma 4.5.

## Proof of Lemma 4.5.

Let \(c=1-2\rho+3\epsilon\) and let \(k=k(c,\epsilon)\) be the constant from Theorem 3.5. Note that the statement of Lemma 4.3 allows us to arbitrarily decrease \(\epsilon\); all parts of the lemma benefit from smaller \(\epsilon\), except for the non-explicit dependence of \(\delta\). For convenience we will therefore decrease \(\epsilon\) whenever convenient.

## Step 1: Removing Popular _k_-Sums.

We will first repeatedly remove elements from _A_ until it contains no more popular _k_-sums/differences. More precisely, we will ensure that \(\mathrm{Pop}^k(\pm A;p)=\emptyset\) for \(p:=|A|^{k-1-c}\).

Run Theorem 3.5 on \(\pm A\) with parameter _p_, leading to one of two possible outcomes. If it certifies that \(\mathrm{Pop}^k(\pm A;p)=\emptyset\), then step 1 is complete and we move on to step 2. Otherwise, Theorem 3.5 identifies a subset \(A'\subseteq A\) of size \(|A'|\ge|A|/K\) along with a _K_-doubling \(K|A|^{2-2\rho+3\epsilon}\)-container of \(A'\), for some \(K=O(|A|^\epsilon)\). In this event we take \((A',B,C)\) as one of the constructed subinstances (the container is not quite as claimed; we deal with this issue in a moment). We then remove \(A'\) from _A_, and repeat the execution of step 1.

All in all, there can be at most \(\widetilde{O}(|A|^\epsilon)\) repetitions as each repetition removes \(\Omega(|A|^{1-\epsilon})\) elements from _A_. In particular, the number of constructed subinstances is \(\widetilde{O}(|A|^\epsilon)\), and each subinstance is \(O(|A|^\epsilon)\)-doubling \(O(|A|^{2-2\rho+4\epsilon})\)-contained. By Lemma 4.6 (applied with \(t=|A|^{4\epsilon}\)) we can further refine these subinstances to \(O(|A|^{5\epsilon})\) instances that are \(\widetilde{O}(|A|^{5\epsilon})\)-doubling \(O(|A|^{2-2\rho})\)-contained. This is as claimed when reducing \(\epsilon\) by a constant.

## Step 2: Small Sets.

Next, we easily assert that \(n\le|A|^{1+\epsilon}\). Otherwise we can solve the whole instance trivially in time \(n^{2-\Omega(\epsilon)}\), and report the set of solutions T .

## Step 3: Popular _k_-Sum Covers.

Once we reach this step, we will exhaustively list all 3SUM solutions. Let T be initially empty. We will successively remove elements from _B_ and _C_, while maintaining the invariant that each 3SUM solution that is eliminated in this way has already been listed in T . The algorithm runs in iterations \(\ell=1,\dots,k\). We also maintain the second invariant that, before the \(\ell\)-th iteration,

\(\left\{\begin{array}{ c c }
B\subseteq\mathrm{Pop}(X,Y_1,\dots,Y_\ell;p_\ell) & \text{if}\ell\text{is even}, \\
C\subseteq\mathrm{Pop}(X,Y_1,\dots,Y_\ell;p_\ell) & \text{if}\ell\text{is odd}.
\end{array}\right.\)

