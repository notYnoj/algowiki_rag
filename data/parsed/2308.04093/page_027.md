In the **for** loop iteration of the first stage where _w=w_<sup>∗</sup> and _c=i_ mod _w_, we have \(z^*[i]\in J\) and \(i\in I\). The input matrix \(A_{I\times J}\) to SMAWK encodes the objective values of extending from _j_ by adding multiples of _w_<sup>∗</sup>; in particular, _A_\[_i,z_<sup>∗</sup>\[_i_\]\] equals our optimal objective \(r^*[i]=q\big[z^*[i]\big]+Q_{w^*}\left(\frac{i-z^*[i]}{w^*}\right)\). So SMAWK correctly returns an AP \(P_{z^*[i]}=\big\{c+kw^*,c+(k+1)w^*,\dots,c+\ell w^*\big\}\) that contains _i_ (unless there is a tie _A_\[_i,z_<sup>∗</sup>\[_i_\]\]=_A_\[_i,j_\] for some other \(j\in J\), and _i_ ends up in the AP _P<sub>j</sub>_, but in this case we could have started the proof with (**_x_**<sup>∗</sup>\[_i],z_<sup>∗</sup>\[_i_\]) being this alternative maximizer \(z^*[i]\leftarrow j\) and \(x^*[i]\leftarrow\frac{i-z^*[i]}{w^*}e_{w^*}\)). Since _i\>z_<sup>∗</sup>\[_i_\], we know _i_ is not removed from _P_<sub>_z_<sup>∗</sup>\[_i_\]</sub> at Line 10. This AP _P_<sub>_z_<sup>∗</sup>\[_i_\]</sub> containing _i_ is then added to P.

In the second stage, each AP in P starts in the bucket indexed by the leftmost element of this AP (Line 13), and during the left-to-right linear scan this AP may win over others in its current bucket (at Line 18) and gets advanced to the bucket corresponding to its next element in the AP (at Line 22), or it may lose at Line 18 and be discarded. (Note that any AP can only appear in buckets whose indices belong to this AP.) Our goal is to show that the AP _P_<sub>_z_<sup>∗</sup>\[_i_\]</sub> can survive the competitions and arrive in bucket _B_\[_i_\], so that it can successfully update the answer for _i_ at Line 20.

Suppose for contradiction that _P_<sub>_z_<sup>∗</sup>\[_i_\]</sub> lost to some other AP \(P'_{j^\prime}\) at Line 18 when they were both in bucket _B_\[_i_<sub>0</sub>\] (for some _i_<sub>0</sub>_\<i_). Suppose this AP \(P'_{j^\prime}\) has common difference \(w'\), and corresponds to the objective value \(q[j']+Q_{w^\prime}\left(\frac{i'-j'}{w'}\right)\) for \(i'\in P'_{j^\prime}\). Note that \(i_0\in P'_{j^\prime}\) satisfies \(i_0>j'\) due to Line 10. Note that \(w'\neq w^*\) must hold, since two APs produced in stage 1 with the same common difference cannot intersect (because SMAWK (Theorem A.1) returns disjoint intervals), and hence cannot appear in the same bucket _B_\[_i_<sub>0</sub>\]. Now we consider an alternative solution for index _i_ defined as<tbc>

\((x',j'):=\big(\frac{i_0-j'}{w'}e_{w^\prime}+\frac{i-i_0}{w^*}e_{w^*},j'\big).\)

<tbc>Note that \(j'+\sum_{w\in[w_{max}]}w\cdot x'_w=i\), and it has objective value

\(q[j']+\sum_{w\in[w_{max}]}Q_w(x'_w)\)<br>
\(=q[j']+Q_{w^\prime}\left(\frac{i_0-j'}{w'}\right)+Q_{w^*}\left(\frac{i-i_0}{w^*}\right)\)<br>
\(\ge q\left[z^*[i]\right]+Q_{w^*}\left(\frac{i_0-z^*[i]}{w^*}\right)+Q_{w^*}\left(\frac{i-i_0}{w^*}\right)\text{(since}P_{j^\prime}\text{ wins over}P_{z^*[i]}\text{in bucket}B[i_0]\text{)}\)<br>
\(\ge q\left[z^*[i]\right]+Q_{w^*}\left(\frac{i_0-z^*[i]}{w^*}+\frac{i-i_0}{w^*}\right)+0\text{(by concavity of}Q_{w^*}(\cdot)\text{)}\)<br>
\(=r^*[i].\)

Now there are two cases:

• \(q[j']+\sum_{w\in[w_{max}]}Q_w(x'_w)>r^*[i]\).<tbc>

<tbc>This contradicts the assumption that _r_<sup>∗</sup>\[_i_\] is the optimal objective value for index _i_.<tbc>

• \(q[j']+\sum_{w\in[w_{max}]}Q_w(x'_w)=r^*[i]\).<tbc>

<tbc>Then, \((x',j')\) is also a maximizer for index _i_, but it has support size \(|\text{supp}(x')|=2\) due to \(i>i_0>j'\) and \(w'\neq w^*\), and hence violates the support containment condition \(\text{supp}(x')\subseteq S[j']\) (Eq. (17)). By definition of Problem 1, we are not required to find a maximizer for index _i_.

Hence, we have shown that the AP _P_<sub>_z_<sup>∗</sup>\[_i_\]</sub> can arrive in bucket _B_\[_i_\]. This finishes the proof that Algorithm 1 correctly solves HintedKnapsackExtend<sup>+</sup> for index _i_.

