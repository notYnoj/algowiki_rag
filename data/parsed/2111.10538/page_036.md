**Case 2:** \(|\widetilde{B}_j|\ge d/\epsilon_0\)**:** Then we throw out this pair. We throw out at least \(d/\epsilon_0\) characters, but we only decrease the entire lcs by at most _d_.

**Case 3:** \(|\widetilde{B}_j|\le d\epsilon_0\) : Then we also throw out this pair. We throw out at least _d_ characters, but we only decrease the entire lcs by at most \(\epsilon_0d\).

Let _Z_ denote the set of _A_-windows that we don’t throw out. Whenever we throw out a pair, the amount of lcs got decreased is always at most \(\epsilon_0\) fraction of the characters we throw out. There are 2_n_ characters in total. Then we decrease the lcs by at most \(2\epsilon_0n\), i.e.,

\(\sum_{j\in Z}\mathsf{lcs}(\widetilde{A}_j,\widetilde{B}_j)\ge\mathsf{lcs}(A,B)-2\epsilon_0n,\) (10)

We now derive, for each \(j\in Z\), a _window_ \(B_j\subseteq\widetilde{B}_j\) of approximately the same length. Let \(i\in\{-f+1,\dots,f\}\) be the layer such that \(|\widetilde{B}_j|\in(d(1+\epsilon_0)^i,d(1+\epsilon_0)^{i+1})\). Similarly, \(\widetilde{B}_j\)’s starting index is in \(\big((y-1)\cdot\epsilon_0d(1+\epsilon_0)^{j-1},y\cdot\epsilon_0d(1+\epsilon_0)^{j-1}\big]\) for some _y_. Let \(B_j\in W_B\) be the window of length \(d(1+\epsilon_0)^{j-1}\) with starting index in \(y\cdot\epsilon_0d(1+\epsilon_0)^{j-1}\). Notice that _B<sub>i</sub>_ ends at

\(y\cdot\epsilon_0d(1+\epsilon_0)^{j-1}+d(1+\epsilon_0)^{j-1}=y\cdot\epsilon_0d(1+\epsilon_0)^{j-1}+d(1+\epsilon_0)^j-\epsilon_0d(1+\epsilon_0)^{j-1}\)<br>
\(=(y-1)\cdot\epsilon_0d(1+\epsilon_0)^{j-1}+d(1+\epsilon_0)^j,\)

which is a lower bound on \(\widetilde{B}_j\)’s end index, hence indeed \(B_j\subseteq\widetilde{B}_j\). Finally, notice that

\(|\widetilde{B}_j\backslash B_j|\le d(1+\epsilon_0)^{i+1}-d(1+\epsilon_0)^{i-1}\)<br>
\(\le d(1+\epsilon_0)^{i-1}3\epsilon_0\)<br>
\(<3\epsilon_0|\widetilde{B}_j|.\) (11)

Therefore, in total the number of characters we lose by restricting to windows _B<sub>j</sub>_ is bounded by \(3\epsilon_0n\):

\(\sum_{i\in Z}|\mathsf{lcs}(A_j,B_j)|\ge\sum_{j\in Z}(|\mathsf{lcs}(A_j,\widetilde{B}_j)|-3\epsilon_0|\widetilde{B}_j|)\text{(Eq. (11))}\)<br>
\(\ge\sum_{j\in Z}|\mathsf{lcs}(A_j,\widetilde{B}_j)|-3\epsilon_0n\text{(}\widetilde{B}_j\text{’s are disjoint)}\)<br>
\(\ge|\mathsf{lcs}(A,B)|-8\epsilon_0n\text{(Eq. (10))}.\)

## 4.2 Window construction for arbitrary \(\lambda\) (Step 0 of Theorem 2.1)

Our construction for this case is similar to Section 4.1, with the exception that when we’re OK with losing constant factors in approximation, we can afford less shifts and less layers, which will improve the running time.

Let

\(f:=\mathrm{log}(1/\epsilon_0).\)

For each \(i\in\{0,\cdots,f\}\), we define \(d_i=d\cdot 2^i\), and _t<sub>i</sub>=n/d<sub>i</sub>_. For each _i_, let \(W_B^i\) denote the set of all the windows in this layer. We consider window set \(W_B^i\), in _i_-th layer, all the window have sizes that are multiples of _d_, and in the range (_d<sub>i</sub>/_2_,d<sub>i</sub>_]. The shift for each layer will be _d<sub>i</sub>_.

