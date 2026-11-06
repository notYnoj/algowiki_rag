All remaining parts and results of this paper are fully due to the author without any assistance from AI, both in terms of idea-generation and writing. This includes (but is not limited to) identifying and formulating all the statements of the lemmas, theorems and corollaries in this paper, discovering the connection between multicolor Ramsey bounds of odd cycles and Conjecture 1.2 as well as the improved bounds for _f_<sub>4</sub>(_k_), discovering the proofs of Theorems 1.3 and 1.5 (as presented in Section 2), coming up with the notion of \(\chi\)-amenability, and discovering the proofs presented in Section 4, with the already mentioned exception that an earlier version of the proof of Lemma 4.5 is due to ChatGPT 5.6 Sol Ultra.

The high-level vision and direction of the research process underlying the presented results is fully due to the author. Furthermore, the author takes full responsibility for the correctness, presentation and originality of the entire manuscript.

## 2 Proof of Theorem 1.5

In this section, we give the definition of the notion of a \(\chi\)_-amenable_ graph parameter, and then proceed to prove our meta-theorem, namely Theorem 1.5, assuming Theorem 1.7.

In the following, a _graph parameter_ for us will simply be a function _f_ assigning to every finite graph _G_ a non-negative real number _f(G_). Roughly speaking, \(\chi\)-amenable parameters are submultiplicative when taking graph unions, and have the property that if they take on a large value on some graph, then we can find a subgraph where the parameter is still relatively large, while the chromatic number of that subgraph is not much larger than its parameter.

**Definition 2.1.** Let _f_ be a graph parameter. We say that _f_ is \(\chi\)_-amenable_ if the following two conditions are satisfied.

1. For every two graphs _G_<sub>1</sub> and _G_<sub>2</sub> on the same vertex-set, we have<tbc>

<tbc>\(f(G_1\cup G_2)\le f(G_1)f(G_2).\)<tbc>

2. There exists an absolute constant \(C\ge 1\) such that every graph _G_ has a subgraph \(G'\subseteq G\) with \(f(G')\ge f(G)/C\) and \(\chi(G')\le Cf(G')\).

With the definition of \(\chi\)-amenability at hand, we are now ready to present the proof of Theorem 1.5, conditional on the Ramsey-theoretic result stated in Theorem 1.7.

_Proof of Theorem 1.5, assuming Theorem 1.7._ In the following, let a \(\chi\)-amenable graph parameter \(f(\cdot)\), an odd number \(g\ge 5\) as well as some \(\varepsilon>0\) be fixed. Clearly, since the statement we are trying to prove becomes stronger the smaller we choose \(\varepsilon\), we may w.l.o.g. assume \(\varepsilon\in(0,1)\) in the following. Let \(C\ge 1\) be a constant for which _f_ satisfies the second condition in the definition of \(\chi\)-amenability. Let \(k\in\mathbb{N}\) be any given, sufficiently large, integer. Let \(p\in\mathbb{N}\) be such that 2_p_+1=_g_-2. Note then that any graph has odd-girth at least _g_ if and only if it is O_<sub>p</sub>_-free.

Now let us consider any graph _G_ such that \(f(G)\ge exp^{\left(\frac{g-3}{2}\right)}(k^{3+\varepsilon})\). Our goal is to prove that _G_ contains a subgraph of odd-girth at least _g_ on which _f_ takes on a value of at least _k_.

