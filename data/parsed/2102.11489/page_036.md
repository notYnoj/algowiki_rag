\(m_\mathrm{red}\ge m_\mathrm{blue}+m/64\) where _m_<sub>red</sub> and _m_<sub>blue</sub> denote the number of `red` and `blue` elements in the input array **X**, respectively.<tbc>

• **Algorithm:**<tbc>

(a) _Base case._ If \(m\le\alpha n\), then return **X**; else continue with the following steps.<tbc>

(b) _Approximate swapper._ Call an (_m,w_)-approximate swapper (see Theorem 9.1) on **X** to swap elements of opposite colors and uncolor them in the process, such that at most _m/_128+_m_<sub>red</sub>-_m_<sub>blue</sub> elements remain colored. Let the outcome be called \(\mathbf{X}'\).<tbc>

(c) _Lossy-extract blue._ Call an \((\alpha,m,w+1)\)-lossy loose compactor to compact \(\mathbf{X}'\) by a half, where the lossy loose compactor treats the `blue` elements as real, and all other elements as fillers (i.e., the loose compactor treats the second bit of the color label as a real-filler indicator, and the first bit of the color label is treated as part of the payload).<br>
Let the outcome be **Y**<sub>blue</sub> whose length is \(\lfloor\mathbf{X}\rfloor/1.9\rfloor\).<tbc>

(d) _Extract red._ Let \(\epsilon'=1/2^{10}\). Apply an \(\epsilon'\)-near-sorter (defined in Section 3.3.1) to the array \(\mathbf{X}'\) treating all `red` elements as smaller than all other elements. Let **Y**<sub>red</sub> be the first \(\lfloor m/32\rfloor\) elements of the resulting near-sorted array. Mark every non-`red` element in **Y**<sub>red</sub> as uncolored, and let \(\mathbf{Y}:=\mathbf{Y}_\mathrm{red}||\mathbf{Y}_\mathrm{blue}\).<tbc>

(e) _Recurse._ Recursively call **Swap**_<sup>n</sup>_(**Y**), and let the outcome be \(\mathbf{Y}'\).<tbc>

(f) _Reverse route._ Reverse the routing decisions made by all selector gates during Steps (c) and (d) (see Remark 4). Specifically,<tbc>

- pad \(\mathbf{Y}'[\): \(\lfloor m/32\rfloor\)] with a vector of fillers to a length of _m_ and reverse-route the padded array by reversing the decisions of Step (d) -- let **Z**<sub>red</sub> be the outcome;<tbc>

**-** reverse-route \(\mathbf{Y}'[\lfloor m/32\rfloor+1:]\) by reversing the decisions of Step (c), resulting in **Z**<sub>blue</sub>.<tbc>

<tbc>Note that both **Z**<sub>blue</sub> and **Z**<sub>red</sub> have length _m_, i.e., length of the input to this recursive call.<tbc>

(g) _Output._ Return **O** which is formed by a performing coordinate-wise select operation between \(\mathbf{X}'\), **Z**<sub>red</sub>, and **Z**<sub>blue</sub>. For every \(i\in[m]\):<tbc>

- if \(\mathbf{X}'[i]\) originally had a `blue` element and the element was not lost during Step (c), then let **O**\[_i_\]:=**Z**<sub>blue</sub>\[_i_\];<tbc>

- if \(\mathbf{X}'[i]\) originally had a `red` element and **Z**<sub>red</sub>\[_i_\] is not a filler, then let **O**\[_i_\]:=**Z**<sub>red</sub>\[_i_\];<tbc>

**-** else let \(\mathbf{O}[i]:=\mathbf{X}'[i]\);<tbc>

Our approximate splitter algorithm actually requires a swapper where elements are of bit-length _w_+1, but for convenience we rename the variable to _w_ in the description of the swapper.

**Remark 4** (Reverse routing details)**.** For every selector gate _g_ in Steps (c) and (d), its reverse selector gate denoted \(g'\) is one that receives a single element as input and outputs two elements; the same control bit _b_ input to the original gate _g_ is used by \(g'\) to select which of the output receives the input element, and the other one will simply receive a filler element. If _g_ selected the first input element to route to the output, then in \(g'\), the input element is routed to the first output.

**Fact 9.4.** _Suppose that n is greater than a sufficiently large constant. If a call to_ **Swap**_<sup>n</sup>_(**X**) _does not hit the base case, then, in the next recursive call to_ **Swap**_<sup>n</sup>_(**Y**) _in Step (e),_ \(m':=|\mathbf{Y}|\le\frac{m}{1.9}+\frac{m}{32}\)_. Therefore, the recursive call will hit the base case after at most_ \(\left\lceil\mathrm{log}_c\frac{1}{\alpha}\right\rceil\) _steps of recursion where c_:=1/(1/1.9+1/32)_\>_1.79.

**Fact 9.5.** _Suppose that n is greater than a sufficiently large constant. If the condition_ \(m_\mathrm{red}\ge\)<tbc>

