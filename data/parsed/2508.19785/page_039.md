We now separately study the probabilities in the two summations above. We start by considering Pr(_R=Z_||_B_|=_i_) when \(0\le i\le h-1\), and we observe that the events _R=Z_ and |_B_|=_i_ jointly imply \(B\cup\{x\}\subseteq Z\) since the returned set always includes all elements in \(B\cup\{x\}\). Then, denoting with \(R'\) the set returned by the call to \(\mathtt{RandomSubset}(A\backslash(B\cup\{x\}),h-|B|-1)\) in line 5, we have:

\(Pr(R=Z||B|=i)=Pr(R=Z|B\cup\{x\}\subseteq Z,|B|=i)\cdot Pr(B\cup\{x\}\subseteq Z||B|=i)\)<br>
\(=Pr(R'=Z\backslash(B\cup\{x\})|B\cup\{x\}\subseteq Z,|B|=i)\)<br>
\(\cdot Pr(x\in Z||B|=i)Pr(B\subseteq Z\backslash\{x\}||B|=i,x\in Z)\)<br>
\(=\genfrac(){pt}{2}{N-i-1}{h-i-1}^{-1}\cdot\frac{h}{N}\genfrac(){pt}{2}{h-1}{i}\genfrac(){pt}{2}{N-1}{i}^{-1}\)<br>
\(=\frac{(h-i-1)!(N-h)!}{(N-i-1)!}\cdot\frac{h}{N}\cdot\frac{(h-1)!}{i!(h-i-1)!}\cdot\frac{i!(N-i-1)!}{(N-1)!}=\genfrac(){pt}{2}{N}{h}^{-1}.\)

Next, we consider Pr(_R=Z_||_B_|=_i_) when \(h\le i<n\). Observe that if _R=Z_ and |_B_|=_i_, then we must have \(B\supseteq Z\) and, in particular, \(x\notin Z\). There are exactly \(\genfrac(){pt}{2}{N-1}{i}\) subsets of _A_\\{_x_} of size _i_ and, whenever \(x\notin Z\), \(\genfrac(){pt}{2}{N-h-1}{i-h}\) of such sets are supersets of _Z_. Then, we can write Pr(_R=Z_||_B_|=_i_) as:

\(Pr(R=Z|B\supseteq Z,x\notin Z,|B|=i)\cdot Pr(B\supseteq Z|x\notin Z,|B|=i)\cdot Pr(x\notin Z||B|=i)\)<br>
\(=\genfrac(){pt}{2}{i}{h}^{-1}\cdot\genfrac(){pt}{2}{N-h-1}{i-h}\genfrac(){pt}{2}{N-1}{i}^{-1}\cdot\frac{N-h}{N}\)<br>
\(=\frac{h!(i-h)!}{i!}\cdot\frac{(N-h-1)!}{(i-h)!(N-i-1)!}\cdot\frac{i!(N-i-1)!}{(N-1)!}\cdot\frac{N-h}{N}=\genfrac(){pt}{2}{N}{h}^{-1}.\)

Hence, for any choice of \(i\in\{0,\dots,N-1\}\), we have \(Pr(R=Z||B|=i)=\genfrac(){pt}{2}{N}{h}^{-1}\) which can be substituted back in the above formula for Pr(_R=Z_) to obtain the claimed probability. Indeed:

\(\frac{1}{2^{N-1}}\genfrac(){pt}{2}{N}{h}^{-1}\left(\sum_{i=0}^{h-1}\genfrac(){pt}{2}{N-1}{i}+\sum_{i=h}^{N-1}\genfrac(){pt}{2}{N-1}{i}\right)=\genfrac(){pt}{2}{N}{h}^{-1}\frac{1}{2^{N-1}}\sum_{i=0}^{N-1}\genfrac(){pt}{2}{N-1}{i}=\genfrac(){pt}{2}{N}{h}^{-1}.\) □

We now show that RandomSubset (_A,h_) can be implemented so that it only requires a linear number of random bits, except for a probability of at most \(O(e^{-\sqrt{|S|}})\).

Lemma A.2. _Let A be any set of N elements and_ \(h\in\{0,\dots,N\}\)_. The number of random bits required by_ RandomSubset (_A,h_) _is at most_ 60_N with probability at least_ \(1-O(e^{-\sqrt{N}})\).

Proof. We focus on an execution of RandomSubset (_A,h_) for a sufficiently large value of _N_=|_A_|, and we classify all the resulting recursive calls \(\mathtt{RandomSubset}(A',h')\) into two regimes: we say that a call is _big_ if \(|A'|\ge\sqrt{N}+1\) and _small_ otherwise. We separately analyze these two regimes to provide finer (probabilistic) upper bounds on the size of set _S_ within each regime.

We start by considering big calls. Let _x_ and _B_ be the element and the subset selected in lines 2 and 3 of Algorithm 3, respectively. For each element \(y\in A\backslash\{x\}\), let _I<sub>y</sub>_ be an indicator random variable that is 1 iff \(y\in B\), so that \(|B|=\sum_{y\in A\backslash\{x\}}I_y\). Using \(\mathbb{E}[|B|]=\sum_{y\in S\backslash\{x\}}\mathbb{E}[I_y]=\frac{|A|-1}{2}\) , Hoeffding’s inequality allows us to write:

\(Pr\left(\frac{|S|-1}{3}\le|A|\le\frac{2(|S|-1)}{3}\right)=1-Pr\left(\left||A|-\mathbb{E}\big[|A|\big]\right|\ge\frac{|S|-1}{6}\right)\)<br>
\(\ge 1-2exp\left(-\frac{(|S|-1)^2}{18(|S|-1)}\right)\ge 1-2exp\left(-\frac{\sqrt{N}}{18}\right).\)

