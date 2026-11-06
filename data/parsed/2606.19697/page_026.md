_Proof._ As we read the bits of _v_ from least significant to most, we can compute _v/_2_<sup>w</sup>_ by keeping a running sum that starts at 0 and is updated as follows: at each step, cut it in half and add the next bit. Concretely, let _v_<sub>0</sub>=0 and, for \(1\le\ell\le w\), define \(v_\ell=\frac{1}{2}v_{\ell-1}+b_{\ell-1}\). It can be verified that _v<sub>w</sub>=v/_2_<sup>w</sup>_.

To perform this computation with CoT using soft tokens, we start with _v_<sub>0</sub>=0, represented internally as \(\phi(0)\). Thus we have access to \(\phi(v_0)\) when bit _b_<sub>0</sub> is ready to be serialized. By induction, we assume that when bit \(b_{\ell-1}\) is serialized using a soft token, we also have \(\phi(v_{\ell-1})\) available and can serialize it as part of the same soft token. In the next step, we read both \(\phi(b_{\ell-1})\) and \(\phi(v_{\ell-1})\) from the transcript, and use Prop. 2 to compute \(\phi(v_\ell)\) as the affine transformation \(\phi(\frac{1}{2}v_{\ell-1}+b_{\ell-1})\). After _w_ steps, we thus have \(\phi(v_w)=\phi(v/2^w)\).

Finally, we use an additional _w_ steps of soft token CoT and Prop. 2 to repeatedly (_w_ times) multiply the result by 2, resulting in \(\phi(v)\) as desired.

An _alternative_ construction for this lemma is to first convert the sequence of bits from least-significant- first to most-significant-first using _w_ steps of attention, and then build _v_ iteratively from _v_<sub>_w_-1</sub> to _v_<sub>0</sub> using the recursion \(v_\ell=2v_{\ell+1}+b_{\ell+1}\).

**Lemma 4** (Steps 1-2: loading values)**.** _Suppose the transcript contains store-summary positions, each tagged and whose soft token stores a pair_ \((\phi(a_j),\phi(v_j))\)_. Let_ \(\tau\) _be a transcript position at which a query address a is available as_ \(\phi(a)\) _in the residual stream, and suppose_ \(a\le\tau\)_. Then a log-precision, finite-width continuous-CoT transformer can retrieve_ \(\phi(v_{j^*})\)_, where j_<sup>∗</sup> _is the largest index with a_<sub>_j_<sup>∗</sup></sub>=_a. If no such j_<sup>∗</sup> _exists, it retrieves_ \(\phi(0)\).

_Proof._ Let \(S=\{j<\tau:\text{position}j\text{is a store-summary}\}\), and for each \(j\in S\) let the store-summary’s soft token contain \((\phi(a_j),\phi(v_j))\). In our restricted simulation, store addresses written at time _j_ satisfy \(a_j\le j\), hence (since \(j<\tau\)) we have \(a_j\le\tau\) for all \(j\in S\); together with the hypothesis \(a\le\tau\), this lets us apply Prop. 1 with \(T=\tau\).

Let \(\delta:=\delta_\tau\) be the corresponding gap, i.e., for every \(j\in S\),

\(\langle\phi(a),\phi(a_j)\rangle=\left\{\begin{array}{ c c }
1 & \text{if}a_j=a, \\
\le 1-\delta & \text{if}a_j\neq a.
\end{array}\right.\)

## Retrieve the most recent matching store (candidate).

Because store-summary positions are tagged, we can restrict an attention head to attend only over _S_. We additionally use a fixed-width, strictly increasing _time coordinate t<sub>j</sub>_ available from the positional embedding (e.g., \(t_j:=-\frac{1}{j+1}\in(-1,0)\)), so that \(t_j<t_{j^\prime}\) whenever \(j<j'\).

Consider a (hard) attention head whose score for a store-summary position \(j\in S\) is

\(\text{score}(j):=\langle\phi(a),\phi(a_j)\rangle+\varepsilon t_j,\)

with \(\varepsilon:=\delta/4\). Since \(t_j\in(-1,0)\), we have \(\varepsilon t_j\in(-\varepsilon,0)\).

If _a<sub>j</sub>=a_ then \(\text{score}(j)\ge 1-\varepsilon=1-\delta/4\). If \(a_j\neq a\) then \(\text{score}(j)\le(1-\delta)+0=1-\delta\). Thus every matching store-summary strictly outscores every non-matching store-summary. Among the matching store-summaries, the additive term \(\varepsilon t_j\) strictly breaks ties in favor of larger _j_ (because _t<sub>j</sub>_ is strictly increasing). Therefore, if _j_<sup>∗</sup> exists, the unique maximizer of score(_j_) over \(j\in S\) is exactly \(j^*=max\{j\in S:a_j=a\}\), and hard attention retrieves the associated value payload \(\phi(v_{j^*})\). We also route \(\phi(a_{j^*})\) into designated residual coordinates alongside \(\phi(v_{j^*})\) for a hit-test below; denote the retrieved pair by \((\phi(\tilde{a}),\phi(\tilde{v}))\).

If no such _j_<sup>∗</sup> exists, the same head returns some store-summary payload \((\phi(\tilde{a}),\phi(\tilde{v}))\) with \(\tilde{a}\neq a\).

## Hit-test and default to zero.

To ensure the output is \(\phi(0)\) when no match exists, we perform a final hit-test using Prop. 1. Fix \(c:=1-\delta/2\) (note \(1-\delta<c<1\)). Use a second hard-attention head that compares only: (i) the current position \(\tau\), whose key contains \(\phi(\tilde{a})\) and whose value contains \(\phi(\tilde{v})\), and (ii) a fixed anchor position (e.g. the start token) whose key contributes the constant score _c_ and whose value is \(\phi(0)\). Concretely, arrange the head so that its score for \(\tau\) is \(\langle\phi(a),\phi(\tilde{a})\rangle\) and its score for the anchor is _c_, with all other positions receiving strictly smaller scores.

