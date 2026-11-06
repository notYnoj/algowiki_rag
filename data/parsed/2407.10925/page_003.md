year, Kiwi and Soto \[16\] generalized Lueker’s lower- bound algorithm to compute lower bounds for a wider range of alphabets and numbers of strings. Along with some results obtained for \(\gamma_{\sigma,2}\) for various values of \(\sigma>2\) (see \[9, 10, 29, 13\]), these were the state-of-the-art results before our project.

In 2022, Bukh and Cox \[5\] used a variant of Push- TASEP to obtain results related to the LCS problem. They first define \(\Delta(2n)=\mathcal{L}(st,uv)-\mathcal{L}(s,u)-\mathcal{L}(t,v)\) where _s,t,u,v_ are independent, random strings of length _n_ and L(_x,y_) denotes the length of a longest common subsequence of the strings _x_ and _y_. They propose a conjecture asserting the existence of constants _c_<sub>1</sub> and _c_<sub>2</sub> such that \(\mathbb{E}(\Delta(n))\sim c_1\sqrt{n}\) and \(\sqrt{\mathrm{Var}(\Delta(n))}\sim c_2\sqrt{n}\). Bukh and Cox also performed Monte-Carlo simulations with a probabilistic \(\mathcal{O}(n^\frac{3}{2})\) LCS approximation heuristic, which they used to conjecture constants \(c_1\approx\frac{1}{2}\) and \(c_2\approx\frac{1}{4}\) \[5\]. Using their conjecture, they estimate the binary Chvátal-Sankoff constant as 0.8122.

Also of note is work by Kiwi, Loebl, and Matoušek \[17\] in 2005 which proves, via subadditivity arguments, that \(\mathrm{lim}_{\sigma\rightarrow\infty}\gamma_{\sigma,2}\sqrt{\sigma}=2\). Additionally, in 2022, Tiskin \[28\] demonstrated that, by linking \(\gamma\) to the parameters of a specific stochastic particle process, \(\gamma\) is the solution to an explicit (but intractably large) system of polynomial equations with integer coefficients.

## 2.1 The Kiwi-Soto Algorithm

Here we introduce the algorithm of Kiwi and Soto \[16\] for calculating lower bounds on the Chvátal-Sankoff constants, which we used with several modifications to obtain our results. This algorithm is based on the overall process described by Lueker \[20\], but generalized for arbitrary values of \(\sigma\) and _d_. We begin by introducing some notation and summarizing the theory behind the algorithm.

Throughout this paper, we adopt the convention that all vectors are represented in bold and that a numerical value in bold is a vector where every coordinate is that value. Additionally, all vectors contain real num<tbc>

<tbc>bers and are of length \(\sigma^{d\cdot\ell}\), corresponding to the number of possible _d_-tuple of strings where each string has \(\ell\) characters taken from an alphabet of size \(\sigma\). Vector inequalities are evaluated coordinate-wise (e.g., we say \(\mathbf{v}_\mathbf{1}\le\mathbf{v}_\mathbf{2}\) if \(\mathbf{v}_\mathbf{1}[i]\le\mathbf{v}_\mathbf{2}[i]\) for all _i_). We also introduce two new definitions.

Definition 2.1. _For a string a, we define the first character of a to be the **head** of a, denoted as h(a). We define the rest of a to be the **tail** of a, denoted T(a). Note that a=h(a)T(a)._

Following Kiwi and Soto’s notation, let _x_<sub>1</sub>_,...,x<sub>d</sub>_ be a collection of _d_ random strings of length _n_ chosen independently and uniformly from an alphabet \(\Sigma\) of size \(\sigma\), let _a_<sub>1</sub>_,...,a<sub>d</sub>_ be a collection of _d_ finite strings over the same alphabet, let _L_ be the function that returns the length of the LCS of two or more strings, and for any string _s_ let _s_\[_..i_\] denote the substring formed by the first _i_ characters of _s_. Finally, let

\(W_n(a_1,\dots,a_d)=\mathbb{E}\left[\mathrm{max}_{i_1+\cdots+i_d=n}L(a_1x_1[..i_1],\dots,a_dx_d[..i_d])\right]\)

This quantity is the expected length of an LCS of _d_ strings with prefixes _a_<sub>1</sub>_,...,a<sub>d</sub>_, respectively, and _d_ suffixes whose lengths sum to _n_ and whose characters are independently and uniformly chosen from \(\Sigma\) \[16\]. Kiwi and Soto show that, for all _a_<sub>1</sub>_,...,a<sub>d</sub>_,

(2.1) \(\gamma_{\sigma,d}=\mathrm{lim}_{n\rightarrow\infty}\frac{W_{nd}(a_1,\dots,a_d)}{n}.\)

Since this quantity is increasing, by lower-bounding it we can also lower-bound \(\gamma_{\sigma,d}\). This is now our goal.

Fix \(\ell\) in N and let **w<sub>n</sub>** denote the \(\sigma^{\ell d}\)- dimensional vector whose coordinates are the values of _W<sub>nd</sub>(a_<sub>1</sub>_,...,a<sub>d</sub>_) when _a_<sub>1</sub>_,...,a<sub>d</sub>_ each vary over all strings in \(\Sigma^\ell\) (the \(\ell\)-ary Cartesian power of \(\Sigma\)). Kiwi and Soto establish a lower bound for each coordinate of **w<sub>n</sub>** as a function of vectors **w<sub>m</sub>**, with _m\<n_.

\begin{tabular}{cccc}
**Researchers** & **Year** & **Proven Bounds** & **Estimates** \\
Chvátal and Sankoff \[8\] & 1975 & \(0.697844\le\gamma\le 0.866595\) & \(\gamma\approx 0.8082\) \\
Deken \[13\] & 1979 & \(0.7615\le\gamma\le 0.8575\) & \\
Steele \[25\] & 1986 & & \(\gamma=^?\frac{2}{1+\sqrt{2}}\approx 0.8284\) \\
Dančík and Paterson \[9, 29\] & 1995 & \(0.77391\le\gamma\le 0.83763\) & \\
Boutet de Monvel \[12\] & 1999 & & \(\gamma\approx 0.812282\) \\
Baeza-Yates et al. \[3\] & 1999 & & \(\gamma\approx 0.8118\) \\
Bundschuh \[6\] & 2001 & & \(\gamma\approx 0.812653\) \\
Lueker \[20\] & 2009 & \(0.788071\le\gamma\le 0.82628\) & \\
Bukh and Cox \[5\] & 2022 & & \(\gamma\approx 0.8122\) \\
\end{tabular}

1: History of bounds and estimates of the Chvátal-Sankoff constant, \(\gamma\).

