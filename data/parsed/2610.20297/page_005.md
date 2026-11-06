**Lemma 3.4** (Candidate Block Witness Verification)**.** _Let K be a block and_ \(p\in[P,2P]\) _be a prime. For every_ \(\varepsilon<\varepsilon^*:=(\mathrm{ln}4)/(5\mathrm{ln}10)=0.1204\dots\) _and every_ \(\kappa>0\) _there is a_ \(\gamma>0\) _such that the following holds._

_If_ \(2BP\le N^\varepsilon\)_, there is an algorithm that decides for every pair_ (_i,j_) _whether K is a candidate block witness with respect to p for_ (_i,j_) _in time_

\(\tilde{O}\left(N^2+NBP^2+N^2P^{1-\gamma} B^{-\gamma}+(BP)^{\kappa-\gamma} N^2\right).\)

_Proof of Lemma 3.4._ Here, we will use the Theorem 1.2, restated below.

**Theorem 1.2** (Theorem 25 of \[AV26\])**.** _For every_ \(\varepsilon<\varepsilon^*:=(\mathrm{ln}4)/(5\mathrm{ln}10)=0.1204\dots\) _and every_ \(\kappa>0\) _there is a_ \(\gamma>0\) _such that the following holds. Given as input matrices_ \(X\in\mathbb{Z}^{N\times D}\) _and_ \(Y\in\mathbb{Z}^{D\times N}\)_, where_ \(2\le D\le N^\varepsilon\)_, whose entries are integers of absolute value at most N_<sup>_O_(1)</sup>_, as well as a set W of at most_ \(N^2/D^\kappa\) _positions of an_ \(N\times N\) _matrix, the entries_ \((XY)[I,J]\), \((I,J)\in W\)_, can be computed deterministically in time_ \(O(N^2\mathrm{log}^2D/D^\gamma)\).

Note that since \(N^2/D^\kappa\) is the output size, we must have \(\gamma\le\kappa\). We begin with the algorithm.

\(\text{\textbf{Verify Candidate Block Witness.}
1. For}r\in\mathbb{Z}_p\text{, let}W_r:=\{(i,j)\text{s.t.}C[i,j]\equiv r\mathrm{mod}p\}\text{.
2. For}r\in\mathbb{Z}_p\text{, construct boolean matrices}X,Y_r\text{with entries}X[i,(k,a)]=\unknown[A[i,k]\equiv a\mathrm{mod}p],Y_r[(k,a),j]=\unknown[B[k,j]\equiv r-a\mathrm{mod}p]\text{.
(}X\text{can be constructed once as it does not depend on}r\text{.)
3. For}r\in Z_p\text{, compute}(XY_r)[(i,j)]\text{for}(i,j)\in W_r\text{.
4. For}r\in\mathbb{Z}_p\text{and}(i,j)\in W_r\text{, return}\unknown[(XY_r)[i,j]>0]\text{.
We begin with correctness. For any pair}(i,j)\in W_r\text{,}(XY_r)[i,j]=\sum_{(k,a)}\unknown[A[i,k]\equiv a\mathrm{mod}p]\unknown[B[k,j]\equiv r-a\mathrm{mod}p]=\sum_kA[i,k]\equiv a\mathrm{mod}p\unknown[A[i,k]+B[k,j]\equiv a+(r-a)\equiv r\equiv C[i,j]\mathrm{mod}p]=\sum_k\unknown[A[i,k]+B[k,j]\equiv C[i,j]\mathrm{mod}p]\text{.
The first equality follows by definition of the matrix product. The second equality follows by}(i,j)\in W_r\text{. The third equality follows by the fact that}A[i,k]\equiv a\mathrm{mod}p\text{for exactly one value of}a\in\mathbb{Z}_p\text{. Thus,}K\text{is a candidate block witness with respect to}p\text{for}(i,j)\in W_r\text{if and only if}(XY_r)[i,j]>0\text{, establishing correctness.
To bound the running time, fix}r\text{and examine the shape of}X\text{and}Y_r\text{. Note that}X\text{has dimension}N\times Bp\text{,}Y_r\text{has dimension}Bp\times N\text{and both can be constructed in linear time. Thus, in order to apply Theorem 1.2, we require}D:=Bp\le 2BP\le N^\varepsilon\text{. Furthermore, if}W_r\ge N^2/D^\kappa\text{, we can partition}W_r\text{into}O(|W_r|D^\kappa/N^2)\text{disjoint subsets of size at most}N^2/D^\kappa\text{. Applying Theorem 1.2 to each disjoint subset, the total time to compute all}(XY_r)[i,j]\text{for all}(i,j)\in W_r\text{over all}r\text{is therefore}\)

We begin with correctness. For any pair \((i,j)\in W_r\),

\((XY_r)[i,j]=\sum_{(k,a)}\unknown[A[i,k]\equiv a\mathrm{mod}p]\unknown[B[k,j]\equiv r-a\mathrm{mod}p]=\sum_k\sum_{A[i,k]\equiv a\mathrm{mod}p}\unknown[A[i,k]+B[k,j]\equiv a+(r-a)\equiv r\equiv C[i,j]\mathrm{mod}p]=\sum_k\unknown[A[i,k]+B[k,j]\equiv C[i,j]\mathrm{mod}p]\text{.}\)

The first equality follows by definition of the matrix product. The second equality follows by \((i,j)\in W_r\). The third equality follows by the fact that \(A[i,k]\equiv a\mathrm{mod}p\) for exactly one value of \(a\in\mathbb{Z}_p\). Thus, _K_ is a candidate block witness with respect to _p_ for \((i,j)\in W_r\) if and only if (_XY<sub>r</sub>_)\[_i,j_\]_\>_0, establishing correctness.

To bound the running time, fix _r_ and examine the shape of _X_ and _Y<sub>r</sub>_. Note that _X_ has dimension \(N\times Bp\), _Y<sub>r</sub>_ has dimension \(Bp\times N\) and both can be constructed in linear time. Thus, in order to apply Theorem 1.2, we require \(D:=Bp\le 2BP\le N^\varepsilon\). Furthermore, if \(W_r\ge N^2/D^\kappa\), we can partition _W<sub>r</sub>_ into \(O(|W_r|D^\kappa/N^2)\) disjoint subsets of size at most \(N^2/D^\kappa\). Applying Theorem 1.2 to each disjoint subset, the total time to compute all (_XY<sub>r</sub>_)\[_i,j_\] for all \((i,j)\in W_r\) over all _r_ is therefore

\(\sum_rO\left(\frac{N^2\mathrm{log}^2D}{D^\gamma}\left(1+\frac{|W_r|D^\kappa}{N^2}\right)\right)=\tilde{O}\left(\frac{N^2P}{D^\gamma}+D^{\kappa-\gamma}\sum_r|W_r|\right)=\tilde{O}\left(\frac{N^2P}{D^\gamma}+D^{\kappa-\gamma} N^2\right).\)

Constructing _X_ requires _O(NBP_) time, while constructing _Y<sub>r</sub>_ over all _r_ requires _O(NBP_<sup>2</sup>) time. Finally, note that the remaining steps requires _O(N_<sup>2</sup>) time.

