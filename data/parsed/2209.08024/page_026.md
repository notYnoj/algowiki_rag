### Case 2.

Assume _z_ is in the path in T between _x_ and _y_. Then, transform _T_ by lifting _z_. The depths of vertices in _B<sub>x</sub>_ increase by one, since each of these vertices gains _z_ as ancestor. The depths of vertices in _B<sub>y</sub>_ are unchanged, since these vertices gain _z_ and lose _x_ as ancestors. The depths of vertices in _B<sub>x,y</sub>_ are decreased by _at least_ one, since each loses at least one ancestor from {_x,y_}. (See Figure 10.2.) We then have

\(\mathtt{cost}_w(T^z)-\mathtt{cost}_w(T)\le w(B_x)-w(B_{x,y})<\frac{1}{3}-\frac{1}{3}=0,\)

again, a contradiction.

### Case 3.

Finally, assume that _z_ is not in the path between _x_ and _y_. Note that this cannot happen in the special case of BSTs, i.e., when T is a path.

Let \(t\in B_{x,y}\) be the unique vertex in T whose removal separates _x_, _y_ and _z_ to different components. Now, transform _T_ by lifting _t_. As in the previous case, depths of vertices in _B<sub>x</sub>_ increase by one, depths of vertices in _B<sub>y</sub>_ stay the same and depths of vertices _B<sub>x,y</sub>_ decrease by _at least_ one. To see this, observe that each vertex in _B<sub>x,y</sub>_ gains _t_ as ancestor and loses two ancestors from {_x,y,z_}, and possibly more. (See Figure 10.3.) As in the previous case, we have `cost`_<sub>w</sub>(T<sup>t</sup>)\<_`cost`_<sub>w</sub>(T_), a contradiction.

## 7 Conclusions

We showed that the average search time in a centroid tree is larger by at most a factor of 2 than the smallest possible average search time in an STT and that this bound is tight. We also showed that centroid trees can be computed in O(_n_log_h_) time where _h_ is the height of the centroid tree.

X
y
C
y
X
B
A
C
B
A
y
A
C
A
B
X
X
Z
y
A3
C
B
X
y
A3
C
Z
A2
y
A1
B
A2
C
B
A1
Z
A1
A2
A3
X
X
y
t
D
B
y
Z
C
X
y
Z
E4
E3
E2
y
C
E
B
E1
E2
D
E3
E3
t
E
D
t
X
E4

Figure 10: Illustration of the proof of Theorem 1.9, Case 1-3, top to bottom. (_Left._) Transformation of search tree _T_. (_Right._) Underlying tree T . Note that some blocks may indicate multiple disjoint subtrees.

