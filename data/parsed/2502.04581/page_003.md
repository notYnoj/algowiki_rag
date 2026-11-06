and let \(\psi\) be a quantifier-free linear arithmetic formula over variables in _X_. We consider the model-checking problem for formulas \(\phi\) in the prenex normal form

\(\phi:=Q_1x_1\dots Q_kx_k:\psi,\)

where the quantifiers \(Q_1,\dots,Q_k\in\{\exists,\forall\}\) are arbitrary. Formally, for such a \(\phi\), we define the model checking problem \(\mathsf{FOP}_\mathbb{Z}(\phi)\) as follows<sup>3</sup>

\(\mathsf{FOP}_\mathbb{Z}(\phi):\) (1)

**Input:** Finite sets \(A_1\subseteq\mathbb{Z}^{d_1},\dots,A_k\subseteq\mathbb{Z}^{d_k}\) and \(\hat{t}_1,\dots,\hat{t}_l\in\mathbb{Z}\).

**Problem:** Does \(Q_1x_1\in A_1\dots Q_kx_k\in A_k:\psi[(t_1,\dots,t_l)\backslash(\hat{t}_1,\dots,\hat{t}_l)]\) hold?

We let _n_:=max_<sub>i</sub>_{|_A<sub>i</sub>_|} denote the input size and will assume throughout the paper that all input numbers (i.e., the coordinates of the vectors in _A_<sub>1</sub>_,...,A<sub>k</sub>_ and the values \(\hat{t}_1,\dots,\hat{t}_l\)) are chosen from a polynomially sized universe, i.e., {-_U,...,U_} with \(U\le n^c\) for some _c_. Let FOP<sub>Z</sub> be the union of all \(\mathsf{FOP}_\mathbb{Z}(\phi)\) problems, where \(\phi\) has at least 3 quantifiers.<sup>4</sup> Besides 3-SUM, a variety of interesting problems is contained in FOP<sub>Z</sub>; we discuss a few notable examples below and in the full version.

Frequently, we will distinguish formulas in FOP<sub>Z</sub> using their quantifier structure; e.g., \(\mathsf{FOP}_\mathbb{Z}(\exists\exists\forall)\) describes the class of model checking problems \(\mathsf{FOP}_\mathbb{Z}(\phi)\) where in \(\phi\) we have \(Q_1=Q_2=\exists\) and \(Q_3=\forall\). Furthermore, we let \(\mathsf{FOP}_\mathbb{Z}^k\) be the union of all \(\mathsf{FOP}_\mathbb{Z}(\phi)\) problems, where \(\phi\) consists of precisely _k_ quantifiers, regardless of their quantifier structure. For a quantifier \(Q\in\{\exists,\forall\}\), we write _Q<sup>k</sup>_ for the repetition \(\underbrace{Q\dots Q}_{k\text{times}}\). Finally, we remark that a small subset of FOP<sub>Z</sub> has already been studied by An et al. [7], for a discussion see Section 1.3.

## 1.2 Our Contributions

We seek to determine completeness results for the class FOP<sub>Z</sub>. In particular: What are the largest fragments of this class for which 3-SUM (or more generally, _k_-SUM) is complete? Is there a problem that is complete for the entire class?

Intuitively, we say that a _T<sub>A</sub>(n_)-time solvable problem _A_ is _(fine-grained) complete_ for a _T_<sub>C</sub>(_n_)-time solvable class of problems C, if the existence of an \(O(T_A(n)^{1-\epsilon})\)-time algorithm for _A_ with \(\epsilon>0\) implies that for _all_ problems _C_ in C there exists \(\delta>0\) such that _C_ can be solved in time \(O(T_\mathcal{C}(n)^{1-\delta})\). We extend this notion to completeness of a _family_ of problems, since strictly speaking, any (geometric) problem over Z_<sup>d</sup>_ expressible in linear integer arithmetic corresponds to a family of formulas FOP<sub>Z</sub> (one for each \(d\in\mathbb{N}\)). Formally, consider a family of problems P with an associated time bound _T_<sub>P</sub>(_n_) and a class of problems C with an associated time bound _T_<sub>C</sub>(_n_); usually _T_<sub>P</sub>(_n),T_<sub>C</sub>(_n_) denote the running time of the fastest known algorithm solving all problems in P or C, respectively (often, we omit these time bounds, as they are clear from context).<sup>5</sup> We say that P is _(fine-grained) complete_ for C, if

<sup>3</sup> Below, we use the notation \(\psi[(t_1,\dots,t_l)\backslash(\hat{t}_1,\dots,\hat{t}_l)]\) to denote the substitution of the variables _t_<sub>1</sub>_,...,t<sub>l</sub>_ by \(\hat{t}_1,\dots,\hat{t}_l\) respectively. <sup>4</sup> It is not too difficult to see that all formulas with 2 quantifiers can be model-checked in near-linear time; see the full version for details. <sup>5</sup> Here, we use _family_ and _class_ as a purely semantic and intuitive distinction: A family consists of a small set of similar problems, and a class consists of a large and diverse variety of problems.

