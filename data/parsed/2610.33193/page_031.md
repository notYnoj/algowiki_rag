at random is \(\Omega(n)\), since for an input with exactly _k≈n/_20’s, it collapses \(\genfrac(){pt}{2}{n}{k}\ge(n/k)^k\) different inputs to the single output 0_<sup>k</sup>_1<sup>_n-k_</sup>. As a result, by Proposition 2.20 applied to the whole circuit, any sorting network necessarily releases heat at least \(\Omega(n)\). In this section we show that the Batcher network gates can be assigned heat functions meeting this bound on heat released: _O(n_) (Theorem 5.2). It remains an open question whether entropy production is necessarily \(\Omega(n)\) in any sorting network but we are able to show that the Batcher’s odd-even mergesort network on binary inputs does have cost \(\Omega(n)\) (Theorem 5.4). We then turn to the integer case, where the Landauer cost (i.e. drop in entropy) of a sorting network acting on a uniformly random permutation of {0,1_,...,n_-1} is \(\Theta(nlogn)\). In this case, however, we show in Theorem 5.13 that, when the input is the distribution resulting from picking _n_ elements of an ordered set without replacement uniformly at random, then Batcher’s network releases heat \(\Theta(nlog^2n)\) with optimal heat functions, which is directly proportional to the size of the network. In Theorem 5.18 we leverage a sorting network of Leighton and Plaxton \[LP98\], to obtain a sorting network with size \(\Theta(nlog^2n)\) but only \(\Theta(nlogn)\) heat dissipation. In contrast, by generalizing to a sorting circuit with more than _n_ wires, it _is_ possible to achieve zero circuit entropy production; see Section 6.1.

The Batcher network is illustrated in Figure 2 with _n_=16 inputs. Each vertical line represents a comparator, which sorts two bits, putting the smaller of the two on the "upper" line, i.e., the line with the smaller index, and the larger on the "lower" line. If \(a\le b\) then we say that the comparator gate Comp(_a,b_)=Comp(_b,a_)=(_a,b_). For simplicity in this section, we will assume that the number of sorting inputs _n_ is a power of two.

More formally, we will index wires _w<sub>i</sub>_ for \(i\in\{0,\dots n-1\}\) for _n_ being a power of two. We use \(w(\ell)\) to denote the value stored in wire _w_ after layer \(\ell\). By the definition of Batcher’s, we know that \(w_0(0)\le\dots\le w_{n/2-1}(0)\) and \(w_{n/2}(0)\le\dots\le w_{n-1}(0)\) as these two halves of the input were sorted during the previous recursive step. We denote a comparator gate acting on indices _i_ and _j_ with _i\<j_ as (_i,j_). Let \(k_\ell=log(n)-\ell\). For layer 1 our set of gates is<tbc>

\(G_1=\{(0,n/2),\dots,(n/2-1,n-1)\}.\)

<tbc>The set of gates at layer \(\ell>1\) are<tbc>

\(G_\ell=\{(i,i+2^{k_\ell})|2^{k_\ell}\le i<n-2^{k_\ell}\text{and}\left\lfloor i/2^{k_\ell}\right\rfloor\equiv 1mod2\}.\) (4)

<tbc>To account for the total number of comparators needed, consider first the number _M(n_) in the non-recursive part (layers 1 to log_n_). We have that _M_(2)=1 and<tbc>

\(M(n)=2M(n/2)+n/2-1,\)

<tbc>where the two _M(n/_2) terms account for the separate sorting of odd-numbered bits and even- numbered bits, and the _n/_2-1 accounts for the last layer. Therefore, \(M(n)=\Theta(nlogn)\). Now let _C(n_) be the total number of comparator gates needed to sort _n_=2_<sup>k</sup>_ bits. We have that _C_(2)=1 and for \(n=2^k\ge 4\),

\(C(n)=2C(n/2)+M(n)=2C(n/2)+\Theta(nlogn).\)

Therefore \(C(n)=\Theta(nlog^2n)\).

## 5.2.1 Binary inputs

We first consider the case where the input to be sorted is a length _n_ bitstring selected uniformly at random. It is known that the correctness of a sorting network can be determined by only checking its behavior on such inputs.

