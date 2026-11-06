<tbc>similarities via Main Theorem 4 on **F**\[_r(q)..r(s_)\] and \(\mathbf{F}'[r(q')..r(s')\)\]. Given the dimensions, this process requires no more than O(T<sub>MUL</sub>(_m_)+_m_<sup>2+_o_(1)</sup>) time. In the unweighted setting, we note that all matrices are monotone and have entries bounded by global tree size O(D). Furthermore, we apply Theorem 4.1 to obtain the necessary inputs. The total time requires no more than O(T<sub>MonMUL</sub>(_m,m,m,_D)+_m_<sup>2+_o_(1)</sup>_g_(D)) time. It is important to note that in both cases where Main Theorem 4 is applied, the required similarities \(\mathrm{sim}(\mathrm{sub}(v),\mathrm{sub}(v'))\) are available from the SED instance, because at most one of _v_ and \(v'\) belongs to a spine.

Note that in O(T<sub>MUL</sub>(_m_)) time we can also compute via max-plus products the four matrices

\(D^{(11)}=(d_{i,j}^{(11)}),D^{(21)}=(d_{i,j}^{(21)}),D^{(12)}=(d_{i,j}^{(12)})\text{and}D^{(22)}=(d_{i,j}^{(22)}),\)

defined as \(D^{(\mathrm{xy})}=A^{(\mathrm{x})}\star B\star C^{(\mathrm{y})}\) for \(\mathrm{x},\mathrm{y}\in\{1,2\}\).

By the discussion in the case distinction, we obtain that we can compute \(\mathrm{sim}(\mathbf{F}[x..y\text{\textbf{)}},\mathbf{F}'[x'..y'\text{\textbf{)}})\) for the sets (11), (12), (13), and (14) as

\(\mathrm{sim}(\mathbf{F}[x..y\text{\textbf{)}},\mathbf{F}'[x'..y'\text{\textbf{)}})=\mathrm{max}\left\{\mathrm{sim}_q(\mathbf{F}[x..y\text{\textbf{)}},\mathbf{F}'[x'..y'\text{\textbf{)}}),\left\{\begin{array}{ c c }
d_{x^\prime-r(q^\prime),y^\prime-r(q^\prime)}^{(11)} & (x,y,x',y')\in(11) \\
d_{x^\prime-r(q^\prime),y-r(q)}^{(12)} & (x,y,x',y')\in(12) \\
d_{y-l(r),y^\prime-r(q^\prime)}^{(21)} & (x,y,x',y')\in(13) \\
d_{y-l(r),y-r(q)}^{(22)} & (x,y,x',y')\in(14)
\end{array}\right\},\)

where the values coming from sim_<sub>q</sub>_ can be obtained in time O(T<sub>MUL</sub>(_m_)+_m_<sup>2+_o_(1)</sup>) (O(T<sub>MonMUL</sub>(_m,m,m,_D)+_m_<sup>2+_o_(1)</sup>_g_(D)) in the unweighted setting) using Lemma 4.10 on sub(_r_), \(\mathbf{F}'[r(q')..r(s')\text{\textbf{)}}\), **S** and _q_. As for the two applications of Main Theorem 3, the necessary input comes from the SED instance.

The proofs in the remaining part of this (sub)sections closely resemble the approach taken in Lemma 5.7. They tackle computing similarities of the form \(\mathrm{sim}(\mathbf{F}[x..y\text{\textbf{)}},\mathbf{F}'[x'..y'\text{\textbf{)}})\) by distinguishing various possible cases for the ranges of \(x,y,x',y'\). Each case will be addressed with expressions that may be rewritten as max-plus products, where the necessary matrices can be constructed using the inputs of the \((s,s',q,q')\)-DISED instance, or by applying one of Lemma 4.10 or Main Theorem 4. Ultimately, we select the maximum among these cases.

For brevity, we omit details beyond the initial case distinction in these proofs--specifically, how all distinct cases are put together into a single formula and how the distinct cases can be written as max-plus product between matrices (we still specify where the entries of these matrices can be retrieved from). It is important to note that in each of these cases, we employ max-plus products on matrices no larger than the instance size and apply Main Theorem 4 and Lemma 4.10 exclusively to forests of instance size, ensuring that either no nodes from **S** or no nodes from \(\mathbf{S}'\) are included. In the unweighted tree edit distance problem, we further note that all matrices are monotone with entries bounded by the size of the trees.

**Lemma 5.8.** _Suppose we are provided with the input of an_ \((s,s',q,q')\)_-DISED instance of size m. Further, let_ \(r\in\mathbf{S}\) _such that s\<r\<q. Then, we can compute_ \(\mathrm{sim}(\mathbf{F}[x..y\text{\textbf{)}},\mathbf{F}'[x'..y'\text{\textbf{)}})\) _for all_ \((x,x')\in(|l(r)\times[r(q')..r(s')])\cup([|l(s)..l(q)]\times r(q'))\) _and_ \((y,y')\in(r(r)\times[r(q')..r(s')])\cup([r(q)..r(r)]\times r(s'))\) _in time_ O(T<sub>_MUL_</sub>(_m_)+_m_<sup>2+_o_(1)</sup>).

_Furthermore, if the DISED instance is unweighted and has global tree size_ D_, then the algorithm requires time_ O(T<sub>_MonMUL_</sub>(_m,m,m,_D)+_m_<sup>2+_o_(1)</sup>_g_(D)) _where_ T<sub>_MonMUL_</sub>(_m,m,m,_D)=O(_f(m)g_(D)).

**Proof.** Refer to Figure 12 for a visualization of the ranges of \(x,y,x',y'\) for which \(\mathrm{sim}(\mathbf{F}[x..y\text{\textbf{)}},\mathbf{F}'[x'..y'\text{\textbf{)}})\) needs to be computed. Observe in Figure 12 that the ranges of \(x,y,x',y'\) for Lemma 5.8, are almost

