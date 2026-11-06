Note that the algorithm from Lemma 5 can report false-negatives, if the choice of _S_ is incorrect, but always outputs a solution if the choice of _S_ is correct. Therefore, we can run the algorithm of Lemma 5 with many choices of _S_, and we will get a solution if at least one of these choices was correct.

## 4.5 Putting all together

function extend(I, P=(_P_<sub>1</sub>_,P_<sub>2</sub>_,...,P<sub>t</sub>_), e<sub>1</sub>,e<sub>2</sub>,...,e<sub>n-1</sub>, S, i)<br>
   if \(|S|\ge k+t\) then<br>
   return Y<sub>ES</sub><br>
   if _Lemma 5 applied to_ I and S returns Y<sub>ES</sub> then<br>
   return Y<sub>ES</sub><br>
   if \(i\ge n-1\) then<br>
   return NO<br>
   if i=0 then<br>
   \(\ell\leftarrow 0\)<br>
   else<br>
   \(\ell\leftarrow\) integer in [t] such that \(e_i\in P_\ell\)<br>
   if i\>0 then // next edge is in the same path<br>
   foreach \(p\in[1,k]\) do // it is the earliest edge with rem. profit p<br>
   \(j\leftarrow\) smallest integer in [i+1,n-1] with \(e_j\in P_\ell\) and rp(S,e<sub>j</sub>)=p, or n;<br>
   if extend (I, P, e<sub>1</sub>,e<sub>2</sub>,...,e<sub>n-1</sub>, \(S\cup\{e_j\}\), j) is Y<sub>ES</sub> then<br>
   return Y<sub>ES</sub><br>
   foreach \(\ell'\in[\ell+1,t]\) do // next edge is in another path \(P_{\ell^\prime}\)<br>
   foreach \(p\in[-\mathbf{w}(A),k]\) do // it has remaining profit p<br>
   \(j\leftarrow\) smallest integer in [i+1,n-1] with \(e_j\in P_{\ell^\prime}\) and rp(S,e<sub>j</sub>)=p, or n;<br>
   if extend (I, P, e<sub>1</sub>,e<sub>2</sub>,...,e<sub>n-1</sub>, \(S\cup\{e_j\}\), j) is Y<sub>ES</sub> then<br>
   return Y<sub>ES</sub><br>
   return NO;

To prove our first main result, Theorem 1, we pipeline the lemmas into an algorithm that solves \(\mathrm{MAS}/\mathrm{MaxST}(\mathbb{Z}_{\ge 1})\) in \(2^{k^{\mathcal{O}(1)}}\cdot n^{\mathcal{O}(1)}\) running time. The core internal subroutine of this algorithm works with a proper path cover and outputs a solution in FPT-time (see Alg. 1). For convenience, we restate Theorem 1 here right before the proof.

**Theorem 1.** \(\mathrm{MAS}/\mathrm{MaxST}(\mathbb{Z}_{\ge 1})\) _admits an algorithm with_ \(2^{k^{\mathcal{O}(1)}}\cdot|\mathcal{I}|^{\mathcal{O}(1)}\) _running time._

_Proof._ Given an instance I=(_G,_**w**_,k_), the algorithm first applies Lemma 3 to I. If it reports a solution to I, the algorithm outputs it and stops. Otherwise, our algorithm obtains an equivalent instance \(\mathcal{I}'\). Lemma 3 guarantees that solving \(\mathcal{I}'\) is equivalent to solving I, as the resulting solution to \(\mathcal{I}'\) can be transformed into a solution to I. Without loss of generality, we put \(\mathcal{I}:=\mathcal{I}'\), assuming that the algorithm always transforms the solution as required.

**Algorithm 1:** The recursive subroutine `extend` of the algorithm of Theorem 1. It takes (as an input) an instance I, a proper path cover P of _T_, and a P-respecting ordering _e_<sub>1</sub>_,...,e<sub>n</sub>_ of _E(T_). `extend`(I, P, _e_<sub>1</sub>_,...,e<sub>n</sub>_, \(\emptyset\), 0) returns Yes iff I is a yes-instance.

