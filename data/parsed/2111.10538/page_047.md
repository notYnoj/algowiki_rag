**Algorithm 9** Constructing the pseudo solutions

procedure ConstructPseudoSutions(cdi<sub>1</sub>,...,cdi\(_\sqrt{n}\)) \(\triangleright\) Lemma 6.3,6.4,6.5<br>
   \(\triangleright\{cdi_i\}_{i\in[\sqrt{n}]}\) is \(\sqrt{n}\) sets of candidate domain intervals<br>
   pseudo-solutions \(\leftarrow\emptyset\)<br>
   while true do<br>
   \(\text{assg}\leftarrow\) largest assignment of candidate domain intervals to subarrays which is monotone<br>
   if assg contains less than \(\epsilon\sqrt{n}\lambda\) non-empty candidate domain intervals then<br>
   break<br>
   else<br>
   Add assg to pseudo-solutions<br>
   for \(i\leftarrow 1\) to \(\sqrt{n}\) do<br>
   if assg contains a candidate domain interval for subarray sa<sub>i</sub> then<br>
remove<br>
the<br>
corresponding<br>
candidate<br>
domain<br>
interval<br>
from<br>
cdi<br>
_<sub>i</sub>_<br>
   end if<br>
   end for<br>
   end if<br>
   end while<br>
   return pseudo-solutions ps<sub>1</sub>,ps<sub>2</sub>,...,ps<sub>t</sub><br>
end procedure

## 6.2 Constructing Approximately Optimal Pseudo-solutions

We call a sequence of \(\sqrt{n}\) intervals \([\ell_1,r_1],[\ell_2,r_2],\dots,[\ell_\sqrt{n},r_\sqrt{n}]\) a pseudo-solution if all of the intervals are monotone. That is \(\ell_1\le r_1<\ell_2\le r_2<\ell_3\le r_3\le\dots\le\ell_\sqrt{n}\le r_\sqrt{n}\). These intervals denote solution-domains for the subarrays. We also may decide not to assign any solution domain to a subarray in which case we show the corresponding interval by \(\emptyset\). We define monotonicity of a pseudo-solution such that it is not violated by \(\emptyset\). The quality of a pseudo-solution is defined as \(\sum_i\text{lis}^{[\ell_i,r_i]}(\text{sa}_i)\). We denote the quality of a pseudo-solution ps by q(ps).

Another way to interpret Corollary 6.2 is that one can construct a pseudo-solution using the sampled elements whose quality is at least a \(1-\epsilon\) fraction of lis(_A_). In this section, we present an algorithm to construct a small set of pseudo-solutions with the promise that at least one of them has a quality of at least lis(_A)/t_, where _t_ is the number of pseudo-solutions. Finally, in Section 6.3, we present a method to approximate the size of the optimal solution using pseudo-solutions.

We construct the pseudo-solutions via Algorithm 9. The input of Algorithm 9 is the set of candidate domain intervals obtained by Algorithm 8 on every subarray. We first find an assignment of candidate solution domains to the subarrays which is monotone and has the largest number of candidate domain intervals. (This step can be implemented by dynamic programming or solved with an algorithm similar to activity selection algorithm.) We make a pseudo-solution out of this assignment and update the set of candidate intervals by removing the ones which are used in our pseudo-solution. We then repeat the same procedure to construct the second pseudo-solution and update the candidate solution domains accordingly. We continue on, until the number of solution domains used in our pseudo-solution drops below \(\epsilon\lambda\sqrt{n}\) in which case we stop.

We first prove in Lemma 6.3 that the number of pseudo-solutions constructed in Algorithm 9 is bounded by \(O(k^2/(\lambda\epsilon))\). Next, we show in Lemma 6.4 that at least one of the pseudo-solutions constructed by Algorithm 9 has a quality of at least \(\Omega(\text{lis}(A)/t)\) where _t_ is the number of pseudo- solutions. Finally we prove in Lemma 6.5 that the running time of Algorithm 9 is \(O(tk^2\sqrt{n}logn)\).

