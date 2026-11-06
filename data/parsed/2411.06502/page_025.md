sim(**F**[_x...y_ ),**F**\('[x'..y'\) )). To this end, it suffices to define _i_, _j_ as the smallest _i_ such that \(x\le\mathrm{I}(v_i)\) and the smallest _j_ such that \(y\le\mathrm{I}(v_j)\), obtaining **F**[_x...y_ ) = **F**[I(_v<sub>i</sub>).._I(_v<sub>j</sub>_) ). Symmetrically, the same holds for \(\mathbf{F}'\).

To conclude, note that whole-versus-infix similarities correspond to paths from the lower border to the upper border and from the left border to the right border, while prefix-versus-suffix similarities correspond to paths from the lower border to the right border and from the left border to the upper border.

To prove Main Theorem 4 and Theorem 4.1, we proceed to develop an algorithm for BBD instances. The weight function w in the algorithm we present can be an arbitrary function.

## 4.3 A decomposition scheme for forests

To solve such BBD instances, we employ a divide-and-conquer approach. Given a \((\mathrm{w},\mathbf{F},\mathbf{F}')\)-BBD instance, we break it into several \((\mathrm{w},\mathbf{H},\mathbf{H}')\)-BBD instances, for smaller forests **H** and \(\mathbf{H}'\). We then merge these solutions to obtain the final solution for **F** and \(\mathbf{F}'\). To derive these smaller instances, we utilize the decomposition scheme introduced by Mao \[Mao22\] in his subcubic algorithm for unweighted tree edit distance (though with a different parameter choice). This scheme, governed by a threshold parameter \(\Delta\), uses transitions of two types:

**I.** transition from two synchronous forests **F**<sub>1</sub>, **F**<sub>2</sub>, both of size no less than \(\Delta/3\), to the synchronous subforest **F**=**F**<sub>1</sub>+**F**<sub>2</sub>;

**II.** transition from a synchronous forest \(\mathbf{F}_s\subset\mathbf{F}\) such that \(|\mathbf{F}\backslash\mathbf{F}_s|\le\Delta\) to a synchronous forest **F**.

The subsequent two lemmas, the proofs of which we defer to Section 4.4, show how transitions in Mao’s decomposition scheme can be adapted to our scenario.

**Lemma 4.6.** _Suppose we are given a_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-BBD instance of size m such that_ **F**=**F**<sub>1</sub>+**F**<sub>2</sub>.

_Then, given the outputs of the_ \((\mathrm{w},\mathbf{F}_1,\mathbf{F}')\)_-BBD instance and the_ \((\mathrm{w},\mathbf{F}_2,\mathbf{F}')\)_-BBD instance, we can solve the_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-BBD instance in time_ O(T_<sub>MUL</sub>(m_)).

_Furthermore, if the BBD instance has diameter_ D_, we can solve the_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-BBD instance in time_ O(T_<sub>MonMUL</sub>(m,m,m,_D)).

**Lemma 4.7.** _Suppose we are given a_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-BBD instance of size m and a synchronous subforest_ \(\mathbf{F}_s\subseteq\mathbf{F}\) _of size_ |**F**_<sub>s</sub>_|=_n<sub>s</sub>. Further, let v_<sub>1</sub>_,...,v_<sub>|**F**|</sub> _be the pre-order of_ **F**_, and let i<sub>s</sub> be such that v<sub>i<sub>s</sub></sub>,...,v<sub>i<sub>s</sub>+n<sub>s</sub></sub> is the pre-order of_ **F**_<sub>s</sub>. Define_ \(\mathbf{F}_\ell=\mathbf{F}[1..\mathrm{I}(v_{i_s})\) ), **F**_<sub>s</sub>_=**F**[I(_v<sub>i<sub>s</sub></sub>).._I(_v<sub>i<sub>s</sub>+n<sub>s</sub>+_1) )_, and_ **F**_<sub>r</sub>_=**F**[I(_v<sub>i<sub>s</sub>+n<sub>s</sub>+_1)_.._2|**F**|+1 ).

_Then, given the outputs of the four BBD instances_ \((\mathrm{w},\mathbf{F}_\ell,\mathbf{F}')\)_-BBD,_ \((\mathrm{w},\mathbf{F}_s,\mathbf{F}')\)_-BBD,_ \((\mathrm{w},\mathbf{F}_r,\mathbf{F}')\)_-BBD, and_ \((\mathrm{w},\mathbf{F}\backslash\mathbf{F}_s,\mathbf{F}')\)_-BBD, we can solve the_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-BBD instance in time_ O(T_<sub>MUL</sub>(m_)).

_Furthermore, if the BBD instance has diameter_ D_, we can solve the_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-BBD instance in time_ O(T_<sub>MonMUL</sub>(m,m,m,_D)).

The decomposition scheme, together with Lemma 4.6 and Lemma 4.7, allows us to establish the following reduction from a \((\mathrm{w},\mathbf{F},\mathbf{F}')\)-BBD instance of size _m_ to \(\mathcal{O}(m^2/\Delta^2)\) BBD instances, each of size at most \(\Delta\).

**Lemma 4.8.** _Suppose, we are given a_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-BBD instance of size m, and a threshold_ \(\Delta\).

_Then, in time_ O(_m_<sup>2</sup>) _we can find forests_ **F**<sub>1</sub>_,...,_**F**_<sub>k</sub> and_ \(\mathbf{F}'_1,\dots,\mathbf{F}'_k\)_, all of size at most_ \(\Delta\)_, such that_ \(k=\mathcal{O}(m^2/\Delta^2)\) _and such that, given the output of the_ \((\mathrm{w},\mathbf{F}_i,\mathbf{F}'_i)\)_-BBD instance for all_ \(i\in[1..k]\)_, we can solve the_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-BBD instance in time_ \(\mathcal{O}(m^2/\Delta^2\cdot\mathsf{T}_{MUL}(m))\).

_Furthermore, if the BBD instance has diameter_ D_, we can solve the_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-BBD instance in time_ \(\mathcal{O}(m^2/\Delta^2\cdot\mathsf{T}_{MonMUL}(m,m,m,\mathrm{D}))\).

