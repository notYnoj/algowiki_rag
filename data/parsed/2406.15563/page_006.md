independent set _C<sub>c</sub>_ given by line 6, \(|C_c|\ge\alpha(G[V])/r'\ge\frac{|V|}{3r'}\) with probability at least \(\frac{1}{2}\). Thus \(\mathbf{Pr}[|C_c|<|V|/(3r')]\le(1/2)^n\) as desired.

**Claim 2.6.** _Algorithm 1 gives a valid coloring of G using at most O(r_) _colors with high probability._

_Proof._ Validity of the coloring follows is clear by construction, since we choose a new color for each independent set. It remains to bound the number of colors used.

Note that \(c\le n\) at all times, since |_V_| reduces by at least one at each iteration. Thus by Claim 2.5, |_V_| reduces by a factor of \((1-1/(3r'))\) at every iteration with probability at least 1-_n/_(2_<sup>n</sup>_). After \(\ell\) iterations,

\(|V|\le n\left(1-\frac{1}{3r'}\right)^\ell\le n\cdot exp\left(-\frac{\ell}{3r'}\right)=n\cdot exp\left(-\frac{\ell ln(n/t)}{3r}\right)=n\cdot\left(\frac{n}{t}\right)^{-\ell/3r}.\)

Therefore, when \(\ell=3r\), \(|V|\le t\), so Algorithm 1 runs for at most 3_r_+1 iterations. Since _G_ is 3-colorable, the final optimum coloring of the remaining vertices on line 10 uses at most 3 colors. Thus the total number of colors used is at most 3_r_+4=_O(r_).

**Claim 2.7.** _Algorithm 1 runs in time_ \(O^*\left(exp\left(\tilde{O}\left(\frac{nlog^{11/2}r}{r^3}\right)\right)\right)\).

_Proof._ We first bound the runtime of the while loop in lines 2-9. By Lemma 2.1, \(IS(G[V],r')\) runs in time \(O^*\left(exp\left(\tilde{O}\left(\frac{nlog^{5/2}r^\prime}{r^{\prime 3}}\right)\right)\right)\). By the analysis in the proof of Claim 2.6, the total number of iterations is at most _O(r_), and in each iteration we run \(IS(G[V],r')r\) times. This the loop runs in time

\(O^*\left(r^2exp\left(\tilde{O}\left(\frac{nlog^{5/2}r^\prime}{r^{\prime 3}}\right)\right)\right)=O^*\left(exp\left(\tilde{O}\left(\frac{nlog^{5/2}(r/log(r^3))}{r^3/log^3(r^3)}\right)\right)\right)\)<br>
\(=O^*\left(exp\left(\tilde{O}\left(\frac{nlog^{11/2}r}{r^3}\right)\right)\right).\)

Using a naive brute force algorithm, the final step in line 10 runs in time \(O\left(3^t\right)=O\left(exp\left(O\left(\frac{n}{r^3}\right)\right)\right)\), giving us our desired time bound.

## References

