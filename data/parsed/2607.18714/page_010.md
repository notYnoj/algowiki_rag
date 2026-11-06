We will prove this lemma in the next section, but let us first explain it intuitively. Our algorithm ENSUREBALLPROXIMITY either already gets a 2-approximation of the st path or it ensures that the dis tance between s and pivot\(_\alpha(s)\) (and symmetrically, between t and pivot\(_\alpha(t)\)) is \(\frac{|st|}{2}\) , up to an additive constant \(c'\). Intuitively, this means that the balls around s and t are very close to each other. Henceforth, we will assume that after termination of ENSUREBALLPROXIMITY, est(s,t)_\>_2|st|. Thus, the two inequalities in the lemma hold. We will use these two inequalities to justify Theorem 2.6. To see this, let us redefine the notation p<sub>s</sub> and p<sub>t</sub> from the overview.

**Definition 4.2.** _Assuming_ \(t\notin ball_\alpha(s)\) _and_ \(s\notin ball_\alpha(t)\)_, let_ p<sub>s</sub> _denote the vertex on the boundary of_ \(ball_\alpha(s)\) _that lies on the_ st _path. Similarly, let_ p<sub>t</sub> _denote the vertex on the boundary of_ \(ball_\alpha(t)\) _that lies on the_ st _path. Thus_ \(|sp_s|=|spivot_\alpha(s)|-1\) _and_ \(|tp_t|=|tpivot_\alpha(t)|-1\).

If \(t\in ball_\alpha(s)\), then using Theorem 3.4, est(s,t)=|st|. Henceforth, we will assume that \(t\notin ball_\alpha(s)\) and \(s\notin ball_\alpha(t)\). We now show several properties of p<sub>s</sub> and p<sub>t</sub> that our algorithm will use. Recall that we defined the vertices \(a_\alpha\) and \(b_\alpha\) on the st path. We now describe the relation between p<sub>s</sub> and \(a_\alpha\) and between p<sub>t</sub> and \(b_\alpha\).

**Lemma 4.3.** _Vertex_ p<sub>s</sub> _lies closer to s than_ \(a_\alpha\)_, that is_ \(|sp_s|\le|sa_\alpha|\)_. Similarly_ \(|tp_t|\le|tb_\alpha|\)_. Moreover, the degree of each edge on the_ sp<sub>s</sub> _and_ tp<sub>t</sub> _paths is at most_ \(\tilde{\mathcal{O}}(2^{2^\alpha})\).

_Proof._ Note that \(u_\alpha\in A_\alpha\) and hence it is also a candidate for \(pivot_\alpha(s)\). Hence \(|spivot_\alpha(s)|\le|su_\alpha|\). We now show that p<sub>s</sub> lies closer to s than \(a_\alpha\) on the st path. Observe that:

\(|sp_s|=|spivot_\alpha(s)|-1\) (Since p<sub>s</sub> lies on the boundary of \(ball_\alpha(s)\))<br>
\(\le|su_\alpha|-1\) (Since \(|spivot_\alpha(s)|\le|su_\alpha|\))<br>
\(\le(|sa_\alpha|+1)-1\) (By triangle inequality)<br>
\(\le|sa_\alpha|\)

This proves the first part of the lemma and, by symmetry, also implies that \(|tp_t|\le|tb_\alpha|\). We now prove the second part. By Theorem 3.9, every edge on the \(sa_\alpha\) path has degree at most \(\tilde{\mathcal{O}}(2^{2^\alpha})\). Since sp<sub>s</sub> forms a subpath of \(sa_\alpha\), every edge on sp<sub>s</sub> also satisfies this bound. The same argument applies to the tp<sub>t</sub> path.

Next, we show that p<sub>s</sub> and p<sub>t</sub> are close to each other on the st path justifying Theorem 2.6.

**Lemma 4.4.** _Vertex_ p<sub>s</sub> _lies closer to s than_ p<sub>t</sub> _on the_ st _path. Formally,_ \(|sp_s|\le|sp_t|\)_. Moreover,_ \(|p_sp_t|\le c\) _where_ \(c=2c'+1\).

_Proof._ By Theorem 4.3, we have \(|sp_s|\le|sa_\alpha|\). Hence p<sub>s</sub> lies on the \(sa_\alpha\) path. Similarly, p<sub>t</sub> lies on the \(tb_\alpha\) subpath of the st path. If we show that \(a_\alpha\) lies closer to s than \(b_\alpha\), we will prove the first part of<tbc>

balla(s)
balla(t)
uα
Vα
s
ps
aα
bα
Pt
t

Figure 3: A diagram showing the relation between \(p_s,a_\alpha,u_\alpha\) and \(p_t,v_\alpha,b_\alpha\)

