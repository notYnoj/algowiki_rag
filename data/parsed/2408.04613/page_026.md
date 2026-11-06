**Proof.** Each value in core(_A_) is a positive integer and contributes at least one to \(\delta^\Sigma(A)\).

\(\blacktriangleright\) **Corollary B.11.** _For a subpermutation s of length n, we have_ \(\delta(M^s)=\mathcal{O}(n)\).

**Proof.** Due to Lemma B.8, all values of _M<sup>s</sup>_ are in \[-2_n..n_\]. Due to Observation 3.1, we have \(-\delta^\Sigma(M^s)=M_{0,0}^s+M_{n,n}^s-M_{0,n}^s-M_{n,0}^s=2n-\mathsf{LIS}(s)=\mathcal{O}(n)\). Therefore, we have \(\delta(M^s)=\mathcal{O}(n)\) due to Observation B.10.<sup>7</sup> \(\blacktriangleleft\)

As implied by Lemma B.8, to answer range LIS value queries on some permutation _s_, it is sufficient to obtain random access to _M<sup>s</sup>_. We first describe a divide-and-conquer procedure that obtains the condensed representation of _M<sup>s</sup>_ and then apply Fact 4.1 to convert it into an efficient oracle. Before we describe the complete divide-and-conquer procedure, we prove a helper lemma that will be required for the conquer step.

\(\blacktriangleright\) **Lemma B.12.** _There is an algorithm that, given a subpermutation s, a subsequence t of s with s_<sup>∗</sup>=_t_<sup>∗</sup>_, and the condensed representation of M<sup>t</sup>, in time_ O(|_s_|) _computes the condensed representation of M<sup>s</sup>._

**Proof.** Let _n_:=|_s_| and _m_:=|_t_|. As _t_ is a subsequence of _s_, a linear-time greedy algorithm computes an increasing injection of _t_ onto _s_. That is, for each \(j\in[0..m)\), we compute pos(_j_) such that _t\[j_\]=_s_[pos(_j_)] and pos(_j_-1)_\<_pos(_j_) for \(j\in(0..m)\). Furthermore, we set pos(_m_)=_n_ for convenience. Moreover, for each \(i\in[0..n]\), we compute rpos(_i_) as the smallest index \(j\in[0..m]\) with \(\mathrm{pos}(j)\ge i\). These mappings allow us to convert the values of _M<sup>s</sup>_ to the values of _M<sup>t</sup>_: For \(i,j\in[0..n]\) with \(i\le j\), we have \(M_{i,j}^s=M_{\mathrm{rpos}(i),\mathrm{rpos}(j)}^t\) because (due to _s_<sup>∗</sup>=_t_<sup>∗</sup>) _s_ is only different from _t_ in ⋆ elements.

We now describe how to obtain the values in the topmost row and the leftmost column of _M<sup>s</sup>_. The values in the leftmost column can be obtained trivially in linear time due to Lemma B.8. That is, \(M_{i,0}^s=-2i\) for \(i\in[0..n]\). Furthermore, we have \(M_{0,j}^s=M_{\mathrm{rpos}(0),\mathrm{rpos}(j)}^t=M_{0,\mathrm{rpos}(j)}^t\) for all \(j\in[0..n]\). Hence, having the values of the topmost row of _M<sup>t</sup>_, we can compute the values of the topmost row of _M<sup>s</sup>_ in linear time. Therefore, it remains to compute the core of _M<sup>s</sup>_.

For conciseness, denote _A_:=_M<sup>s</sup>_ and _B_:=_M<sup>t</sup>_. Note that _s_ can be obtained from _t_ by repeatedly inserting ⋆ at some positions. We first consider the case _m=n_-1, when _s_ is obtained from _t_ by inserting ⋆ at a single position \(k\in[0..m]\). Then, due to Lemma B.8, the following equalities are trivial: _A_\[0_..k_\]\[0_..k_\]=_B_\[0_..k_\]\[0_..k_\], _A_\[0_..k_\]\((k..n]=B[0..k][k..m]\), and _A(k..n_\]\((k..n]=B[k..m][k..m]\).

Thus, it follows that \(A^\square[0..k)[0..k)=B^\square[0..k)[0..k)\), \(A^\square[0..k)(k..n)=B^\square[0..k)[k..m)\), and \(A^\square(k..n)(k..n)=B^\square[k..m)[k..m)\). Furthermore, as _A_\[0_..k_\]\[_k_+1_..k_+1\]=_A_\[0_..k_\]\[_k..k_\] due to Lemma B.8, we have that \(A^\square[0..k)[k..k_\]\) consists of zeros. Analogously, as _A_\[_k_+1_..k_+1\]\((k..n]=A[k..k](k..n]\), we have that \(A^\square[k..k](k..n)\) consists of zeros. Moreover, due to Corollary B.9, \(A_{i,j}^\square=0\) for all \(i,j\in[0..n)\) with _i\>j_. The only element of \(A^\square\) that was not yet considered is \(A_{k,k}^\square=A_{k,k+1}+A_{k+1,k}-A_{k,k}-A_{k+1,k+1}=\mathsf{LIS}(\{\star\})+(-2)-0-0=-2\) due to Lemma B.8.

Putting all these facts together, we derive that every core element \((i,j,v)\in\mathrm{core}(B)\) is replaced in core(_A_) by (_i,j,v_) if \(i,j\in[0..k)\), by (_i,j_+1_,v_) if \(i\in[0..k)\) and \(j\in[k..m)\), and by (_i_+1_,j_+1_,v_) if \(i,j\in[k..m)\). Furthermore, one new core element (_k,k,_-2) is added to core(_A_).

<sup>7</sup> As _M<sup>s</sup>_ is anti-Monge, Observation B.10 implies \(\delta(M^s)\le-\delta^\Sigma(M^s)\).

