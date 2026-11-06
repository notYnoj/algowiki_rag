The **String**<sub>**I**<sub>_k_<sub>1</sub></sub></sub>(_L_) representation of _A_ and the zeros are all very compressible with straight line programs. For _B_ they create its string _S<sub>B</sub>_ by basically merging each vector \(b\in\mathbf{List}_{k_2}(L)\) with _A_ which is structured like **String**<sub>**I**<sub>_k_<sub>1</sub></sub></sub>(_L_).

So, while the length of each string is _n_<sup>_k_<sub>2</sub>+_k_<sub>1</sub></sup> the compressions are of size _n_<sup>_k_+1</sup>. We need a gadget that forces our representation to align the two strings with no gaps in the LCS. If we do so, we can then check if an OV exists.

Now let us work through a small example. Let _k_<sub>1</sub>=2 and _k_<sub>2</sub>=1.

\(v_1=<0,1,1,1>\) (2)

\(v_2=<1,1,0,1>\) (3)

\(v_3=<1,0,1,1>\) (4)

\(v_4=<0,1,1,0>\) (5)

\(L=\{v_1,v_2,v_3,v_4\}\) (6)

For both _B_ and _C_ we form lists that are concatenations of vectors.

\(B=C=v_1,v_2,v_3,v_4\)

For _A_ we first we want to generate all the vectors \(v_{i,j}[p]=v_i[p]\cdot v_j[p]\).

\(v_{1,2}=<0,1,0,1>v_{1,3}=<0,0,1,1>v_{1,4}=<0,1,0,0>\) (7)

\(v_{2,3}=<1,0,0,1>v_{2,4}=<0,1,0,0>\) (8)

\(v_{3,4}=<0,0,1,0>\) (9)

Then we form _A_ by taking the first bit of each of these vectors then the second bits, etc. For this example, we put a semicolon in between the first bits and second bits. We do this here for making it easier to read.<tbc>

\(A=0,0,0,1,0,0;1,0,1,0,1,0;0,1,0,0,0,1;1,1,0,1,0,0\)

<tbc>Note that if we take the bits _p,p_+6_,p_+12_,p_+18 these correspond to a single vector _v<sub>i,j</sub>_. We want the ability to merge _A_ and a single vector _v<sub>i</sub>_. For this, if there is _v<sub>i</sub>_\[_p_\]=0 then we replace all those bits with zeros, otherwise we leave the bits of _A_ as is.

\((A\&v_1)=0,0,0,0,0,0;1,0,1,0,1,0;0,1,0,0,0,1;1,1,0,1,0,0\) (10)

\((A\&v_2)=0,0,0,1,0,0;1,0,1,0,1,0;0,0,0,0,0,0;1,1,0,1,0,0\) (11)

\((A\&v_3)=0,0,0,1,0,0;0,0,0,0,0;0,1,0,0,0,0;1;1,1,0,1,0,0\) (12)

\((A\&v_4)=0,0,0,0,0,0;1,0,1,0,1,0;0,1,0,0,0,1;0,0,0,0,0\) (13)

We also want to generate the padded vectors for _S<sub>C</sub>_. These padded vectors have ‘real’ vector values at locations 0,6,12,18. We want this because it means that if we line up one of these padded vectors, (0&_v<sub>i</sub>_), against a vector mixed with _A_, (_A&v<sub>j</sub>_), the ‘real’ values correspond to a vector in _A_.

\((0\&v_1)=0,0,0,0,0,0;1,0,0,0,0;0;1,0,0,0,0;0;1\) (14)

\((0\&v_2)=1,0,0,0,0,0;1,0,0,0,0;0,0,0,0;1\) (15)

\((0\&v_3)=1,0,0,0,0,0;0,0,0,0,0;0;1,0,0,0,0;0;1\) (16)

\((0\&v_4)=0,0,0,0,0,0;1,0,0,0,0,0;1,0,0,0,0;0\) (17)

Specifically, if we line up (0&_v<sub>i</sub>_) and (_A&v<sub>j</sub>_) with an offset of \(\Delta\) every lined up set of entries has a zero if there are _k_<sub>1</sub>+2_k_<sub>2</sub> vectors that are orthogonal. Lets consider this example:

\((A\&v_1)=0,0,0,0,0;0;1,0,1,0,1,0;0,1,0,0,0;1;1,1,0,1,0,0\) (18)

\((0\&v_2)=1,0,0,0,0,0;1,0,0,0,0;0,0,0,0,0;0;1\) (19)

\(\text{This alignment}=0;0,0,0,0,0;0;0,0,0,0,0;0,0,0,0,0,0,0,0\) (20)

By picking this alignment, \(\Delta=5\), we are picking the sixth vector that went into _A_ which is _v_<sub>3,4</sub>. So, this alignment is checking the orthogonality of _v_<sub>1</sub>_,v_<sub>2</sub>_,v_<sub>3</sub>_,v_<sub>4</sub>. Lets look at a set of non-orthogonal vectors to compare. The vectors _v_<sub>1</sub>_,v_<sub>2</sub>_,v_<sub>1</sub>_,v_<sub>4</sub> are not orthogonal. The vector _v_<sub>1,4</sub> corresponds to \(\Delta=2\).

\((A\&v_1)=0,0,0,0,0,0;1,0,1,0,1,0;0,1,0,0,0,1;1,1,0,1,0,0\) (21)

\((0\&v_2)=1,0,0,0,0,0;1,0,0,0,0;0,0,0,0,0;1\) (22)

\(\text{This alignment}=0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0\) (23)

