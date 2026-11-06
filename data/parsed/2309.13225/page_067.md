_Proof._ As before, constructing _E<sub>i</sub>_ can easily be done in _O(m_)=_O(n_<sup>2</sup>) time. To construct _D<sub>i</sub>_, for every vertex with degree at least _s<sub>i</sub>_, we compute a hitting set for its neighborhood restricted to the _s<sub>i</sub>_-1 lightest neighbors. In particular, we compute a hitting set for the sets \(\{v\}\cup\{w\in N(v)\text{s.t. rank}_v(w)<s_i\}\) of size _s<sub>i</sub>_ for each \(v\in V_{s_i}\). Then, this guarantees that the edge \((v,w)\in E_i^*\) satisfies the additional constraint rank_<sub>v</sub>(v,w)\<s<sub>i</sub>_ for \(v\in V_{s_i}\). By our previous arguments, _D<sub>i</sub>_ dominates _V<sub>s<sub>i</sub></sub>_ and has size \(\tilde{O}\left(\frac{n}{s_i}\right)\). Note that as before computing _D<sub>i</sub>_ requires \(\tilde{O}(n^2)\) time.

## B.1 Useful Results on Fast Matrix Multiplication

We will extensively use various algorithms for efficiently computing matrix products. We lay out some of the key results used below. The matrix multiplication exponent \(\omega(a,b,c)\) denotes infimum over all constants _t_ such that we can multiply two matrices of dimension \(n^a\times n^b\) and \(n^b\times n^c\) in _O(n<sup>t</sup>_) time. Denote \(\omega(1,1,1)\) as the constant \(\omega\). As the results given in this section are quite involved, we omit them for brevity and instead provide references to the relevant proofs.

**Theorem B.1.** _(\[DWZ22\]) The matrix multiplication exponent_ \(\omega\le 2.37188\).

See Duan, Wu, and Zhou \[DWZ22\] for the appropriate proof. The dual matrix multiplication exponent \(\alpha\) is the supremum over all constants _k_ such that \(\omega(1,k,1)\le 2\).

**Theorem B.2.** _(\[GU18\]) The dual matrix multiplication exponent_ \(\alpha\ge 0.31389\).

**Lemma B.3.** _(\[Gal12\]) For any fixed value_ \(0\le k_0<1\) _and_ \(k_0\le k\le 1\),

\(\omega(1,k,1)\le\omega(1,k_0,1)+(\omega-\omega(1,k_0,1))\frac{k-k_0}{1-k_0}\)

We refer the reader to Le Gall and Urrutia \[GU18\] and Le Gall \[Gal12\] for the proofs of the above two results. We will also use some useful properties of \(\omega\), in particular that it is convex, symmetric and linear.

**Lemma B.4.** _(Corollary 5.1 of \[LR83\]) Suppose_ \(\omega(1,a,b)=\omega(1,a',b')=c\)_. Then, for_ \(t\in[0,1]\),<tbc>

\(\omega(1,t*a+(1-t)*a',t*b+(1-t)*b')\le c\)

<tbc>**Lemma B.5.** _Let_ \(t,a,b,c\ge 0\)_. Then,_<tbc>

\(\omega(a,b,c)=\omega(a,c,b)=\omega(b,a,c)=\omega(b,c,a)=\omega(c,a,b)=\omega(c,b,a)\)

<tbc>_and_

\(\omega(ta,tb,tc)=t\omega(a,b,c)\)

See, for example, Lotti and Romani \[LR83\] for the former result and Huang and Pan \[HP98\] for the latter. The following theorem of Huang and Pan \[HP98\] gives improved bounds on general rectangular matrix multiplication for matrix products where _a,b,c_ are distinct.

**Theorem B.6.** _(Theorem 8.1 of \[HP98\]) Suppose r\>_1_\>t\>_0_. Then,_<tbc>

\(\omega(t,1,r)\le\left\{\begin{array}{ c c }
r+1 & t\le\alpha \\
\frac{r(1-\alpha)+(1-t)+(\omega-1)(t-\alpha)}{1-\alpha} & \alpha<t\le 1
\end{array}\right.\)

<tbc>See Huang and Pan \[HP98\] for the proof of the above result. We will use the following corollary as a generalization,

