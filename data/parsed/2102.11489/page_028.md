• Else, let _S_ be the number received earlier from its parent.<tbc>

– if \(S\ge S(\mathsf{lc})\) then pass "1" to lc and pass "M" to rc;<tbc>

**–** else, pass "M" to lc and pass "0" to rc.<tbc>

4. If a leaf node receives "0" or "1" from the parent, then output the corresponding bit. Otherwise, let _S_ be the 1-bit number received from the parent, output _S_.

**Implementation as a circuit.** All numbers use a delayed-carry representation. Let _v_<sub>1</sub>:=_x_<sub>1</sub>+_y_<sub>1</sub> and _v_<sub>2</sub>:=_x_<sub>2</sub>+_y_<sub>2</sub> be two \(\ell\)-bit numbers in delayed-carry representation, and suppose that \(v_1\ge v_2\). Then, _v_<sub>1</sub>-_v_<sub>2</sub> can be derived by computing _x_<sub>1</sub>+_x_<sub>2</sub>+<o>_y_</o><sub>1</sub>+<o>_y_</o><sub>2</sub>+2 and keeping only the last \(\ell\) bits, where <o>_y_</o><sub>b</sub> denotes the number obtained by flipping all bits of _y<sub>b</sub>_ for \(b\in\{1,2\}\). Therefore, we can use the shallow addition trick to compute subtraction. Of course, before a node receives the label from {M,0,1} from its parent, it is not guaranteed that \(S\ge S(\mathsf{lc})\), but we can just pretend it will be the case and continue. Therefore, Step 2 can be implemented in _O_(log_n_) depth.

Step 3 must be implemented in a pipelined manner to save depth: basically, as soon as a node receives the number _S_ from its parent during Step 2, it immediately starts to compute the comparison between _S_ and _S_(lc) which takes _O_(loglog_n_) depth. In other words, the nodes do not wait for its parent to compute this comparison before it computes its own comparison, but rather pre-computes this comparison ahead of time. Using this pipelining trick, Step 3 can also be accomplished in _O_(log_n_) depth.

Finally, observe that _S_ is at most log_n_+1 bits at the root; and at level _i_ it is at most log_n_+1-_i_ bits. Therefore, the above can be implemented with an _O(n_)-sized circuit.

This gives rise to the following fact.

**Fact 6.5.** _There is a circuit with O(n_) _generalized boolean gates and of O_(log_n_) _depth that solves the aforementioned generalized binary-to-unary conversion problem._

## 7 Lossy Loose Compaction Circuit

### 7.1 Definitions

**Lossy loose compactor.** Let \(\alpha\in[0,1)\). An \((\alpha,n,w)\)-lossy loose compactor (also written as \(\alpha\)-lossy loose compactor when _n_ and _w_ are clear from the context) solves the following problem:

• **Input**: an array **I** containing _n_ elements of the form \(\{(b_i,v_i)\}_{i\in[n]}\), where each \(b_i\in\{0,1\}\) is a metadata bit indicating whether the element is _real_ or _filler_, and each \(v_i\in\{0,1\}^w\) is the _payload_. The input array is promised to _have at most n/_128 _real elements_.<tbc>

• **Output**: an array **O** containing \(\lfloor n/1.9\rfloor\) elements, such that \(mset(\mathbf{O})\subseteq mset(\mathbf{I})\), and moreover, \(|mset(\mathbf{I})-mset(\mathbf{O})|\le\alpha n\) where _mset_(**O**) denotes the _multiset_ of real elements contained in **O**, and _mset_(**I**) is similarly defined.

In other words, lossy loose compaction takes a relatively sparse input array containing only a small constant fraction of real elements; it compresses the input to slightly more than half its original length<sup>6</sup> while preserving all but \(\alpha\cdot n\) real elements in the input.

**Loose compactor.** If \(\alpha=0\), i.e., there is no loss, we also call it a loose compactor. More formally, an (0_,n,w_)-lossy loose compactor is also called an (_n,w_)-loose compactor.

<sup>6</sup>It is not exactly half the original length due to rounding issues -- See Remark 3.

