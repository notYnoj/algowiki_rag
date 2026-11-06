## 6 Longest Increasing Subsequence

We outlined the algorithm in Section 1.3.3. Here, we bring the details for each step of the algorithm. In Section 6.1 we discuss the solution domains and show how we construct them. Next, in Section 6.2 we discuss the details of constructing pseudo-solutions and finally in Section 6.3 we show how we can obtain an approximate solution from the pseudo-solutions. Also, in Section 6.4 we bring an improvement to the running time at the expense of having a larger approximation factor for the algorithm.

### 6.1 Solution Domains

We assume from now on that \(\mathsf{lis}(A)\ge n\lambda\) holds. As mentioned earlier, we divide the input array into \(\sqrt{n}\) subarrays of size \(\sqrt{n}\) and denote them by<br>
\(\mathsf{sa}_1,\mathsf{sa}_2,\dots,\mathsf{sa}_{\sqrt{n}}\). For a fixed optimal solution opt, our goal is to approximate the smallest and the largest number of each subarray that contribute to opt. Let us refer to these numbers as the _domain_ of each subarray. Let \(\epsilon:=1/1000\) be the accuracy parameter. For a subarray sa<sub>i</sub>, we sample k (will be decided later) different elements and refer to them by a<sub>j<sub>1</sub></sub>,a<sub>j<sub>2</sub></sub>,...,a<sub>j<sub>k</sub></sub>.

**Algorithm 8** Constructing the candidate domains

procedure ConstructCandidateDomains(sa<sub>i</sub>) \(\triangleright\) Lemma 6.1<br>
   \(\triangleright\) Given random access to a subarray sa<sub>i</sub><br>
   \(k\leftarrow 20log(1/\delta)/(\lambda\epsilon^2)\)<br>
   Sample k elements from sa<sub>i</sub>, and denote the sampled elements by a<sub>j<sub>1</sub></sub>,a<sub>j<sub>2</sub></sub>,...,a<sub>j<sub>k</sub></sub><br>
   for \(\alpha\) in [k] do<br>
   for \(\beta\) in [k] do<br>
   If \(a_{j_\alpha}\le a_{j_\beta}\), then construct a candidate domain \([a_{j_\alpha},a_{j_\beta}]\)<br>
   end for<br>
   end for<br>
   return all the constructed candidate domains<br>
end procedure

We first prove that,

**Lemma 6.1** (constructing candidate domains)**.** _Let_ \(\lambda\in(0,1)\), \(\epsilon\in(0,1/2)\) _and_ \(\delta\in(0,1/10)\)_. Let_ sa<sub>i</sub> _be a length-_\(\sqrt{n}\) _subarray whose contribution to the optimal solution is at least_ \(\epsilon\sqrt{n}\lambda\)_, i.e.,_ \(\mathsf{lis}^{[\mathsf{sm}(\mathsf{sa}_i),\mathsf{lg}(\mathsf{sa}_i)]}(\mathsf{sa}_i)\ge\epsilon\sqrt{n}\lambda\)_. If we uniformly sample_ \(k=20log(1/\delta)/(\lambda\epsilon^2)\) _elements a_<sub>j<sub>1</sub></sub>,a<sub>j<sub>2</sub></sub>,...,a<sub>j<sub>k</sub></sub> _from_ sa<sub>i</sub>_, then with probability at least_ \(1-\delta\)_, there exists a pair_ \((\alpha,\beta)\in[k]\times[k]\) _such that the following two conditions hold_

1. \(\mathsf{sm}(\mathsf{sa}_i)\le a_{j_\alpha}\le a_{j_\beta}\le\mathsf{lg}(\mathsf{sa}_i)\),<tbc>

_2._ \(\mathsf{lis}^{[a_{j_\alpha},a_{j_\beta}]}(\mathsf{sa}_i)\ge(1-\epsilon)\mathsf{lis}^{[\mathsf{sm}(\mathsf{sa}_i),\mathsf{lg}(\mathsf{sa}_i)]}(\mathsf{sa}_i)\).

_Proof._ At least \(\epsilon\sqrt{n}\lambda\) elements of sa<sub>i</sub> appear in opt. Let us put all these elements in an array b in the same order that they appear in sa<sub>i</sub>. Then it is obvious that b has at least \(\epsilon\sqrt{n}\lambda\) elements. To prove the lemma, we bound the probability that none of the first \(\epsilon/2\) fraction of the elements of b<tbc>

