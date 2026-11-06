**Algorithm 10** Evaluate the pseudo solutions

procedure EvaluatePseudoSutions(ps<sub>1</sub>_,...,_ps<sub>_t_</sub>) \(\triangleright\) Lemma 6.6<br>
   \(\triangleright\{\mathsf{ps}_i\}_{i\in[t]}\) is a set of pseudo solutions<br>
   \(p\leftarrow\frac{1000tlog^4n}{\epsilon^4\lambda\sqrt{n}}\)<br>
   Randomly sample each \(i\in[\sqrt{n}]\) with probability p, and put all the samples in a set W<br>
   for each ps<sub>j</sub> do<br>
   \(\widetilde{\mathsf{q}}(\mathsf{ps}_j)\leftarrow 0\)<br>
   for each interval \([\ell_i,r_i]\) in ps<sub>j</sub> do<br>
   if \(i\in W\) then<br>
   \(\widetilde{\mathsf{q}}(\mathsf{ps}_j)\leftarrow\widetilde{\mathsf{q}}(\mathsf{ps}_j)+\mathsf{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)/p\)<br>
   end if<br>
   end for<br>
   end for<br>
   return largest \(\widetilde{\mathsf{q}}(\mathsf{ps}_j)\) for all \(j\in[t]\)<br>
end procedure

_Proof._ Lemma 6.3 states that Algorithm 9 terminates after constructing _t_ pseudo-solutions. Now we show that constructing each pseudo-solution takes time<br>
\(O(k^2\sqrt{n}logn)\). Our solution is based on a dynamic programming technique. Let \(D:[\sqrt{n}]\times[k^2]\rightarrow\mathbb{N}\) be an array such that _D_\[_i_\]\[_j_\] stores the size of the largest monotone pseudo-solution for the first _i_ subarrays which ends with the _j_’th candidate domain interval of sa<sub>_i_</sub>. Using classic segment-tree data structure (this data structure can be found in many textbooks, e.g. \[CLRS09\]), one can compute the value of _D_\[_i_\]\[_j_\] in time _O_(log_n_) from the previously computed elements of the array.

Thus, the total running is bounded by \(O(tk^2\sqrt{n}logn)\).

## 6.3 Evaluating the Pseudo-solutions

We finally use a concentration bound to show that the quality of a pseudo-solution can be approximated well by sampling a small number of subarrays. Since a pseudo-solution specifies the range of the numbers used in every subarray, the quality of a pseudo-solution, or in other words, the size of the corresponding increasing subsequence of a pseudo-solution can be formulated as

\(\mathsf{q}(\mathsf{ps}):=\sum_{i=1}^{\sqrt{n}}\mathsf{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)\)

where \([\ell_i,r_i]\) denotes the corresponding solution domain of ps for sa<sub>_i_</sub>.

In Lemma 6.6, we prove that by sampling \(O(log^{O(1)}n/\lambda^4)\) many subarrays and computing \(\mathsf{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)\) for them, one can approximate the quality of a pseudo-solution pretty accurately.

**Lemma 6.6** (the quality of pseudo-solution)**.** _Let_ \(\lambda\in(0,1)\) _and_ \(\epsilon\) _be a constant in_ (0,1/100)_. Let_ \(\mathsf{ps}_1,\mathsf{ps}_2,\cdots,\mathsf{ps}_t\) _be a set of t pseudo-solutions. With probability at least_ \(1-exp(-\Omega(log^2n))\)_, Algorithm 10 runs in time_ \(O(t^2\sqrt{n}log^{O(1)}n/\lambda)\) _such that,_

1. _If there exists an_ \(i\in[t]\), \(\mathsf{q}(\mathsf{ps}_i)\ge\frac{\lambda n}{2t}\) _, then the algorithm outputs an estimation at least_ \(\frac{\lambda n}{4t}\) .<tbc>

_2._ _If_ \(\mathsf{q}(\mathsf{ps}_i)<\frac{\lambda n}{8t}\) _for all_ \(i\in[t]\)_, then the algorithm outputs an estimation smaller than_ \(\frac{\lambda n}{4t}\) .<tbc>

