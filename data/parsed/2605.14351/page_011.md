\(\langle A^sb,A^tb\rangle=\sum_{j=1}^n|(V^*b)_j|^2p_j^s\bar{p}_j^t.\) (A.1)

This is an atomic disk measure. A Schur triangular form _A=QTQ_<sup>∗</sup> is not enough: the strictly upper triangular part of _T_ produces polynomial factors multiplying _p<sup>t</sup>_, which cannot generally be absorbed into positive scalar atoms.

## Appendix B. IMPLEMENTATION NOTES

For complex-valued dictionaries, one may either work directly with complex conic solvers or split all variables into real and imaginary parts. The epigraph constraint \(a_m\ge|c_m|\) becomes

\(\|(\Re c_m,\unknown c_m)\|_2\le a_m.\) (B.1)

Group penalties over conjugate pairs are handled similarly. When real-valued impulse responses are required, poles are sampled in conjugate pairs and the residues are constrained to be conjugates, or an equivalent real sinusoidal basis is used. The parallel realization can be ill-conditioned when many poles are close; in that case column normalization and post-solve residue rescaling are recommended before applying sparsity penalties.

## REFERENCES

4
Model Output
Impulse Response
1
true ANM
KRM+RED
6
true ANM
KRM+RED
RAF
true ANM
2
KRM
RAF
4
KRM
0.5
KRM
KRM+RED
RAF
2
0
0
0
-2
-2
-0.5
-4
-4
-1
0
20
40
60
80
100
0
5
10
15
20
-1
0
1
4
true ANM
6
1
true ANM
2
RAF
4
RAF
0.5
RAF
2
0
0
Imag
-2
-2
-0.5
-4
-4
-1
0
20
40
60
80
100
0
5
10
15
20
-1
0
1
4
6
1
true
true
RAF
RAF
RAF
2
4
0.5
0
2
0
0
-2
-2
-0.5
-4
-4
-1
0
20
40
60
80
100
0
5
10
15
20
-1
0
1
Time
Time

Fig. 3. Fitting results. Top row: stability prior only. Middle row: pole-sector constraints plus sparsity. Bottom row: RAF with all priors imposed.

