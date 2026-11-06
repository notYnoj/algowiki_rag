in D<sub>1</sub> contains \(\Theta(M)\) elements, including the elements already deleted.) After the split, we make the appropriate changes in the binary search tree of upper bounds in _O_(max{1,log(_N/M_)}) time.<tbc>

BATCHPrepEND(L) Let _L_ denote the size of L. When \(L\le M\), we simply create a new block for L and add it to the beginning of D<sub>0</sub>. Otherwise, we create _O(L/M_) new blocks in the beginning of D<sub>0</sub>, each containing at most \(\lceil M/2\rceil\) elements. We can achieve this by repeatedly taking medians which completes in _O(L_log(_L/M_)) time.<tbc>

Pull() To retrieve the smallest _M_ values from \(\mathcal{D}_0\cup\mathcal{D}_1\), we collect a sufficient prefix of blocks from D<sub>0</sub> and D<sub>1</sub> separately, denoted as \(S'_0\) and \(S'_1\), respectively. That is, in D<sub>0</sub> (D<sub>1</sub>) we start from the first block and stop collecting as long as we have collected all the remaining elements or the number of collected elements in \(S'_0\) (\(S'_1\)) has reached _M_. If \(S'_0\cup S'_1\) contains no more than _M_ elements, it must contain all blocks in \(\mathcal{D}_0\cup\mathcal{D}_1\), so we return all elements in \(S'_0\cup S'_1\) as \(S'\) and set _x_ to the upper bound _B_, and the time needed is \(O(|S'|)\). Otherwise, we want to make \(|S'|=M\), and because the block sizes are kept at most _M_, the collecting process takes _O(M_) time.<tbc>

<tbc>Now we know the smallest _M_ elements must be contained in \(S'_0\cup S'_1\) and can be identified from \(S'_0\cup S'_1\) as \(S'\) in _O(M_) time. Then we delete elements in \(S'\) from D<sub>0</sub> and D<sub>1</sub>, whose running time is amortized to insertion time. Also set returned value _x_ to the smallest remaining value in \(\mathcal{D}_0\cup\mathcal{D}_1\), which can also be found in _O(M_) time.

We now describe our BMSSP algorithm (Algorithm 3) in detail. Recall that the main algorithm calls BMSSP with parameters \(l=\lceil(logn)/t\rceil,S=\{s\},B=\infty\) on the top level.

In the base case of _l_=0, _S_ is a singleton {_x_} and _x_ is complete. We run a mini Dijkstra’s algorithm (Algorithm 2) starting from _x_ to find the closest vertices _v_ from _x_ such that _d(v)\<B_ and the shortest path to _v_ visits _x_, until we find _k_+1 such vertices or no more vertices can be found. Let _U_<sub>0</sub> be the set of them. If we do not find _k_+1 vertices, return \(B'\leftarrow B,U\leftarrow U_0\). Otherwise, return \(B'\leftarrow max_{v\in U_0}d(v),U\leftarrow\{v\in U_0:d(v)<B'\}\).

If _l\>_0, first we use FindPivots from Lemma 3.2 to obtain a pivot set \(P\subseteq S\) and a set _W_. We initialize the data structure D from Lemma 3.3 with _M_:=2<sup>(_l_-1)_t_</sup> and add each \(x\in P\) as a key associated with value \(\widehat{d}[x]\) to D. For simplicity, we write D as a set to refer to all the keys (vertices) in it.

Set \(B'_0\leftarrow min_{x\in P}\widehat{d}[x]\); \(U\leftarrow\emptyset\). The rest of the algorithm repeats the following iteration of many phases, during the _i_-th iteration, we:

1. Pull from D a subset _S<sub>i</sub>_ of keys associated with the smallest values and _B<sub>i</sub>_ indicating a lower bound of remaining value in D ;<tbc>

2. Recursively call BMSSP(_l_-1_,B<sub>i</sub>,S<sub>i</sub>_), obtain its return, \(B'_i\) and _U<sub>i</sub>_, and add vertices in _U<sub>i</sub>_ into _U_;<tbc>

3. Relax every edge (_u,v_) for \(u\in U_i\) (i.e. \(\widehat{d}[v]\leftarrow min\{\widehat{d}[v],\widehat{d}[u]+w_{uv}\}\)). If the relax update is valid (\(\widehat{d}[u]+w_{uv}\le\widehat{d}[v]\)), do the following (even when \(\widehat{d}[v]\) already equals \(\widehat{d}[u]+w_{uv}\)):

(a) if \(\widehat{d}[u]+w_{uv}\in[B_i,B)\), then simply insert \(\langle v,\widehat{d}[u]+w_{uv}\rangle\) into D;<tbc>

(b) if \(\widehat{d}[u]+w_{uv}\in[B'_i,B_i)\), then record \(\langle v,\widehat{d}[u]+w_{uv}\rangle\) in a set _K_;<tbc>

4. Batch prepend all records in _K_ and \(\langle x,\widehat{d}[x]\rangle\) for \(x\in S_i\) with \(\widehat{d}[x]\in[B'_i,B_i)\) into D;<tbc>

5. If D is empty, then it is a successful execution and we return;<tbc>

6. If |_U|\>k_2<sup>_lt_</sup>, set \(B'\leftarrow B'_i\). We expect a large workload and we prematurely end the execution.<tbc>

