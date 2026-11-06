\(\rho\leftarrow\frac{1}{2}+\frac{4pq+5(p-q)}{1-p-q};\text{//}\rho\text{is a shrinking rate in}\left(\frac{8pq+10(p-q)}{1-p-q},1\right)\text{(see Section 5.1)}\)<br>
\(S_{\lfloor w_S\rfloor}\leftarrow S;\)<br>
\(w\leftarrow\lfloor w_S\rfloor;\)<br>
while \(w\ge 1\) do<br>
   \(B_1,\dots,B_{\lceil\frac{m}{w}\rceil}\leftarrow\text{Partition}S_w\text{into}\lceil\frac{m}{w}\rceil\) baskets of consecutive elements such that each of the first<br>
   \(\lceil\frac{m}{w}\rceil-1\) baskets contains exactly w elements and the last basket contains at most w elements;<br>
   for \(i=1,\dots,\lceil\frac{m}{w}\rceil\) do<br>
   \(B\leftarrow\bigcup_{j=max\{i+3,\lceil m/w\rceil\}}^{min\{i+3,\lceil m/w\rceil\}}B_j\);<br>
   foreach \(x\in B\) do \(score(x)\leftarrow|\{y\in B\backslash x|y<x\}|\);<br>
   \(A\leftarrow\text{Sort}4\) the elements in B in non-decreasing order of \(score(\cdot)\);<br>
   foreach \(x\in B_i\) do \(\tau_w(x)\leftarrow max\{0,i-4\}\cdot w+pos(x,A)\);<br>
   \(S_{\lfloor\rho w\rfloor}\leftarrow\text{Sort}4\) the elements in S<sub>w</sub> in non-decreasing order of \(\tau_w(\cdot)\);<br>
   \(w\leftarrow\lfloor\rho w\rfloor\);<br>
return S<sub>0</sub>;

<tbc>probability, and the running time of the algorithm as functions of \(\rho\) throughout our analysis. Notice that the above interval is non-empty as long as \(p<\frac{9q+1}{8q+11}\). For q=0, the condition becomes \(p<\frac{1}{11}\), while p=q yields \(p<\frac{1}{4}\).

The pseudocode of our algorithm is shown in Algorithm 2. The algorithm iteratively "sorts" the sequence of elements while maintaining a (tentative) upper bound w, called the window size, to their dislocation. The algorithm terminates in \(O(log_{1/\rho} w_S)\) rounds, where the i-th round considers a window size w of roughly \(\rho^{i-1}w_S\) and permutes an associated sequence S<sub>w</sub> to obtain a new sequence \(S_{\lfloor\rho w\rfloor}\) with a (tentative) upper bound on the maximum dislocation of \(\rho w\). The initial sequence \(S_{\lfloor w_S\rfloor}\) is exactly S, while the output of the algorithm is the sequence S<sub>0</sub>.

To compute \(S_{\lfloor\rho w\rfloor}\), the algorithm uses S<sub>w</sub> to find an estimate \(\tau_w(x)\) of the true rank of each element \(x\in S\), and then sorts the elements in non-decreasing order of \(\tau_w(\cdot)\). The quantity \(\tau_w(x)\) is obtained as follows: we partition S<sub>w</sub> into consecutive baskets B<sub>1</sub>,B<sub>2</sub>,... of w elements (except possibly for the last basket when m is not a multiple of w) and we restrict our attention to the union B of the elements that are "at most 3 baskets away" from the baskets B<sub>i</sub> containing x. Note that if the dislocation of S<sub>w</sub> is at most w, then all elements not in B are in the correct relative order w.r.t. x and rank(x,S)=max{(i-4)w,0}+rank(x,B), so we are left with the problem of estimating rank(x,B). We say that \(x\in B\) has a score score(x) equal to the number of elements \(y\in B\backslash\{x\}\) with y\<x, we sort B according to the scores of the elements to obtain a sequence A, and we use the position of x in A as a proxy for rank(x,B), i.e., we define \(\tau_w(x)=max\{0,i-4\}\cdot w+pos(x,A)\).

Clearly, we cannot hope for the tentative upper bound w on the dislocation of S<sub>w</sub> to hold with high probability until w=0. However, as we will show in Section 5.2, \(disl(S_w)\le w\) holds with high probability for \(w=\Omega(logm)\), and the combined effect of all subsequent rounds only affects the dislocation by at most a multiplicative constant.<br>
We start by analyzing the running time of BasketSort.

Lemma 5.1. _The running time of_ BasketSort _is_ \(O(\frac{m\cdot w_S}{1-\rho})\).

4We assume that the used sorting algorithm is stable.

**Algorithm 2:** BasketSort(S,w<sub>S</sub>)

