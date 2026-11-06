functions. Observe that \(|\mathcal{W}_{k,\ell}|=(\ell!)^k\) and the spread of each weight function is \(k\cdot(2^{\ell+1}-1)+1\), so (i) and (ii) hold.

We claim that for any weight function \(w\in\mathcal{W}\), the centroid tree of \((\mathcal{T}_{k,\ell},w)\) is unique, i.e., (iv) holds. Indeed, let \(w=w_{\pi_1,\dots,\pi_k}\), and observe that the unique centroid of \(\mathcal{T}_{k,\ell}\) is _c_ (since we assumed \(k\ge 2\)). The removal of _c_ splits \(\mathcal{T}_{k,\ell}\) into the _k_ stars with centers _v_<sub>1</sub>_,...,v<sub>k</sub>_. For all \(1\le i\le k\), the centroid tree of the star with center _v<sub>i</sub>_ is uniquely determined by the weight assignment by the permutation \(\pi_i\), and it is easily seen to be the path on vertices \(v_{i,1},\dots,v_{i,\ell}\) in decreasing order of weights, followed by the star center _v<sub>i</sub>_. Finally, the entire search tree has height \(\ell+2\), thereby (iii) holds.

In the case _k_=1, we omit the vertex _c_ and directly build a single star. Claims (i)-(iv) are easy to verify if we build \(\mathcal{W}_{k,\ell}\) as above.

We are now ready to show our lower bounds.

**Theorem 1.6.** _Let_ \(h\ge 3\) _and_ \(n\ge h+1\) _be integers. Then there is a tree_ T _on at most n vertices and a class_ W _of weight functions on V_(T) _such that for every_ \(w\in\mathcal{W}\)_, every centroid tree of_ (T_,w_) _has height h, and every binary decision tree that solves_ T _for_ W _has height_ \(\Omega(nlogh)\).

_Proof._ We use Lemma 5.3 with \(k=\lfloor\frac{n-1}{h}\rfloor\) and \(\ell=h-1\). The number of leaves in the decision tree is \(|\mathcal{W}_{k,\ell}|\), so its height is \(log|\mathcal{W}_{k,\ell}|=log((\ell!)^k)\in\Omega(\frac{n}{h}log(h!))=\Omega(nlogh)\).

Theorem 1.6 implies that Theorem 1.5 is tight (up to a constant factor) for all _n_ and _h_.

A slight adaptation of the argument yields the following:

**Theorem 5.6.** _Let_ \(n\in\mathbb{N}\) _and_ \(\sigma\in\mathbb{R}\) _with_ \(4n\le\sigma\le 2^n\)_. Then there is a tree_ T _on n vertices and a class_ W _of weight functions on V_(T) _with spread at most_ \(\sigma\)_, such that every binary decision tree that solves_ T _for_ W _has height_ \(\Omega(nlog(\frac{\sigma}{n}))\).

_Proof._ We use Lemma 5.3 with \(\ell=\lfloor log\sigma-logn\rfloor\ge 2\) and \(k=\lfloor\frac{n}{\ell}\rfloor\ge 1\). The spread of each \(w\in\mathcal{W}_{k,\ell}\) is at most \(\frac{n}{\ell}\cdot 2\frac{\sigma}{n}\le\sigma\), as desired. The height of each decision tree is \(log|\mathcal{W}_{k,\ell}|\in\Omega(\ell klog\ell)=\Omega(nloglog(\frac{\sigma}{n}))\).

We now discuss for which range of the parameter \(\sigma\) the bounds in Theorems 5.5 and 5.6 are tight. First note that any reasonable model of computation will require \(\Omega(n)\) time to read the input. Since we can pad the tree in the lower bound construction of Theorem 1.6 with zero-weight leaves, we can get a lower bound of \(\Omega(n+mloglog(\frac{\sigma}{m}))\) for all \(m\le n\), where _m_ is the number of positive-weight vertices.

Note that \(\sigma\ge m\). If \(\sigma>2^m\), we can use Theorem 5.6 with \(\sigma=2^m\), and obtain a tight \(\Theta(n+mlogm)\) bound together with Theorem 5.5.

If \(\sigma\le 2^m\) and \(\sigma\ge m\cdot 2^{log^\varepsilon m}\) for some constant \(\varepsilon>0\) (i.e., \(\sigma\) is very slightly superlinear in _m_), then \(loglog(\frac{\sigma}{m})\in\Theta(loglog\sigma)\), so we obtain a tight \(\Theta(n+mloglog\sigma)\) bound from Theorem 5.6 and Theorem 5.5.

If \(\sigma\) is close to linear in _m_, then our upper bound \(\mathcal{O}(n+mloglog\sigma)\) and our lower bound \(\Omega(n+mloglog(\frac{\sigma}{m}))\) differ. We leave the problem of finding the correct bounds in this case as an open question.

## 6 Approximation guarantees of \(\alpha\)-centroid trees

### 6.1 Upper bounds

**Theorem 1.7.** _Let_ T _be a tree,_ \(w:V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\)_, m=w_(T)_. We have_

\((i)\mathtt{cent}^\alpha(\mathcal{T},w)\le\frac{1}{1-\alpha}\cdot\mathtt{OPT}(\mathcal{T},w)-\frac{\alpha}{1-\alpha}m,\text{\textit{for}}\alpha\in(0,1),\)<br>
\((ii)\mathtt{cent}^\alpha(\mathcal{T},w)\le\frac{1}{2-3\alpha}\cdot\mathtt{OPT}(\mathcal{T},w)-\frac{3\alpha-1}{2-3\alpha}m,\text{\textit{for}}\alpha\in\left[\frac{1}{3},\frac{1}{2}\right].\)

