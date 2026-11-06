of the middle arc (_u<sub>i</sub>,v<sub>j</sub>_). We have:

\(\frac{1}{w_i+2W}\ge\frac{1}{\frac{W}{m}+2W}=\frac{m}{W(1+2m)}=\frac{4mn^2}{2m+1}.\)

Because we assume \(n\ge 6\) and \(m\ge 2\), we have \(n^2\ge 36\) and \(\frac{m}{2m+1}\ge\frac{2}{5}\). Therefore \(\frac{1}{w_i+2W}\ge 4\times\frac{2}{5}\times 36>2\). Since the delay of this single arc strictly exceeds 2, we have \(d_{s\rightarrow u_i\rightarrow v_j\rightarrow t}>2=b_2\), ruling out this path for commodity _k_<sub>2</sub>.

Similarly, the minimum delay through a path \(s\rightarrow u_i\rightarrow v_j\rightarrow v_j^1\rightarrow\cdots\rightarrow v_j^N\rightarrow t\) is strictly greater than 2, since it contains the arc (_u<sub>i</sub>,v<sub>j</sub>_), whose zero-load delay we just showed exceeds 2. Notice that the minimum delay through the chain of arcs \(v_j\rightarrow v_j^1\rightarrow\cdots\rightarrow v_j^N\) exceeds \(N\frac{1}{W\frac{(n+1)(n-3)}{n}+1}=\frac{1}{W}\frac{1}{\frac{n^2-2n-3}{4n^3}+1}>\frac{1}{W}\frac{1}{2}\) and therefore the delay of a path \(s\rightarrow u_i\rightarrow v_j\rightarrow v_j^1\rightarrow\cdots\rightarrow v_j^N\rightarrow t\) strictly exceeds \(d_L=2+\frac{1}{2W}\), also preventing _k_<sub>2</sub> from using it.

Finally, for \(j\in J\), paths \(s\rightarrow v_j\rightarrow v_j^1\rightarrow\cdots\rightarrow v_j^N\rightarrow t\) have a minimum delay:

\(d_{s\rightarrow v_j\rightarrow v_j^1\rightarrow\cdots\rightarrow v_j^N\rightarrow t}=\frac{1}{2}+(N-1)\frac{1}{W\frac{(n+1)(n-3)}{n}+1}+\frac{1}{W\frac{(n+1)(n-3)}{n}+2}.\)

Because \(n\ge 6\) and \(W=\frac{1}{4n^2}\), the capacity \(W\frac{(n+1)(n-3)}{n}+1\) is strictly less than 2. As a result, the delay of each of the _N_-1 internal arcs strictly exceeds \(\frac{1}{2}\). Since \(N=4n^2\ge 144\), the total delay is vastly greater than 2. Therefore, commodity _k_<sub>2</sub> cannot use this path.

## A.2 Proof of Lemma 2.2

_Proof._ From Lemma 2.1, the set of feasible paths for _k_<sub>2</sub> contains _n_+2_m_ paths. Let us suppose that one of these paths is not used by _k_<sub>2</sub> (i.e., it carries a load of zero). Because the total size of _k_<sub>2</sub> is _b_<sub>2</sub>=_n_+2_m_, the average load on the remaining paths must be strictly greater than \(1+\delta\),<tbc>

