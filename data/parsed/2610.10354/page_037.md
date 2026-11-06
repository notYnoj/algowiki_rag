We will think of \(X\times Y\) as a grid in the plane \[0_,n_\]<sup>2</sup>. The multiples of \(\Delta_X\) (i.e., the vertical axes) are called _anchors_, and we say that an integer is _anchored_ at the largest anchor smaller than that index. For an anchor \(x\in X\), we define

\(L_A[x]=\mathrm{min}_{x\le i<x+\Delta_X}A[i],L_B[x]=\mathrm{min}_{x\le j<x+\Delta_X}B[j],\)<br>
\(U_A[x]=\mathrm{max}_{x\le i<x+\Delta_X}A[i],U_B[x]=\mathrm{max}_{x\le j<x+\Delta_X}B[j];\)

i.e., the smallest and largest entries in the respective segments of _A_ and _B_ anchored at _x_. We call an anchor _xA-light_ if \(U_A[x]-L_A[x]<\Delta_Y\) and _A-heavy_ if \(U_A[x]-L_A[x]\ge\Delta_Y\). Similarly define _B-light_ and _B-heavy_. We say that an index _k_ is _heavy_ if it has a witness, _A_\[_i_\]+_B_\[_j_\]=(_A∗B_)\[_k_\], where _i_ is anchored at an _A_-heavy anchor or _j_ is anchored at a _B_-heavy anchor. Otherwise, we call _k light_. We will now deal with the heavy and light indices _k_ individually.

## Heavy Anchors.

We deal with the heavy indices by brute-force: For all \(i\in[0,n]\) anchored at an _A_-heavy anchor, and all \(j\in[0,n]\), update \(C[i+j]\leftarrow\mathrm{min}\{C[i+j],A[i]+B[j]\}\). Analogously, enumerate all \(j\in[0,n]\) anchored at a _B_-heavy anchor and all \(i\in[0,n]\) to perform the same update. This clearly correctly assigns _C_\[_k_\] for all heavy _k_.

To bound the running time of this step, recall that _A_ and _B_ (and thus also _A_<sub>1</sub> and _B_<sub>1</sub>) are monotone. Each _A_-heavy anchor witnesses a jump from _A_\[_x_\] to \(A[x+\Delta_X]\) of at least \(\Delta_Y\). Thus, there can be at most \(O(n/\Delta_Y)A\)-heavy anchors. But each anchor covers only \(\Delta_X\) indices, and therefore the running time is \(O(n/\Delta_Y\cdot\Delta_X\cdot n)=O(n^{2-\delta})\).

## Light Anchors.

To deal with the light indices we rely on the BSG theorem. Let

\(\mathcal{A}=\{(x,L_A[x]):x\in X\text{is}A\text{-light}\},\)<br>
\(\mathcal{B}=\{(y,L_B[y]):y\in X\text{is}B\text{-light}\}.\)

Moreover, compute the following sequence by brute-force,<tbc>

\(L_C[z]=\mathrm{min}\{L_A[x]+L_B[z-x]:x\in X\text{is}A\text{-light and}z-x\in X\text{is}B\text{-light}\}(z\in 2X),\)

<tbc>and let

\(\mathcal{C}=\{(z,L_C[z]+h):z\in 2X,0\le h<2\Delta_Y\}.\)

We apply the BSG Covering Theorem (Theorem 5.7) on A,B,C with parameters \(t=4\Delta_Y\), \(\alpha=n^{-\delta}\) and size bound |_X_|, yielding subsets \(\mathcal{A}_1,\dots,\mathcal{A}_m\subseteq\mathcal{A}\) and \(\mathcal{B}_1,\dots,\mathcal{B}_m\subseteq\mathcal{B}\) and a remainder set \(\mathcal{R}\subseteq\mathcal{A}\times\mathcal{B}\). We enumerate all remainder pairs \(((x,L_A[x]),(y,L_B[y]))\in\mathcal{R}\). For each such pair, list all indices _i_ anchored at _x_, and all indices _j_ anchored at _y_, and update \(C[i+j]\leftarrow\mathrm{min}\{C[i+j],A[i]+B[j]\}\).

Then enumerate all pairs \(\mathcal{A}_\ell,\mathcal{B}_\ell\) for \(1\le\ell\le m\). Let \(X_\ell\) be the subset of anchors _x_ appearing in \(\mathcal{A}_\ell\), and similarly let \(Y_\ell\) be the subset of anchors _y_ appearing in \(\mathcal{B}_\ell\). Repeat the following steps 100log_n_ times: Let \(\hat{p}=\Theta(n\alpha^{-5}t^3\Delta_Y\mathrm{log}u)\) (for a sufficiently large constant), and let _p_ be a random<tbc>

