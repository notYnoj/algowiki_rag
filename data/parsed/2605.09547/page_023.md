_Proof of Theorem 5.1._ We round \(\tau_e\) to nearest \((1+\epsilon')^i\) for some integer _i_, which we are guaranteed we can query for each edge we receive from the stream. The rounding to \((1+\epsilon')^i\) discretizes the vector \(\widetilde{\tau}\) which will later allow us to project the vector into a smaller dimensional space.

We use \(\text{round}_{1+\epsilon^\prime}(\tau_e)\) to denote the number after rounding \(\tau_e\). We have \(n/m\le\tau\le 1\), so there are at most \(O(\epsilon'^{-1}logm)\) possible values. Formally speaking, let _I_ be defined as<tbc>

\(I:=\{i\in\mathbb{Z}|n/m\le(1+\epsilon')^i\le 1\}\)

<tbc>Then,

\(|I|=O(\epsilon'^{-1}logm)\)

We also round _v<sub>e</sub>_ to nearest \(j\cdot\epsilon'\) for some integer _j_. Let us use \(\text{round}_{\epsilon^\prime}(v_e)\) to denote the number after rounding _v<sub>e</sub>_.

We have \(-1\le v\le 1\) so there are at most \(O(\epsilon'^{-1})\) possible values. Formally speaking, we define set _J_ as follows<tbc>

\(J:=\{i\in\mathbb{Z}|0\le j\cdot\epsilon'\le 2\}\)

<tbc>Then

\(|J|=O(\epsilon'^{-1})\)

Let _k_ be the number of possible pairs \((i,j)\in I\times J\).

Using the the above simple argument, we know the maximum number of groups is

\(k=|I|\times|J|\)<br>
\(=O(\epsilon'^{-1}logm)\cdot O(\epsilon'^{-1})\)<br>
\(=O(\epsilon'^{-2}logm)\)

Let \(p:E\rightarrow[k]\) be the function that for any edge _e_ returns the group we rounded to.

Throughout our pass of the stream, we count how often we round to each pair (_i,j_), which takes \(k=O(\epsilon'^{-2}logm)\) space and _O(mT_) time.

In Lemma 5.3 let \(\overline{g}\in\mathbb{R}^k\) be the vector that counts how often we rounded to each group. Let \(\overline{h},\overline{v}\in\mathbb{R}^k\) such that<tbc>

\(f(\text{round}_{\epsilon^\prime}(v_e))=\overline{h}_{p(e)}\)

<tbc>and<tbc>

\(Clog(4m/n)\cdot\sqrt{\text{round}_{1+\epsilon^\prime}(\tau_e)}=\overline{v_{p(e)}}.\)

<tbc>Then by Lemma 5.3 and Definition 4.6 the maximizer<tbc>

\(\overline{u}=argmax_{\overline{w}\in\mathbb{R}^k:\|\overline{f}\overline{vw}\|_2+\|\overline{w}\|_\infty\le 1}\langle\overline{hf},\overline{w}\rangle\)

<tbc>has the property

\(\overline{u}_{p(e)}=\left(argmax_{w:\|w\|_{(\text{round}_{1+\epsilon^\prime}(\tau))+\infty}\le 1}\langle w,f(\text{round}_{\epsilon^\prime}(v))\rangle\right)_e=\left((f(\text{round}_{\epsilon^\prime}(v))^{b(\text{round}_{\epsilon^\prime}(\tau))}\right)_e=:g_e\)

We can use Lemma 5.2 to compute this <o>_u_</o> in \(O(klogk)=\widetilde{O}(1)\) time.

**Query** Now consider the case where we want to query _g<sub>e</sub>_ for a given edge _e_. To do this, we compute _p(e_), which requires computing _v<sub>e</sub>_ and \(\tau_e\) and rounding them. Then we return <o>_u_</o><sub>_p(e_)</sub>. In total, this takes _T+O_(1) time.

