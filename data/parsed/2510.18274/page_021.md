### Organization.

For the remainder of this section, we will prove Claim 5.1. We assume the its setting throughout the section: let _f,k_, and \(k'=\frac{k}{2}\) be known parameters with a promise that \(\nu(G)\ge f\), and also given for free is \(H\unknown G\) with \(\nu(H)\ge f-k\). We wish to obtain \(H^\mathrm{after}\unknown G\) with \(\nu(H^\mathrm{after})\ge f-k'=f-\frac{k}{2}\). We first begin with a quick reminder of our witness argument in Section 5.1. Then, Section 5.2 presents a fresh perspective of the algorithm. Section 5.3 discusses the arisen subproblem and addresses how to solve it with low cut-query complexity. Finally, Section 5.4 puts together all the ingredients and proves Claim 5.1.

## 5.1 Quick Recollection from Section 3

We now recall the definitions of witnesses and formally prove its invariant given in Section 3.

**Definition 3.6** (Witness)**.** _Let_ G=(_V,E_) _be an unweighted undirected graph with two designated terminals s and t. A tuple_ W=(_S,T,Y_) _is called a_ witness _of_ G _if the following conditions hold:_

1. (_S,T_) _is an s-t cut of_ G _with value_ \(|E_\mathcal{G}(S,T)|\le f-k'-1\).<tbc>

_2._ \(Y\subseteq S\times T\) _such that_ \(|Y|=f-k'-1\) _and_ \(E_\mathcal{G}(S,T)\subseteq Y\) .

_Finally, let_ W(G) _denote the set of all witnesses of_ G.

**Invariant 3.7** (Witness Invariant)**.** _For any graph_ G_, we have_ \(\nu(\mathcal{G})\ge f-k'\) _if and only if_ \(\mathcal{W}(\mathcal{G})=\emptyset\).

_Proof._ First, suppose that \(\nu(\mathcal{G})\ge f-k'\). Assume for the sake of contradiction that a witness exists and let (_S,T_) be a cut with respect to that witness. By definition of a witness and \(\nu(\mathcal{G})\) being the value of _s-t_ min-cut, we have \(f-k'-1\ge|E_\mathcal{G}(S,T)|\ge\nu(G)\ge f-k'\) which is a contradiction. Thus, \(\mathcal{W}(\mathcal{G})=\emptyset\).

Conversely, suppose that \(\nu(\mathcal{G})\le f-k'-1\). Again, by the definition of \(\nu(G)\), we know that the min _s-t_ cut of G is of value \(\nu(\mathcal{G})\le f-k'-1\). Let (_S,T_) be such cut. Let _X_ be an arbitrary subset of \((S\times T)\backslash E_\mathcal{G}(S,T)\) of size \(f-k'-1-|E_\mathcal{G}(S,T)|\). This set in fact exists because \(f-k'-1\le n-1\le|S\times T|\). Then by definition, \((S,T,E_\mathcal{G}(S,T)\cup X)\) is a witness of G, implying \(\mathcal{W}(\mathcal{G})\neq\emptyset\).

**Definition 3.8** (Killing a witness)**.** _Let_ G=(_V,E_) _be an unweighted and undirected graph with terminals s and t, and let_ W=(_S,T,Y_) _be one of its witnesses. We say a pair of vertices_ (_a,b_) kills _witness_ W=(_S,T,Y_) _if and only if_ \(a\in S\), \(b\in T\)_, and_ \((a,b)\notin Y\) .

It is also useful to keep in mind a general description of our algorithm. Let \(\gamma>0\) be a suitable parameter. At any point that we have an explicit graph \(H\unknown G\), we wish to find a \(\gamma\)-good edge \(e\in G\backslash H\) such that \(|\mathcal{W}(H\cup\{e\})|\le(1-\gamma)\cdot|\mathcal{W}(H)|\). Then, we set \(H\leftarrow H\cup\{e\}\) and recurse until we reach the termination condition \(\mathcal{W}(H)=\emptyset\) which, by our invariant, we firmly conclude \(\nu(H)\ge f-k'\).

## 5.2 Witness as a Cut Indicator

Here, we tweak the definition of witness of _H_ by a bit: for a witness \(\mathsf{W}=(S,T,Y=E_H(S,T)\cup X)\), we instead represent a cut (_S,T_) by a binary vector \(Z\in\{0,1\}^V\) which \(z_v=\unknown(v\in T)\) indicates whether _v_ belong to _t_-side of the cut. From time to time, we vary the cut representation by (_S,T_) and _Z_ depending on the context. We always have _z<sub>s</sub>_=0 and _z<sub>t</sub>_=1 as _s_ always appears in _S_-side of the cut, and _t_ always appears in _T_-side of the cut. With this notion, the cut-size condition of witness is equivalent to:

\(\sum_{(u,v)\in\mathcal{G}}|z_u-z_v|\le f-k'-1\) (3)

