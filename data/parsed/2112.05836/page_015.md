\(\delta_\mathrm{max}\) of some string in this set. So adding these strings to _S_ gives that _S_ now has size at most \(3n\tau/\delta_\mathrm{max}\) and has the desired properties.

For an efficient implementation of this procedure, we can compute the optimal LZ77 factorization in _O_(|_X_|) time \[RPE81\]. Given the LZ77 factorization, we decompose _X_ into \(X_1\circ X_2\circ X_3\) as before, and recursively compute an array _A_ for indices in \([1..|X_1|-\tau+1]\) and set _B_ with the following property: the length \(\tau\) substrings starting at indices _i_ and _A_\[_i_\] are within edit distance \(\delta_\mathrm{max}\), and _A_ has at most \(3(n-1)\tau/\delta_\mathrm{max}\) distinct values, which are exactly the values in _B_.

Since the LZ77 factorization gives us the position of _X_<sub>2</sub> in _X_<sub>1</sub>, we can fill in _A_ for the "good" indices in _X_<sub>2</sub> in time linear in the number of good indices. We can also fill in the values of _A_ for the bad indices, in time linear in the number of bad indices, and add these values to _B_. Overall, the algorithm takes linear time to compute _A,B_. _A_ now serves as the desired efficient data structure, and _B_ as our implicit representation of _S_.

There are _O_(log_N_) values of _d_ and \(\tilde{O}(\mathrm{log}N/\epsilon)\) values of \(\Delta\), so we can do Steps 1 and 2 in time \(\tilde{O}(N/\epsilon)\) time. We also show that Step 3 can be performed efficiently:

**Lemma 4.7.** _Given strings X_<sub>1</sub>_,X_<sub>2</sub>_,...X<sub>k</sub>, there exists a data structure that can be computed in_ \(O(\sum_i|X_i|)\) _time that can answer queries of the following form in O(d<sup>k</sup>_) _time: Given indices s_<sub>1</sub>_,s_<sub>2</sub>_,...,s<sub>k</sub> and e_<sub>1</sub>_,e_<sub>2</sub>_,...,e<sub>k</sub>, if_ \(\delta_E(X_1[s_1..e_1],X_2[s_2..e_2],\dots,X_k[s_k..e_k])\le d\)_, output_ \(\delta_E(X_1[s_1..e_1],X_2[s_2..e_2],\dots,X_k[s_k..e_k])\)_, otherwise output_ \(\infty\).

_Proof._ Given _X_<sub>1</sub>_,X_<sub>2</sub>_,...X<sub>k</sub>_, let `Slide`<sub>_d_<sub>2</sub>_,d_<sub>3</sub>_,...,d<sub>k</sub>_</sub>(_j_)=max{_q:X_<sub>1</sub>\[_j..q_\]=_X_<sub>2</sub>\[_j+d_<sub>2</sub>_..q+d_<sub>2</sub>\]=_X_<sub>3</sub>\[_j+d_<sub>3</sub>\(..q+d_3]=\cdots=X_k[j+d_k..q+d_k]\}}. We can rewrite `Slide`<sub>_d_<sub>2</sub>_,d_<sub>3</sub>_,...,d<sub>k</sub>_</sub>(_j_) as \(\mathrm{min}_{i\in\{2,3,\dots,k\}}\mathrm{max}\{q:X_1[j..j+q]=X_i[j+d_i..q+d_i]\}\). Section 2.3 of \[LMS98\] shows that we can compute max{_q:X_<sub>1</sub>\[_j..j+q_\]=_X<sub>i</sub>_\[_j+d<sub>i</sub>;q+d<sub>i</sub>_\]} for any _i,j,d<sub>i</sub>_ in _O_(1) time after _O_(|_X_<sub>1</sub>|+|_X<sub>i</sub>_|) preprocessing time. So we can compute `Slide`<sub>_d_<sub>2</sub>_,d_<sub>3</sub>_,...,d<sub>k</sub>_</sub>(_i_) in _O_(1) time after \(O(\sum_i|X_i|)\) preprocessing time (recall that _k=O_(1)).

Let _L<sup>h</sup>(d_<sub>2</sub>_,d_<sub>3</sub>_,...d<sub>k</sub>_) be the largest value of _j_ such that \(\delta_E(X_1[1..j],X_2[1..j+d_2],X_3[1..j+d_3],\dots,X_k[1..j+d_k])\le h\). We have the following recurrence relation:

\(L^h(d_2,d_3\dots,d_k)=\mathtt{Slide}\left(\mathrm{max}\left\{\begin{array}{ c }
L^{h-1}(d_2+1,d_3+1\dots,d_k+1) \\
\mathrm{max}_iL^{h-1}(d_2,d_3,\dots,d_i-1,\dots,d_k) \\
\mathrm{max}_{e\in\{0,1\}^k}L^{h-w}(d_2-e_2+e_1,d_3-e_2+e_1,\dots,d_k-e_k+e_1) \\
\text{for}w=\mathrm{min}_{i:e_i=1}|\{j\neq i:X_i[x_i]\neq X_j[x_j]\vee e_j=0\}|
\end{array}\right\}\right)\)

The first case considers deleting from _X_<sub>1</sub>, the second case considers deleting a character from any of _X_<sub>2</sub>_,X_<sub>3</sub>_,...X<sub>k</sub>_, and the third case considers inserting characters into some subset of the strings (for which _e<sub>i</sub>_=0), and then matching the inserted characters with a character in the remaining strings (for which _e<sub>i</sub>_=1), such that we use at most _w_ insertions or substitutions.

Each \(L^h(\cdot)\) only depends on _O_(1) other values, and so we can compute each value in _O_(1) time. In turn, we can compute the values _L<sup>h</sup>(d_<sub>2</sub>_,d_<sub>3</sub>_,...d<sub>k</sub>_) for all \(0\le h\le d,0\le d_2+d_3+\cdots+d_k\le d\) in _O(d<sup>k</sup>_) time. Our output for the edit distance is the smallest _h_ such that \(L^h(|X_2|-|X_1|,|X_3|-|X_1|,\dots,|X_k|-|X_1|)\ge|X_1|\), or \(\infty\) if \(L^d(|X_2|-|X_1|,|X_3|-|X_1|,\dots,|X_k|-|X_1|)<|X_1|\).

The total number of strings in any \(\tilde{\mathcal{W}}_{i,d}\) is \(\sum_{\Delta\in\mathcal{D}}O(n(\tau+\Delta)/\epsilon d)=O(n\tau/\epsilon^3d)\). In turn, combined with Lemma 4.7, the total time needed to compute \(\tilde{\delta}_E\) for all _k_-tuples in \(\tilde{\mathcal{W}}_{1,d}\times\tilde{\mathcal{W}}_{2,d}\times\cdots\times\tilde{\mathcal{W}}_{k,d}\) is \(O(n^k\tau^k/\epsilon^{3k})\). There are _O_(log_N_) choices of _d_, so in total this step takes time \(\tilde{O}(n^k\tau^k/\epsilon^{3k})\).

For Step 4, it takes _O_(1) time to process the first case in the recurrence relation. For the second and third case, there are _O_(log_N_) values of _d_, \(O(\mathrm{log}N/\epsilon)\) values of \(\Delta\), and for each \(i,x_i,\Delta\) there is 1 window \(W_{i,\Delta,p}\) such that \(\tilde{e}(W_i)=x_i\). Lemma 4.7 gives an _O_(1)-time method to determine if \(W_1=W_2=\cdots=W_k\) in the second case, and we have precomputed all the necessary values in the third case. So, the time to compute each \(c(x_1,x_2,\dots x_k)\) is \(O((\mathrm{log}^2N/\epsilon)^k)\).

The number of tuples _x_<sub>1</sub>_,x_<sub>2</sub>_,...x<sub>k</sub>_ such that \(\sum_{i\neq 1}|x_i-x_1|\le D\) is _O(ND_<sup>_k_-1</sup>). Of these, fraction \(O(\frac{1}{\lceil\epsilon D\tau/N\rceil^{k-1}\tau})\) satisfy that _x_<sub>1</sub> is a multiple of \(\tau\) and _x_<sub>2</sub>_...x<sub>k</sub>_ are multiples of \(\lceil\epsilon D\tau/N\rceil\). So the number of entries we need to compute is \(O(N^k/\epsilon^k\tau^k)\), and the total time to compute all these entries is \(\tilde{O}(N^k/\epsilon^{2k}\tau^k)\).

Putting it all together, Steps 3 and 4 dominate the runtime with total runtime \(\tilde{O}(N^k/\epsilon^{2k}\tau^k+n^k\tau^k/\epsilon^{3k})\). Setting \(\tau=(N/n\epsilon)^{1/2}\), we get an overall runtime of \(\tilde{O}(N^{k/2}n^{k/2}\epsilon^{-5k/2})\).

We complete our analysis by showing that the final value computed by _k_-ED-Alg is close to \(\delta_E(X_1,X_2,\dots X_k)\).

