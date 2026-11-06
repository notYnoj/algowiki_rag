**Algorithm 3:** Recall from Theorem 15 that Algorithm 3 w.h.p. returns \(\widetilde{L}=\widetilde{\Omega}\big(min\big\{\frac{\lambda}{\sqrt{T}},\frac{\lambda\sqrt{T}}{\mu}\big\}\big)\). Assuming that \(\lambda\ge L^2T^{0.7}/n^{1.4}\), we have<tbc>

\(\widetilde{L}=\widetilde{\Omega}\big(min\big\{\frac{L^2T^{0.2}}{n^{1.4}},\frac{L^2T^{1.2}}{\mu n^{1.4}}\big\}\big).\)

<tbc>Bounding one factor _L_ by (6) and \(\mu\) by (7) yields<tbc>

\(\widetilde{L}=\widetilde{\Omega}\big(min\big\{\frac{LT^{0.4}}{n^{0.8}},\frac{LT^{1.3}}{n^{1.6}}\big\}\big).\)

<tbc>It remains to see that \(T^{1.3}/n^{1.6}\ge T^{0.4}/n^{0.8}\), which is equivalent to \(T^{0.9}\ge n^{0.8}\) and thus follows from \(T\ge n\). Hence, Algorithm 3 satisfies the claimed approximation guarantee \(\widetilde{L}=\widetilde{\Omega}(LT^{0.4}/n^{0.8})\), under our assumption on \(\lambda\). We can thus from now on assume

\(\lambda<\frac{L^2T^{0.7}}{n^{1.4}}.\) (8)

**Algorithm 4:** We first verify that (6), (7), and (8) imply the assumptions of Theorem 17:<tbc>

\(\frac{L^2T^{0.5}}{n^2},\frac{L^2T^{1.5}}{\lambda n^2},\frac{L^3T^{1.5}}{\lambda\mu n^2}=n^{\Omega(1)}.\)

<tbc>Indeed, we have<tbc>

\(\frac{L^2T^{0.5}}{n^2}>^\text{(6)}\frac{T^{0.9}}{n^{0.8}}\ge n^{0.1}=n^{\Omega(1)},\)

<tbc>where we used \(T\ge n\). Similarly, we have<tbc>

\(\frac{L^2T^{1.5}}{\lambda n^2}>^\text{(8)}\frac{T^{0.8}}{n^{0.6}}\ge n^{0.2}=n^{\Omega(1)},\)

<tbc>and

\(\frac{L^3T^{1.5}}{\lambda\mu n^2}>^\text{(8)}\frac{LT^{0.8}}{\mu n^{0.6}}>^\text{(7)}\frac{T^{0.9}}{n^{0.8}}\ge n^{0.1}=n^{\Omega(1)}.\)

As these assumptions hold, Theorem 17 shows that Algorithm 4 w.h.p. returns \(\widetilde{L}=\Omega(min\{\frac{L^3}{n^2},\frac{L^3T}{\lambda n^2},\frac{L^4T}{\lambda\mu n^2}\})\). We verify that assuming (6), (7), and (8) this yields the claimed approximation guarantee. Indeed, we have<tbc>

\(\frac{L^3}{n^2}>^\text{(6)}\frac{LT^{0.4}}{n^{0.8}}.\)

<tbc>Similarly, we have<tbc>

\(\frac{L^3T}{\lambda n^2}>^\text{(8)}\frac{LT^{0.3}}{n^{0.6}}\ge\frac{LT^{0.4}}{n^{0.8}},\)

<tbc>since \(T\le n^2\). Finally, we have

\(\frac{L^4T}{\lambda\mu n^2}>^\text{(7)}\frac{L^3T^{1.1}}{\lambda n^{2.2}}>^\text{(8)}\frac{LT^{0.4}}{n^{0.8}}.\)

In all cases we obtain a lower bound of \(\widetilde{L}=\widetilde{\Omega}(LT^{0.4}/n^{0.8})\).

In summary, we proved that w.h.p. at least one of the Algorithms 1-4 satisfies the desired approximation guarantee of \(\widetilde{L}=\widetilde{\Omega}(LT^{0.4}/n^{0.8})\). This concludes the proof of Theorem 9.

## Acknowledgements.

We thank an anonymous reviewer for suggesting how to turn the near-linear-time algorithm that we obtained in a previous version of this paper into a linear-time algorithm.

