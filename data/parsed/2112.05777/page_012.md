**Theorem 3.** _Parameterized by the number m of hospitals,_ IHR-T _is W\[1\]-hard even if_ \(|\mathcal{P}_1\oplus\mathcal{P}_2|=1\).

_Proof._ We reduce from the COM HR-T problem: Given an instance of HR-T, decide whether there is a stable matching which matches all residents. Boehmer and Heeger \[2021, Proposition 8\] showed that COM HR-T is W\[1\]-hard when parameterized by the number _m_ of hospitals. Given an instance \(\mathcal{I}=(R=\{r_1,\dots,r_n\}\cup H=\{h_1,\dots,h_m\},\mathcal{P})\) of COM HR-T, let _N_ be an arbitrary stable matching in I (we assume that _N_ does not match all residents, as we otherwise know that I is a yes-instance).

To construct an instance of IHR-T, we first add _R_ to the set of residents and _H_ to the set of hospital. Subsequently, we add a penalizing component consisting of two hospitals \(h_1^\star\) and \(h_2^\star\), both with upper quota one, and two hospitals \(\tilde{h}_1\) and \(\tilde{h}_2\) both with upper quota _n_+1. We additionally add a resident _r<sup>⋆</sup>_ and two sets of _n_+1 residents \(\tilde{r}_1,\dots,\tilde{r}_{n+1}\) and \(\tilde{r}'_1,\dots,\tilde{r}'_{n+1}\).

Turning to the agents’ preferences in P<sub>1</sub>, all agents from \(R\cup H\) have their preferences from P, except that, for each resident, _h<sup>⋆</sup>_ is added at the end of her preferences. The preferences of the agents from the penalizing component are:

\(h_1^\star:r_1\succ\cdots\succ r_n\succ r^\star;r^\star:h_1^\star\succ h_2^\star\succ\tilde{h}_1;h_2^\star:r^\star;\)<br>
\(\tilde{h}_1:r^\star\succ\tilde{r}'_1\succ\cdots\succ\tilde{r}'_{n+1}\succ\tilde{r}_1\succ\cdots\succ\tilde{r}_{n+1};\)<br>
\(\tilde{h}_2:\tilde{r}_1\succ\cdots\succ\tilde{r}_{n+1}\succ\tilde{r}'_1\succ\cdots\succ\tilde{r}'_{n+1};\)<br>
\(\tilde{r}_i:\tilde{h}_1\succ\tilde{h}_2;\tilde{r}'_i:\tilde{h}_2\succ\tilde{h}_1,i\in[n+1].\)

Profile P<sub>2</sub> equals P<sub>1</sub> except that we swap \(h_2^\star\) and \(\tilde{h}_1\) in the preferences of _r<sup>⋆</sup>_. Let _i<sup>⋆</sup>_ be the smallest index of a resident unmatched in _N_. We set _k_:=2(_n_+1) and

\(M_1:=N\cup\{\{r_{i^\star},h_1^\star\},\{r^\star,h_2^\star\}\}\cup\{\{\tilde{r}_i,\tilde{h}_1\},\{\tilde{r}'_i,\tilde{h}_2\}|i\in[n+1]\}.\)

It is easy to see that the matching _M_<sub>1</sub> is stable. There is clearly no blocking pair involving an original agent, all residents \(\tilde{r}_i\) and \(\tilde{r}'_i\) are matched to their top choice, and _r<sup>⋆</sup>_ does not form a blocking pair with \(h_1^\star\) as \(h_1^\star\) is matched better.

Note that the construction of the instance of IHR-T can be done in polynomial time since the matching _N_ can be computed in linear time by the Gale-Shapley algorithm.

It remains to prove that the given instance I of COM HRT is a yes-instance if and only if the constructed instance \(\mathcal{I}'\) of IHR-T is a yes-instance.

\((\Rightarrow):\) Assume that _N<sup>⋆</sup>_ is a perfect stable matching in I. Let _M_<sub>2</sub> be the following matching:

\(M_2=N^\star\cup\{\{r^\star,h_1^\star\}\}\cup\{\{\tilde{r}_i,\tilde{h}_1\},\{\tilde{r}'_i,\tilde{h}_2\}|i\in[n+1]\}.\)

Matching _M_<sub>2</sub> is stable in P<sub>2</sub>, as _N<sup>⋆</sup>_ is stable in P and all residents from the penalizing component are matched to their top choice. Furthermore, it holds that \(|M_1\triangle M_2|=|N^\star\triangle N|+|\{\{r_{i^\star},h_1^\star\},\{r^\star,h_2^\star\},\{r^\star,h_1^\star\}|\}\le 2(n+1)\).

\((\Leftarrow):\) Let _M_<sub>2</sub> be a solution to the constructed IHR-T instance \(\mathcal{I}'\). We claim that it needs to hold that \(\{r^\star,h_1^\star\}\in M_2\). For the sake of contradiction, assume that this is not the case. Then, as _r<sup>⋆</sup>_ is the top choice of \(\tilde{h}_1\), which is the second-most preferred hospital of _r<sup>⋆</sup>_ (after \(h_1^\star\)), it needs to hold that \(\{r^\star,\tilde{h}_1\}\in M_2\). However, as both \(\tilde{h}_1\) and \(\tilde{h}_2\) have upper quota _n_+1, this implies that one resident among the residents \(\tilde{r}_1,\dots,\tilde{r}_{n+1}\) and \(\tilde{r}'_1,\dots,\tilde{r}'_{n+1}\) needs to be unmatched in _M_<sub>2</sub>. This needs to be resident \(\tilde{r}'_{n+1}\), as all other of these residents appear in one of the first _n_+1 positions in the preferences of either \(\tilde{h}_1\) or \(\tilde{h}_2\). For \(\tilde{r}'_{n+1}\) to be unmatched and not to form a blocking pair with \(\tilde{h}_1\) or \(\tilde{h}_2\), it needs to hold that for all \(i\in[n]\), \(\{\tilde{r}'_i,\tilde{h}_1\}\in M_2\) and thereby also that for all \(i\in[n+1]\), \(\{\tilde{r}_i,\tilde{h}_2\}\in M_2\). This in turn implies that \(|M_1\triangle M_2|\ge|\{\{\tilde{r}_i,\tilde{h}_1\},\{\tilde{r}'_i,\tilde{h}_2\}|i\in[n+1]\}\cup\{\{\tilde{r}'_i,\tilde{h}_1\},\{\tilde{r}_i,\tilde{h}_2\}|i\in[n]\}\cup\{\{r^\star,h_2^\star\},\{r^\star,\tilde{h}_1\},\{\tilde{r}_{n+1},\tilde{h}_2\}\}|>2(n+1)\), a contradiction. Thus, it needs to hold that \(\{r^\star,h_1^\star\}\in M_2\). This implies that all original residents need to be matched to original hospitals, as an unmatched original resident would form a blocking pair together with \(h_1^\star\). Consequently, matching _M_<sub>2</sub> restricted to original agents induces a perfect stable matching in the given COM HRT instance I.

