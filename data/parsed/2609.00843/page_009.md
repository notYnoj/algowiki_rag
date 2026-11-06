Once the local CDFs have been constructed, the number _N<sub>t</sub>_ of elements in tile _t_ is given by the final local-CDF entry _H_\[_b<sub>t</sub>+w<sub>t</sub>_-1\]. Because the tiles are ordered by value, prefix sums of the numbers of elements in the tiles give the output starting position _O_\[_t_\] of tile _t_. Algorithm 6 shows this operation. For the reason explained in Section 3.3, Algorithm 6 constructs the offsets sequentially.

**Algorithm 6** Construction of tile offsets

procedure BuildTileOffsets(_H,O,R,T,m_)<br>   \(offset\leftarrow 0\)<br>   for t=0 to m-1 do<br>   \(O[t]\leftarrow offset\)<br>   \(offset\leftarrow offset+H[b_t+w_t-1]\)<br>   end for<br>   end procedure

Output generation uses only the local CDFs and does not rescan the input array. Algorithm 7 shows the processing of one tile. First, the local CDF _H_\[_b..b+w_-1\] in global memory is loaded into _C_\[0_..w_-1\] in shared memory. For each output position _p_ within the tile, a binary search finds the smallest _x_ satisfying \(C[x]\ge p+1\), and _b+x_ is written to _B_\[_O_\[_t_\]+_p_\].

**Algorithm 7** Output generation from a local CDF

procedure GenerateOutputFromLocalCDF(_H,O,B,t,b,w_)<br>   Allocate C\[0_..w_-1\] in shared memory<br>   \(C[0..w-1]\leftarrow H[b..b+w-1]\)<br>   \(tileStart\leftarrow O[t]\)<br>   \(tileCount\leftarrow C[w-1]\)<br>   for all \(p\in[0,tileCount)\) in parallel do<br>   \(x\leftarrow min\{j|C[j]\ge p+1\}\)<br>   \(B[tileStart+p]\leftarrow b+x\)<br>   end for<br>end procedure

Like RefHP, the proposed algorithm determines output intervals from a CDF. During output generation, however, it does not compute a prefix maximum over an array of length _n_; instead, it loads a local CDF into shared memory and directly determines output values. When the number of tiles is small, the costs of per-tile kernel launches and binary searches are relatively low, and avoiding a prefix maximum over the entire output array provides a substantial advantage. Histogram construction, however, scans the input array once for every tile, so the scanning overhead increases with the number of tiles _m_. Because each tile scans the entire input array during histogram construction, the amount of data read from the input array increases with the number of tiles. This is the principal performance limitation of the proposed algorithm.

