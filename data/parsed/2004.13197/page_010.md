_Proof._ In both cases, we count the total number of possible output permutations and the maximum permutations achievable during a single I/O, or during the input of one element (_w/B_ I/Os), whichever is larger.

1. \(1\le w<B\): Assume that _w_ divides _B_. In a linear scan, we can internally sort every block, which restricts the possible output permutations to<tbc>

<tbc>\(\frac{(V/w)!}{((B/w)!)^{V/B}}.\)<tbc>

<tbc>When a block is input, there are at most (_M-B)/w_ sorted elements in memory. The incoming block contains _B/w_ sorted elements, so the number of remaining output permutations reduces by at most a factor of<tbc>

<tbc>\(\genfrac(){pt}{2}{(M-B)/w+B/w}{B/w}=\genfrac(){pt}{2}{M/w}{B/w}.\)<tbc>

<tbc>Thus we get that the algorithm requires at least<tbc>

<tbc>\(\Omega\left(\frac{log\left((V/w)!/((B/w)!)^{V/B}\right)}{log\genfrac(){pt}{2}{M/w}{B/w}}\right)\)<tbc>

<tbc>block transfers. Using the same bounds for \(\genfrac(){pt}{2}{n}{k}\) as in Lemma 5, we get the desired bound.<tbc>

2. \(w\ge B\): Assume for simplicity that _w_ is an integer multiple of _B_. In this case, there are (_V/w_)! possible output permutations. One can scan every chunk of size _M_, but this does not change the bound we present asymptotically ( log<sub>_M/w_</sub>_V/w_ changes to log<sub>_M/w_</sub>_V/M_).<tbc>

<tbc>When an element is input, there are at most (_M-w)/w_=(_M/w_)-1 (sorted) elements in memory. The input of an element costs _w/B_ I/Os, and this element can go into any one of _M/w_ positions between the elements in memory. Hence the maximum branching factor for one element input is _M/w_.<tbc>

<tbc>This implies that the number of element inputs is<tbc>

<tbc>\(\Omega\left(\frac{(V/w)log(V/w)}{log(M/w)}\right)=\Omega\left(\frac{V}{w}log_{M/w}\frac{V}{w}\right),\)<tbc>

<tbc>and multiplying by the cost of every large element input (_w/B_) gives us the claimed bound.<tbc>

