3. If \(|N(V_i^{(b)})|>\frac{n}{|S_\mathrm{in}|}\):<tbc>

(a) Construct \(S'\times V_i^{(b)}\) matrix _X_ and \(V_i^{(b)}\times N_{G_b}(V_i^{(b)})\) matrix _Y_ with entries<tbc>

<tbc>\(X[s,u]=\left\{\begin{array}{ c c }
\widehat{\mathrm{d}}(s,u) & u\in\mathcal{A}(s,b) \\
\infty & \mathrm{o}/\mathrm{w}
\end{array}\right.,Y[u,v]=\left\{\begin{array}{ c c }
\mathrm{wt}(u,v) & (u,v)\in E_b \\
\infty & \mathrm{o}/\mathrm{w}
\end{array}\right..\)<tbc>

<tbc>(b) Compute _X⋆Y_ using Lemma 5.9.<tbc>

(c) For all \(s\in S'\) and \(v\in N_{G_b}(V_i^{(b)})\), update \(\widehat{\mathrm{d}}(s,v)\leftarrow^\mathrm{min}(X\star Y)[s,v]\).<tbc>

4. For all \(s\in S'\):<tbc>

(a) Update \(\hat{L}(s,\mathrm{level}(s)+1)\leftarrow^\unknown\left\{v\mathrm{s}.\mathrm{t}.\widehat{\mathrm{d}}(s,v)=\mathrm{level}(s)+1\right\}\).<tbc>

(b) Remove \(V_i^{(b)}\) from A(_s,b_) and decrement score\((i,b)\leftarrow^\unknown 1\).<tbc>

(c) If \(\mathcal{A}(s,b)=\emptyset\): run `updateScores`(_s,b_).

`updateScores`(_s,b_):<tbc>

1. Update \(\mathrm{level}(s,b)\leftarrow^\unknown b\) and \(\mathrm{level}(s)\leftarrow\mathrm{min}_b\mathrm{level}(s,b)\).<tbc>

2. If \(\bigcup_{r=0}^{\mathrm{level}(s)}\hat{L}(s,r)=V\) : then remove _s_ from _S_ and return.<tbc>

3. If level(_s_) increased, then for all _b_ with level(_s,b_)=level(_s_):<tbc>

(a) Update \(\mathcal{A}(s,b)\leftarrow\bigcup_{r=\mathrm{level}(s)-b+1}^{\mathrm{level}(s)}\hat{L}(s,r)\).<tbc>

(b) For all \(V_i^{(b)}\cap\mathcal{A}(s,b)\neq\emptyset\), increment score(_i,b_).

`increaseLevel` \(\left(s,\{\mathrm{level}(s,b)\},\mathrm{level}(s),\left\{\hat{L}(s,r)\right\},\{\mathcal{C}_b\}\right)\)**:**

1. Update \(\hat{L}(s,\mathrm{level}(s)+1)\leftarrow^\unknown\left\{v\mathrm{s}.\mathrm{t}.\widehat{\mathrm{d}}(s,v)=\mathrm{level}(s)+1\right\}\).<tbc>

2. Increment \(\mathrm{level}(s,b)\leftarrow^\unknown b\) for all _b_ with level(_s,b_)=level(_s_) and update \(\mathrm{level}(s)\leftarrow\mathrm{min}_b\mathrm{level}(s,b)\).<tbc>

3. For all _b_ with level(_s,b_)=level(_s_):<tbc>

(a) Update \(\mathcal{A}(s,b)\leftarrow\bigcup_{r=\mathrm{level}(s)-b+1}^{\mathrm{level}(s)}\hat{L}(s,r)\).<tbc>

(b) For all \(V_i^{(b)}\cap\mathcal{A}(s,b)\neq\emptyset\), increment score(_i,b_).

_Proof of Theorem 1.3._ We prove the correctness and running time of our algorithm.

## Correctness.

We argue that our algorithm terminates and outputs correct distances. As before, we can show that the estimated distances are always valid.

**Lemma 5.10.** _In every iteration of the while loop_ \(\widehat{\mathrm{d}}(s,v)\ge\mathrm{dist}(s,v)\) _for all_ \(s\in S_\mathrm{in},v\in V\) .

_Proof of Lemma 5.10._ We argue that at the end of each iteration of the while loop \(\widehat{\mathrm{d}}(s,v)\) can be realized by a path in _G_ from _s_ to _v_ for all \(s\in S_\mathrm{in},v\in V\) . Consider the first iteration where this is not the case.

