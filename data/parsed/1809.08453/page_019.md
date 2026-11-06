### 5 The GGI Stable Marriage Problem with a Bounded Number of Non-zero Weights

In this section, we provide an algorithm whose complexity is _O_(2_<sup>K</sup>n_<sup>2_K_+4</sup>) where \(K=max\{i:\lambda_i>0\}\). Hence, the complexity is polynomial time if _K_ is assumed to be a constant, where _K_ is the number of non-zero weights in the GGI operator. In the parametrized complexity terminology \[Niedermeier, 2006\], this means that the GGI stable marriage problem belongs to class XP for parameter _K_.

We adopt a brute-force approach to solve the problem in _O_(2_<sup>K</sup>n_<sup>2_K_+4</sup>). Let

\(\mathbf{t}(\mathbf{x})=((d(m_1,\mathbf{x}),m_1,\mu_\mathbf{x}(m_1)),\dots,(d(m_n,\mathbf{x}),m_n,\mu_\mathbf{x}(m_n)),\)<br>
\((d(w_1,\mathbf{x}),w_1,\mu_\mathbf{x}(w_1)),\dots,(d(w_n,\mathbf{x}),w_n,\mu_\mathbf{x}(w_n))\)

denote the vectors of triples \((d(a_i,\mathbf{x}),a_i,\mu_\mathbf{x}(a_i))\) induced by stable marriage **x**, where _d(a<sub>i</sub>,_**x**) is the dissatisfaction of agent _a<sub>i</sub>_ when matched with \(\mu_\mathbf{x}(a_i)\). We denote by \(T^\downarrow(\mathbf{x})\) the set of vectors \(\mathbf{t}^\downarrow(\mathbf{x})\) that can be obtained from **t**(**x**) by sorting the triples in decreasing or der of dissatisfactions. The projection of a vector \(\mathbf{t}^\downarrow(\mathbf{x})\in T^\downarrow(\mathbf{x})\) on the _K_ first components is denoted by \(\mathbf{t}_K^\downarrow(\mathbf{x})\). We denote by \(T_K^\downarrow(\mathbf{x})\) the set \(\{\mathbf{t}_K^\downarrow(\mathbf{x}):\mathbf{t}^\downarrow(\mathbf{x})\in T^\downarrow(\mathbf{x})\}\).

For instance, assume that **t**(**x**)=((1_,m_<sub>1</sub>_,w_<sub>2</sub>),(2_,m_<sub>2</sub>_,w_<sub>1</sub>),(2_,w_<sub>1</sub>_,m_<sub>2</sub>),(1_,w_<sub>2</sub>_,m_<sub>1</sub>)). Then the set \(T^\downarrow(\mathbf{x})\) is

\(\{((2,m_2,w_1),(2,w_1,m_2),(1,m_1,w_2),(1,w_2,m_1)),\)<br>
\(((2,w_1,m_2),(2,m_2,w_1),(1,m_1,w_2),(1,w_2,m_1)),\)<br>
\(((2,m_2,w_1),(2,w_1,m_2),(1,w_2,m_1),(1,m_1,w_2))\)<br>
\(((2,w_1,m_2),(2,m_2,w_1),(1,w_2,m_1),(1,m_1,w_2))\}\)

and the set \(T_2^\downarrow(\mathbf{x})\) is {((2_,m_<sub>2</sub>_,w_<sub>1</sub>),(2_,w_<sub>1</sub>_,m_<sub>2</sub>)),((2_,w_<sub>1</sub>_,m_<sub>2</sub>),(2_,m_<sub>2</sub>_,w_<sub>1</sub>))}.

The idea is to enumerate all vectors in \(T_K^\downarrow=\cup_{\mathbf{x}\in\mathcal{X}}T_K^\downarrow(\mathbf{x})\) without redundancy. The polynomiality of the approach follows from the fact that \(|T_K^\downarrow|\le(2n^2)^K\) because the num ber of distinct triples is upper bounded by 2_n_<sup>2</sup>. Note that we have:

\(min_{\mathbf{x}\in\mathcal{X}}\mathtt{GGI}_\unknown(\mathbf{d}(\mathbf{x}))=min_{\mathbf{t}\in\mathcal{T}_K^\downarrow}\mathtt{GGI}_\unknown(\mathbf{t})\)

because \(\lambda_i=0\) for all _i\>K_, where, by abuse of notation, we denote by \(\mathtt{GGI}_\unknown(\mathbf{t})\) the value of the GGI operator applied to the vector of dissatisfactions obtained from **t**<sup>1</sup>. Hence identifying an optimal GGI stable marriage will be performed by finding a vector \(\mathbf{t}\in T_K^\downarrow\) minimizing the GGI operator and computing a corresponding stable marriage.

**Example 9** _Coming back to the instance of Example 1, assume that K_=2 _and that the disutility function is defined by d(i_)=_i. Then, our enumeration algorithm would produce the following set_ \(\mathcal{T}_2^\downarrow\):

<sup>1</sup> Note that vector \(\mathbf{t}\in T_K^\downarrow\) is incomplete as it only has _K_ components, but it is sufficient to apply the GGI operator because \(\lambda_i=0\) for all _i\>K_.

