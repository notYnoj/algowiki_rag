work register to 0, as required for clean output, apply for each \(i\in\{1,\dots,n\}\) in turn the reversible decrement \((Z,s_i)\mapsto(Z-s_i,s_i)\), the inverse of the increment above, with the retained sorted key bit _s<sub>i</sub>_ as the control. Since _Z_ starts at |_s_|<sub>1</sub>, _Z_ ends at 0. This uses _n_ decrements of _O_(log_n_) gates and depth per bit, i.e., _O(n_log_n_) gates and depth total.

The erasure portion uses \(\sum_{i=1}^n(i+1)=\Theta(n^2)\) controlled erasure gates, one for each possible numerator _z<sub>i</sub>_ at each stage _i_; the forward and reverse demultiplexers use _O(n_<sup>2</sup>) additional reversible gates in total. Together with the reversible sorting computation, the total gate complexity is _O(t(n)m_) (for the sorting network) plus _O(n_<sup>2</sup>), i.e., _O(t(n)m+n_<sup>2</sup>). The depth is _O(d(n_)log_m+n_log_n_) since we have _n_ layers of single-bit erasure, one for each _b<sub>i</sub>_, and each layer requires _O_(log_n_) depth as justified above (plus the _O(d(n_)log_m_) depth of the reversible sorting computation.) The circuit uses _O(t(n_)+_nm_) wires beyond the _n(m_+1) input wires: _n(m_+1) for the register that receives (_s,W_); _t(n_) for the garbage bits _G_; _O(nm_) for the copy trees of the comparators in one layer of _C_, which are returned to 0 after each layer and reused by the next; and _O(n_) for the register _Z_, the demultiplexers, and the pairs of wires feeding the controlled erasure gates, which are likewise returned to 0 after each stage and reused by the next.

Now we show that this gives us zero circuit entropy production. Overall, we are mapping (_b,V_)∼D to _C(b,V_)=(_s,W_).

Since _C_ is a deterministic function, we have that \(\mathcal{S}((b,V))-\mathcal{S}(C((b,V)))=\mathcal{S}((b,V)|(s,W))=\mathcal{S}(b|(s,W))\). Since D is exchangeable, _W_ is irrelevant to the conditional probability distribution,<sup>41</sup> so this equals \(\mathcal{S}(b|s)=\mathcal{S}(b||b|_1)=\sum_{k\le n}\mathrm{Pr}\left[|b|_1=k\right]\cdot\mathcal{S}(b||b|_1=k)\). Since D is exchangeable, each _b_ with a fixed value of |_b_|<sub>1</sub> is equally likely, so \(\mathcal{S}(b||b|_1=k)=\mathrm{log}\genfrac(){pt}{2}{n}{k}=\mathrm{log}\frac{n!}{k!(n-k)!}\) and the total drop in entropy is:<tbc>

\(\sum_{k\le n}\mathrm{Pr}[|b|_1=k]\mathrm{log}\frac{n!}{k!(n-k)!}.\) (11)

<tbc>We will now show that our choices of heat function _Q<sub>i</sub>_ for erasing each bit of any fixed _b_ with |_b_|<sub>1</sub>=_k_ result in the circuit releasing exactly this much heat in expectation. We now fix _k_ and any _b_ such that |_b_|<sub>1</sub>=_k_. As a reminder, we are picking the optimal heat function per Lemma 3.1 for erasing bit _b<sub>i</sub>_ based on the probability that _b<sub>i</sub>_ is 1 is \(|b_{\le i}|_1/i\). This gives us the heat function<tbc>

\(Q_i(b_i,|b_{\le i}|_0,|b_{\le i}|_1)=\left\{\begin{array}{ c c }
\mathrm{log}(i/|b_{\le i}|_0) & b_i=0 \\
\mathrm{log}(i/|b_{\le i}|_1) & b_i=1
\end{array}\right.\)

<tbc>for erasing the _i_’th bit of _b_. Let _I=i_<sub>1</sub>_,...,i_<sub>_n-k_</sub> denote the indices of _b_ where \(b_{i_\ell}=0\) and _J=j_<sub>1</sub>_,...,j<sub>k</sub>_ denote the indices of _b_ where \(b_{j_\ell}=1\). Then the expected heat released on input _b_ is exactly<tbc>

\(\sum_{i_\ell\in I}\mathrm{log}(i_\ell/\ell)+\sum_{j_\ell\in J}\mathrm{log}(j_\ell/\ell)=\sum_{\ell\in[n]}\mathrm{log}(\ell)+\sum_{i\in[n-k]}\mathrm{log}(1/i)+\sum_{j\in[k]}\mathrm{log}(1/j)=\mathrm{log}\frac{n!}{k!(n-k)!}.\)

demultiplexer used to route the bits to erase, so there is no asymptotic benefit in optimizing the increment depth. In fact, given our setup, there is no way to demultiplex in _o_(log_n_) depth, since we need a single value _b<sub>i</sub>_ to reach one of \(\Omega(n)\) different wires, but due to _O_(1) size gates, each layer only enables it to reach a constant multiple more wires than the previous. This does not rule out a more sophisticated approach that can achieve _O_(1) amortized depth per bit erasure, using some sort of "pipelining" for instance, or perhaps some way to erase \(\omega(1)\) bits in parallel. <sup>41</sup>The distribution over payloads must be independent of their input index and _b_ is a permutation of _s_.

