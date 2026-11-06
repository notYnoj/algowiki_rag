<tbc>\(q\checkmark n\). Our basic reference implementation did not outperform gbmv though. Little effort went into its optimization as it would not be our method of choice for the more common scenario of \(q\gg n\).

## 4. Towards Generalization.

DAGs recorded by adjoint AD are typically neither layered nor uniform. According to Definition 2.3 the term "layered" refers to a decomposition of the DAG into a sequence of bipartite sub-DAGs representing the elemental Jacobians \(F'_i\). For a DAG to be uniformly layered all layers must consist of the same number (_n_) of vertices as formally stated in Definition 2.4.

In the following we present ideas on how to make invertible DAGs uniformly layered. We formalize the corresponding methods and we prove their numerical correctness, respectively. All proofs rely on the following formulation of the chain rule of differentiation.

Lemma 4.1 (Chain Rule of Differentiation on DAG). _Let G be the DAG of a differentiable program_ \(F:\mathbb{R}^n\rightarrow\mathbb{R}^m\) _as in Definition 2.2 with Jacobian_<tbc>

\(F'\equiv\left(\frac{dy_k}{dx_i}\right)_{i=1,\dots,n}^{k=1,\dots,m}=\left(\frac{dv_{p+k}}{dv_{i-n}}\right)_{i=1,\dots,n}^{k=1,\dots,m}\in\mathbb{R}^m\times\mathbb{R}^n.\)

<tbc>_Then_

(4.1) \(\frac{dv_{p+k}}{dv_{i-n}}=\sum_{(i-n,\dots,p+k)(s,t)\in(i-n,\dots,p+k)}\partial_{t,s}\)

_for i_=1_,...,n and k_=1_,...,m._

_Proof._ See \[1\].

An illustrative explanation of each method is followed by its formalization and the proof of numerical correctness.

### 4.1. Edge Splitting.

Consider a minor modification of the sample program from Section 2 as

**for** (**int** i=0;i\<q;i++) {<br>
\(\mathrm{x}\left[\mathrm{i}\%\mathrm{2}\right]\unknown=\mathrm{x}\left[\left(\mathrm{i}+\mathrm{1}\right)\%\mathrm{2}\right]\);<br>
**if** (!(i%2)) x\[(i+1)%2\]=sin(x\[(i+1)%2\]);<br>
}

2
3
2
3
a1,1
a2,1
a1,1
a2,1
1
1
1
3,0
b1,1
b1,2
b1,1
b1,2
b2,2
-1
0
-1
0
(a)
(b)

Fig. 4. _Edge Splitting_

