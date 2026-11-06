**Algorithm 2** Partition Algorithm

**Input:** two nodes \(s,q\in\mathbf{S}\) such that _s\<q_, and a threshold \(\Delta\).

**Output:** a subset \(s=r_1<r_2<\cdots<r_d=q\in\mathbf{S}\).

1 \(r_1\leftarrow s\);

2 \(i\leftarrow 1\);

3 while \(r_i\neq q\) do

4 Define \(r_{i+1}\in\mathbf{S}\) to be the farthest node from _ri<sub>i</sub>_ on **S** such that \(r_i<r_{i+1}\le q\) and \(|\mathrm{sub}(r_i)\backslash\mathrm{sub}(r_{i+1})|\le\Delta\). If no such _r_<sub>_i_+1</sub> exists, pick _r_<sub>_i_+1</sub> such that _ri<sub>i</sub>_ immediately precedes _r_<sub>_i_+1</sub>;

5 \(i\leftarrow i+1\);

6 return {_ri<sub>i</sub>}<sub>i</sub>_;

We can think of Lemma 5.2 and Lemma 5.3 as tools that allow us to cover the base case and to divide a larger problem into two smaller ones, respectively. Note, when we say ‘reducing’, we are not merely referring to utilizing the output of the smaller instance to compute the larger instance. We are also accounting for the time and computation required to compute the input of the smaller instances. This input may not necessarily be an input of the larger instance but is essential for invoking any subroutine on the smaller instances. In these reductions, we assume that the output of a smaller instance is available to us as soon as we compute its inputs.

Intuitively, in Lemma 5.3 we would like to break down an instance \((s,s',q,q')\)-DISED into two instances \((s,s',r,q')\)-DISED and \((r,s',q,q')\)-DISED such that \(|\mathrm{sub}(s)\backslash\mathrm{sub}(r)|\approx|\mathrm{sub}(r)\backslash\mathrm{sub}(q)|\approx|\mathrm{sub}(s)\backslash\mathrm{sub}(q)|/2\). However, since this is not always possible, we need another division scheme that uses Lemma 5.3 as a subroutine.

**Lemma 5.4.** _Let be given an_ \((s,s',q,q')\)_-DISED instance of size m and a positive threshold_ \(\Delta\)_. Then, we can find_ \(9m^2/\Delta^2\) _DISED instances in time_ O(_m_<sup>2</sup>)_, each of size at most_ \(\Delta\)_, such that given the input of all such instances, we can solve the_ \((s,s',q,q')\)_-DISED instance in time_ \(\mathcal{O}(m^2/\Delta^2\cdot(\mathsf{T}_{MUL}(m)+m^{2+o(1)}))\).

_Furthermore, if the SED instance is unweighted and has global tree size_ D_, the algorithm requires time_ \(\mathcal{O}(m^2/\Delta^2\cdot(\mathsf{T}_{MonMUL}(m,m,m,\mathrm{D})+m^{2+o(1)}g(\mathrm{D})))\) _where_ T<sub>_MonMUL_</sub>(_m,m,m,_D)=O(_f(m)g_(D)).

**Proof.** We can simplify the proof to demonstrate the following: Given an \((s,s',q,q')\)-DISED instance of size _n_ and a threshold \(\Delta\), we can find in time O(_m_) a set \(I\subseteq\mathbf{S}\times\mathbf{S}\) satisfying all of the following:

\(|I|\le 3m/\Delta\);

\(s\le a<b\le q\) for \((a,b)\in I\);

\(|\mathrm{sub}(a)\backslash\mathrm{sub}(b)|\le\Delta\) for \((a,b)\in I\); and

the \((s,s',q,q')\)-DISED instance can be reduced to the \((a,s',b,q')\)-DISED instances for \((a,b)\in I\) in time \(\mathcal{O}(m/\Delta\cdot(\mathsf{T}_{MUL}(m)+m^{2+o(1)})+\mathcal{O}(m))\). In the unweighted setting, we require time \(\mathcal{O}(m/\Delta\cdot(\mathsf{T}_{MonMUL}(m,m,m,\mathrm{D})+m^{2+o(1)}g(\mathrm{D}))+\mathcal{O}(m))\).

Using swap symmetry, we can use the simplified version of the lemma first on the \((s,s',q,q')\)-DISED instance, and then apply it on the \((a,s',b,q')\)-DISED instances for all \((a,b)\in I\), thereby proving the original statement of the lemma.

To construct set _I_, we employ Algorithm 2 on _s_ and _q_ with threshold \(\Delta\), yielding a sequence of spine nodes \(s=r_1<r_2<\cdots<r_d=q\). The algorithm guarantees that for each \(i\in[1..d)\), either the \((r_i,s',r_{i+1},q')\)-DISED instance has size at most \(\Delta\), or _ri<sub>i</sub>_ immediately precedes _r_<sub>_i_+1</sub>. To complete the reduction, we recursively solve \((r_i,s',r_j,q')\)-DISED instances for \(i,j\in[i..d]\) with _i\<j_. This is achieved by selecting an arbitrary _i\<k\<j_, and applying Lemma 5.3 to the \((r_i,s',r_k,q')\)-DISED and

