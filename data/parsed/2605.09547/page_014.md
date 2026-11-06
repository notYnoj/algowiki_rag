Observe that within a single pass over the input, we can count how many entries of \(\widetilde{v}^t\) are rounded to the same value. That is, within a single pass we compute two \(\widetilde{O}(1)\)-dimensional vectors: \(\widetilde{w}^t\) containing the rounded values, and \(\widetilde{k}^t\) where \(\widetilde{k}_i^t\) counts how many entries have been rounded to \(\widetilde{w}_i^t\). We can now solve (13) locally in \(\widetilde{O}(1)\) space, because (i) we know the output vector also has only \(\widetilde{O}(1)\) distinct values, (ii) we can compute the norm of the _m_-dimensional vector _h_ in (13) by using the counting vector (i.e., we know how often each entry will be duplicated).

**Summary, space efficient implementation.** In each iteration of the central path method, we must compute (9). We have implicit access to _x<sup>t</sup>,s<sup>t</sup>_ which allows us to compute implicit access to _g<sup>t</sup>_ and \(\overline{\tau}^t\). We can then construct the spectral sparsifier **H**_<sup>t</sup>_. With these, we can then within a constant number of passes through the stream compute \(\delta_y^{t+1},\delta_c^{t+1},y^{t+1}\). We thus have all information that is required for the implicit representation of _x_<sup>_t_+1</sup>_,s_<sup>_t_+1</sup> so we can proceed with the next iteration. After \(\widetilde{O}(\sqrt{n})\) iterations, our algorithm terminates. Since each iteration takes \(\widetilde{O}(1)\) passes, we take \(\widetilde{O}(\sqrt{n})\) passes in total. The space requirement is \(\widetilde{O}(n^{1.5})\) since we store \(y^t,\delta_c^t,\delta_y^t,\overline{\tau}^t,g^t\) for \(t=1,\dots,\widetilde{O}(\sqrt{n})\).

## 4 Low Space Implementation of IPM

In this section, we summarize the interior point method from \[BLL<sup>+</sup>21\] and show that it can be efficiently implemented in the streaming model. The following result states that, if we have access to an initial point via entry queries, then the interior point method can be implemented in \(\widetilde{O}(n^{1.5})\) space.

**Theorem 4.1.** _Given_ \(\mu^{(\mathrm{target})}\in\mathbb{R}_{>0}\) _and_ \(\epsilon\)_-centered (see Definition 4.4)_ \((x^{(\mathrm{init})},s^{(\mathrm{init})},\mu^{(\mathrm{init})})\) _in im plicit representation (i.e., we can query any entry in time T_<sub>0</sub>_), then in_ \(\widetilde{O}(T_0mn\mathrm{log}^2(\mu^{(\mathrm{init})}/\mu^{(\mathrm{target})}))\) _time,_ \(\widetilde{O}(\sqrt{n}\mathrm{log}(\mu^{(\mathrm{init})}/\mu^{(\mathrm{target})}))\) _passes, and_ \(\widetilde{O}(n^{1.5}\mathrm{log}(\mu^{(\mathrm{init})}/\mu^{(\mathrm{target})}))\) _space, we construct_ \(\epsilon\)_-centered_ \((x,s,\mu^{(\mathrm{target})})\) _in implicit representation with query time_ \(O(T_0+\sqrt{n}\mathrm{log}(\mu^{(\mathrm{init})}/\mu^{(\mathrm{target})}))\)_. The algorithm is randomized and the output is correct w.h.p._

Here, \(\epsilon\)-centered roughly means on the central path that the algorithm follows and is formalized in Definition 4.4.

### 4.1 Overview of Analysis

We will show how to implement the interior point method (Algorithm 1) in low space in the streaming model. The interior point method was previously outlined in Section 3.2, in particular (9) stated the required calculations. To implement this interior point method, we store several objects in memory. We call the collection of these objects that are accessible during the _t_-th iteration of the interior point method the "_t_-1-transcript of the IPM".

**Definition 4.2** (_t_-1-transcript of the IPM)**.** _We call the following collection of values the t_-1_-transcript of the IPM. Here_ \(\mathcal{T}(\cdot)\) _is a function describing the time complexity of a query._

• \(\delta_y^1,\cdots,\delta_y^{t-1}\in\mathbb{R}^n\), \(\delta_c^1,\cdots,\delta_c^{t-1}\in\mathbb{R}^n\), \(y^1,\cdots,y^{t-1}\in\mathbb{R}^n\) , \(\mu^1,\cdots,\mu^{t-1}\in\mathbb{R}_{>0}\)<tbc>

• \(g^1,\cdots,g^{t-1}\in\mathbb{R}^m\) _in implicit representation, i.e. for any_ \(e=(u,v)\), \(1<\ell<t\) _we can query g_<sup>1</sup> _in time T_<sub>0</sub> _and_ \(g_e^\ell\) _in time_ T(_t_-1).<tbc>

• \(x^1,\dots,x^{t-1}\in\mathbb{R}^m\) _in implicit representation, i.e. for any e_=(_u,v),_ 1_\<l\<t, we can query x_<sup>1</sup> _in time T_<sub>0</sub> _and_ \(x_e^l\) _in time_ T(_t_-1).<tbc>

• \(s^1,\dots,s^{t-1}\in\mathbb{R}^m\) _in implicit representation, i.e. for any e_=(_u,v),_ \(1\le l<t\)_, we can query_ \(s_e^l\) _in time O_(1).<tbc>

• \(\tau^1,\cdots,\tau^{t-1}\in\mathbb{R}^m\) _in implicit representation, i.e. for any_ \(e=(u,v)\), \(1\le\ell<t\) _we can query_ \(\overline{\tau}_e^\ell\) _in time_ \(T_x+\widetilde{O}(1)\)_, where T<sub>x</sub> is the time needed to query_ \(x_e^{t-1}\).<br>
In general, the time to query_ \(\overline{\tau}_e^\ell\) _is_ \(\mathcal{T}(t-1)+\widetilde{O}(1)\) _time. However, for many of our use cases when we want to find_ \(\tau_e^t\) _we also want to calculate_ \(x_e^{t-1}\) _itself as well; in that case, we can temporarily save the value of_ \(x_e^{t-1}\) _and expedite query time for_ \(\tau_e^t\) _to just_ \(\widetilde{O}(1)\) _time._

