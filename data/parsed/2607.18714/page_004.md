Thorup and Zwick \[TZ01\] presented a sampling method that bounds the size of clusters as well. For the overview, we assume the following.

**Assumption 2.3.** _For each_ \(s\in\mathsf{V}\), \(|\mathsf{ball}_A(s)|=\tilde{\mathsf{O}}(\mathsf{n}^{0.05})\) _and_ \(|\mathsf{cluster}_A(s)|=\tilde{\mathsf{O}}(\mathsf{n}^{0.05})\).

Observe that the ball contains all vertices at distance \(\le|\mathsf{s}\mathsf{pivot}_A(s)|-1\) from s. No vertex strictly inside the ball, that is, at distance \(\le|\mathsf{s}\mathsf{pivot}_A(s)|-2\) from s, has degree greater than \(\tilde{\mathsf{O}}(\mathsf{n}^{0.05})\), since otherwise the ball size exceeds \(\tilde{\mathsf{O}}(\mathsf{n}^{0.05})\). Thus, we obtain the following lemma.

**Lemma 2.4.** _For each_ \(s\in\mathsf{V}\)_, every vertex strictly inside_ ball<sub>A</sub>(s)_, that is, at distance_ \(\le|\mathsf{s}\mathsf{pivot}_A(s)|-2\) _from s, has degree_ \(\le\tilde{\mathsf{O}}(\mathsf{n}^{0.05})\).

## 2.2 A new idea

We now present a new approach to this problem. To connect the local balls of s and t to the global shortest path, we examine where the st path crosses the boundaries of their respective balls.

**Definition 2.5.** _Assuming_ \(t\notin\mathsf{ball}_A(s)\) _and_ \(s\notin\mathsf{ball}_A(t)\)_, let_ p<sub>s</sub> _denote the vertex on the boundary of_ ball<sub>A</sub>(s) _that lies on the_ st _path. Similarly, let_ p<sub>t</sub> _denote the vertex on the boundary of_ ball<sub>A</sub>(t) _that lies on the_ st _path. See Figure 1. Thus_ |sp<sub>s</sub>|=|spivot<sub>A</sub>(s)|-1 _and_ |tp<sub>t</sub>|=|tpivot<sub>A</sub>(t)|-1.

Using Theorem 2.4, each vertex on the sp<sub>s</sub> path, except possibly p<sub>s</sub>, has degree \(\le\tilde{\mathsf{O}}(\mathsf{n}^{0.05})\). We make the same argument for the vertices on the p<sub>t</sub>t path. Thus, the prefix sp<sub>s</sub> and the suffix p<sub>t</sub>t of the st path have low degree, and we will use this crucially to design faster algorithms. But what about the middle segment, p<sub>s</sub>p<sub>t</sub>? Unfortunately, p<sub>s</sub>p<sub>t</sub> may contain vertices with high degree. But what if we could show that p<sub>s</sub>p<sub>t</sub> is short? This is exactly our main assumption in this section.

**Assumption 2.6.** \(|\mathsf{p}_\mathsf{s}\mathsf{p}_\mathsf{t}|\le\mathsf{c}\)_, where_ c _is a constant._

We will prove this assumption in later sections. But how does it help us find the st path? By definition, \(s\in\mathsf{cluster}_A(\mathsf{p}_\mathsf{s})\) and \(t\in\mathsf{cluster}_A(\mathsf{p}_\mathsf{t})\). Unfortunately, given s and t, we do not know the identities of p<sub>s</sub> and p<sub>t</sub>. But what if we just guess them? Consider the following simple algorithm that iterates over all pairs x and y, treating them as candidates for p<sub>s</sub> and p<sub>t</sub>, and checks the paths between their clusters.

**Algorithm 1:** Trivial Pairwise Update

1 **foreach** x,y _pair in_ G **do**

2 **foreach** (s,t) _in_ \(\mathsf{cluster}_A(\mathsf{x})\times\mathsf{cluster}_A(\mathsf{y})\) **do**

3 \(\mathsf{est}(s,\mathsf{t})=\mathsf{min}\left\{\begin{array}{ c }
\mathsf{est}(s,\mathsf{t}), \\
\mathsf{est}(s,\mathsf{x})+\mathsf{est}(\mathsf{x},\mathsf{y})+\mathsf{est}(\mathsf{y},\mathsf{t})
\end{array}\right.\)

ballA(s)
ballA(t)
Ps
Pt
s
t

Figure 1: Vertices p<sub>s</sub> and p<sub>t</sub> lie on the boundary of ball<sub>A</sub>(s) and ball<sub>A</sub>(t) respectively and lie on the st path.

