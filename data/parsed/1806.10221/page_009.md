<tbc>In our protocol, we utilize _N_-1 ancillary qubits to find out the parity of the column sums of _N_-1 columns, i.e. every column except the last. This is because, the only case in which all such _N_-1 column sums are odd is when each of the _N_ column sums are 1. If at least one of the _N_ column sum is greater than 1 and is odd, then there are at least two out of the _N_ column sums which is zero. If at least one of the _N_ column sum is greater than 1 and is even, then there is at least one out of the _N_ column sums which is zero. These claims are a result of the following proposition, which is based on the fact that the total of the column sums is constrained to be _N_, a consequence of the already satisfied Row Criteria. This proposition enables us to check the parity of the column sums of any _N_-1 columns instead of all _N_ columns.

**Proposition 1.** _Let the sum of N non-negative integers be N,_ \(N\in\mathbb{N}\)_. Then, the number of even integers among the N non-negative integers is even, where_ 0 _is also considered to be even._

_Proof._ We know that the sum of any number of even integers is even. However, the sum of an even number of odd integers is even and the sum of an odd number of odd integers is odd.

Among the _N_ integers, let us assume _N<sub>o</sub>_ is the number of odd integers and _N<sub>e</sub>_ is the number of even integers (which includes 0). It is evident that _N<sub>o</sub>+N<sub>e</sub>=N_. Also, let _S<sub>o</sub>_ and _S<sub>e</sub>_ be the sum of the odd integers and even integers respectively. Thus, _S<sub>o</sub>+S<sub>e</sub>=N_. It is to be noted that _S<sub>e</sub>_ is always even.

Consider the following cases,

_N_ **is odd:** _N_ is odd iff either _N<sub>o</sub>_ or _N<sub>e</sub>_ is odd. Also, since _S<sub>e</sub>_ is even, _S<sub>o</sub>_ is odd. This is only possible if _N<sub>o</sub>_ is odd. Hence, _N<sub>e</sub>_ is even.

_N_ **is even:** _N_ is even iff _N<sub>o</sub>_ and _N<sub>e</sub>_ are either both even or both odd. Since _S<sub>e</sub>_ is even, _S<sub>o</sub>_ is even. This is only possible if _N<sub>o</sub>_ is even. Hence, _N<sub>e</sub>_ is even.

Thus for all _N_, _N<sub>e</sub>_ is even.

Below, we show that the computational time complexity of our algorithm is O(_N_<sup>3</sup>).

**Proposition 2.** _The time complexity for the proposed quantum N-Queens algorithm is of the order_ O(_N_<sup>3</sup>).

_Proof._ The computational time complexity of an algorithm is estimated as the limiting behaviour of the number of elementary operations (gates) required by the computation as a function of the input size _N_, as \(N\rightarrow\infty\). The quantum _N_-Queens algorithm performs computation for,

**Column checks:** 2(_N_-1) Hadamard gates are used in the column checks, since two Hadamard gates are applied to each column check ancilla. _N_ controlled phase shifts are applied to the system from each ancilla, hence a total of _N(N_-1) controlled phase shifts are used. Thus, a total of (_N_-1)(_N_+2) gates are used in the column checks.

**Diagonal checks:** The diagonal checks are performed by imagining the system of _N_<sup>2</sup> qubits to be arranged as a \(N\times N\) matrix, such that the _i_th qubit of the _j_th block encodes the matrix element of the _i_th column and _j_th row. Every pair of qubits that encode elements positioned diagonally are checked for the diagonal condition. Since for every such pair a Toffoli gate with the corresponding qubits as controls is used, the number of gates required is equal to the number of such diagonal pairs. The general equation for the number of diagonal pairs is, \(\sum_{i=1}^{N-1}\sum_{j=1}^{N-i}2(N-j)\), which can be equivalently notated as \(2\sum_{i=1}^{N-1}\sum_{j=1}^i(N-j)\). This evaluates to \(N^2(N-1)-N(N-1)-\frac{N(N-1)(N-2)}{3}\) .

Thus, the total number of gates as a function of input size _N_ has the limiting behaviour (as \(N\rightarrow\infty\)) defined by \(f:\mathbb{N}\rightarrow\mathbb{N},f(N)=N^3\). Hence, the time complexity is of the order O(_N_<sup>3</sup>).

