We can bound the last line by observing that the geometric distribution observes the memorylessness property: for any _j\>i_ we have \(Pr[R_i\le i+j|R_i\ge i]\le Pr[R_i\le j]\). Combining this with the equation above we have

\(Pr[X_i|I_i]\le Pr[R_i<\mathrm{dist}_G(s,u)+w(u,v)|R_i\ge\mathrm{dist}_G(s,u)]\le Pr[R_i\le w(u,v)]\le pw(u,v),\) (16)

where the last inequality follows from a simple analysis of the geometric distribution: each coin is head with probability _p_, so \(Pr[R_i\le w(u,v)]\) is the probability that one of the first _w(u,v_) coins is a head, which by the union bound is at most _pw(u,v_).

**Remark D.5.** _The second inequality of (16) used the memorylessness property of the geometric distribution, but we have to be a bit careful because recall that in our analysis, in order to maintain a finite probability space, we argued the algorithm sampling R<sub>i</sub>_∼Geo(_p_) _is equivalent to the algorithm sampling R<sub>i</sub>_∼Geo(_p_) _but then rounding down to R<sub>i</sub>=R<sub>max</sub>=nW<sub>max</sub> if R<sub>i</sub>\>R<sub>max</sub>. This means that we can only apply the memorylessness property in Equation (16) if_ \(\mathrm{dist}_G(s,u)+w(u,v)\le R_{max}\)_. Fortunately, this is indeed the case because W<sub>max</sub> is the maximum edge weight, so_ \(w(u,v)\le W_{max}\) _and_ \(\mathrm{dist}_G(s,u)\le(n-1)W_{max}\).

We have thus completed the proof of Lemma 6.9.

