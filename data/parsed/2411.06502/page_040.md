\((r_k,s',r_j,q')\)-DISED instances. Recursion stops when _j=i_+1. At this point, if _r<sub>i</sub>_ immediately precedes _r_<sub>_i_+1</sub>, we use Lemma 5.2; otherwise, we add (_r<sub>i</sub>,r_<sub>_i_+1</sub>) to _I_.

Therefore, starting with _i_=1 and _j=d_, we achieve the desired reduction of the \((s,s',q,q')\)-DISED instance to \(|I|\le d-1\) DISED instances in time \(\mathcal{O}((d-1)\cdot(\mathsf{T}_\mathsf{MUL}(m)+m^{2+o(1)}))\). In the unweighted setting, the time is \(\mathcal{O}((d-1)\cdot(\mathsf{T}_\mathsf{MonMUL}(m,m,m,\mathsf{D})+m^{2+o(1)}g(\mathsf{D}))\).

To conclude the proof, it suffices to prove \(d-1\le 2m/\Delta+1\le 3m/\Delta\). To this end, we analyze Line 5 in Algorithm 2. Here is an important observation: if \(|\mathsf{sub}(r_i)\backslash\mathsf{sub}(r_{i+1})|<\Delta\), then either _d=i_+1 or \(|\mathsf{sub}(r_i)\backslash\mathsf{sub}(r_{i+1})|+|\mathsf{sub}(r_{i+1})\backslash\mathsf{sub}(r_{i+2})|>\Delta\). Consequently, we iterate at most

\(2|\mathsf{sub}(s)\backslash\mathsf{sub}(q)|/\Delta+1\le 2m/\Delta+1\)

times in Line 3, obtaining \(d-1\le 2m/\Delta+1\).

**Corollary 5.5.** _There exists an algorithm_ **A**_<sub>DISED</sub> solving DISED running in time_ \(\mathcal{O}(\mathsf{T}_\mathsf{MUL}(m)+m^{2+o(1)})\) _on instances of size m._

_Furthermore, if the DISED instance is unweighted and has global tree size_ D_, then the algorithm requires time_ \(\mathcal{O}(\mathsf{T}_\mathsf{MonMUL}(m,m,m,\mathsf{D})+m^{2+o(1)}g(\mathsf{D}))\) _where_ \(\mathsf{T}_\mathsf{MonMUL}(m,m,m,\mathsf{D})=\mathcal{O}(f(m)g(\mathsf{D}))\).

**Proof.** To devise such **A**<sub>DISED</sub>, it suffices to apply recursively Lemma 5.4 with threshold \(\Delta(m)=m/\alpha\) for a constant \(\alpha\ge 1\) to be determined later. The base case is handled using Lemma 5.2. Thus, we obtain the following recurrence for the running time

\(\mathsf{T}(m)\le c_1\cdot m^2/\Delta^2\cdot\mathsf{T}(\Delta)+c_2\cdot m^2/\Delta^2\cdot(\mathsf{T}_\mathsf{MUL}(m)+m^{2+o(1)})+c_3\cdot m^{2+o(1)}\)<br>
\(=c_1\alpha^2\cdot\mathsf{T}(m/\alpha)+c_2\alpha^2\cdot(\mathsf{T}_\mathsf{MUL}(m)+m^{2+o(1)})+c_3\cdot m^{2+o(1)}\)

where _c_<sub>1</sub>=9 and we write out the constants _c_<sub>2</sub>_,c_<sub>3</sub> hidden in the time needed to solve the original \((s,s',q,q')\)-DISED instance, and to find the smaller DISED instances, respectively. Performing similar analysis to Corollary 4.9, we conclude that \(\mathsf{T}(m)=\mathcal{O}(\mathsf{T}_\mathsf{MUL}(m)+m^{2+o(1)})\). In the unweighted case, we note that the recurrence is instead

\(\mathsf{T}(m)=c_1\alpha^2\cdot\mathsf{T}(\alpha\cdot m)+c_2\alpha^2\cdot(\mathsf{T}_\mathsf{MonMUL}(m,m,m,\mathsf{D})+m^{2+o(1)}g(\mathsf{D}))+c_3\cdot m^{2+o(1)}.\)

and we bound the running time as in Corollary 4.9.

## 5.2 Proof of Main Theorem 3

Now, we show how to prove Main Theorem 3 using the algorithm for DISED from Corollary 5.5.

**Main Theorem 3.** _Suppose there exists an algorithm computing the min-plus product of two_ \(m\times m\) _matrices in time_ T<sub>_MUL_</sub>(_m). Then, there is an algorithm for SED running in time_ \(\mathcal{O}(\mathsf{T}_\mathsf{MUL}(n)+n^{2+o(1)})\)_, where_ \(n=max(|\mathbf{F}|,|\mathbf{F}'|)\).

We also prove the following theorem for unweighted SED.

**Theorem 5.6.** _There is an algorithm for unweighted SED running in time_ \(\mathcal{O}(\mathsf{T}_\mathsf{MonMUL}(n)+n^{2+o(1)}g(n))\)_, where_ \(n=max(|\mathbf{F}|,|\mathbf{F}'|)\) _and_ \(\mathsf{T}_\mathsf{MonMUL}(m,m,m,\mathsf{D})=\mathcal{O}(f(m)g(\mathsf{D}))\).

**Proof of Main Theorem 3 and Theorem 5.6.** Suppose _s_ is the first node (i.e., the root) and _q_ is the last node appearing in **S**. Similarly, suppose \(s'\) is the first node and \(q'\) is the last node appearing in \(\mathbf{S}'\). The algorithm for SED is simple, we use **A**<sub>DISED</sub> to solve the \((s,s',q,q')\)-DISED instance.

\(\includegraphics{}\) **Corollary 5.5.** _There exists an algorithm_ **A**_<sub>DISED</sub> solving DISED running in time_ \(\mathcal{O}(\mathsf{T}_\mathsf{MUL}(m)+m^{2+o(1)})\) _on instances of size m._

