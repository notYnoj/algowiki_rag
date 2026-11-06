By a careful calculation, one can still show that the proportion of _X_-, _Y_-, _Z_-variables in T<sub>2</sub> that are not in T<sub>1</sub> is at most a 1-2<sup>-_o(N_)</sup> fraction of those in T<sub>2</sub>. These variables become holes. Unfortunately, the methods in previous works \[Sch81, DWZ23\] do not apply, as they are unable to fix holes that are present in all three dimensions (_X_-, _Y_-, _Z_-variables).

Next, we discuss how we fix the technical issue.

## Intuition of the fix.

The first step towards resolving this issue is to decrease the fraction of holes in all three dimensions, from 1-2<sup>-_o(N_)</sup> all the way down to \(2^{-\Omega(N)}\). Then we describe a generic method adapted from \[Dua22\] for fixing holes in all three dimensions as long as the fractions of holes are small.

For the first step, we slightly relax the condition for zeroing out variables in T<sub>1</sub> and T<sub>2</sub>. Let \(\varepsilon>0\) be an arbitrary constant. For any _T<sub>i,j,k</sub>_, we use \(T_{i,j,k}^{\otimes n}[\beta_X,\beta_Y,\beta_Z,\varepsilon]\) to denote \(T_{i,j,k}^{\otimes n}\) but we zero out all level-1 _X_-, _Y_-, _Z_-variables, where the proportion of each chunk in \(\{0,1,2\}^{2^{\ell-1}}\) in their level-1 block sequence differs at most \(\varepsilon\) from the corresponding probability in \(\beta_X,\beta_Y,\beta_Z\) respectively. That is, we allow some small flexibility when zeroing out variables. Then, let<tbc>

\(\mathcal{T}'_1:=\left(T_{i^\prime,j^\prime,k^\prime}\otimes T_{i-i^\prime,j-j^\prime,k-k^\prime}\right)^{\otimes n}\big[\beta_X^{(L)}\times\beta_X^{(R)},\beta_Y^{(L)}\times\beta_Y^{(R)},\beta_Z^{(L)}\times\beta_Z^{(R)},\varepsilon\big],\)

<tbc>and recall

\(\mathcal{T}_2=\left(T_{i^\prime,j^\prime,k^\prime}^{\otimes n}\big[\beta_X^{(L)},\beta_Y^{(L)},\beta_Z^{(L)}\big]\right)\otimes\left(T_{i-i^\prime,j-j^\prime,k-k^\prime}^{\otimes n}\big[\beta_X^{(R)},\beta_Y^{(R)},\beta_Z^{(R)}\big]\right).\)

Intuitively, we allow more flexibility in T<sub>1</sub> than that in T<sub>2</sub>, so that more variables remain in T<sub>1</sub> compared to T<sub>2</sub>, and the fraction of holes should become smaller. The idea for proving this is to use concentration bounds: if we pick a uniformly random level-1 _X_-variable block from \(T_{i^\prime,j^\prime,k^\prime}^{\otimes n}\big[\beta_X^{(L)},\beta_Y^{(L)},\beta_Z^{(L)}\big]\) and another uniformly random level-1 _X_-variable block from \(T_{i-i^\prime,j-j^\prime,k-k^\prime}^{\otimes n}\big[\beta_X^{(R)},\beta_Y^{(R)},\beta_Z^{(R)}\big]\), then with very high probability (\(1-2^{-\Omega(n)}\)), the combination (interleaving the length \(2^{\ell-2}\) chunks between their level-1 block sequences) of them satisfies \(\beta_X^{(L)}\times\beta_X^{(R)}\), up to \(\varepsilon\) additive error. Then the fraction of holes is \(2^{-\Omega(n)}\). Similar reasons also apply to _Y_ - and _Z_-variables.

## Fixing the holes in all three dimensions.

Suppose we have many "broken" copies of some tensor _T_, in each of which a small fraction of variables (holes) are missing. The goal of this step is to degenerate these broken tensors into one without holes. Schönhage \[Sch81\] solved this problem for matrix multiplication tensors with holes in only _X_- and _Y_ -variables, but not _Z_, via an elegant linear transformation. Duan et al. \[DWZ23\] introduced another method for so-called standard form tensors, which are quite general and are able to capture tensor products of constituent tensors, but can only deal with holes in a single dimension. Duan \[Dua22\] developed a method utilizing an elegant recursive approach for fixing holes in all three dimensions, but only for matrix multiplication tensors.

We generalize the method of \[Dua22\] so that it can fix holes in all three dimensions simultaneously, while supporting a broad class of tensors similar to \[DWZ23\]. The only additional requirement compared to \[DWZ23\] is that the fraction of holes is below _O_(1/log_N_), where _N_ is the number of variables in the tensor _T_. This requirement is satisfied via the previous step of the fix.

Next, we provide some intuition of the recursive hole-fixing approach. Assume _T_ is supported on variable sets _X,Y,Z_, and the fraction of holes in every copy of _T_ does not exceed \(c\checkmark 1\). We first take one broken copy of _T_, which we call _T_<sub>hole</sub>, and let _X_<sup>(0)</sup>_,Y_<sup>(0)</sup>_,Z_<sup>(0)</sup> denote the set of holes in _T_<sub>hole</sub>; let _X_<sup>(1)</sup>:=_X_\\_X_<sup>(0)</sup>, _Y_<sup>(1)</sup>:=_Y_\\_Y_<sup>(0)</sup>, _Z_<sup>(1)</sup>:=_Z_\\_Z_<sup>(0)</sup> represent the set of non-hole variables. We can further divide _T_ into the<tbc>

