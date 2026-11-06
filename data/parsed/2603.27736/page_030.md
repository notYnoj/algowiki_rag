3.2. _(Heavy Entries)_ Focus on the row-heavy entries in \(A'\) for now. For each such row-heavy entry (_i,k_) we will update \(A_\mathrm{sm}[i,k]\leftarrow A[i,k]\). Recall that we need to update the respective rank decomposition of _A_<sub>sm</sub> to match these new entries. To this end observe that each row in \(A'_\mathrm{row}\) contains at most _r/q_ distinct entries, so we can trivially compute a rank-(_r/q_) decomposition \((U',V',S')\) of \(A'_\mathrm{row}\). Next we adjust this decomposition by<tbc>

\(U[i,\ell]=U'[i,\ell]-u[i],\)<br>
\(V[\ell,j]=V'[\ell,j]-v[j],\)

leading to a same-rank decomposition \((U,V,S=S')\) of the restriction of _A_ to the row-heavy entries (of \(A'\)). Indeed, for each heavy entry (_i,k_) we have that<tbc>

\(A[i,k]=A'[i,k]-u[i]-v[k]\)<br>
\(=U'[i,S'[i,k]]+V'[S'[i,k],k]-u[i]-v[k]\)<br>
\(=U[i,S[i,k]]+V[S[i,k],k].\)

We repeat the same procedure with the column-heavy entries \(A'_\mathrm{col}\) to update _A_<sub>sm</sub>. Then, symmetrically, we update _B_<sub>sm</sub> and _C_<sub>sm</sub> for all row-heavy and column-heavy entries in \(B'\) and \(C'\). In the upcoming step 4 we will see why this treatment was useful.<tbc>

\(\includegraphics{}\)

<tbc>After we have enumerated all instances in I<sub>unif</sub> in this way, we claim that we have transformed the initial instance in a potential-adjusting manner into

\((\mathcal{I}_\mathrm{reg}\cup\{(A_\mathrm{sm},B,C),(A,B_\mathrm{sm},C),(A,B,C_\mathrm{sm})\},\mathcal{T}_\mathrm{unif}).\)

To see that this is correct take any exact triangle (_i,k,j_) in (_A,B,C_). After step 2, the triangle is part of T<sub>unif</sub> or it appears as an exact triangle in some instance \((A',B',C')\in\mathcal{I}_\mathrm{unif}\). In the former case we are done, so focus on the latter case. We continue with two subcases: If the entries (_i,k),(k,j),(i,j_) are all light in \(A',B',C'\), respectively, then by construction (_i,k,j_) appears as an exact triangle in some instance in I<sub>reg</sub>. Otherwise, if (_i,k_) is row-heavy, say, then (_i,k,j_) appears as an exact triangle in (_A_<sub>sm</sub>_,B,C_).<tbc>

4. _(Recursion)_ We recurse on the three instances (_A_<sub>sm</sub>_,B,C_), (_A,B_<sub>sm</sub>_,C_) and (_A,B,C_<sub>sm</sub>). Recall that we have indeed constructed low-rank decompositions for the three matrices _A_<sub>sm</sub>_,B_<sub>sm</sub>_,C_<sub>sm</sub> as required by the theorem statement. We will soon analyze how small these rank decompositions actually are, and discuss why this recursion leads to a terminating algorithm. Let (I_<sub>A</sub>,_T_<sub>A</sub>),_(I_<sub>B</sub>,_T_<sub>B</sub>),_(I_<sub>C</sub>,_T_<sub>C</sub>_) denote the outputs of the three recursive calls. We return \((\mathcal{I},\mathcal{T})=(\mathcal{I}_A\cup\mathcal{I}_B\cup\mathcal{I}_C\cup\mathcal{I}_\mathrm{reg},\mathcal{T}_A\cup\mathcal{T}_B\cup\mathcal{T}_C\cup\mathcal{T}_\mathrm{unif})\).

This completes the description of the recursive step. In the base case, when _r_=0, one of the matrices contains only \(\perp\)-entries and so we can trivially return \(\mathcal{I},\mathcal{T}\leftarrow\emptyset\). It follows from the in-text explanation that this algorithm is indeed a potential-adjusting reduction (assuming it terminates), and that all resulting instances are regular. It remains to argue that we have constructed sets (I,T) of the claimed sizes.

## Analysis of the Recursion.

The critical part is to analyze the rank decompositions of _A_<sub>sm</sub>_,B_<sub>sm</sub>_,C_<sub>sm</sub>. Note that with each iteration of step 3.2 we increase their sizes by at most 2_r/q_ (namely, plus _r/q_ due to the row-heavy entries, and plus _r/q_ due to the column-heavy entries). Thus, letting _n_=max{_n_<sub>1</sub>_,n_<sub>2</sub>_,n_<sub>3</sub>} and letting \(r'\) denote the final size of the rank decompositions, we have that

\(r'\le\frac{2r}{q}\cdot|\mathcal{I}_\mathrm{unif}|\le O\big(\frac{2r}{q}\cdot|\mathcal{I}_\mathrm{sl}|\cdot t_\mathrm{unif}^{41}\cdot\mathrm{log}^2n\big)\le O\big(\frac{2r}{q}\cdot t_\mathrm{sl}^2\cdot t_\mathrm{unif}^{41}\cdot\mathrm{log}^3n\big).\)

