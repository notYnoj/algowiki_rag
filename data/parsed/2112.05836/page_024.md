**Definition 6.7.** Let _L_ be the list of vectors to a _k_-OV instance. Let |_L_|=_n_.

We define the serial version as:<tbc>

\(\mathbf{String}_{\mathbf{B}_\ell}(L)=\circ_{j_1\in[1,n]\dots,j_\ell\in[1,n]}\left(\circ_{i=1}^dL[j_1][i]\cdot L[j_2][i]\cdots L[j_\ell][i]\right).\)

<tbc>Note that this is equivalent to<tbc>

\(\mathbf{String}_{\mathbf{B}_\ell}(L)=\circ_{j\in[1,n^\ell]}\circ_{i\in[1,d]}\mathbf{List}(L)[j][i].\)

<tbc>We define the interleaving version as:<tbc>

\(\mathbf{String}_{\mathbf{I}_\ell}(L)=\circ_{i=1}^d\left(\circ_{j_1\in[1,n]\dots,j_\ell\in[1,n]}L[j_1][i]\cdot L[j_2][i]\cdots L[j_\ell][i]\right).\)

<tbc>Note that this is equivalent to

\(\mathbf{String}_{\mathbf{I}_\ell}(L)=\circ_{i\in[1,d]}\circ_{j\in[1,n^\ell]}\mathbf{List}(L)[j][i].\)

So the difference between these versions is really just what order we represent the vectors. But crucially if there is a particular vector in **List**(_L_) that is of interest, this will appear in different places. In \(\mathbf{String}_{\mathbf{B}_\ell}(L)\) a vector \(\vec{v}=\mathbf{List}(L)[i]\) appears as bits \([i\cdot d,(i+1)\cdot d-1]\). Where as in \(\mathbf{String}_{\mathbf{I}_\ell}(L)\) the vector \(\vec{v}=\mathbf{List}(L)[i]\) appears as bits _i,i+n<sup>k</sup>,...,i_+(_d_-1)_n<sup>k</sup>_.

We give one final version that merges a single vector with the interleaved representation.

**Definition 6.8.** We will expand the previous definition of an interleaved string to allow a merge with a single other vector. Recall that

\(\mathbf{String}_{\mathbf{I}_\ell}(L)=\circ_{i\in[1,d]}\circ_{j\in[1,n^\ell]}\mathbf{List}(L)[j][i].\)

Recall that for a vector _u_=**List**(_L_)\[_j_\] it is represented in bits _j,j+n<sup>k</sup>,...,j_+(_d_-1)_n<sup>k</sup>_ in \(\mathbf{String}_{\mathbf{I}_\ell}(L)\).

We will define

\(\mathbf{Vec}\mathbf{S}_{\mathbf{I}_\ell}(L,v)=\circ_{i\in[1,d]}\circ_{j\in[1,n^\ell]}\mathbf{List}(L)[j][i]v[i].\)

Note that now if we take bits \(j,j+n^\ell,\dots,j+(d-1)n^\ell\) we give a vector _w_ such that _w_\[_i_\]=_u_\[_i_\]_v_\[_i_\] where _u_=**List**\[_j_\].

## 6.4 Intuition for our Reduction

We will describe at a high level the reduction of \[ABBK17\] and the idea for generalizing it. In this section we will informally explain how to use the serial and interleaved representations of the vectors to build a reduction from SETH to compressed _k_-LCS. We hope to build understanding for what the different levels of alignment gadgets are doing through small examples and intuition.

### 6.4.1 Why We Care About Lining up the Strings

Lets say we have a representation \(\mathbf{String}_{\mathbf{I}_\ell}(L)\) and we have a single vector, _v_ of length _d_. We create a new vector \(\hat{v}\) where \(\hat{v}[i\cdot n^\ell]=v[i]\) and otherwise \(\hat{v}\) is zero. \(\hat{v}\) will have length \(n^\ell(d-1)+1\).

Now we will note the following: the locations of the bits in \(\hat{v}\) have exactly the offsets that single vectors do in \(\mathbf{String}_{\mathbf{I}_\ell}(L)\)! So, if we consider sub-string \(\mathbf{String}_{\mathbf{I}_\ell}(L)[i,i+n^\ell(d-1)]\) then _v_ forms an orthogonal \(\ell+1\) tuple with the vectors represented by \(\mathbf{List}(L)_\ell[i]\) if \(\hat{v}\) is orthogonal to \(\mathbf{String}_{\mathbf{I}_\ell}(L)[i,i+n^\ell(d-1)]\). This is why we care about offsets. The next few subsections will simply be building the gadgets necessary to get this "perfect alignemnt" and the gadgets needed to represent _k_-OV coordinates in the edit distance setting.

### 6.4.2 The Case of LCS With Two Strings

How did all of this work in \[ABBK17\]? Start with _k_-OV. Now consider a _k_<sub>1</sub> and _k_<sub>2</sub> that have this property: _k=k_<sub>1</sub>+2_k_<sub>2</sub>. They then create three sets: _A_ represents _k_<sub>1</sub> vectors at once, _B_ represents _k_<sub>2</sub> vectors at once and _C_ represents _k_<sub>2</sub> vectors at once. We will give a text explanation and then give a small example.

For _C_ they create its string _S<sub>C</sub>_ by taking **List**(_L_)<sub>_k_<sub>2</sub></sub> and making \(Y[i]=\mathbf{List}'_{k_2}(L)[i]\). That is they pad the vector with _n_<sup>_k_<sub>1</sub></sup>-1 zeros after each entry in the original vector.

