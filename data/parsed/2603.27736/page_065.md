We return to the construction of _S_. If |_G(S_)|_\<|I|/_(16_s_) we have that \(E_{[r]}(G(S),U(S))\ge|I|/(8r)\) by the correctness argument from before. Moreover, note that for any dyadic intervals \(J=J_1\sqcup J_2\), _E<sub>J</sub>(G,U_) is exactly the average of _E_<sub>_J_<sub>1</sub></sub>(_G,U_) and _E_<sub>_J_<sub>2</sub></sub>(_G,U_). Based on this insight, we binary-search for _j_. We start with _J_=\[_r_\]. While _J_ can be split into \(J=J_1\sqcup J_2\) we update \(J\leftarrow J_1\) if \(E_{J_1}(G(S),U(S))\ge E_J(G(S),U(S))\), and update \(J\leftarrow J_2\) otherwise. Eventually we reach _J_={_j_}, and then

\(\frac{|I|}{8r}\le E_{\{j\}}(G(S),U(S))=\phi(S\cup\{j\})-\phi(S)\)

as claimed.

## Running Time.

We finally analyze the running time of this algorithm. In the preprocessing step we consider the _n_ items and _O(r_log_r_) dyadic intervals; with a little care we can precompute all sizes \(|C_i\cap J|\) and \(|\{x_i\}\cap J|\) in time _O(nr_log_r_).

To analyze the main phase of the algorithm we first bound the size of the sets _S_. Recall that whenever we insert an element _j_ into some set _S_ then the potential \(\phi(S)\) increases by at least |_I|/_(8_r_). Hence, we have that

\(|G(S)|\ge\phi(S)\ge\frac{|S||I|}{8r},\)

and thus after inserting at most _r/s_ elements into _S_ the algorithm halts the construction and proceeds to the next set _S_. That is, \(|S|\le r/s\). In particular, we query at most \(O(|\mathcal{S}|\cdot r/s\cdot logr)\) values _E<sub>J</sub>(G,U_) in total. Each query takes time _O(n_), so the total query time is \(O(|\mathcal{S}|\cdot r/s\cdot logr\cdot n)=O(nrlognlogr)\). All other bookkeeping steps run in negligible time _O(nr_).

