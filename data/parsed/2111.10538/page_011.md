an array \(A=\langle 1,2,\dots,n\rangle\) which is strictly increasing. Based on _A_, we construct two inputs \(A'\) and \(A''\) in the following way:

• \(A'\) is exactly equal to _A_ except that a _p_ fraction of the elements in \(A'\) are replaced by 0.<tbc>

• \(A''\) is exactly equal to _A_ except that every block of length \(\sqrt{n}\) is reversed in \(A''\). In other words, \(A''=\langle\sqrt{n},\sqrt{n}-1,\sqrt{n}-2,\dots,1,2\sqrt{n},2\sqrt{n}-1,\dots,\sqrt{n}+1,\dots,n,n-1,n-2,\dots,n-\sqrt{n}+1\rangle\).

We subsample the two arrays \(A'\) and \(A''\) with a rate of \(1/\sqrt{n}\) to obtain two smaller arrays \(B'\) and \(B''\) of size roughly \(O(\sqrt{n})\). It is easy to prove that \(\text{lis}(B')=\Omega(\sqrt{n})\) and \(\text{lis}(B'')=\Omega(\sqrt{n})\), yet \(\text{lis}(A')=\Omega(n)\) but \(\text{lis}(A'')=O(\sqrt{n})\). By setting _p_=1_/e_<sup>11</sup> we can also make sure that \(\text{lis}(B')\) and \(\text{lis}(B'')\) are within a small multiplicative range even though the gap between \(\text{lis}(A')\) and \(\text{lis}(A'')\) is substantial.

The above observation shows that the problem is very elusive when random sampling is involved. We bring a remedy to this issue in the following. Divide the input array into \(\sqrt{n}\) subarrays of size \(\sqrt{n}\). We denote the subarrays by \(\mathsf{sa}_1,\mathsf{sa}_2,\dots,\mathsf{sa}_{\sqrt{n}}\) and fix an optimal solution opt for the longest increasing subsequence of _A_. Define sm(sa_<sub>i</sub>_) to be the smallest number in sa_<sub>i</sub>_ that contributes to opt and lg(sa_<sub>i</sub>_) to be the largest number in sa_<sub>i</sub>_ that contributes to opt. Moreover, define \(\text{lis}^{[\ell,r]}\) to be the longest increasing subsequence of an array subject to the elements whose values lie within the interval \([\ell,r]\). This immediately implies<tbc>

\(\text{lis}(A)=\sum_{i=1}^{\sqrt{n}}\text{lis}^{[\mathsf{sm}(\mathsf{sa}_i),\text{lg}(\mathsf{sa}_i)]}(\mathsf{sa}_i).\)

<tbc>Another observation that we make here is that since we assume \(||\text{lis}(A)||\ge\lambda\) and the size of each subarray is bounded by \(\sqrt{n}\), then we have

\(\frac{\text{lis}(A)}{max_i\text{lis}^{[\mathsf{sm}(\mathsf{sa}_i),\text{lg}(\mathsf{sa}_i)]}(\mathsf{sa}_i)}\ge\sqrt{n}\lambda\)

which means that in order to approximate lis(_A_) it suffices to compute lis<sup>\[sm(sa_<sub>i</sub>),_lg(sa_<sub>i</sub>_)\]</sup>(sa_<sub>i</sub>_) for \(\widetilde{O}(1/\lambda)\) many randomly sampled subarrays. This is quite helpful since this shows that we only need to sample \(\widetilde{O}(1/\lambda)\) many subarrays and solve the problem for them. However, we do not know the values of sm(sa_<sub>i</sub>_) and lg(sa_<sub>i</sub>_) in advance. Therefore, the main challenge is to predict the values of sm(sa_<sub>i</sub>_) and lg(sa_<sub>i</sub>_) before we sample the subarrays.

Indeed, one needs to read the entire array to correctly compute sm(sa_<sub>i</sub>_) and lg(sa_<sub>i</sub>_) for each of the subarrays. However, we devise a method to approximately guess these values without losing too much in the size of the solution. Roughly speaking, we show that if we sample \(k=O(1/(\lambda\epsilon))\) different elements from a subarray sa_<sub>i</sub>_ for some constant \(\epsilon\) and denote them by _a_<sub>_j_<sub>1</sub></sub>_,a_<sub>_j_<sub>2</sub></sub>_,...,a<sub>j<sub>k</sub></sub>_, then for at least one pair \((\alpha,\beta)\), \([a_{j_\alpha},a_{j_\beta}]\) is approximately close to \[sm(sa_<sub>i</sub>),_lg(sa_<sub>i</sub>_)\] up to a \((1-\epsilon)\) factor.

The above argument provides \(O((1/(\lambda\epsilon))^2)\) candidate domain intervals for each sa_<sub>i</sub>_. This does not provide a solution since we do not know which candidate domain interval approximates \[sm(sa_<sub>i</sub>),_lg(sa_<sub>i</sub>_)\] for each sa_<sub>i</sub>_. Of course, if we were to randomly choose one candidate interval for every subarray, we would make a correct guess for at least \(O(\sqrt{n}(\lambda\epsilon)^2)\) subarrays which provides an approximation guarantee of \(\Omega(\lambda^2)\) for our algorithm. However, our assignments have to be mono tone too. More precisely, let \([\widetilde{\mathsf{sm}}(\mathsf{sa}_i),\widetilde{\text{lg}}(\mathsf{sa}_i)]\) be the guesses that our algorithm makes, then we should have<tbc>

<sup>11</sup>\(e\simeq 2.7182\).

