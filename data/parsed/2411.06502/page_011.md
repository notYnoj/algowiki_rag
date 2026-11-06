## 2.3 From TED on caterpillar trees to spine edit distance

### Spine edit distance.

Our algorithm for TED on caterpillar trees generalizes to a problem known as _Spine Edit Distance_ (SED), initially proposed in \[BGHS19\].

In SED, besides two forests **F** and \(\mathbf{F}'\), we are provided with a spine for each forest. A spine \(\mathbf{S}\subseteq\mathbf{F}\) is any root-to-leaf path within a forest (in cases where the forest contains multiple trees, the spine can start from any root of a tree contained in the forest). In SED we are given the similarity between all pairs of subtrees of **F** and \(\mathbf{F}'\), provided at least one of the two roots does not lie on a spine. The task is to compute the similarity for all missing pairs of subtrees. Put more formally:

Spine Edit Distance (SED)

**Input:** Two forests \(\mathbf{F},\mathbf{F}'\), two spines \(\mathbf{S}\subseteq\mathbf{F},\mathbf{S}'\subseteq\mathbf{F}'\), and \(\text{sim}(\text{sub}(v),\text{sub}(v'))\) for all \((v,v')\in(\mathbf{F}\times\mathbf{F}')\backslash(\mathbf{S}\times\mathbf{S}')\).

**Output:** \(\text{sim}(\text{sub}(v),\text{sub}(v'))\) for all \((v,v')\in\mathbf{S}\times\mathbf{S}'\).

As already noticed in \[BGHS19\], TED can be reduced to SED by employing appropriate tree decompositions. In Section 6, we will prove the following:

**Lemma 2.1.** _Suppose there exists an algorithm for SED on two forests_ \(\mathbf{H},\mathbf{H}'\) _running in time_ \(\mathsf{T}_{SED}(m,m')=\mathcal{O}(f(m)g(m'))\)_, where_ \(m=|\mathbf{H}|,m'=|\mathbf{H}'|\) _and_ \(f(m)=\Omega(m),g(m')=\Omega(m')\) _are some functions. Then, there is an algorithm for TED on two forests_ \(\mathbf{F},\mathbf{F}'\) _running in time_ \(\mathcal{O}(f(n)g(n')log^2max(n',n))\)_, where_ \(n=|\mathbf{F}|,n'=|\mathbf{F}'|\).

### Reducing spine edit distance to APSP.

In the remaining part of this (sub)section, we describe the main ingredients we need to reduce SED to APSP.

We can assume, without loss of generality, that **F** and \(\mathbf{F}'\) are trees (by adding a virtual root and defining weights accordingly to enforce their deletion).

Let us further decompose **F** and \(\mathbf{F}'\) into **L**, **S**, **R** and \(\mathbf{L}',\mathbf{S}',\mathbf{R}'\), where **R** is obtained from **F** by removing all nodes in **S** and those to the left of it. Similarly, **L** is obtained from **F** by removing all nodes in **S** and

T
T'
(n + 1, n' + 1)
la
r'
(b, b')
C' a'
(1, 1)
cb

**Figure 3** The general case for similarity mappings on caterpillar trees.

