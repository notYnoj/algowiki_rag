## 4.2 Constant Slice Rank Polygon Triangulation is APSP-hard

In fact, the we can modify the reduction in Theorem 4.1 such that it preserved slice rank as well.

**Theorem 4.3.** (2D LWS \(\rightarrow\) 2D LWS<sup>PT</sup>_, slice rank version) There exists an O(nd_) _time reduction from_ 2D LWS_<sub>n</sub> with slice rank d, w_<sub>1</sub>=_w_<sub>2</sub>=_w, to_ 2D LWS\(_{2n}^\text{PT}\) _with slice rank d._

_Proof._ Given an 2D LWS instance with \(n\times n\) tensor _w_ with rank _d_, by the proof of Theorem 4.1, we know it suffices to construct a \(2n\times 2n\) tensor \(w'\) such that

• \(w'[i,j,k]=0\) when \((i,j)\notin[1,n]\times[n+1,2n]\).<tbc>

• When \((i,j)\in[n]\times[n+1,2n]\), \(w'[i,j,k]=w[i,j-n,k]\) for all \(k\in[n]\) and \(w'[i,j,k]=w[i,j-n,k-n]\) for all \(k\in[n+1,2n]\).

Now for each slice in _w_, there are three possibilities. For each case we convert the slice into a new slice with dimension \(2n\times 2n\times 2n\) such that \(w'\) is the sum of them.

• \(f(i,k)\cdot g(j)\): let<tbc>

<tbc>\(f'(i,k)=\left\{\begin{array}{ c }
f(i-n,k)\text{if}i\in[1,n],k\in[1,n] \\
f(i-n,k-n)\text{if}i\in[1,n],k\in[n+1,2n] \\
0\text{otherwise}
\end{array}\right.,g'(j)=\left\{\begin{array}{ c }
g(j)\text{if}j\in[n+1,2n] \\
0\text{otherwise}.
\end{array}\right.\)<tbc>

<tbc>As a result, \(f'(i,k)\cdot g'(j)=f(i,k)\cdot g(j-n)\) when \(i\in[1,n],j\in[n+1,2n]\) and \(k\in[n]\), \(f'(i,k)\cdot g'(j)=f(i,k-n)\cdot g(j-n)\) when \(i,j\in[n+1,2n]\) and \(k\in[n+1,2n]\), and \(f'(i,k)\cdot g'(j)=0\) if \((i,j)\notin[1,n]\times[n+1,2n]\). Thus it satisfies the conditions above.<tbc>

• \(f(i,j)\cdot g(k)\): let<tbc>

<tbc>\(f'(i,j)=\left\{\begin{array}{ c }
f(i,j-n)\text{if}i\in[1,n],j\in[n+1,2n] \\
0\text{otherwise}
\end{array}\right.,g'(k)=\left\{\begin{array}{ c }
g(k)\text{if}k\in[n] \\
g(k-n)\text{if}k\in[n+1,2n].
\end{array}\right.\)<tbc>

<tbc>As a result, \(f'(i,j)\cdot g'(k)=f(i,j-n)\cdot g(k)\) when \((i,j)\in[1,n]\times[n+1,2n]\) and \(f'(i,j)\cdot g'(k)=0\) otherwise. Again it satisfies the conditions above.<tbc>

• \(f(j,k)\cdot g(i)\): let<tbc>

<tbc>\(f'(j,k)=\left\{\begin{array}{ c }
f(j-n,k)\text{if}j\in[n+1,2n],k\in[n] \\
f(j-n,k-n)\text{if}j\in[n+1,2n],k\in[n+1,2n] \\
0\text{otherwise}.
\end{array}\right.,g'(i)=\left\{\begin{array}{ c }
g(i)\text{if}i\in[n] \\
0\text{otherwise}.
\end{array}\right.\)<tbc>

<tbc>When \((i,j)\in[n]\times[n+1,2n],k\in[n]\), \(f'(j,k)\cdot g'(i)=f(j-n,k)\cdot g(i)\), and when \((i,j)\in[n]\times[n+1,2n],k\in[n+1,2n]\), \(f'(j,k)\cdot g'(i)=f(j-n,k-n)\cdot g(i)\). When \((i,j)\notin[n]\times[n+1,2n]\), \(f'(j,k)\cdot g'(i)=0\). It satisfies the conditions above.

Therefore, the sum of these slices must also satisfy the conditions of \(w'\) imposed in Theorem 4.1, and the reduction takes _O(nd_) time.

**Corollary 4.4.** _Under_ APSP _conjecture, there is no truly sub-cubic algorithm for_ 2D LWS<sup>PT</sup> _with weight function whose slice rank is_ 3 _or above._

_Proof._ When we reduce APSP to 2D LWS in Theorem 3.5, the tensors \(\alpha\) that we use are the same, so Theorem 3.5 immediately gives a reduction from APSP to 2D LWS with _w_<sub>1</sub>=_w_<sub>2</sub>, which further reduces to 2D LWS<sup>PT</sup> (preserving slice rank) by Theorem 4.1.

