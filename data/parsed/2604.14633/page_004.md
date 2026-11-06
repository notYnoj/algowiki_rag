are in \(\partial_{G_f}^+S\), so \(\partial_{G_f}^+S\neq\emptyset\). If \(s\in S\) and \(t\notin S\), then a path from _s_ to _t_ in _G<sub>f</sub>_ must contain an edge in \(\partial_{G_f}^+S\), so \(\partial_{G_f}^+S\neq\emptyset\). Finally, if \(s,t\in S\) or \(s,t\notin S\), then by the conservation of flow, we have \(|\partial_{G_f}^+S|=|\partial_G^+S|\), and since _G_ is strongly connected by preprocessing, we conclude that \(|\partial_{G_f}^+S|=|\partial_G^+S|\neq 0\).

Our algorithm always finds augmenting paths that avoid the arcs (_t,s_), so while the current flow is not maximum, we may assume that _G<sub>f</sub>_ is strongly connected.

## 2 Balancing Weights

In this section, we construct our balancing weights on the residual graph and describe a data structure to maintain them over the course of the algorithm. The weights assigned to the arcs are determined by a potential function \(\mathbf{y}:V\rightarrow\mathbb{R}\) on the vertices. For a given potential function **y**, the weight of arc (_u,v_) is

\(w(u,v)=\frac{1}{max\{\mathbf{y}(v)-\mathbf{y}(u),0\}+1}.\)

In particular, we have \(w(u,v)=\frac{1}{\mathbf{y}(v)-\mathbf{y}(u)+1}\) whenever \(\mathbf{y}(v)\ge\mathbf{y}(u)\), and _w(u,v_)=1 whenever \(\mathbf{y}(v)\le\mathbf{y}(u)\).

The algorithm tries to find a potential function \(\mathbf{y}:V\rightarrow\mathbb{R}\) such that all cuts are approximately balanced in the two directions: for any set \(S\subseteq V\) , we require that \(\frac{1}{2}w(\partial^-S)\le w(\partial^+S)\le 2w(\partial^-S)\). Actually, we only need to enforce \(\frac{1}{2}w(\partial^-S)\le w(\partial^+S)\) because the other inequality follows by replacing _S_ with _V_\\_S_. If there is a violating set _S_ with \(w(\partial^+S)<\frac{1}{2}w(\partial^-S)\), then the algorithm increases the potential slightly for all vertices in _S_, i.e., sets \(\mathbf{y}(v)\leftarrow\mathbf{y}(v)+\Delta\) for all \(v\in S\), where \(\Delta>0\) is small enough. By a potential function argument, this process must terminate eventually. In particular, a balancing function **y** exists, which is already a non-trivial statement.

To ensure a fast algorithm, we need to find a balancing function **y** quickly, and moreover, dynamically maintain the function upon finding augmenting paths. We interpret the balance of a directed graph as the _minimum ratio cut_ of the underlying _undirected_ graph, and then use the dynamic minimum ratio cut data structure from a recent interior-point method-based flow algorithm \[VDBCK<sup>+</sup>24\].

We first define the minimum ratio cut of an undirected graph, whose input includes a _gradient function_ \(\mathbf{g}:V\rightarrow\mathbb{R}\) with \(\mathbf{g}\perp\unknown\), i.e., \(\sum_{v\in V}\mathbf{g}(v)=0\).

**Definition 4.** _The_ minimum ratio cut _of a positively weighted, undirected graph with gradient function_ \(\mathbf{g}\perp\unknown\) _is the minimum ratio_ \(\mathbf{g}(S)/w(\partial S)\) _over all_ \(S\subseteq V\) _with_ \(w(\partial S)\neq 0\).

Observe that the requirement \(\mathbf{g}\perp\unknown\) means that **g**(_S_)+**g**(_V_\\_S_)=0 for any \(S\subseteq V\) , so either _S_ or _V_\\_S_ has non-positive ratio. Intuitively, the goal is to maximize |**g**(_S_)| while minimizing \(w(\partial S)\), and then take either _S_ or _V_\\_S_, whichever has non-positive ratio.

We construct our minimum ratio cut instance as follows. Consider the _undirected_ graph with edge weights _w(u,v_) together with the gradient function \(\mathbf{g}:V\rightarrow\mathbb{R}\) defined as<tbc>

\(\mathbf{g}=\sum_{(u,v)}w(u,v)\cdot(\unknown_u-\unknown_v),\)

