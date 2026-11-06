2. \(|\mathrm{ball}_\alpha(s)|=\tilde{\mathcal{O}}(2^{2^\alpha})\) _and_ \(|\mathrm{cluster}_\alpha(s)|=\tilde{\mathcal{O}}(2^{2^\alpha})\) _for each_ \(s\in V\)<tbc>

_3._ _The running time of the algorithm is_ \(\tilde{\mathcal{O}}(\mathfrak{n}^2)\)

For completeness, we prove this lemma in Section A. The above algorithm finds a set \(A_\alpha\) such that every vertex has bounded ball and cluster size. In Theorem 3.2 we start the sampling process from A<sub>1</sub>. We now modify this step. Instead of starting from A<sub>1</sub>, we start from \(A_\alpha\) where \(1\le\alpha\le\mathrm{loglog}n-1\) and obtain \(A_\alpha\) using Theorem 3.5. After computing \(A_\alpha\), we apply nested vertex sampling to construct \(\{A_{\alpha+1},A_{\alpha+2},\dots,A_{\mathrm{loglog}n-1}\}\). We describe the modified nested vertex sampling process below.

**Definition 3.6** (Modified Nested Vertex Sampling)**.** _Fix an integer_ \(\alpha\) _where_ \(1\le\alpha\le\mathrm{loglog}n-1\)_. Using Theorem 3.5 find the set_ \(A_\alpha\)_. For each_ \(\alpha+1\le\mathrm{i}\le\mathrm{loglog}n-1\), A<sub>i</sub> _is sampled from_ A<sub>i-1</sub> _with probability_ \(\frac{1}{2^{\mathrm{i}-1}}\).

To understand the advantage of this sampling process, consider the bounds it provides. First, Theorem 3.4 still holds for all \(\mathrm{i}\ge\alpha\) (see Section C for a complete proof). For \(A_\alpha\), we can bound both \(|\mathrm{ball}_\alpha(s)|\) and \(|\mathrm{cluster}_\alpha(s)|\) for all \(s\in V\) . However, for any \(\mathrm{i}>\alpha\), we bypass Theorem 3.5 and can therefore only bound |ball<sub>i</sub>(s)|, not |cluster<sub>i</sub>(s)|. Our algorithm crucially leverages the fact that \(\mathrm{cluster}_\alpha(\cdot)\) remains bounded. We now describe a simple property of our modified nested sampling.

**Lemma 3.7.** _Let_ \(\alpha\le\mathrm{i}\le\mathrm{loglog}n-1\)_. Let z be a vertex with degree at least_ \(\tilde{\mathcal{O}}(2^{2^\mathrm{i}})\)_. Then, with high probability, z has a neighbor in_ A<sub>i</sub> _where_ A<sub>i</sub> _is constructed using modified nested vertex sampling._

Note that the above lemma is immediate when we use only nested vertex sampling. In Section B, we show that the lemma also holds under modified vertex sampling. We now move to the next important definition, which we adapt from \[Gup25\].

**Definition 3.8.** _Consider an_ st _path and let_ \(\mathrm{i}\ge\alpha\)_. Let_ a<sub>i</sub> _be the vertex closest to s on the_ st _path such that its distance to_ pivot<sub>i</sub>(a<sub>i</sub>) _is at most_ 1_. Define_ u<sub>i</sub>:=pivot<sub>i</sub>(a<sub>i</sub>)_. Similarly, let_ b<sub>i</sub> _be the vertex closest to_ t _on the_ st _path such that its distance to_ pivot<sub>i</sub>(b<sub>i</sub>) _is at most_ 1_. Define_ v<sub>i</sub>:=pivot<sub>i</sub>(b<sub>i</sub>).

In \[Gup25\], the vertices a<sub>i</sub>,u<sub>i</sub>,b<sub>i</sub>,v<sub>i</sub> are defined for all \(\mathrm{i}\ge 0\). Since our modified vertex sampling starts from \(\alpha\), we define these terms only for \(\mathrm{i}\ge\alpha\). We first show that, for each \(\mathrm{i}\ge\alpha\), the vertex a<sub>i</sub> exists. For this, we rely on Theorem 3.1, which states that there is a vertex of degree at least \(\tilde{\mathcal{O}}(\sqrt{n})\) on the st path. Let z be the vertex closest to s with degree \(\ge\tilde{\mathcal{O}}(\sqrt{n})\). By Theorem 3.7, with high probability, a vertex adjacent to z lies in A<sub>loglogn-1</sub>. Thus, pivot<sub>loglogn-1</sub>(z) is at a distance \(\le 1\) from z. Hence, we set a<sub>loglogn-1</sub>:=z and u<sub>loglogn-1</sub>:=pivot<sub>loglogn-1</sub>(z).

Since vertex sampling is nested, u<sub>loglogn-1</sub> which lies in A<sub>loglogn-1</sub> also lies in A<sub>loglogn-2</sub>,<br>
\(A_{\mathrm{loglog}n-3},\dots,A_{\alpha+1},A_\alpha\). This implies the existence of a<sub>i</sub> and u<sub>i</sub> for all \(\mathrm{i}\ge\alpha\) along the st path. By a symmetric argument, the vertices b<sub>i</sub> and v<sub>i</sub> also exist for all \(\mathrm{i}\ge\alpha\) along the st path.

We now state another lemma that bounds the degree of the vertices on the sa<sub>i</sub> path and the tb<sub>i</sub> path for each \(\mathrm{i}\ge\alpha\). The lemma follows from the fact that a<sub>i</sub> is the vertex closest to s whose distance to pivot<sub>i</sub>(a<sub>i</sub>) is at most 1. We formally prove this lemma in Section D.

ui
ui+1
Vi+1
Vi
S
ai
ai+1
bi+1
bi
t
Figure 2: Figure shows the relative position of ai’s, ui’s, bi’s and vi’s along the st path

Figure 2: Figure shows the relative position of a<sub>i</sub>’s, u<sub>i</sub>’s, b<sub>i</sub>’s and v<sub>i</sub>’s along the st path

