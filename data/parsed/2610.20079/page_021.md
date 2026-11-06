5. Sort each column.<tbc>

6. Prepend _r/_2 negative sentinels and append _r/_2 positive sentinels, shifting column boundaries by half a column. There are now _s_+1 columns, each still of length _r_.<tbc>

7. Sort these _s_+1 columns.<tbc>

8. Delete the first and last _r/_2 records.

Negative sentinels precede every ordinary record, and positive sentinels follow every ordinary record. A two-bit tag distinguishes the three types. All sentinels of one type use the same canonical record. Recursion reuses the same tag and removes exactly the multiplicity of sentinels introduced by the current call.

The parameters satisfy even _r_, _s|r_, and \(r\ge 2s(s+1)\). First consider zero-one inputs. After step 1, write the number of zeros in original column _c_ as _Z<sub>c</sub>=a<sub>c</sub>s+b<sub>c</sub>_, with \(0\le b_c<s\). Since _s|r_, step 2 sends _a<sub>c</sub>_+**1**_<sub>d\<b<sub>c</sub></sub>_ zeros from this column to new column _d_. Summing over the _s_ original columns, the new zero counts _z<sub>d</sub>_ satisfy \(z_\mathrm{max}-z_\mathrm{min}\le s\).

After step 3, every entry in a row below _z_<sub>min</sub> is zero, and every entry in a row at least _z_<sub>max</sub> is one. The inverse permutation moves position _dr+q_ to _sq+d_, so after step 4 all possible disorder is confined to the half-open interval

\(I=[sz_\mathrm{min},sz_\mathrm{max}),|I|\le s^2\le r/2;\)

all entries before _I_ are zero, and all entries after it are one. Step 5 preserves these outside regions, since sorting within a column preserves its all-zero prefix and all-one suffix. If _I_ is empty or lies in a single old column, the array is now sorted. Otherwise, _I_=[_A,E_) crosses exactly one old column boundary _b=kr_, and \(E-A\le r/2\) gives \(I\subseteq[b-r/2,b+r/2)\). Prepending half a column of negative sentinels in step 6 moves this interval into the single new column [_b,b+r_). Sorting that column in step 7 therefore sorts the entire padded sequence, including the boundary case |_I_|=_r/_2.

For general ordered records, an inversion in the padded output would admit a nondecreasing threshold map taking its two values to 1 followed by 0, with negative and positive sentinels mapped to 0 and 1. This map commutes with fixed rearrangements and with the ordered value sequence produced by each column sort, contradicting the zero-one case. Stability of column sorting is not needed. Every sort and rearrangement preserves the multiset of records. Step 8 removes _r/_2 records from each end of the sorted sequence, exactly cancelling the added sentinel multiplicities. Even if the input already contains sentinels with the same tags, cancellation by multiplicity preserves the original multiset; no recursion-level tags are needed, and no ordinary records are removed. The additional suffix of positive padding is removed by its exact multiplicity in the same way. The output is therefore a sorted permutation of the input.

Since _rs_=2<sup>4_t_</sup>, writing record addresses as four fields of _t_ bits makes \(\pi\) the rotation \([x_1,x_2,x_3,x_4]\mapsto[x_4,x_1,x_2,x_3]\). Interchanging fields 3,4, then 2,3, then 1,2 implements \(\pi\); the reverse sequence implements \(\pi^{-1}\). The two permutations therefore need six interchanges in total, and all remaining movement consists of scans. A record’s internal bits move together as an unchanged suffix, without storing a permutation table.

## 7.2 The Local Sorting Bound

Implement column sorts recursively. Since the input has at most the square of memory size, a constant number of reductions in column length suffices to reach an in-memory problem.

