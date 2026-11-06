bounds resulting in low-density regions suffer from long running times. Our method draws samples from the unrestricted unit square and maps the results onto the restricted subspace.

The method is composed of the following steps. First generate a sample (_u_<sub>1</sub>_,u_<sub>2</sub>) from the uniform distribution over the unit square. Then, based on the value of _u_<sub>2</sub>, determine which region \(R_s\subset C\) this point falls into and transform the coordinates using \(u'_j=g_s(u_j)\). These new coordinates fall within \(C'\) with the same probability distribution that rejection sampling would give but satisfies the constraints with only a single draw needed. After the draw, apply the inverse CDFs to the \((u'_1,u'_2)\) to transform to the original two random variables with \(X_j=F_j^{-1}(u'_j)\). Lastly, take the minimum to obtain a sample from our desired distribution: _Y_=min(_X_<sub>1</sub>_,X_<sub>2</sub>). Figure 1 shows a diagram of the two spaces and their divisions for some example values, graying out the regions where samples in \(C'\) cannot be located.

To partition the restricted space \(C'\) into regions, first note that there are three ways which the _X<sub>i</sub>_ could satisfy the bounds: only _X_<sub>1</sub> is less than _B_, both _X_<sub>1</sub> and _X_<sub>2</sub> are less than _B_, or only _X_<sub>2</sub> is less than _B_. _B_ is the only bound mentioned because in all scenarios both random variables must be greater than _A_. Create an ordered list of the index combinations for _X<sub>i</sub>_ which are less than _B_ in each possibility: _S_={{1},{1,2},{2}}. Assign coordinates \((u'_1,u'_2)\) to the axes of our unit square, and divide it into three regions \(R'_s\) for each \(s\in S\)

C
C'
u2
u'2
1
1
R3
f1 + f2
R'
R2
g1(u1,u2)
b2
f1
R'2
R'3
R1
(u1,u2)
a2
u1
u1
1
a1
b1
1

Figure 1: Unrestricted to restricted mapping for _k_=1_,N_=2.

