The strict saving is simply 2_v_=222_\>_3_c_=189. Section 5.2 verifies the ranks of the differences between source and sink matrices, and Section 5.3 completes the count.

## 4.3 Using coding to accelerate address interchange

An array element’s _address_ is its position numbered from zero; a consecutive group of digits in its representation is a _field_. Exchanging two fields specifies each element’s new position while keeping the other fields fixed. In Figure 3, the element at position 28 moves to position 42. If its original value is 7, it remains 7 after the move: rearrangement changes positions and preserves values.

Let _H,D_ be the fields to exchange. Split each into _m_ equal short fields and regard the short fields as the coordinates of two vectors. An orthogonal projection _P_ keeps the component in a chosen subspace and removes its perpendicular component; write _I_ for the identity matrix. We call the following address operation a _partial swap_:

\((H,D)\longmapsto\big((I-P)H+PD,PH+(I-P)D\big).\)

It exchanges the components in the image of _P_ and keeps the complementary components fixed. Projection zero does nothing, and projection _I_ exchanges the whole fields. Address arithmetic uses a suitable fixed radix; the stored data remain bits, and all circuit gates still use XOR.

Fixing the address digits before _H_ selects a contiguous _prefix segment_. Distribute these equal- length segments cyclically among the circuit’s _W_ inputs. Each input now holds a _stream_, an ordered sequence of bits on disk, containing 1_/W_ of the original array. A gate’s subspace specifies the same storage order for every incident stream, so XOR of corresponding positions still implements the original gate. For nested subspaces, the rank of the difference of their projection matrices equals the difference of their dimensions. Temporary copies undergo the same changes of storage order and their costs are included.

The XOR circuit ultimately returns every bit to the correct output stream. The source and sink partial swaps compose to the full interchange, so each recovered bit also has its correct new address. Restoring the original segment order removes the circuit’s permutation of streams. Thus the new construction performs the full field interchange directly.

When the projection _P_ has rank _r_, the partial swap decomposes into _r_ operations, each exchanging a one-dimensional component. Each such operation first changes coordinates by a lower- triangular matrix, exchanges one pair of short fields, and undoes the coordinate change. The two coordinate changes use scans, leaving exactly _r_ recursive exchanges. Section 6 gives the matrices and proves the memory bound.

The total is _S_ child exchanges, each on _V/W_ bits and fields 1_/m_ as wide. Ordinary pairwise exchange would use _m_ children on the whole array. Here the total child volume is (_S/W)V\<mV_ , and the stronger inequality \(S/W<m^{1-\varepsilon}\) makes these savings accumulate over levels. Every child again interchanges two equal-width address fields, so the same procedure applies at the next level.<tbc>

Old position 28 0
01 1
10 0
New position 42 0
10 1
01 0

Figure 3: A binary address divided into five fields. The colored fields are interchanged; the gray fields stay in place.

