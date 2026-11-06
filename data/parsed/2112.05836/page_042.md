## 6.14 Putting it all Together

Now that we have proven the above lemmas, we can prove our desired result.

**Reminder of Theorem 6.5.** _If the_ \(k'\)_-OV hypothesis is true for all constants_ \(k'\)_, then for all constant_ \(\epsilon\in(0,1]\) _grammar-compressed k-median edit distance requires_ \(\left(M^{k-1}m\right)^{1-o(1)}\) _time when the alphabet size is_ \(|\Sigma|=\Theta(k)\) _and_ \(m=M^{\epsilon\pm o(1)}\)_. Here, M and m denote the total uncompressed and compressed length of the k input strings respectively._

_Proof._ We will use Lemma 6.27 and Lemma 6.28. Given an instance of (_bk+a(k_-1))-OV we can produce strings _EDOV_<sub>1</sub>(_a,b,k,L),...,EDOV<sub>k</sub>(a,b,k,L_) such that they have length _M=n_<sup>_a+b+o_(1)</sup> and _m=n_<sup>_b+o_(1)</sup>+_n_<sup>1+_o_(1)</sup>=_n_<sup>_b+o_(1)</sup> when \(b\ge 1\).

Our alphabet is of size \(|\Sigma|=O(k)\), so this lower bound applies as long as the size of the alphabet is \(\Theta(k)\).

Now note that _M_<sup>_k_-1</sup>_m=n_<sup>(_k_-1)_a_+(_k_-1)_b+b_</sup>=_n_<sup>(_k_-1)_a+kb_</sup>. So, an algorithm that runs in \((M^{k-1}m)^{1-\epsilon}\) time \(\epsilon>0\) implies an algorithm for (_bk+a(k_-1))-OV that violates our assumption. Thus, _k_-edit distance requires \(\left(M^{k-1}m\right)^{1-o(1)}\) time given the assumption on (_bk+a(k_-1))-OV.

Now we consider a contradiction to our theorem statement. There would be an algorithm running in \((M^{k-1}m)^{1-\gamma}\) time to solve grammar compressed _k_-median edit distance when \(m=M^{\epsilon\pm o(1)}\) and \(\epsilon\in(0,1]\). In the easiest case we can pick an _a,b_ such that \(b/(a+b)=\epsilon\), in this case we are done. For irrational \(\epsilon\) we need to approximate and then pad the strings. Choose an _a_ and _b_ such that \(\epsilon\le b/(a+b)<\epsilon(1+\gamma/2)\). Such _a,b_ exist that are in \(O(\frac{1}{\epsilon\gamma})\). We add a new character 3 to our alphabet. Let \(S'_i=S_i3^x\), where we will set \(x\in[M,M^2]\) later. Note that \(\delta_E(S_1,\dots,S_k)=\delta_E(S'_1,\dots,S'_k)\). Note that the compression of these strings is \(m'=m+lg(x)=\Theta(m)\) where as the length is \(M'=M+x=\Theta(x)\). Choose \(x=m^{1/\epsilon\pm o(1)}=M^{b/(a+b)\cdot 1/\epsilon}\). So now \(m'=M'^{1/\epsilon\pm o(1)}\). Note that \(1\le b/(a+b)\cdot 1/\epsilon\le(1+\gamma/2)\). Now consider running the claimed fast algorithm on our new \(S'_1,\dots,S'_k\) instance. The running time is

\((M'^{(k-1)}m')^{1-\gamma}=O((M^{(1+\gamma/2)(k-1)}m)^{1-\gamma-o(1)}).\)

This running time can be simplified to \(O(M^{(k-1)}m)^{(1+\gamma/2)(1-\gamma-o(1))}\). Note that \((1+\gamma/2)(1-\gamma-o(1))\) is less than 1-_o_(1). This algorithm violates the lower bound for the original _S_<sub>1</sub>_,...,S<sub>k</sub>_ instance. This is a contradiction.

So any algorithm running in \((M^{k-1}m)^{1-\gamma}\) time to solve grammar compressed _k_-median edit distance when \(m=M^{\epsilon\pm o(1)}\) and \(\epsilon\in(0,1]\) violates \(k'\)-OV for some \(k'\) that depends on \(\epsilon,\gamma\). This implies our theorem statement.

Finally we will apply this same lower bound to _k_-center edit distance using a reduction from \[HBGT20\].

## 6.15 k-Center Edit Distance

In Section 3 of \[HBGT20\] they present a reduction from median _k_-edit distance to _k_-center distance \[HBGT20\]. We will restate their reduction here.

Say we are given a _k_-median edit distance instance with _k_ strings _X_<sub>1</sub>_,...,X<sub>k</sub>_ where |_X<sub>i</sub>_|=_N_. Then, as \[HBGT20\] suggest, construct the following strings:

\(Y_1=X_1\$^NX_2\$^N\cdots\$^NX_{k-1}\$^NX_k\)<br>
\(Y_2=X_2\$^NX_3\$^N\cdots\$^NX_k\$^NX_1\)<br>
\(\vdots\)<br>
\(Y_k=X_k\$^NX_1\$^N\cdots\$^NX_{k-2}\$^NX_{k-1}\)

**Claim of Section 3 in \[HBGT20\]:** \(\delta_{CE}(Y_1,Y_2,\dots,Y_k)=\delta_E(X_1,X_2,\dots,X_k)\).

As a quick intuition for this claim, we have to match the \(\$^N\) sections. First note that we can achieve this bound by taking a string _T_ which is one of the median edit distance minimizing strings of the _X<sub>i</sub>_ and creating a center string for the _Y<sub>i</sub>_ strings _C=T_ \(\$^NT\$^N\dots\$^NT\). Now note that the distance to this string from all _Y<sub>i</sub>_ is \(\delta_E(X_1,X_2,\dots,X_k)\). Thus, \(\delta_{CE}(Y_1,Y_2,\dots,Y_k)\le\delta_E(X_1,X_2,\dots,X_k)\). For the<tbc>

