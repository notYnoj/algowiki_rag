Let us now try to reproduce Claim 3.9 in a language of _Z_. Denote (Z,Y) to be a uniform distribution over all witnesses of _H_. To draw a uniformly random witness (_Z,Y_)∼(Z,Y), we can (1) draw _Z_∼Z, and (2) draw _Y_∼Y|_Z_. We also define a _real-valued_ vector \(\hat{Z}:=\{\hat{z}_v\}_{v\in V}\in[0,1]^V\) such that for any vertex \(v\in V\) , we let:

\(\hat{z}_v:=\mathbb{E}_{Z\sim\mathcal{Z}}z_v.\)

Since _z<sub>s</sub>_ is always 0 and _z<sub>t</sub>_ is always 1, it follows that \(\hat{z}_s=0\) and \(\hat{z}_t=1\). Intuitively, the vector \(\hat{Z}\) can be viewed as an _average cut_ over all remaining witnesses in W(_H_). In particular, \(\hat{z}_v\) admits a natural probabilistic interpretation: it corresponds to the probability that \(v\in T\) under a uniformly random witness (_S,T,Y_). Importantly, we remark that the explicit description of the _H_ alone is sufficient to enumerate all remaining witnesses in W(_H_), and thus to compute \(\hat{Z}\).

**Claim 5.3.** _For any pair of vertices_ \((u,v)\notin H\)_, we have_ \(Pr_{Z\sim\mathcal{Z}}(z_u\neq z_v)\ge|\hat{z}_u-\hat{z}_v|\).

_Proof._ Such probability is

\(\mathbb{E}_{Z\sim\mathcal{Z}}|z_u-z_v|\ge\left|\mathbb{E}_{Z\sim\mathcal{Z}}z_u-\mathbb{E}_{Z\sim\mathcal{Z}}z_v\right|=|\hat{z}_u-\hat{z}_v|\)

via the triangle inequality.

**Claim 5.4.** _Fix a pair of vertices_ \((u,v)\notin H\)_. Let_ \(Z\in supp(\mathcal{Z}|z_u\neq z_v)\)_. Then,_

\(Pr_{Y\sim\mathcal{Y}|Z}\left[(u,v)\notin Y\backslash E_H(S,T)|Z\right]\ge\frac{k'+1}{k}.\)

_Proof._ Observe that Y|_Z_ is equivalent to \(E_H(S,T)\cup(\mathcal{X}|Z)\) where X|_Z_ is a uniform distribution over \(\genfrac(){pt}{2}{(S\times T)\backslash E_H(S,T)}{f-k'-1-E_H(S,T)}\). Note that (_u,v_) is one of those pair of vertices among \((S\times T)\backslash E_H(S,T)\). Thus, the probability that (_u,v_) is included in _X_ is

\(\frac{f-k'-1-|E_H(S,T)|}{|S\times T|-|E_H(S,T)|}\le\frac{f-k'-1-|E_H(S,T)|}{n-1-|E_H(S,T)|}\) (\(|S\times T|\ge n-1\))

\(\le\frac{f-k'-1-(f-k)}{n-1-(f-k)}\) (\(|E_H(S,T)|\ge\nu(H)\ge f-k\))

\(\le\frac{k-k'-1}{k}\) (\(f\le n-1\))

Subtracting both sides from 1 concludes the proof.

These two claims have important implications. The left-hand side of Claim 5.3 can be interpreted as the probability that _u_ and _v_ lie on opposite sides of a uniformly random witness cut _Z_. Additionally, the left-hand side of Claim 5.4 can be viewed as the probability that, conditioned on a fixed choice of _Z_ with _u_ and _v_ on the different sides, a random witness is _killed_ by the edge (_u,v_). By combining these two interpretations, we arrive the following bound.

**Claim 5.5.** _For any edge_ \((u,v)\in G\backslash H\)_, we have_

\(Pr_{(Z,Y)\sim(\mathcal{Z},\mathcal{Y})}\left[(u,v)\text{\textit{kills}}(Z,Y)\right]\ge\frac{k'+1}{k}\cdot|\hat{z}_u-\hat{z}_v|.\)

