## Correctness.

It is clear that if the algorithm terminates then we have satisfied the two claimed properties: By construction _X<sub>i</sub>_ is indeed partitioned into _X_<sub>_i,_1</sub>_,X_<sub>_i,_2</sub>_,..._ and \(X_i^*\), we have that \(X_{i,g}\subseteq S_g+s_{i,g}\), and when the algorithm terminates then also \(|\{(i,j)\in[n]\times[m]:P_{2d/p}(X_i^*,Y_j)\neq\emptyset\}|\le nm/p\) (as \(P_{2d/p}(X_i,Y_j)\subseteq P_{i,j}\)).

It remains to prove that the algorithm terminates after at most _p_<sup>2</sup> iterations. To see this, focus on an arbitrary iteration _g_, let _j_ be the index picked in step 3, and let _i_ be good in this iteration. We claim that the constructed set _X<sub>i,g</sub>_ has size at least _d/p_. Indeed, as \(s_{i,g}\in P_{i,j}\subseteq P_{d/p}(X_i,Y_j)\) we have that

\(|X_{i,g}|=|X_i\cap(s_{i,g}+S_g)|=|X_i\cap(s_{i,g}-Y_j)|=r_{X_i+Y_j}(s_{i,g})\ge\frac{d}{p}.\)

Thus, we reduce the size |_X<sub>i</sub>_| of every good index _i_ by at least _d/p_. In total there are at least _n/p_ such good indices, hence in each step we reduce \(\sum_{i\in[n]}|X_i|\) by at least _nd/p_<sup>2</sup>. Initially we have \(\sum_{i\in[n]}|X_i|\le nd\), and so the claim follows.

## Running Time.

Focus on a single iteration. In step 1 we apply Lemma 4.8 _nm_ times. Each execution takes deterministic time \(d^2/(d/p)\cdot u^{o(1)}=dp\cdot u^{o(1)}\), so step 1 takes time \(nmdp\cdot u^{o(1)}\). Testing the condition in step 2 takes negligible time _O(nm_). In step 3 we spend time proportional to the total set sizes, _O(nmd_). Summing over these contributions and over the at most _p_<sup>2</sup> iterations, the claimed time bound \(nmdp^3\cdot u^{o(1)}\) follows. The randomized time bound follows analogously.

## Proof of Lemma 4.5.

Let (_A,B,C_) denote the given _d_-slice-uniform instance. Note that the statement is symmetric with respect to the sizes _n_<sub>1</sub>_,n_<sub>2</sub>_,n_<sub>3</sub>, hence by rotating and/or transposing the given instance we may assume without loss of generality that the rows of _A_ contain at most _d_ distinct entries each.

## Outer Regularization.

Before we give the core reduction, we run the following simple preprocessing step to ensure that all entries in _A_ appear roughly equally often in their columns, and similarly for _B_. We partition _A_ into \(L=\lceil logn_2\rceil\) matrices _A_<sub>0</sub>_,...,A<sub>L</sub>_ where in the matrix \(A_\ell\) we include all entries that appear at least \(2^\ell\) and at most \(2^{\ell+1}\) times in their respective _row_. Similarly partition _B_ into _B_<sub>0</sub>_,...,B<sub>L</sub>_ according to the frequencies per _column_. It remains to deal with all pairs of instances \((A_\ell,B_{\ell^\prime},C)\) (for \(\ell,\ell'\in[L]\)).

For the rest of the proof, fix one such instance, and let us write \(A=A_\ell\) and \(B=B_{\ell^\prime}\) for simplicity of notation. Let \(d_A=min\{d,n_2/2^\ell\}\) and \(d_B=n_2/2^{\ell^\prime}\), and verify that there are at most _d<sub>A</sub>_ distinct entries per row in _A_, and at most _d<sub>B</sub>_ distinct entries per column in _B_. Let \(d'=max\{d_A,d_B\}\).

Finally, we argue that we may assume that \(d_B\le d_A\cdot t\) in the following. Indeed, if instead \(d_B\ge d_A\cdot t\) then we can solve the instance by brute-force as follows. Enumerate all pairs \((i,j)\in[n_1]\times[n_3]\), enumerate the at most _d<sub>A</sub>_ entries _x_ in the _i_-th row of _A_, and enumerate all \(k\in[n_2]\) with _B_\[_k,j_\]=_C_\[_i,j_\]-_x_. We insert all exact triangles (_i,k,j_) enumerated in this step into T .

