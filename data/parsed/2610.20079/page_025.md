## 9 Conclusion

We turn the communication savings of a finite linear circuit into recursive address-field interchange and combine it with Columnsort and most-significant-digit radix sorting to obtain a deterministic external-memory integer sorting algorithm. Its I/O upper bound asymptotically improves on classical comparison sorting in some parameter ranges. The same finite construction also gives a strict coding advantage in an undirected multiple-unicast network.

Directions for further work include improving the finite coding construction to increase the saving exponent and developing simpler, more efficient algorithmic implementations. It is also natural to ask whether network coding can accelerate other data-movement tasks in a similar way.

## A Buffered I/O and Memory Simulation

### A.1 Simulating sequential tape access

Put _b=Bw_, the number of bits in a disk block. A tape here is a packed bit sequence with one head; an elementary step reads or changes the bit under the head and moves it by at most one position. A fixed alphabet and a fixed number of tracks change the packing density only by a constant factor. This definition does not permit arbitrary jumps to data elsewhere on a tape.

**Lemma A.1** (Buffered tape phases)**.** Fix the number of tapes. A phase of _T_ elementary tape steps, including all head movements, can be simulated with _O(B_) resident words and _O_(1+_T/(Bw_)) block transfers. For _J_ separately activated phases, with total step count _T_, the bound is _O(J+T/(Bw_)), including writing modified (dirty) buffers back to disk.

_Proof._ For each tape, keep the block containing its head and its two neighbors. At activation, load this three-block window, with the current block in the middle. While the head stays in the window, its operations incur no transfers. Upon exit, write back the dirty blocks and load a new window centered on the new current block. The head must move at least _b_ positions between two such exits: it starts somewhere in the middle block and must cross a whole neighboring block before leaving the window. Each replacement uses at most a constant number of transfers. Thus a tape with _T<sub>i</sub>_ head movements costs _O_(1+_T<sub>i</sub>/b_) transfers, including the initial load and final writeback. Summing over the fixed number of tapes proves the first bound. Apply it separately to the _J_ phases for the second. Reversing direction does not invalidate a window, so short alternating accesses to adjacent blocks do not introduce a transfer per tape step.

The stream transformations in Section 6 satisfy the lemma’s hypothesis. In particular, the controlled-shift and scaling procedures of OpenAI [Ope26, Lemmas 3-4] concatenate the work streams for successive fixed-prefix segments; a new segment does not start a new buffer allocation. Their local reversals, head returns, and erasures are included in the linear tape-step bound. Within one recursion node there are only a fixed number of such elementary procedures. Arithmetic on call descriptors uses a fixed number of machine words of width _w_ and free resident computation in our I/O model. Its operands are dimensions, offsets, and addresses bounded by a fixed polynomial in _N_.

