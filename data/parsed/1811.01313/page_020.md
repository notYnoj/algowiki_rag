**Theorem 2** _Assuming Conjecture 1, any randomized algorithm for the external memory sorting problem with_ \(w=\Omega(lgn)\) _bit integers, having error probability at most_ 1/3_, must make an expected_

\(\Omega\big(min\left\{n,\frac{n}{B}\cdot lg_{2M/B}\frac{n}{B}\right\}\big)\)

_I/Os._

## 4.1 Finding Vectors with a Coordinator

In the following we prove Lemma 7. The coordinator wishes to specify (prefix-free) bit strings \(\tau_1,\dots,\tau_n\in\left\{0,1\right\}^w\) to the _n_ players such that \((\tau_1\oplus X_1)\circ\cdots\circ(\tau_n\oplus X_n)\in\mathcal{F}\). The algorithm is straightforward: The coordinator searches for the bit string \(y\in\mathcal{F}\) with the least Hamming distance to \(X=X_1\circ\cdots\circ X_n\). The coordinator then computes \(\tau=y\oplus X\) and breaks \(\tau\) into _w_-bit pieces \(\tau_1,\dots,\tau_n\). The coordinator then sends \(\tau_i\) to player _i_ as follows:

1. The coordinator computes the number of 1’s in \(\tau_i\). Let us denote this by _k<sub>i</sub>_. The coordinator then sends a prefix-free encoding of _k<sub>i</sub>_ using _O_(lg_k<sub>i</sub>_) bits. This is done as follows: First send a unary encoding of \(\left\lceil lgk_i\right\rceil\) by sending \(\left\lceil lgk_i\right\rceil\) 0’s, followed by a 1. Then send \(\left\lceil lgk_i\right\rceil\) bits specifying _k<sub>i</sub>_ in binary.<tbc>

2. If \(k_i\ge 1\), the coordinator now sends \(\left\lceil lg\genfrac(){pt}{2}{w}{k_i}\right\rceil\) bits specifying the positions of the 1’s.<tbc>

<tbc>The number of bits send to player _i_ is thus _O_(lg(_k<sub>i</sub>_+2)+_k<sub>i</sub>_lg(_w/k<sub>i</sub>_)) and the messages are clearly prefix-free. Summing over all players, we get that the total amount of communication is:<tbc>

\(O\left(\sum_{i=1}^nlg(k_i+2)+k_ilg(w/k_i)\right).\)

<tbc>Define _Y_ to be the random variable taking the value _k<sub>i</sub>_ with probability 1_/n_ for every _i_. Then the above equals:<tbc>

\(O\left(n\cdot\mathbb{E}[lg(Y+2)+Ylg(w/Y)]\right).\)

<tbc>Using that lg(_x_+2) and _xlg(w/x_) are concave functions, we get from Jensen’s inequality that this is bounded by:<tbc>

\(O\left(n\cdot(lg(\mathbb{E}[Y]+2)+\mathbb{E}[Y]lg(w/\mathbb{E}[Y]))\right).\)

<tbc>But \(\mathbb{E}[Y]=(\sum_ik_i)/n\). Thus if we define \(K=\sum_ik_i\), we get that the amount of communication is no more than<tbc>

\(O\left(nlg(K/n+2)+Klg(nw/K)\right).\)

<tbc>Taking expectation and again using that lg(_x/n_+2) and (_x/n_)lg(_nw/x_) are concave functions in _x_, we get that the expected amount of communication is:

\(O\left(nlg(\mathbb{E}[K]/n+2)+\mathbb{E}[K]lg(nw/\mathbb{E}[K])\right).\)

Thus what remains is to argue that E\[_K_\] is small. That is, we have to show that the Hamming distance between the uniform random _X_ and the nearest _y_ in F is small in expectation.

We prove this by considering a concrete distribution over pairs (_Z,Y_) where _Z_ is uniform random in {0,1}_<sup>nw</sup>_, _Y_ is uniform random in F and the expected Hamming distance between _Z_<tbc>

