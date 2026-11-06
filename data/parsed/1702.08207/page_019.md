\begin{tabular}{cccccccccc}
_v_ & a & b & c & d & e & f & g & h \\
\(w'(v)\) & \(\frac{2}{8}\) & \(\frac{4}{8}\) & \(\frac{8}{8}\) & \(\frac{2}{8}\) & \(\frac{3}{8}\) & \(\frac{2}{8}\) & \(\frac{4}{8}\) & \(\frac{1}{8}\) \\
\end{tabular}

a
2/8
4/8
b
c
8/8
2/8
d
e
f
2/8
3/8
g
4/8
h
O
1/8

ca[0,e]=2/4
2
ca[1,e]=0/4
a
c[0,e]=2/4
c
2
1
c[1,e]=1/4
e
c[0,e]=2/4
2
1
c[1,e]=1/4

a
2/8
4
2
4/8
b
c
8/8
4
4
3
4
4
2/8
d
e
f
2/8
2
3/8
2
1
g
4/8
1
4
v
a
b
c
d
e
f
g
h
h
1/8
1

a
(f,a)
(f,e,d,c)
b
c
(b)
d
e
f
(f)
(d)
(e)
g
(h,g)
h
(h)

(a) Tree \(T'\) with vertex weights.

(c) Contribution of load of vertex _e_ to different vertices of the tree.

Figure 4.1: Illustration of Algorithm 4.1 and {_a,b,c,d,e,f,g,h_} and vertex weights:

(b) Sample schedule \((s_v,t_v)_{v\in V}\) obtained by backtracking procedure BuildStrategy with parameters \(c=1,n=8,\omega=\frac{4}{8}\), (box size \(\frac{4}{8}\), slot size \(\frac{1}{8}\), 4 slots per box), _L_=4. Note that the schedules \((s_v)_{v\in V}\) may correspond to different starting times of jobs within the prescribed box; the provided _t<sub>v</sub>_ are an example.

(d) Sequences _S(v_) computed by Algorithm 3 based on provided \((s_v,t_v)_{v\in V}\). Note that vertex _e_ does not appear in _S(a_) because of the query to _c_ on the way.

