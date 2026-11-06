**Algorithm 2** Our Streaming Algorithm

procedure ShortStep(_t_-transcript Trans_<sup>t</sup>_)<br>
   Construct implicit representation of \(\overline{\tau}\approx_\epsilon\tau(x^t)\) via Theorem 4.8.<br>
  // This takes \(\widetilde{O}(1)\) pass, \(\widetilde{O}(n)\) space, \(\widetilde{O}(m(t+T_0))\) time.<br>
   Construct implicit representation of \(g=-\gamma\nabla\Psi(\overline{v})^{\mathsf{b}(\overline{\tau})}\) via Theorem 4.11.<br>
  // This takes 1 pass, \(\widetilde{O}(1)\) space, \(\widetilde{O}(m(t+T_0))\) time.<br>
   Construct spectral sparsifier \(\mathbf{H}\approx_\gamma\mathbf{A}^\top\overline{\mathbf{T}^{-1}}\Phi''(x)^{-1}\mathbf{A}\) using Lemma 2.1.<br>
  // This takes 1 pass, \(\widetilde{O}(n)\) space, \(\widetilde{O}(m(t+T_0))\) time.<br>
   Compute \(\mathbf{A}^\top\Phi''(x)^{-\frac{1}{2}}g\) (using implicit representation of _g_, Theorem 4.11)<br>
  // Takes 1 pass, _O(n_) space, \(\widetilde{O}(m(t+T_0))\) time.<br>
   Store \(\delta_y^{t+1}\leftarrow\mathbf{H}^{-1}\mathbf{A}^\top\Phi''(x)^{-\frac{1}{2}}g\) via Laplacian solver on **H**, in \(\widetilde{O}(n)\) time, \(\widetilde{O}(n)\) space.<br>
   Store \(y^{t+1}\leftarrow y^t+\delta_y^{t+1}\) in _O(n_) space.<br>
   Store \(\delta_c^{t+1}\leftarrow\mathbf{H}^{-1}(\mathbf{A}^\top x^t-b)\) by computing \((\mathbf{A}^\top x^t-b)\) (using implicit representation of _x<sup>t</sup>_), then calling Laplacian solver. Takes 1 pass, _O(n_) space, \(\widetilde{O}(m(t+T_0))\) time.<br>
   Store (_t_+1)-transcript Trans<sup>_t_+1</sup>=\((\text{Trans}^t,\mathbf{H},\delta_y,\delta_c,y,\mu,\overline{\tau},g)\). Increases size of transcript by _O(n_).<br>
  // For \(\delta_x^{t+1}=\Phi''(x)^{-\frac{1}{2}}g-\overline{\mathbf{T}^{-1}}\Phi''(x)^{-1}\mathbf{A}(\delta_y^{t+1}+\delta_c^{t+1})\), and \(\delta_s^{t+1}=\mu\mathbf{A}\delta_y^{t+1}\),<br>
  // we have access to \(x^{t+1}\leftarrow x+\delta_x^{t+1}\) and \(s^{t+1}\leftarrow s+\delta_s^{t+1}\) via Lemmas 4.15 and 4.14.<br>
   return (_t_+1)-transcript Trans<sup>_t_+1</sup><br>
end procedure

**Lemma 4.18.** _Given t_-1_-transcript of the IPM, we can compute w.h.p the t-transcript in_ \(\widetilde{O}(1)\) _passes,_ \(\widetilde{O}(m(t+T_0))\) _time, and_ \(\widetilde{O}(n)\) _additional space._

_Proof._ Our statement follows directly from the above theorems by adding the number of passes, space, and time complexity in each line of the algorithm.

We can now prove the following:

**Theorem 4.1.** _Given_ \(\mu^{(\text{target})}\in\mathbb{R}_{>0}\) _and_ \(\epsilon\)_-centered (see Definition 4.4)_ \((x^{(\text{init})},s^{(\text{init})},\mu^{(\text{init})})\) _in im plicit representation (i.e., we can query any entry in time T_<sub>0</sub>_), then in_ \(\widetilde{O}(T_0mnlog^2(\mu^{(\text{init})}/\mu^{(\text{target})}))\) _time,_ \(\widetilde{O}(\sqrt{n}log(\mu^{(\text{init})}/\mu^{(\text{target})}))\) _passes, and_ \(\widetilde{O}(n^{1.5}log(\mu^{(\text{init})}/\mu^{(\text{target})}))\) _space, we construct_ \(\epsilon\)_-centered_ \((x,s,\mu^{(\text{target})})\) _in implicit representation with query time_ \(O(T_0+\sqrt{n}log(\mu^{(\text{init})}/\mu^{(\text{target})}))\)_. The algorithm is randomized and the output is correct w.h.p._

_Proof._ By Lemma 4.7, the algorithm runs for \(O(\sqrt{n}log(\mu^{(\text{init})}/\mu^{(\text{target})}))\) iterations.<br>
We use Lemma 4.18. We have \(\widetilde{O}(1)\) passes per iteration, so \(O(\sqrt{n}log(\mu^{(\text{init})}/\mu^{(\text{target})}))\) total.<br>
We can upper bound _t_ by \(\sqrt{n}log(\mu^{(\text{target})}/\mu^{(\text{init})})\) to get \(\widetilde{O}(m(\sqrt{n}log(\mu^{(\text{init})}/\mu^{(\text{target})})+T_0)\) per iteration, or \(\widetilde{O}(T_0mnlog^2(\mu^{(\text{init})}/\mu^{(\text{target})}))\) total across all iterations.<br>
Finally, we also use \(\widetilde{O}(n)\) additional space per iteration, for a total of \(\widetilde{O}(n^{1.5}log(\mu^{(\text{init})}/\mu^{(\text{target})}))\) space.<br>
By Proposition 4.17, the query time is \(O(T_0+\sqrt{n}log(\mu^{(\text{target})}/\mu^{(\text{init})}))\).

We can also extend this to the 2-party communication setting.

**Theorem 4.19.** _Consider the 2-party model, where both parties have the same_ \(\mu^{(\text{target})}\in\mathbb{R}_{>0}\) _and_ \(\epsilon\)_- centered (see Definition 4.4)_ \((x^{(\text{init})},s^{(\text{init})},\mu^{(\text{init})})\) _in implicit representation (i.e., a party can query any entry_ \(x_e^{(\text{init})}\) _or_ \(s_e^{(\text{init})}\)_, provided they know the corresponding edge e and its cost and capacity). Then, with_ \(\widetilde{O}(n^{1.5}log(\mu^{(\text{init})}/\mu^{(\text{target})}))\) _bits of communication, both parties jointly construct the same_ \(\epsilon\)_-centered_ \((x,s,\mu^{(\text{target})})\) _in implicit representation. The communication protocol is randomized and the output is correct w.h.p._

_Proof._ We show the claim iteratively. Suppose both parties know the transcript up to iteration _t_. We claim that with only \(\widetilde{O}(n)\) bits of communication, they are able to jointly compute the transcript for iteration<tbc>

