## Correctness.

First, it is clear that the algorithm terminates after at most \(|\mathcal{S}|\le O(s\mathrm{log}n)\) rounds. Indeed, in each round we decrease |_I_| by at least \(|G(S)|\ge|I|/(16s)\), so after _O(s_) rounds the size of |_I_| has at least halved, and after _O(s_log_n_) rounds the remaining set _I_ must be empty.

It remains to prove the key claim that whenever |_G(S_)|_\<|I|/_(16_s_) we can find some \(j\in[r]\) with a potential increase of at least \(\phi(S\cup\{j\})-\phi(S)\ge|I|/(8r)\). In the construction of _S_ the initial potential \(\phi(\emptyset)\) is zero and it stays nonnegative throughout, thus we can bound the number of bad items by:

\(|B(S)|=2s\cdot(|G(S)|-\phi(S))\le 2s\cdot|G(S)|\le\frac{|I|}{8}.\)

It follows that almost all items are undecided:<tbc>

\(|U(S)|=|I|-|B(S)|-|G(S)|\ge|I|-\frac{|I|}{8}-\frac{|I|}{16s}\ge\frac{3|I|}{4}.\)

<tbc>Now pretend that we sample an element \(j\in[r]\) uniformly at random. On the one hand, for each undecided item \(i\in U(S)\) the probability that _i_ becomes good in \(S\cup\{j\}\) is exactly 1_/r_. On the other hand, for each good item \(i\in G(S)\sqcup U(S)\) the probability that _i_ becomes bad in \(S\cup\{j\}\) is at most _s/r_, and thus:<tbc>

\(\mathbb{E}[|G(S\cup\{j\})|-|G(S)|]\ge\frac{|U(S)|}{r}-\frac{s|G(S)|}{r}\ge\frac{3|I|}{4r}-\frac{s|I|}{16rs}\ge\frac{5|I|}{8r}.\)

<tbc>At the same time, the probability that any item _i_ becomes bad is at most _s/r_, hence<tbc>

\(\mathbb{E}[|B(S\cup\{j\})|-|B(S)|]\le\frac{s|I|}{r}.\)

<tbc>It follows that

\(\mathbb{E}[\phi(S\cup\{j\})-\phi(S)]=\mathbb{E}\left[|G(S\cup\{j\})|-|G(S)|-\frac{|B(S\cup\{j\})|-|B(S)|}{2s}\right]\ge\frac{5|I|}{8r}-\frac{s|I|}{2rs}=\frac{|I|}{8r}.\)

In particular, there exists an element \(j\in[r]\) so that by adding _j_ to _S_ the potential would increase by at least |_I_|/(8_r_).

## Efficient Implementation.

We now turn to the problem of efficiently constructing the set _S_. Specifically, we give an efficient algorithm that, while |_G(S_)|_\<|I|/_(16_s_), finds some \(j\in[r]\) with a potential increase of at least \(\phi(S\cup\{j\})-\phi(S)\ge|I|/(8r)\).

We rely on some preprocessing. If necessary increase _r_ to a power of 2. Recall that a _dyadic_ interval \(J\subseteq[r]\) is a set of the form \(a2^\ell+\{1,\dots,2^\ell\}\) for some \(0\le\ell\le\mathrm{log}r\) and \(a\in\{0,\dots,r/2^\ell-1\}\). In the preprocessing phase we compute and store, for all \(i\in[n]\) and all dyadic intervals \(J\subseteq[r]\), the sizes \(|C_i\cap J|\) and \(|\{x_i\}\cap J|\). With access to this data we can, given any sets \(G,U\subseteq[n]\) and any dyadic interval \(J\subseteq[r]\), evaluate the following quantity in time _O(n_):<tbc>

\(E_J(G,U)=\frac{1}{|J|}\left(\sum_{i\in U}|\{x_i\}\cap J|-\sum_{i\in G}|C_i\cap J|-\frac{1}{2s}\sum_{i\in G\cup U}|C_i\cap J|\right).\)

<tbc>The key here is that \(E_J(G(S),U(S))=\mathbb{E}[\phi(S\cup\{j\})-\phi(S)]\), where _j_ is sampled uniformly random from _J_. Indeed, by the same argument as before we have that

\(E_J(G(S),U(S))=\mathbb{E}\left[\sum_{i\in U(S)}|\{x_i\}\cap\{j\}|-\sum_{i\in G(S)}|C_i\cap\{j\}|-\frac{1}{2s}\sum_{i\in G(S)\cup U(S)}|C_i\cap\{j\}|\right]\)<br>
\(=\mathbb{E}\left[|G(S\cup\{j\})|-|G(S)|-\frac{|B(S\cup\{j\})|-|B(S)|}{2s}\right]\)<br>
\(=\mathbb{E}[\phi(S\cup\{j\})-\phi(S)].\)

