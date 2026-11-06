## 3.1 Sparsification for constant \(\lambda\) (Step 1 of Theorem 2.2)

Fix an arbitrary LCS for every pair of windows and refer to that as opt_<sub>i,j</sub>_ for two windows _w<sub>i</sub>_ and _w<sub>j</sub>_. Note that we do not explicitly compute opt_<sub>i,j</sub>_ in our algorithm. Let us for simplicity, think of each opt_<sub>i,j</sub>_ as a matching between the characters of the two windows. Also, denote by \(\big(\mathsf{opt}_{i,a}\cap\mathsf{opt}_{a,b}\cap\mathsf{opt}_{b,j}\big)\) a solution which is constructed for windows _w<sub>i</sub>_ and _w<sub>j</sub>_ by taking pairs of characters (_x,y_) such that:

\((x,y)\in\big(\mathsf{opt}_{i,a}\cap\mathsf{opt}_{a,b}\cap\mathsf{opt}_{b,j}\big)\Longleftrightarrow\exists x',y'\text{such that}\)<br>
\((x,y')\in\mathsf{opt}_{i,a}\text{and}\)<br>
\((y',x')\in\mathsf{opt}_{a,b}\text{and}\)<br>
\((x',y)\in\mathsf{opt}_{b,j}.\)

Let \(\big\|\big(\mathsf{opt}_{i,a}\cap\mathsf{opt}_{a,b}\cap\mathsf{opt}_{b,j}\big)\big\|=\frac{\big|\big(\mathsf{opt}_{i,a}\cap\mathsf{opt}_{a,b}\cap\mathsf{opt}_{b,j}\big)\big|}{\sqrt{|w_i||w_j|}}\) .

Our analysis is based on a notion which roughly reflects "in how many ways a desirable solution can be made for a pair of windows (_w<sub>i</sub>,w<sub>j</sub>_) by taking the intersection of the LCS for other pairs". Below, we provide a definition for this notion.

**Definition 3.1** (\((\epsilon,\lambda)\)-constructive)**.** Let \(0<\epsilon,\lambda<1\) be fixed values. We call a tuple \(\langle w_i,w_a,w_b,w_j\rangle(w_i\neq w_a\neq w_b\neq w_j)\) an \((\epsilon,\lambda)\)_-constructive_ tuple, if

\(\big\|\big(\mathsf{opt}_{i,a}\cap\mathsf{opt}_{a,b}\cap\mathsf{opt}_{b,j}\big)\big\|\ge(1-\epsilon)\lambda^3.\)

The advantage of a constructive tuple is that if opt_<sub>i,a</sub>,_opt_<sub>a,b</sub>_, and opt_<sub>b,j</sub>_ are provided, one can construct a desirable solution for opt_<sub>i,j</sub>_ in linear time by taking the intersection of the given matchings.

We parametrize our algorithm by a value \(0<\gamma<1\) to be set later. One may optimize the runtime of the algorithm by setting the value of \(\gamma\) in terms of the number of windows and the length of the windows. We first sample a set _S_ of \(O(k^\gamma logk)\) windows. Next, we compute opt_<sub>i,j</sub>_ of every window \(w_i\in S\) and every other window _w<sub>j</sub>_ (not necessarily in _S_). Finally, we find all tuples \(\langle w_i,w_a,w_b,w_j\rangle\) such that \(w_a,w_b\in S\) and they satisfy the following property:

\(\big\|\big(\mathsf{opt}_{i,a}\cap\mathsf{opt}_{a,b}\cap\mathsf{opt}_{b,j}\big)\big\|\ge(1-\epsilon)\lambda^3.\)

Recall that we call such tuples \((\epsilon,\lambda)\)_-constructive_ and update \(\widehat{\mathsf{O}}_{\lambda^2}[i][j],\widehat{\mathsf{O}}_{\lambda^2}[j][i]\leftarrow 1\) accordingly. This is shown in Algorithm 1.

The running time of our algorithm is equal to \(O(k|S|\mathsf{w}_\mathsf{max}^2+k^2|S|^2\mathsf{w}_\mathsf{max})\). The rest of this section is dedicated to proving that what remains in the lcs-graph is sparse; this is formalized in Lemma 3.4.

**Definition 3.2** (\(\mathsf{NG}_\lambda\))**.** Define a graph \(\mathsf{NG}_\lambda\) with _k_ vertices and the following edges:

\(E(\mathsf{NG}_\lambda)=\big\{(i,j)\big||\mathsf{lcs}(w_i,w_j)||\ge\lambda\text{and}\widehat{\mathsf{O}}_{\lambda^2}[i][j]=0\big\}.\)

In other words, \(\mathsf{NG}_\lambda\) contains all of the edges that are not detected in our algorithm. We extend the notion of constructive tuples to the undetected edges in our algorithm. We call such tuples _undetected-constructive_.

**Definition 3.3** (undetected-constructive tuple)**.** We say a tuple \(\langle w_i,w_a,w_b,w_j\rangle\) is \((\epsilon,\lambda)\)-undetected-constructive if it is \((\epsilon,\lambda)\)-constructive and also<tbc>

\((i,a),(a,b),(b,j),(i,j)\in E(\mathsf{NG}_\lambda).\)

