## 6 Modular Arithmetic with Constant Local Complexity

In this section we turn our attention to 2-symmetric (also known as bi-symmetric) functions, in which the input bits can be partitioned into two sets, and the output of the function depends only on the total count of 1 bits in each set.

We focus in particular on balanced 2-symmetric functions, of the form \(f:\{0,1\}^{2n}\rightarrow\mathbb{N}\), where the partitions evenly divide the bits into two sets of size _n_. One can therefore interpret a function _f(a_<sub>1</sub>_,a_<sub>2</sub>_,...a<sub>n</sub>,a_<sub>_n_+1</sub>_,...a_<sub>2_n_</sub>) of this type as calculating _g<sub>f</sub>_(#<sub>1</sub>(_a_<sub>1</sub>_...a<sub>n</sub>),_#(_a_<sub>_n_+1</sub>_...a_<sub>2_n_</sub>)), for a function of the form \(g_f:[n]\times[n]\rightarrow\mathbb{N}\).

We turn our attention balanced 2-symmetric functions in part because they are the natural next class to consider after we established in the previous section that symmetric functions can be solved with constant local complexity. We emphasize that the local complexity jump from symmetric to 2-symmetric is non- trivial. A straightforward counting argument establishes that there must _exist_ 2-symmetric functions with a local complexity in \(\omega(1)\). Identifying a specific function with this larger complexity would resolve a major open problem in circuit complexity. This follows due to ability of any linear-sized circuit to be simulated in our setting by a protocol with constant local complexity (e.g., see the discussion in \[4\]). A function that cannot be solved with constant local complexity is a function that cannot be implemented by a linear-sized circuit.

Specifically, we begin by studying many standard modular arithmetic functions on two operands. Perhaps not surprisingly, given the connection between local and circuit complexity, we identify solutions to all functions considered that require only constant local complexity. We then build on these solutions to show that even the more complex GCD function can be implemented with constant complexity. These results underscore the surprisingly power of distributed function computation with a very small number of bits sent and received at any one node.

### 6.1 Standard Arithmetic Functions with Constant Local Complexity

We begin by studying standard arithmetic functions, including basic mathematical and comparison operations, and their composition. In all cases, we prove that constant local complexity is sufficient. A reasonable starting place for designing a protocol to compute a given balanced 2-symmetric function _g<sub>f</sub>_ is to first run two instances of our (_n,n_)-counting solutions in parallel on _a_<sub>1</sub>_...a<sub>n</sub>_ and _a_<sub>_n_+1</sub>_...a_<sub>2_n_</sub>. This allows some player _i_ in the first partition to learn _x_=#<sub>1</sub>(_a_<sub>1</sub>_...a<sub>n</sub>_) and some player _j_ in the second to learn _y_=#<sub>1</sub>(_a_<sub>_n_+1</sub>_...a_<sub>2_n_</sub>). If _i_ shared _x_ with _j_ (or vice versa) then the function can be computed. These values, however, might be much too large to directly share while preserving constant local complexity. Therefore, more complexity is required for each partition to learn the necessary information about the other partition’s count.

Formally, we prove the following is possible with constant local complexity:

**Theorem 6.1.** _Suppose n_+1 _is a prime number. A balanced 2-symmetric function_ \(f:\{0,1\}^{2n}\rightarrow\mathbb{N}\) _can be computed with constant local complexity if the corresponding function_ \(g_f:[n]\times[n]\rightarrow\mathbb{N}\) _is:_

1. _a function of only one of the two variables with range_ {0,1_,...,n},_<tbc>

2. _comparison operator_ \((>,\ge,=,\le,<)\) _on two variables with output_ 0 _or_ 1,<tbc>

3. _a modular (mod (n+1)) addition, subtraction, multiplication or division, exponentiation or_<tbc>

_4._ _a constant applications/composition of functions from first three items in this list._

_Proof._ We start with some basic assumptions that _n_+1 is prime, and all arithmetic operations are modular _n_+1. There is a natural linear order among numbers in {0,1_,...,n_} and so the comparison operators are well defined.

Given a 2-symmetric function \(f:\{0,1\}^{2n}\rightarrow\{0,1,\dots,n\}\), we will describe a protocol which notify the player _P<sub>i</sub>_ to be responsible for the output if the output of _f_ is _i_.

