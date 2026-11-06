_(ii) on each pair of windows uses the common subsequence length from M._

_The algorithm runs in time_ |_W<sub>A</sub>_||_W<sub>B</sub>|._

_Proof._ The proof is based on a classic DP. Define _D_\[_i_\]\[_j_\] which stores the size of the solution ending at windows \(w_i\in A\) and \(w_j\in B\). We then can update the size of the solution for each pair in time _O_(1) which gives us a solution in time _O_(|_W<sub>A</sub>_||_W<sub>B</sub>_|).

