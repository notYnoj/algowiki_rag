be the vector _v<sub>k</sub>_ but an added last index \(v_k^*[d+1]=0\). Now we add additional characters 5 and 4. We add copies where \(p=100|IED'_i(L,\ell,v'_i)|\) and _q_=10_p_. Now we generate the following:

\(IED_i(L,\ell,v_i)=5^q4^pIED'_i(L,\ell,v'_i)4^p5^q\)<br>
\(EED(v_k)=5^qEED'(v_k^*)4^pEED'(u')5^q.\)

Here we match up the 5 characters. Finally, we must match the 4_<sup>q</sup>_ symbols. There will be _q_ unmatched 4 symbols. Finally, we will have \(|EED'(v_k^*)|=|EED'(u')|\) unmatched symbols no matter what. Now, how much comes from matching the \(IED'\) and \(EED'\) gadgets? If there are \((k-1)\ell\) vectors are orthogonal to _v_<sub>1</sub>_,...,v<sub>k</sub>_ then the cost is _C_. If there aren’t then the cost of matching the symbols to \(EED'(u')\) instead is _C+C_<sup>+</sup>-_C_<sup>-</sup>. So, \(D=C+q+|EED'(v_k^*)|\), and _w=C_<sup>+</sup>-_C_<sup>-</sup>.

For the size of the SLP we are doubling the number of \(EED'\) gadgets, and we are adding in the 5 and 4 symbols. So the total size should be \(O(2xd+nd+\ell lg(n)+7x(lg(p)+lg(q)))\). Given the size of _p_ and _q_ this gives: _O(xd+nd+x_lg(_n_)).

For the length of the strings we have at most \(O(dn^\ell)\) coordinate gadgets and the number of unmatched symbols is \(O(dn^\ell)\). Note that the size of coordinate gadgets is constant when _k_ is constant and _d=n_<sup>_o_(1)</sup>. So the total length of our generated strings _IED_ and _EED_ is \(O(n^{\ell+o(1)})\).

Now that we have generated interleave vector gadgets we will put multiple copies of them and align them. We want to set this up using the same ‘sliding pyramid’ set up as we used for the interleave gadgets.

## 6.13 Aligning Interleave Vector Gadgets

For aligning our gadgets we generalize the idea from \[HBGT20\] for aligning gadgets. First, we create a fake list of vectors _F_ that is _n_ vectors of dimension _d_ where every entry of the vectors is 1. Then we create "fake" versions of the alignment and empty vector gadgets, build from _F_ instead of _L_. We concatenate the "real" \(IED'\) and \(EED'\) gadgets with many matchable symbols in between. We surround these real gadgets with our "fake" gadgets. We also build a "pyramid" that allows the strings to have any valid alignment of the real gadgets while having the same number of matches of the fake gadgets. Around these we put an additional number of unmatchable characters (characters that are unique to each set). See Figure 1 for a depiction. These fake gadgets allow for any choice of alignment of the real gadgets to have the same value of matches outside of the _k_ gadgets we are matching with the alignment.

We start by proving we can create strings such that _k_-edit distance can be used to detect (_a(k_-1)+_bk_)- _OV_s.

**Lemma 6.27.** _Let a,b, and k be positive constant integers. Let L be a list of n length d vectors, where d=n_<sup>_o_(1)</sup>.

_There are k strings EDOV<sub>i</sub>(a,b,k,L_) _such that:_

\(\delta_E(EDOV_1(a,b,k,L),\dots,EDOV_k(a,b,k,L))\left\{\begin{array}{ c c }
\ge E & \text{\textit{if there is a}}(a(k-1)+bk)\text{\textit{-OV in}}L \\
\le E-1 & \text{\textit{else}}
\end{array}\right.\)

_The length of each of these strings is O(n_<sup>_a+b+o_(1)</sup>) _with an alphabet of size O(k_).

_Proof._ We are given as input a (_a(k_-1)+_bk_)-OV instance. Say the list is _L_. It contains _n_ zero one vectors of length _d_.

We define some new symbols. We add a new symbol $, we will use this to encourage matching in lined up sections. We will also add %<sub>_i_</sub> symbols for \(i\in[1,k]\). A symbol %<sub>_i_</sub> appears only in string _i_, thus it can not be matched, it must be deleted or substituted.



Figure 1: A visual depiction of the structure of our alignment. This is using the ideas from \[HBGT20\]. The dark blue section is a depiction are the real gadgets. The light-gray section are the "fake" gadgets. The white sections are unmatchable characters (a distinct character in each string).

