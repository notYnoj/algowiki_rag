(Algorithm 1), apply our BBD algorithm on each instance, and combining the results using the following two lemmas.

**Lemma 4.11.** _Suppose we are given a_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-LRBBD instance of size_ \((n,n')\) _such that_ **F**=**F**<sub>1</sub>+**F**<sub>2</sub>.

_Then, given the outputs of the_ \((\mathrm{w},\mathbf{F}_1,\mathbf{F}')\)_-LRBBD instance and the_ \((\mathrm{w},\mathbf{F}_2,\mathbf{F}')\)_-LRBBD instance, we can solve the_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-LRBBD instance in time_ \(\mathcal{O}(\mathsf{T}_{MUL}(n',n',n))\).

_Furthermore, if the LRBDD instance has diameter_ \(\mathcal{O}(n')\)_, we can solve the_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-LRBBD instance in time_ \(\mathcal{O}(\mathsf{T}_{MonMUL}(n',n',n,n'))\).

**Lemma 4.12.** _Suppose we are given a_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-LRBBD instance of size_ \((n,n')\) _and a synchronous subforest_ \(\mathbf{F}_s\subseteq\mathbf{F}\) _of size_ |**F**_<sub>s</sub>|=n<sub>s</sub>. Further, let v_<sub>1</sub>_,...,v_<sub>|**F**|</sub> _be the pre-order of_ **F**_, and let i<sub>s</sub> be such that v<sub>i<sub>s</sub></sub>,...,v<sub>i<sub>s</sub>+n<sub>s</sub></sub> is the pre-order of_ **F**_<sub>s</sub>. Define_ \(\mathbf{F}_\ell=\mathbf{F}[1\dots\mathrm{l}(v_{i_s})\) **),** \(\mathbf{F}_s=\mathbf{F}[\mathrm{l}(v_{i_s})\dots\mathrm{l}(v_{i_s+n_s+1})\) **), and** \(\mathbf{F}_r=\mathbf{F}[\mathrm{l}(v_{i_s+n_s+1})\dots 2|\mathbf{F}|+1\mathbf{)}\).

_Then, given the outputs of the four LRBDD instances_ \((\mathrm{w},\mathbf{F}_\ell,\mathbf{F}')\)_-LRBBD,_ \((\mathrm{w},\mathbf{F}_s,\mathbf{F}')\)_-LRBBD,_ \((\mathrm{w},\mathbf{F}_r,\mathbf{F}')\)_- LRBDD, and_ \((\mathrm{w},\mathbf{F}\backslash\mathbf{F}_s,\mathbf{F}')\)_-LRBBD, we can solve the_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-LRBBD instance in time_ \(\mathcal{O}(\mathsf{T}_{MUL}(n',n',n))\).

_Furthermore, if the LRBDD instance has diameter_ \(\mathcal{O}(n')\)_, we can solve the_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-LRBBD instance in time_ \(\mathcal{O}(\mathsf{T}_{MonMUL}(n',n',n,n'))\).

The decomposition scheme of Algorithm 1, together with Lemma 4.11 and Lemma 4.12, allows us to establish the following reduction from a \((\mathrm{w},\mathbf{F},\mathbf{F}')\)-LRBDD instance of size \((n,n')\) to \(\mathcal{O}(n/\Delta)\) LRBDD instances, each of size at most \((\Delta,n')\) for any threshold \(\Delta\).

**Lemma 4.13.** _Suppose, we are given a_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-LRBBD instance of size_ \((n,n')\) _and threshold_ \(\Delta\)_. Assume without loss of generality_ \(n\ge n'\).

_Then, there exist forests_ **F**<sub>1</sub>_,...,**F**<sub>k</sub> all of size at most_ \(\Delta\)_, such that_ \(k=\mathcal{O}(n/\Delta)\) _and such that, given the output of the_ \((\mathrm{w},\mathbf{F}_i,\mathbf{F}')\)_-LRBBD instance for all_ \(i\in[1..k]\)_, we can solve the_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-LRBBD instance in time_ \(\mathcal{O}(\frac{n^2}{\Delta n^\prime}\cdot\mathsf{T}_{MUL}(n')\).

_Furthermore, if the LRBDD instance has diameter_ \(\mathcal{O}(n')\)_, we can solve the_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-LRBBD instance in time_ \(\mathcal{O}(\frac{n^2}{\Delta n^\prime}\cdot\mathsf{T}_{MonMUL}(n'))\).

**Proof.** As in Lemma 4.8, we utilize Algorithm 1 on the \((\mathrm{w},\mathbf{F},\mathbf{F}')\)-LRBDD instance. Algorithm 1 applies recursively Mao’s transitions with the same parameter \(\Delta\) on forests \(\mathbf{H}\subseteq\mathbf{F}\), until it is left with forests of size at most \((\Delta,n')\). We use Lemma 4.11 and Lemma 4.12 to combine results as appropriate. The correctness of the algorithm follows directly from Lemma 4.11 and Lemma 4.12.

What remains to be demonstrated is a bound on _k_ and on the running time. For that purpose, notice that _k=_O(_t_<sub>1</sub>+_t_<sub>II</sub>) where _t_<sub>1</sub>_,t_<sub>II</sub> is the number of times we apply transition of type I and II, respectively. As argued in Lemma 4.8, we have \(k=\mathcal{O}(t_1+t_\mathrm{II})=\mathcal{O}(n/\Delta)\). Then, the running time can be bounded by

\(\mathcal{O}\left(\frac{n}{\Delta}\cdot\mathsf{T}_{MUL}(n',n',n)\right)=\mathcal{O}\left(\frac{n^2}{\Delta n^\prime}\cdot\mathsf{T}_{MUL}(n')\right).\)

If the diameter is at most \(\mathcal{O}(n')\), we instead obtain

\(\mathcal{O}\left(\frac{n}{\Delta}\cdot\mathsf{T}_{MonMUL}(n',n',n,n')\right)=\mathcal{O}\left(\frac{n^2}{\Delta n^\prime}\cdot\mathsf{T}_{MonMUL}(n')\right)\)

**Corollary 4.14.** _There is an algorithm that solves in time_ \((n/n')^{1+o(1)}\cdot\left(\mathsf{T}_{MUL}(n')+n'^{2+o(1)}\right)\) _a_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_- LRBDD instance of size_ \((n,n')\) _where_ \(n\ge n'\).

_Furthermore, if the LRBDD instance has diameter_ \(\mathcal{O}(n')\)_, then the algorithm runs in time_ \((n/n')^{1+o(1)}\cdot\left(\mathsf{T}_{MonMUL}(n')+n'^{2+o(1)}g(n')\right)\) _where_ \(\mathsf{T}_{MonMUL}(n',n',n',\mathrm{D})=\mathcal{O}(f(n')g(\mathrm{D}))\).

\(\includegraphics{}\) **Lemma 4.11.** _Suppose we are given a_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-LRBDD instance of size_ \((n,n')\) _such that_ **F**=**F**<sub>1</sub>+**F**<sub>2</sub>.

