## 7.2 Existential Proof

In this subsection we finally prove the existential statement of Theorem 2.4. Recall that we start from integer sets _A,B_ with energy

\(E(A,B)\ge\alpha|A|^2|B|.\)

The proof can conceptually be split into four steps. In the first step we will successively replace _A_ by "smoother" sets _A_<sub>1</sub>_,A_<sub>2</sub>_,..._ that admit more additive structure. As an instructive example, consider the set _B_={1_,...,|B_|} and let _A_ be a random subset of _B_. When _B_ is large compared to _A_, _A_ essentially admits no additive structure at all. We will therefore replace _A_ by smoother sets (think of _A-A,_2_A_-2_A,..._) converging to the highly structured set _B_. Once we reach a set that is sufficiently structured, in the second step we apply the symmetric BSG theorem to identify a large low-doubling subset _H_. In the third step we unroll the iterative smoothing procedure to relate _H_ to the initial set _A_. In the fourth step we relate _H_ to _B_.

Following \[TV06\], we introduce a useful piece of notation. We write _f=O<sub>j</sub>(g_) if there exists a positive constant _C(j_) (that only depends on _j_) such that

\(f\le C(j)\cdot\alpha^{-C(j)}\cdot\left(1+log\frac{|B|}{|A|}\right)^{C(j)}\cdot g;\)

that is, the _O<sub>j</sub>_ notation hides constant factors, polynomial factors in \(1/\alpha\), and polylogarithmic factors in |_B|/|A_|. Similarly define \(f=\Omega_j(g)\).

### Step 1: Iteratively Smoothing _A_.

Let \(J=J(\epsilon)\) be a constant to be fixed later. Let \(\alpha_1=\alpha/2\) and recursively define \(\alpha_2,\dots,\alpha_J\) by \(\alpha_{j+1}=\alpha_j^2/2\). Note that \(\alpha_1>\cdots>\alpha_J>0\) and \(\alpha_j=\Omega_j(1)\). We will inductively construct a sequence of sets _A_<sub>0</sub>_,A_<sub>1</sub>_,...,A<sub>J</sub>_ with the following properties:

(i) for all \(1\le j\le J\), \(A_j\subseteq Sym(B;\alpha_j)\),<tbc>

(ii) for all \(0\le j<J\) and all \(x\in A_{j+1}\), \(r_{A_j-A_j}(x)\ge\Omega_j(|A_j|^2/|A_{j+1}|)\),<tbc>

(iii) for all \(0\le j\le J\), \(|A_j|=\Omega_j(|A|)\).

In fact, Property (iii) is always implied by Property (ii): If \(\sum_{x\in A_{j+1}}r_{A_j-A_j}(x)\ge\Omega_j(|A_j|^2)\), then we must have \(|A_{j+1}|\ge\Omega_j(|A_j|)\), and then Property (iii) follows by induction. For this reason we will only ensure Properties (i) and (ii) in the following construction.

The base case is concerned with the construction of _A_<sub>0</sub> and _A_<sub>1</sub>. We trivially take _A_<sub>0</sub>=_A_. To construct _A_<sub>1</sub>, first observe that

\(E(A,B)=\sum_{a_1,a_2\in A}r_{B-B}(a_1-a_2)\)<br>
\(\le\sum_{a_1,a_2\in A}\frac{\alpha|B|}{2}+|\{(a_1,a_2)\in A^2:a_1-a_2\in Sym(B;\alpha/2)\}|\cdot|B|.\)

In particular, recalling that \(E(A,B)\ge\alpha|A|^2|B|\), and letting \(D=Sym(B;\alpha/2)\), we must have<tbc>

\(\sum_{x\in D}r_{A-A}(x)\ge\frac{\alpha|A|^2}{2}.\)

