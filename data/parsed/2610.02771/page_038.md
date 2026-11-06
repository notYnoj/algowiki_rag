## D Proofs for Section 4 (Lower bound)

The proof of Theorem 12 establishes an information-theoretic limit by explicitly constructing a "hard pair" of distributions \((\nu_0,\nu_1)\). These distributions are carefully engineered to have a mean gap of exactly \(\Delta\), yet they are geometrically structured so that any single 1-bit measurable set query yields at most \(O(\Delta^2/(J\sigma^2))\) KL information. We then use opposite perturbations to embed this construction into a _K_-arm base instance and alternatives changing one arm at a time, and apply a change-of-measure argument over the predictable \(\sigma\)-algebra of the algorithm’s interaction sequence.

### D.1 Construction of the hard pair

Let _J_ be the largest integer such that

\(2^{J-1}\le\frac{\sigma}{2\Delta}.\)

This definition implies \(\frac{\sigma}{4\Delta}<2^{J-1}\le\frac{\sigma}{2\Delta}\), so taking the base-2 logarithm yields \(J=\lfloor log_2(\frac{\sigma}{\Delta})\rfloor\). Consequently, the number of scales is \(J=\Theta(log\frac{\sigma}{\Delta})\).

For each index _i_=1_,...,J_, we define the geometric support scales _m<sub>i</sub>_ and their corresponding base probability weights _w<sub>i</sub>_:<tbc>

\(m_i:=2^{i-1},w_i:=\frac{1}{Jm_i^2}.\)

<tbc>To create the mean shift, we introduce the probability mass perturbations<tbc>

\(\xi_i:=\frac{\Delta}{2Jm_i\sigma}.\)

<tbc>To ensure that we can subtract these perturbations without producing negative probabilities, we verify that \(\xi_i\le w_i/4\). By definition,<tbc>

\(\xi_i\le\frac{w_i}{4}\Longleftrightarrow\frac{\Delta}{2Jm_i\sigma}\le\frac{1}{4Jm_i^2}\Longleftrightarrow m_i\le\frac{\sigma}{2\Delta}.\)

<tbc>Since \(m_i=2^{i-1}\le 2^{J-1}\le\frac{\sigma}{2\Delta}\) for all \(i\le J\), the condition holds. We now define the baseline distribution \(\nu_0\) and the perturbed distribution \(\nu_1\) over the finite support \(\{0\}\cup\{\pm m_i\sigma\}_{i=1}^J\):

\(\nu_0=\left(1-\sum_{i=1}^Jw_i\right)\delta_0+\sum_{i=1}^J\frac{w_i}{2}\delta_{m_i\sigma}+\sum_{i=1}^J\frac{w_i}{2}\delta_{-m_i\sigma},\)<br>
\(\nu_1=\left(1-\sum_{i=1}^Jw_i\right)\delta_0+\sum_{i=1}^J\left(\frac{w_i}{2}+\xi_i\right)\delta_{m_i\sigma}+\sum_{i=1}^J\left(\frac{w_i}{2}-\xi_i\right)\delta_{-m_i\sigma},\)

where \(\delta_x\) denotes the Dirac measure at _x_. Note that the central mass at 0 is strictly positive because \(\sum_{i=1}^Jw_i=\frac{1}{J}\sum_{i=1}^J4^{-(i-1)}<\frac{1}{J}\frac{4}{3}\le 1\) for \(J\ge 2\).

**Lemma 34** (Moments of the hard pair)**.** _The distributions_ \(\nu_0\) _and_ \(\nu_1\) _satisfy_

\(\mathbb{E}_{\nu_0}[X]=0,\mathbb{E}_{\nu_1}[X]=\Delta,\)

_and have variances bounded by_ \(\sigma^2\).

_Proof._ For \(\nu_0\), symmetry across the origin immediately yields \(\mathbb{E}_{\nu_0}[X]=0\). Its second moment expands to exactly the variance proxy:<tbc>

\(\mathbb{E}_{\nu_0}[X^2]=\sum_{i=1}^Jw_i(m_i\sigma)^2=\sum_{i=1}^J\left(\frac{1}{Jm_i^2}\right)m_i^2\sigma^2=\sum_{i=1}^J\frac{\sigma^2}{J}=\sigma^2.\)

<tbc>For \(\nu_1\), the perturbations \(\xi_i\) are explicitly designed to shift the mean. Because the support points are symmetric, the base weights _w<sub>i</sub>/_2 cancel, leaving only the perturbations:

\(\mathbb{E}_{\nu_1}[X]=\sum_{i=1}^J\left[\left(\frac{w_i}{2}+\xi_i\right)(m_i\sigma)+\left(\frac{w_i}{2}-\xi_i\right)(-m_i\sigma)\right]=\sum_{i=1}^J2\xi_im_i\sigma.\)

