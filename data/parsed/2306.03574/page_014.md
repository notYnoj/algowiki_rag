**Lemma 11.** _\[25, Corollary 6.3.4\] For_ \(N\times N\) _Hermitian matrices_ **H** _and_ **E**_, if_ \(\hat{\lambda}\) _is an eigenvalue of_ **H**+**E**_, then there exists an eigenvalue_ \(\lambda\) _of_ **H** _such that_

\(|\lambda-\hat{\lambda}|\le||\mathbf{E}||_2.\)

The following lemma indicates that the spectrum of the preconditioned matrix \(\mathcal{P}_\alpha^{-1}\mathcal{YT}\) is located in a disjoint interval excluding the origin.

**Lemma 12.** _For_ \(\alpha\in(0,1/2]\)_, we have_<tbc>

\(\sigma(\mathcal{P}_\alpha^{-1}\mathcal{YT})\subset[-1-\alpha c_1,-1+\alpha c_1]\cup[1-\alpha c_1,1+\alpha c_1],\)

<tbc>_where c_<sub>1</sub>_\>_0 _independent of_ \(\alpha\) _is given as follows_

\(c_1=c_0\left(\sqrt{||L||_2^2+1}+1\right),\)

_with c_<sub>0</sub> _given in Lemma 10._

**Proof:** By matrix similarity and (2.1), we have \(\sigma(\mathcal{P}_\alpha^{-1}\mathcal{YT})=\sigma(\mathcal{P}_\alpha^{-1/2}\mathcal{YT}\mathcal{P}_\alpha^{-1/2})=\sigma(\mathcal{Q}_\alpha-\mathcal{E}_\alpha)\). Since both \(\mathcal{Q}_\alpha\) and \(-\mathcal{E}_\alpha\) are Hermitian, Lemma 11 is applicable. In other words, for \(\hat{\lambda}\in\sigma(\mathcal{Q}_\alpha-\mathcal{E}_\alpha)\), there exists \(\lambda\in\sigma(\mathcal{Q}_\alpha)\) such that \(|\hat{\lambda}-\lambda|\le||\mathcal{E}_\alpha||_2\). By Lemma 6, we know that either \(\lambda=1\) or \(\lambda=-1\). That means either \(|\hat{\lambda}-1|\le||\mathcal{E}_\alpha||_2\) or \(|\hat{\lambda}+1|\le||\mathcal{E}_\alpha||_2\). Thus, we have

\(\sigma(\mathcal{P}_\alpha^{-1}\mathcal{YT})=\sigma(\mathcal{Q}_\alpha-\mathcal{E}_\alpha)\) (2.3)

\(\subset[-1-||\mathcal{E}_\alpha||_2,-1+||\mathcal{E}_\alpha||_2]\cup[1-||\mathcal{E}_\alpha||_2,1+||\mathcal{E}_\alpha||_2].\)

Hence, it suffices to show that \(||\mathcal{E}_\alpha||_2\le c_1\alpha\). By (2.2) and Lemma 10, we have<tbc>

\(||\mathcal{E}_\alpha||_2\le||\mathcal{C}_\alpha^{-1/2}||_2^2||\mathcal{R}_\alpha||_2\le c_0||\mathcal{R}_\alpha||_2.\)

<tbc>Notice that<tbc>

\(\mathcal{R}_\alpha=\alpha\mathcal{R}_1,\mathcal{R}_1=\left[\begin{array}{ c c }
L & -2I_m \\
 & L
\end{array}\right].\)

<tbc>Therefore, it is straightforward to check that<tbc>

\(||\mathcal{R}_\alpha||_2=\alpha||\mathcal{R}_1||_2=\alpha\lambda_{max}\left(\left[\begin{array}{ c c }
L & -2I_m \\
L & 
\end{array}\right]\left[\begin{array}{ c c }
L &  \\
-2I_m & L
\end{array}\right]\right)=\alpha\left(\sqrt{||L||_2^2+1}+1\right).\)

