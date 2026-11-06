_Proof._ For any \(T\unknown z\), fix _p_:=_p(T)\>_0 so that _T/z=T<sup>p</sup>_. Then, we have<tbc>

\(p(T)=\frac{log(T/z)}{log(T)}=\frac{logT-logz}{logT}\)

<tbc>is increasing for \(T\unknown 1\). In particular, we can upper bound<tbc>

\(\frac{\mathsf{T}_\mathrm{BMM}\left(T/z,T,T\right)}{T^2}\unknown\frac{T^{\omega\left(p(T),1,1\right)+o(1)}}{T^2}=T^{\omega\left(p(T),1,1\right)-2+o(1)}.\)

<tbc>Since \(\omega(p(T),1,1)\) is increasing in _T_, we have

\(\mathrm{max}_{z<T\unknown Z}\frac{\mathsf{T}_\mathrm{BMM}\left(T/z,T,T\right)}{T^2}=\mathrm{max}_{z<T\unknown Z}T^{\omega\left(p(T),1,1\right)-2+o(1)}=Z^{\omega\left(p(Z),1,1\right)-2+o(1)}\)

is maximized at _T=Z_.

We now prove the second statement, which is necessary for establishing equivalence to BMM. It suffices to consider \(z\unknown T\unknown n\) where _T_ is a power of 2, as changing _T_ by a constant factor changes T<sub>BMM</sub>(_T/z,T,T)/T_<sup>2</sup> by a constant factor. It follows from our assumption that

\(\frac{\mathsf{T}_\mathrm{BMM}\left(2T/z,2T,2T\right)}{(2T)^2}\unknown\frac{\mathsf{T}_\mathrm{BMM}\left(T/z,T,T\right)}{T^2}\)

for all \(T\unknown z\) so that the expression is maximized at _T=Z_.

To conclude the running time analysis, we apply Claim 5.8 with _z=n/|S_<sub>in</sub>| and _Z=n_ to obtain _p_:=_p(Z_)=_p(n_) satisfying _n<sup>p</sup>_=|_S_<sub>in</sub>|. In particular, we can bound the final running time as<tbc>

\(O\left(d\phi^2(logn)^2n^{\omega\left(p,1,1\right)+o(1)}\right).\)

<tbc>To establish equivalence with BMM, we apply the second statement of Claim 5.8, and bound the final running time as

\(O\left(d\phi^2(logn)^2\mathsf{T}_\mathrm{BMM}\left(|S_\mathrm{in}|,n,n\right)\right).\)

## 5.2 Extension to Bounded Weights

We now extend our algorithm to handle undirected graphs with small integer weights.

**Theorem 1.3.** MSSP _on undirected graphs with integer edge weights in_ \[_B_\] _is equivalent to_ MPP(|_S_<sub>in</sub>|_,n,n|B), up to n_<sup>_o_(1)</sup>log_B factors, for randomized algorithms._<sup>9</sup> _In particular, if_ \(B\unknown\mathrm{poly}(n)\)_, there is a randomized algorithm computing_ MSSP _on undirected graphs with integer edge weights in_ \[_B_\] _in n_<sup>_o_(1)</sup>T<sub>MPP</sub>(|_S_<sub>in</sub>|_,n,n|B_) _time._

Note that it is without loss of generality that we assume all weights are positive: a negative edge in undirected graphs creates a negative cycle, and all pairwise distances become \(-\infty\) (recall we assume the graph is connected). Also, any vertices joined by a weight 0 edge can be merged and treated as one vertex. Assume without loss of generality that _B_ is a power of 2. We will require a simple generalization of bounded Min-Plus products.

**Lemma 5.9.** _Let X be an_ \(n_1\times n_2\) _integer matrix with all finite entries bounded between_ \[_B_<sub>0</sub>_,B_<sub>0</sub>+_B_\] _and Y be an_ \(n_2\times n_3\) _integer matrix with entries bounded between_ \[0_,B_\]_. Then, X⋆Y can be computed in_ \(O\left(\mathsf{T}_\mathrm{MPP}(n_1,n_2,n_3|B)\right)=O\left(B\cdot\mathsf{T}_\mathrm{MUL}(n_1,n_2,n_3)\right)\) _time._

<sup>9</sup>Like Theorem 1.2, the equivalence holds under the mild assumption that \(\mathsf{T}_\mathrm{MPP}(2m,2n,2n|B)\unknown 4\mathsf{T}_\mathrm{MPP}(m,n,n|B)\) for all \(m,n\unknown 1\). As before, our improved running time holds regardless of the assumption.

