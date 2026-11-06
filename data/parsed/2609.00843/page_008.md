**Algorithm 4** Overview of RT-CDF

**Require:** Input array _A_\[0_..n_-1\], range size _R_, and tile width _T_

**Ensure:** Sorted array _B_\[0_..n_-1\]

1: \(m\leftarrow\lceil R/T\rceil\)

2: \(H[0..R-1]\leftarrow 0\)

3: **for all** \(t\in[0,m)\) **in parallel do**

4: BuildTileHistogram(_A,H,n,b<sub>t</sub>,w<sub>t</sub>_)

5: **end for**

6: **for all** \(t\in[0,m)\) **in parallel do**

7: InclusiveScanInPlace(\(H[b_t..b_t+w_t-1]\)) \(\triangleright\) Construct a local CDF

8: **end for**

9: BuildTileOffsets(_H,O,R,T,m_)

10: **for** \(t\in[0,m)\) **do**

11: GenerateOutputFromLocalCDF(_H,O,B,t,b<sub>t</sub>,w<sub>t</sub>_)

12: **end for**

13: **return** _B_

Algorithm 5 shows histogram construction for one range tile. Each thread block has an array _S_\[0_..w_-1\] of tile width _w_ in shared memory. After initializing _S_ to zero, the threads scan multiple elements of the input array _A_. Only when input value _A_\[_i_\] belongs to the current tile \[_b,b+w_\] do they perform `atomicAdd` on _S_\[_A_\[_i_\]-_b_\]. The histogram obtained within each block in shared memory is finally added to _H_\[_b..b+w_-1\] in global memory.

After histogram construction is complete, prefix sums are computed over _H_\[_b..b+w_-1\], and the result is written back to the same region. This produces the local CDF for the range tile.

**Algorithm 5** Histogram construction for one range tile

1: **procedure** BuildTileHistogram(_A,H,n,b,w_)

2: Allocate _S_\[0_..w_-1\] in shared memory

3: \(S[0..w-1]\leftarrow 0\)

4: **for all** \(i\in[0,n)\) **in parallel do**

5: \(x\leftarrow A[i]-b\)

6: **if** \(0\le x<w\) **then**

7: `atomicAdd`(_S_\[_x_\],1)

8: **end if**

9: **end for**

10: **for all** \(x\in[0,w)\) **in parallel do**

11: `atomicAdd`(_H_\[_b+x_\]_,S_\[_x_\])

12: **end for**

13: **end procedure**

