<tbc>_Proof._ As in the _k_-LCS Lemma 6.14 consider the _k_-1 lists \(\mathbf{VecS}_{\mathbf{I}_\ell}(L,v_i)\) for \(i\in[1,k-1]\). Additionally, let<tbc>

\(Vec_E(v_k)[j]=\left\{\begin{array}{ c c }
v_k[h] & \text{if}j=h\cdot n^\ell \\
0 & \text{else.}
\end{array}\right.\)

<tbc>We will build our gadgets IED’ and EED’ from these lists. Every entry in these lists is either a zero or a one. We want to force a prefect alignment and check orthogonality of the perfect alignment. That is, we want to hit one value if there exists a \(\Delta_1,\dots,\Delta_{k-1}\) such that<tbc>

\(\sum_{j=0}^{n^\ell(d-1)+1}Vec_E(v_k)[j]\cdot\mathbf{VecS}_{\mathbf{I}_\ell}(L,v_1)[j+\Delta_1]\cdots\mathbf{VecS}_{\mathbf{I}_\ell}(L,v_{k-1})[j+\Delta_{k-1}]=0.\)

<tbc>To do this we will use the very convenient coordinate gadgets, but alter them with a selector. We want the selector gadget to force an alignment of the true correct values. We add a new character 2, this character is just there to be matched in these gadgets. We add another new character 3, which encourages lining up coordinate gadgets. We will set _x_=100|_CGED<sub>i</sub>(b<sub>i</sub>_)|. We want to have enough copies of the _SCSG_ gadgets that lining up real gadgets with each-other is optimal. We set _y_=100_x|SCSG<sub>i</sub>_(2)|, we want enough copies of 3 to force coordinate alignments to be optimal. Finally, our updated coordinate gadgets are below<tbc>

\(CGED'_i(b_i)=3^y\circ(SCSG_i(2))^x\circ CGED_i(b_i).\)

<tbc>Next we need to generate "fake" coordinate gadgets to fill out space, so that any offset will be valid. We add the characters %_<sub>i</sub>_ for \(i\in[1,k]\). The character %_<sub>i</sub>_ will only appear in the _i<sup>th</sup>_ string. This will guarantee these characters are unmatched. A fake gadget will have a selector gadget wrapped around one of these unmatchable characters and a coordinate gadget of a zero:<tbc>

\(F_i=3^y\circ(SCSG_i(\%_i))^x\circ CGED_i(0).\)

<tbc>Let \(f=|\mathbf{VecS}_{\mathbf{I}_\ell}(L,v_i)|-|Vec_E(v_k)|=n^\ell-1\). Now, we will define the three parts of the strings. The section of real gadgets, the section of fake gadgets, and the section of unmatchable characters. We add _k_ new characters #_<sub>i</sub>_, with the intention of making them unmatchable. Let \(z=|CGED'_i(b_i)|=|F_i|\). See Figure 1 for a visual depiction.

\(REAL_i=\circ_{j\in[1,dn^\ell]}(CGED'_i(\mathbf{VecS}_{\mathbf{I}_\ell}(L,v_i)[j]))\text{when}i\in[1,k-1]\)<br>
\(REAL_k=\circ_{j\in[1,n^\ell(d-1)+1]}(CGED'_k(Vec_E(v_k)[j]))\)<br>
\(FAKE_i=F_i^{f(k+1-i)}\)<br>
\(UNMA_i=\#_i^{(k+i+1)zf}.\)

Now that we have defined these useful parts we can define the overall gadgets:

\(IED'_i(L,\ell,v_i)=UNMA_i\circ FAKE_i\circ REAL_i\circ FAKE_i\circ UNMA_i\)<br>
\(EED'(v_k)=UNMA_k\circ FAKE_k\circ REAL_k\circ FAKE_k\circ UNMA_k\)

Now let us consider what happens if there are \((k-1)\ell\) vectors that are orthogonal to _v_<sub>1</sub>_,...,v<sub>k</sub>_ then we want to compute the edit distance. Note that all characters in _UNMA<sub>i</sub>_ will either be deleted or substituted which has an edit distance of one per character. This gives a total edit distance cost of _zfk(k_+5)/2. Let \(p_i=\delta_E(F_1,\dots,F_i)\). Now, on any valid alignment we have 2_f_ fake gadgets completely unmatched, 2_f_ fake gadgets matched with one other fake gadget, 2_f_ fake gadgets matched with two other fake gadgets, etc. Until we get to (_k_-1) fake gadgets matched together at which point we have 3_f_ of these. When the fake gadgets are matched with each other they are also "matched" with the unmatchable characters. Those characters will simply substitute/delete to equal the output string. We have enough unmatchable characters that their length is longer than the overhanging fake characters. So we can be assured no insertions will need to happen. So the edit distance contribution of these is<tbc>

\(fp_{k-1}+\sum_{i=1}^{k-1}2fp_i.\)

<tbc>Now, we have 2_f_ fake gadgets which line up with a mix of fake and real gadgets. Each of these _k_ tuples of lined up gadgets have a contribution of _x(Q+v_) from their _SCSG_ gadgets, and the _CGED_ gadgets<tbc>

