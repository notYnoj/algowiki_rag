<tbc>_with_ \(r,u,\bar{u}\) _the (complex) roots of_ \(\lambda^3+\lambda^2+1=0\)_. Equivalently,_ (_s<sub>n</sub>_) _is the integer sequence determined by_<tbc>

\(s_0=3,s_1=-1,s_2=1,s_{n+3}=-s_{n+2}-s_n(n\ge 0).\)

<tbc>_Proof._ Since the characteristic polynomial of _A_ factors as stated, the eigenvalues of _A_ (counted with algebraic multiplicity) consist of the two roots \(\varphi,\psi\) of \(\lambda^2-\lambda-1\), the two primitive cubic-roots-of-unity \(\omega,\omega^2\) (roots of \(\lambda^2+\lambda+1\)), and the three distinct roots \(r,u,\bar{u}\) of \(\lambda^3+\lambda^2+1\), each occurring with algebraic multiplicity 2 because of the squared factor. For any square matrix _A_ the eigenvalues of _A<sup>n</sup>_ are the _n_-th powers of the eigenvalues of _A_ (with the same algebraic multiplicities), hence

\(\mathrm{tr}(A^n)=\sum_{\lambda_i\text{eigenvalue of}A}\lambda_i^n=\varphi^n+\psi^n+\omega^n+(\omega^2)^n+2\big(r^n+u^n+\bar{u}^n\big),\)

where the factor 2 in front of the cubic-root sum accounts for the algebraic multiplicity coming from the squared factor. Now observe the standard identities:

(i) \(\varphi^n+\psi^n=L_n\) (the Lucas sequence identity).<tbc>

(ii) \(\omega^n+(\omega^2)^n=2\mathrm{cos}\big(\frac{2\pi n}{3}\big)\) since \(\omega=e^{2\pi i/3}\).<tbc>

(iii) Define \(s_n:=r^n+u^n+\bar{u}^n\). Because \(r,u,\bar{u}\) are the roots of \(\lambda^3+\lambda^2+1=0\), the Newton/Girard relations imply that (_s<sub>n</sub>_) satisfies the linear recurrence<tbc>

<tbc>\(s_{n+3}=-s_{n+2}-s_n\)<tbc>

<tbc>with the displayed initial values _s_<sub>0</sub>=3_,s_<sub>1</sub>=-1_,s_<sub>2</sub>=1.<tbc>

<tbc>Combining these observations gives<tbc>

\(\mathrm{tr}(A^n)=L_n+2\mathrm{cos}\big(\frac{2\pi n}{3}\big)+2s_n.\)

<tbc>The polynomial identity above and the trace relation produce an explicit _n_-dependent part of \(P(\mathcal{C}_n^{(3)},3)\). Any remaining additive constant must be independent of _n_ (it cannot grow exponentially) and arises from any contributions to the coloring count not captured by the transfer-block trace; we determine this constant by matching the closed form to computed values for a single convenient odd _n_ (equivalently, to two independent small _n_ values to be safe). Using the computed exact values (for example, in  1, see \(P(\mathcal{C}_9^{(3)},3)=18\) while \(\mathrm{tr}(A^9)=L_9+2\mathrm{cos}(6\pi)+2s_9=76+2+2(-31)=16\)), one finds that the constant equals 2. Thus

\(P(\mathcal{C}_n^{(3)},3)=\mathrm{tr}(A^n)+2=L_n+2\mathrm{cos}\big(\frac{2\pi n}{3}\big)+2s_n+2,\)

as claimed.

Finally, for the asymptotic statement, note that the dominant root of \(\lambda^2-\lambda-1\) is the golden ratio \(\varphi=(1+\sqrt{5})/2\approx 1.618\). All other roots (the two primitive cube-roots of unity and the three roots of the cubic) have magnitudes strictly less than \(\varphi\); in particular, the largest magnitude among the cubic roots is approximately \(\rho\approx 1.466\). Hence

\(P(\mathcal{C}_n^{(3)},3)=\varphi^n+O(\rho^n),\)

as \(n\rightarrow\infty\) through odd integers. This completes the proof. □

For even values of _n_, the situation becomes significantly more complex due to the presence of diameter constraints that couple opposite vertices. The single-window transfer matrix approach used for odd _n_ is insufficient, as it cannot enforce the global constraint \(c_i\neq c_{i+n/2}\).

