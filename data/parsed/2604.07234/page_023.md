<tbc>and the bound (3.22) holds simultaneously over all \(\left(Y^{(1)},\dots,Y^{(B)}\right)\in\mathcal{N}\mathcal{E}_\mathrm{ind}(Y)\) with probability at least \(1-e^{-\Omega(N)}\). Then we have that

\(T_\mathrm{ind}(X',Y)=^\text{(3.5)}\mathrm{sup}_{\left(Y^{(1)},\dots,Y^{(B)}\right)\in\mathcal{N}\mathcal{E}_\mathrm{ind}(Y)}\frac{1}{B}\sum_{i=1}^BA_\mathrm{loc}\left(X'^{(i)},Y^{(i)}\right)\)<br>
\(\le^\text{(3.22)}T_\mathrm{std}(X',Y)+\frac{\beta^\star(\alpha)}{2}<^\text{(Proposition 3.9)}\frac{1}{2}+\beta^\star(\alpha)\) (3.23)

with probability \(\ge 1-e^{-\Omega(N)}\), producing the desired distinction with Proposition 3.8. The key idea in establishing (3.22) is reducing the extremal behavior of the mapping \(\varphi_Y\) to the sizes of fluctuations from the simple random walk of contiguous substrings of _Y_ . We proceed to formally establish this observation.

**Definition 3.11** (Biased stretch)**.** A _biased stretch_ of \(y\in\{0,1\}^M\) is a contiguous substring of _y_ of length at most \(b^{1+\epsilon}\) which has a contiguous (sub-)substring _z_ of length at most \(b^{1/2+2\epsilon}\) such that \(\Delta(z)\ge b^{1/2-2\epsilon}\). A contiguous substring of _y_ of length at most \(b^{1+\epsilon}\) that is not biased is said to be an _unbiased stretch_.

The importance of Definition 3.11 is illustrated by the following key observation. Let \(y\in\{0,1\}^M\). Fix an induced near-equipartition \(\left(y^{(1)},\dots,y^{(B)}\right)\in\mathcal{N}\mathcal{E}_\mathrm{ind}(y)\). Let \(\left(y^{(i+1)},\dots,y^{(j)}\right)\) denote a sequence of these strings that is transformed into the corresponding sequence of strings \(\left(\tilde{y}^{(i+1)},\dots,\tilde{y}^{(j)}\right)\) when the standardization algorithm is invoked on \(\left(y^{(1)},\dots,y^{(B)}\right)\). It holds for any \(k\in\{i+1,\dots,j\}\) that the symmetric difference of _y_<sup>(_k_)</sup> and \(\tilde{y}^{(k)}\), where we regard _y_<sup>(_k_)</sup> and \(\tilde{y}^{(k)}\) as substrings of _y_ (i.e., we do not compare them bit-by-bit), is exactly given by two contiguous substrings of \(y^{(i+1)}\cdots y^{(j)}\). Specifically, it holds that

\(\bullet\) one contiguous substring is a (possibly empty) _prefix_ \(\mathcal{P}\left(y^{(k)},\tilde{y}^{(k)}\right)\) of either _y_<sup>(_k_)</sup> or \(\tilde{y}^{(k)}\);<tbc>

\(\bullet\) the other contiguous substring is a (possibly empty) _suffix_ \(\mathcal{S}\left(y^{(k)},\tilde{y}^{(k)}\right)\) of either _y_<sup>(_k_)</sup> or \(\tilde{y}^{(k)}\).

<tbc>We may now bound the size of the prefix and the suffix via

(3.24) \(\left|\mathcal{P}\left(y^{(k)},\tilde{y}^{(k)}\right)\right|\vee\left|\mathcal{S}\left(y^{(k)},\tilde{y}^{(k)}\right)\right|\le^\text{(Definition 3.10, Cond. (b))}\delta\alpha b\cdot b^\epsilon=^\text{(3.4)}\alpha\cdot b^{-1/2+\epsilon}\cdot b^{1+\epsilon}\le b^{1/2+2\epsilon}.\)

Now, if we further have that the contiguous substring _y_<sup>(_i_+1)</sup>_...y_<sup>(_j_)</sup> of _y_ is an unbiased stretch, then we may use Definition 3.11 to bound the corresponding difference of local alignment values via

(3.25) \(\left|A_\mathrm{loc}\left(X'^{(k)},y^{(k)}\right)-A_\mathrm{loc}\left(X'^{(k)},\tilde{y}^{(k)}\right)\right|\le\delta\left|\sum_{j=1}^{|y^{(k)}|}\left(2(y^{(k)})_j-1\right)-\sum_{j=1}^{|\tilde{y}^{(k)}|}\left(2(\tilde{y}^{(k)})_j-1\right)\right|\)

\(\le\delta\left(\Delta\left(\mathcal{P}\left(y^{(k)},\tilde{y}^{(k)}\right)\right)+\Delta\left(\mathcal{S}\left(y^{(k)},\tilde{y}^{(k)}\right)\right)\right)\)<br>
\(\le^\text{(3.26)}\delta\left(b^{1/2-2\epsilon}+b^{1/2-2\epsilon}\right)=^\text{(3.4)}2b^{-1/2+\epsilon}\cdot b^{1/2-2\epsilon}=2b^{-\epsilon},\)

where the inequality of (3.25) follows by routine casework and the definition of local alignment. This casework is based on, as per (3.7),

\(\bullet\) whether the local alignment term \(A_\mathrm{loc}\left(X'^{(k)},y^{(k)}\right)\) is 0, \(\delta\Delta\left(y^{(k)}\right)\), or 1;<tbc>

\(\bullet\) whether the local alignment term \(A_\mathrm{loc}\left(X'^{(k)},\tilde{y}^{(k)}\right)\) is 0, \(\delta\Delta\left(\tilde{y}^{(k)}\right)\), or 1.

We note that if exactly one of the two local alignment terms is 0, then the definition of local alignment (3.7) implies that the two sums considered in this initial bound have opposite signs, from which the validity of the bound readily follows. As this final bound can be made arbitrarily small by choosing _b_ large, the identity (3.26) suggests a method via which we may relate induced near-equipartitions NE<sub>ind</sub>(_Y_) with their mappings under the standardization algorithm map \(\varphi_Y\). Our strategy will thus be to show that the

