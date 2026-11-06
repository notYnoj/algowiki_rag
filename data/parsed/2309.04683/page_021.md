## 4 Polygon Triangulation (2D LWS<sup>PT</sup>)

In this section, we discuss the polygon triangulation problem 2D LWS<sup>PT</sup> and its connections with 2D LWS. It was shown in \[HS02, HS82, HS84, LG21\], that if \(w[i,j,k]=x_i\cdot x_j\cdot x_k\) for all _i,j,k_ with _x<sub>i</sub>,x<sub>j</sub>,x<sub>k</sub>\>_0 for all _i_, then 2D LWS<sup>PT</sup> can be solved in _O(n_<sup>2</sup>) time. We establish several conditional hardness results of 2D LWS<sup>PT</sup> based on SETH and APSP conjecture. Namely, 2D LWS where _w_<sub>1</sub>=_w_<sub>2</sub> can be reduced to 2D LWS<sup>PT</sup> with rank/slice rank unchanged, and thus finding the optimal triangulation for certain weight functions (rank 2<sup>_O_(log<sup>∗</sup>_n_)</sup> or slice rank 3) is hard under SETH.

### 4.1 Low Rank Polygon Triangulation is SETH-hard

**Theorem 4.1.** (2D LWS \(\rightarrow\) 2D LWS<sup>PT</sup>)_. There exists an O(nd_) _time reduction from_ 2D LWS_<sub>n</sub> with rank d, w_<sub>1</sub>=_w_<sub>2</sub>=_w, to_ 2D LWS\(_{2n}^\text{PT}\) _with rank d._

_Proof._ Given an 2D LWS_<sub>n</sub>_ instance _T_ with rank _d_ tensor \(w[i,j,k]=\langle\mu_i,\sigma_j,\tau_k\rangle\) and recurrence relation<tbc>

\(T[i,j]=min\left\{min_{1\le k<j}\left\{T[i,k]+w[i,j,k]\right\},min_{i<k\le n}\left\{T[k,j]+w[i,j,k]\right\}\right\},\)

<tbc>we want to compute _T_\[1_,n_\]. We construct an 2D LWS\(_{2n}^\text{PT}\) instance \(T'\) as follows.

\(\mu'_i=\left\{\begin{array}{ c }
\mu_i\text{if}i\in[1,n] \\
0^d\text{if}i\in[n+1,2n],
\end{array}\right.\sigma'_j=\left\{\begin{array}{ c }
0^d\text{if}j\in[1,n] \\
\sigma_{j-n}\text{if}j\in[n+1,2n],
\end{array}\right.\tau'_k=\left\{\begin{array}{ c }
\tau_k\text{if}k\in[1,n] \\
\tau_{k-n}\text{if}k\in[n+1,2n],
\end{array}\right.\)

and define a \(2n\times 2n\times 2n\) tensor as \(w'[i,j,k]=\langle\mu'_i,\sigma'_j,\tau'_k\rangle\). We make a few observations:

• \(w'[i,j,k]=0\) when \((i,j)\notin[1,n]\times[n+1,2n]\), and thus \(T'[i,j]=0\) for all \((i,j)\notin[1,n]\times[n+1,2n]\).<tbc>

• When \((i,j)\in[n]\times[n+1,2n]\), \(w'[i,j,k]=w[i,j-n,k]\) for all \(k\in[n]\) and \(w'[i,j,k]=w[i,j-n,k-n]\) for all \(k\in[n+1,2n]\).

We now prove that for all \((i,j)\in[n]\times[n+1,2n]\), we have \(T'[i,j]=T[i,j-n]\), which will suffice since when _i_=1_,j_=2_n_, we have \(T'[1,2n]=T[1,n]\).

We proceed by induction. The base case is \(T'[n,n+1]=0\). Now for each \((i,j)\in[1,n]\times[n+1,2n]\), by induction hypothesis we have

\(T'[i,j]=min_{i<k<j}\left\{T'[i,k]+T'[k,j]+w'[i,j,k]\right\}\)<br>
\(=min\left\{min_{i<k\le n}\left\{T'[i,k]+T'[k,j]+w'[i,j,k]\right\},min_{n+1\le k<j}\left\{T'[i,k]+T'[k,j]+w'[i,j,k]\right\}\right\}\)<br>
\(=min\left\{min_{i<k\le n}\left\{T'[k,j]+\langle\mu'_i,\sigma'_j,\tau'_k\rangle\right\},min_{1\le k<j-n}\left\{T'[i,k-n]+\langle\mu'_i,\sigma'_j,\tau'_k\rangle\right\}\right\}\)<br>
\(=T[i,j-n].\)

The time for our reduction is _O(nd_), so the proof is complete.

**Corollary 4.2.** _Under_ SETH_, there is no truly sub-cubic algorithm for_ 2D LWS<sup>PT</sup> _with weight function whose rank is_ 2<sup>_O_(log<sup>∗</sup>_n_)</sup> _or above._

_Proof._ When we reduce 3Min-IP to 2D LWS in Theorem 3.1, the tensors \(w_\ell\) that we use are all the same, so Theorem 3.1 immediately gives a reduction from 3Min-IP to 2D LWS with _w_<sub>1</sub>=_w_<sub>2</sub> (preserving rank), which further reduces to 2D LWS<sup>PT</sup> (preserving rank) by Theorem 4.1.

