<tbc>matchings are stable: _M_<sub>1</sub>={_e_<sub>2</sub>_,e_<sub>4</sub>_,f_<sub>2</sub>_,f_<sub>5</sub>}_,M_<sub>2</sub>={_f_<sub>2</sub>_,f_<sub>4</sub>_,e_<sub>2</sub>_,e_<sub>5</sub>}_,M_<sub>3</sub>={_g,e_<sub>3</sub>_,f_<sub>2</sub>_,f_<sub>5</sub>}_,M_<sub>4</sub>={_h,f_<sub>3</sub>_,e_<sub>2</sub>_,e_<sub>5</sub>}.

Consider vertex _v_, which must be matched in any stable matching _M_. If \(f_1\in M\) or \(g\in M\) (resp., \(e_1\in M\) or \(h\in M\)), then \(e_3\in M\) (resp., \(f_3\in M\)) too since otherwise _e_<sub>4</sub> (resp., _f_<sub>4</sub>) blocks _M_, so \(M\cup M_2\) (resp., \(M\cup M_1\)) contains a desired alternating path _e_<sub>2</sub>_e_<sub>3</sub>_e_<sub>5</sub> (resp., _f_<sub>2</sub>_f_<sub>3</sub>_f_<sub>5</sub>). If \(f_4\in M\) (resp., \(e_4\in M\)), then \(M\cup M_3\) (resp., \(M\cup M_4\)) contains a desired alternating path _gf_<sub>4</sub>_f_<sub>5</sub> (resp., _he_<sub>4</sub>_e_<sub>5</sub>).

The second observation is about the integrality gap. Observe that max-smpo on _G_=(_U,W;E_) can be modeled with the following integer programming problem (IP) with variables \(\{p_e\}_{e\in E}\). Since we allow parallel edges, to distinguish edges connecting the same vertices, say _u_ and _w_, we use a notation (_u,w)<sub>i</sub>_ where distinct edges have distinct subscripts _i_:

\(\mathrm{max}\sum_{e\in E}p_e\)<br>
\(\mathrm{s}.\mathrm{t}.\sum_{e\in\delta_G(v)}p_e\le 1\forall v\in U\cup W\) (1)

\(\sum_{e^\prime\in\delta_G(u):e\unknown\unknown_ue^\prime} p_{e^\prime}+\sum_{e^\prime\in\delta_G(w):e\unknown\unknown_we^\prime} p_{e^\prime}-\sum_{e^\prime\in\delta_G(u)\cap\delta_G(w):e\unknown\unknown_ue^\prime,e\unknown\unknown_we^\prime} p_{e^\prime}\ge 1\forall e=(u,w)_i\in E\) (2)

\(p_e\in\{0,1\}\forall e\in E\)

In the special case of max-smti, that is, the case with weak orders, it is known that the integrality gap of the linear programming (LP) relaxation of this IP is at least 1.5-_o_(1) \[24\]. This fact is sometimes considered to indicate a potential barrier to improving the approximation ratio 1.5.

We show that this integrality gap can be 2 for the general max-smpo while it is at most 1.5 even for interval orders. First, we give an example showing the former claim.

**Example 14.** Consider an instance of max-smpo with vertices \(u,u',w,w'\) and edges \(e_i=(u,w')_i\) for \(i\in[2]\), \(f_i=(u',w)_i\) for \(i\in[2]\), and _g<sub>j</sub>_=(_u,w)<sub>j</sub>_ for \(j\in[4]\). The partial orders of _u_ and _w_ are given by \((g_1\succ_ue_1)\wedge(g_2\succ_ue_1)\wedge(g_3\succ_ue_2)\wedge(g_4\succ_ue_2)\) and \((g_1\succ_wf_1)\wedge(g_2\succ_wf_2)\wedge(g_3\succ_wf_1)\wedge(g_4\succ_wf_2)\). The orders of \(u'\) and \(w'\) are defined arbitrarily.

In this instance, _p_<sub>_e_<sub>1</sub></sub>=_p_<sub>_e_<sub>2</sub></sub>=_p_<sub>_f_<sub>1</sub></sub>=_p_<sub>_f_<sub>2</sub></sub>=0.5, _p_<sub>_g<sub>j</sub>_</sub>=0 (\(j\in[4]\)) is a solution to the LP relaxation of the above IP, but any stable matching must have size one (it must contain one of the _g<sub>j</sub>_ edges). Thus, the integrality gap is 2.

We next show that, in contrast to this example, the integrality gap is at most 1.5 for interval orders. The proof depends on the correctness of our 1.5-approximation algorithm shown in Section 3.

**Theorem 15.** _For a max-smpo instance consisting of G_=(_U,W;E_) _and_ \(\{\succ_v\}_{v\in U\cup W}\)_, if_ \(\succ_v\) _are interval orders, then the output of our algorithm_ 1.5_-approximates the LP optimum of the relaxation of the above IP. In particular, the integrality gap of the IP is at most_ 1.5.

_Proof._ Since max-smpo with interval orders is a special case of max-kernel-po with interval orders (recall the remark just after Theorem 1), we can apply our algorithm in Section 3 to the given instance. Let \(M^*\subseteq\cup_{e\in E}\{x_e,y_e,z_e\}\) be the stable matching in the corresponding modified instance and _M_ be its projection to _E_, i.e., the algorithm’s output. Let \(\{p_e^*\}_{e\in E}\in[0,1]^E\) be an optimal solution to the LP. We show \(\sum_{e\in E}p_E^*\le\frac{3}{2}|M|\), which completes the proof.

