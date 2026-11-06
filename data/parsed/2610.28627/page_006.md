occupy different positions; the next step lets us align each target with the sources, which are Full in the first _d_ variables and Mid in the last _d_.)

### From SL-PP to PP.

So far, the same-left polynomial packing (SL-PP) computes _w_ retained targets sharing one left input _A_. We now want independent pairs _A<sub>i</sub>,B<sub>i</sub>_. Write each right input as

\(B_i=[B_{i,0}\cdots B_{i,w-1}],\)

where the brackets denote horizontal concatenation of column blocks in every coefficient matrix. Thus group _i_ consists of the blocks of one _B<sub>i</sub>_, all multiplied by the same _A<sub>i</sub>_. We batch the _A<sub>i</sub>_ into one auxiliary univariate polynomial \(A(\xi)\) satisfying _A(i_)=_A<sub>i</sub>_. For each _i_, encode the column blocks _B<sub>i,j</sub>_ in a univariate polynomial \(B'_i(\xi)\) satisfying \(B'_i(i+\varepsilon j)=B_{i,j}\). Both encodings have degree at most _w_-1, so the requested coefficients of \(A(\xi)B'_i(\xi)\) are polynomials of degree at most 2_w_-2 in \(\xi\). We recover these polynomials by interpolation from 2_w_-1 common evaluation points. Fix one such point _k_. We need the requested coefficients of the products \(A(k)B'_0(k),\dots,A(k)B'_{w-1}(k)\). Their right inputs differ, but their left input is the single value _A(k_) of the polynomial encoding all the _A<sub>i</sub>_. Thus one application of the same-left packing computes all these products’ requested coefficients modulo \(\varepsilon\). We repeat this for each of the 2_w_-1 evaluation points; _A(k_) may change between applications. Evaluating the recovered polynomials at \(i+\varepsilon j\) gives the requested coefficients of _A<sub>i</sub>B<sub>i,j</sub>_ modulo \(\varepsilon\), since \(A(i+\varepsilon j)\equiv A_i(\mathrm{mod}\varepsilon)\).<sup>2</sup> Concatenating these output blocks recovers the requested coefficients of _A<sub>i</sub>B<sub>i</sub>_ for each _i_. (OpenAI \[Ope26a\] proves a related separation lemma using finite Fourier projection and a weight degeneration.)

### A Strassen-like identity.

Transposing the matrix products gives a row-reduction gadget. Exchanging the left-input and output roles, by transposing the corresponding encoding and decoding maps, gives an inner-dimension reduction. Combining these with the column reduction gives one gadget that reduces all three matrix dimensions simultaneously. The resulting family is ordinary matrix multiplication at _a=b_=1, is symmetric in _a,b_ under fixed coefficient permutations, and at _a=b=L_ can be computed using _O(L_<sup>6_d_</sup>) matrix multiplications. We can therefore compose a step increasing _b_ with one increasing _a_: for _d=c_<sup>3</sup>, one round increases both lengths by a factor approaching 1+3_/c_, reduces each matrix dimension by approximately (1+2_/c_)<sup>4_d_</sup>, and multiplies the number of remaining products by at most 64. The exponent approaches

\(\frac{\mathrm{log}64+6d\mathrm{log}(1+3/c)}{4d\mathrm{log}(1+2/c)}\longrightarrow\frac{9}{4}.\)

After finitely many rounds, amplification and constant-coefficient interpolation give a fixed exact rational identity with this saving. Clearing its denominators and applying ordinary block recursion gives our integer-arithmetic algorithm.

## 2 Polynomial packings

We now define packing and the two operations used to build larger packings. We then construct the univariate gadgets, combine them across variables, and give their targets independent left inputs. We first fix notation for polynomials, linear maps, and their matrix inputs.

<sup>2</sup>The formal proof replaces the original packing’s parameter by \(\varepsilon^w\), ensuring that divisions by \(\varepsilon\) in the right-input encoding leave the decoded error divisible by \(\varepsilon\).

