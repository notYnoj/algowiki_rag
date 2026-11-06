## 2.3 The Main Idea: Sample and Round

To begin the discussion of our approaches, notice that it is possible to compute the shortest/longest path on the grid graphs exactly in a divide-and-conquer fashion: Suppose for the sub-problem on (_l,r_\], we want to know the boundary-to-boundary length of the shortest/longest path between \(\langle l,y_l\rangle\) and \(\langle r,y_r\rangle\) for every pair of rows (_y<sub>l</sub>,y<sub>r</sub>_). For a branching factor _M_, we divide the sub-problem into _M_ equal parts (_m<sub>i</sub>,m_<sub>_i_+1</sub>\] for \(m_i=l+i\cdot\frac{r-l}{M}\) and solve them recursively<sup>7</sup>. To find the optimal sub-path from \(\langle l,y_l\rangle\) and \(\langle r,y_r\rangle\), we look for the best _anchors_ (_p(m_<sub>1</sub>)_,p(m_<sub>2</sub>)_,...,p(m_<sub>_M_-1</sub>)) where _p(m<sub>i</sub>_) is the row the path visits in column _m<sub>i</sub>_ (i.e., the unique cell \(\langle m_i,p(m_i)\rangle\) that the sub-path visits). More formally, to compute the length of the shortest path<sup>8</sup> between \(\langle l,y_l\rangle\) and \(\langle r,y_r\rangle\), denoted by ans\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\], we can use the following recursion:

\(\mathrm{ans}[l,y_l,r,y_r]:=\mathrm{min}_\widehat{Y}\sum_{i=1}^M\mathrm{ans}[m_{i-1},\widehat{y}_{i-1},m_i,\widehat{y}_i],\) (1)

where the minimization is over every anchor path defined by some sequence <o>_Y_</o>=(<o>_y_</o><sub>i</sub>) that satisfies

• <o>_y_</o><sub>0</sub>=_y<sub>l</sub>_ and <o>_y_</o><sub>M</sub>=_y<sub>r</sub>_;<tbc>

• For \(1\le i\le M\), \(\left|\overline{y_i}-\overline{y_{i-1}}\right|\le\frac{r-l}{M}\) .

At a high level, the algorithm for constant additive error is very simple: we sub-sample the columns<sup>9</sup> of the (rotated) grid, discarding all but a \(2^{-\mathrm{log}^{\Omega(1)}(n)}\)-fraction (this is where we get our running time saving). Specifically, starting from (0,2_n_\], we recursively partition the x-axis into equal-width intervals, with a branching factor _M_:=polylog(_n_). Ideally, this gives rise to _S_:=log_<sub>M</sub>_(2_n_) _scales_ in the divide-and- conquer recursion tree. Each scale \(s\in[S]\) contains all intervals of width 2_n/M_<sup>_S-s_</sup> on the same level<tbc>

<sup>7</sup>In the actual algorithm we only recurse until reaching a slightly sub-linear size problem (see "rounding threshold for columns" in Definitions 5.1 and 5.2) and then use the standard DP in sub-quadratic time for smaller sub-problems. <sup>8</sup>The computation for longest path follows analogously by replacing min with max. We will highlight the difference between the setting when we discuss going from additive to multiplicative factor approximation. <sup>9</sup>For the sake of the overview, we slightly abuse notation and talk about discarding an interval of (consecutive) columns, by which we simply mean setting all the edge weights between columns in this interval to 0.

t = (n, n)
a = (.8n, 1.4n)
a = (2n, .6n)
Change of coordinates (for convenience)
= (2n, n)
b = (6n, .4n)
b = (n, .8n)
S =

Figure 2: Convenient coordinate system

