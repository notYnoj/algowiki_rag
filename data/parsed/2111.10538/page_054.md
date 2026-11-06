**Algorithm 11** Recursive Estimate LIS with Oracle

procedure RecursiveEstimationWithOracle(Oracle,\(A,\lambda,\ell,r\)) \(\triangleright\) Lemma 6.9<br>
   \(\triangleright\) input: sequence A, parameter \(\lambda\), domain interval \([\ell,r]\)<br>
   \(\triangleright\) assume \(\mathsf{sa}_1,\mathsf{sa}_2,\dots,\mathsf{sa}_{n^\kappa}\) are subarrays of A<br>
   \(\triangleright\) subroutine Oracle approximate LIS for subarrays with approximation factor \(f(\lambda)\)<br>
   for \(i\in[\zeta]\) do<br>
   \(\mathsf{cdi}_i\leftarrow\) ConstructCandidateDomains(sa<sub>i</sub>)<br>
   discard all the intervals which are not in \([\ell,r]\) from cdi<sub>i</sub><br>
   end for<br>
   \(\{\mathsf{ps}_1,\dots,\mathsf{ps}_t\}\leftarrow\) ConstructPseudoSolutions(\(\mathsf{cdi}_1,\dots,\mathsf{cdi}_\zeta\))<br>
   \(\lambda_0\leftarrow\left(\frac{\lambda}{2^8}\right)^4\)<br>
   \(p\leftarrow\frac{20\mathrm{log}^4n}{\lambda_0\zeta}\)<br>
   randomly sample each \(i\in[\zeta]\) with probability p, and put all the samples in a set Q<br>
   for \(j\in[t]\) do<br>
  \(\mathsf{c}\leftarrow 0\)<br>
   for \(i\in W\) do<br>
   if \(\exists[\ell_i,r_i]\in\mathsf{ps}_j\) and Oracle\((\mathsf{sa}_i,\lambda_0,\ell_i,r_i)\) accepts then<br>
   \(\mathsf{c}\leftarrow\mathsf{c}+1\)<br>
   end if<br>
   end for<br>
   if \(\mathsf{c}\ge 3\lambda_0p\zeta/4\) then<br>
**return**<br>
accept<br>
   end if<br>
   end for<br>
   return reject<br>
end procedure

<tbc>_as a subroutine is a_ \(\left(f\left(\frac{\lambda^4}{2^{32}}\right)\cdot\frac{\lambda^4}{2^{33}}\right)\)_-approximate LIS algorithm with_

\(O\left(\lambda^{-4}g\left(\frac{n}{\zeta},\frac{\lambda^4}{2^{32}}\right)\mathrm{log}^{O(1)}n+\lambda^{-7}\zeta\mathrm{log}^{O(1)}n\right)\)

_running time and success probability_ \(1-\mathrm{exp}(-\Omega(\mathrm{log}^2n))\)_, where_ \(\zeta\) _is the number of subarrays._

_Proof._ We first prove the correctness of the algorithm. Let _A_ be a sequence of length _n_, and \(\mathsf{sa}_1,\dots,\mathsf{sa}_\zeta\) be the subarrays.

Consider the case of \(\mathsf{lis}^{[\ell,r]}(A)\ge\lambda n\). By Corollary 6.2 and Lemma 6.4 with \(\epsilon=\delta=1/10\), with probability \(1-\mathrm{exp}(-\Omega(\zeta\lambda))\), there exists a pseudo-solution \(\mathsf{ps}_j\) within interval \([\ell,r]\) satisfying<tbc>

\(\mathsf{q}(\mathsf{ps}_j)\ge\frac{\mathsf{lis}^{[\ell,r]}(A)}{2t}\ge\frac{\mathsf{lis}^{[\ell,r]}(A)\lambda\epsilon}{2k^2}\ge\frac{\mathsf{lis}^{[\ell,r]}(A)\lambda\epsilon}{2\cdot 20^2\mathrm{log}^2(1/\delta)/(\lambda^2\epsilon^4)}\ge\frac{\epsilon^5\lambda^4}{800\mathrm{log}^2(1/\delta)}n\ge\frac{\lambda^4}{2^{31}}n.\)

<tbc>Let \(\alpha\) denote the number of subarrays sa_<sub>i</sub>_ such that \(\mathsf{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)\ge\lambda_0n/\zeta\) where \([\ell_i,r_i]\) is the interval for subarray sa_<sub>i</sub>_ in ps_<sub>j</sub>_. We have<tbc>

\(\alpha\ge\frac{\mathsf{q}(\mathsf{ps}_j)-\lambda^4n/2^{32}}{n/\zeta}\ge\frac{\lambda^4\zeta}{2^{32}}.\)

