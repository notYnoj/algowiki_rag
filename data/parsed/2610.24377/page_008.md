**Definition 2.1** (Transducer Output Tape)**.** A space _s=s(n_) **transducer TM** _M_ computing a function family \(f_n:\{0,1\}^n\rightarrow\{0,1\}^\star\) has access to:

i) An _n_-bit input tape with a read-only random-access head.<tbc>

ii) An _s_-bit work tape with a read-write random-access head.<tbc>

iii) An output tape initialized to all zeros with a write-only one-way head, which starts in the leftmost cell and can only move right by one cell. Once the machine halts, the output is defined as all the bits up to the head’s current position. (The tape is at most 2<sup>_O(s_)</sup> bits long.)

As the output tape is initialized to zero, moving right by one cell without overwriting the previous one is implicitly equivalent to writing a 0 symbol to that previous cell, in the above definition. Observe both the input and work tapes are random access -- only the output tape is restricted to be one-way access. While the access is one-way, Definition 2.1 does not restrict it to be write-once too (though, without loss of generality, this does not make a difference). Observe that this definition allows the output length to depend on the input itself, not only the input length.

All time-space lower bounds for multi-bit problems appealing to the branching program type defined in the Borodin-Cook argument \[BC80\] apply only to the "append-only" output form. This append-only notion, where we can choose to append some bit to the final output, is equivalent to Definition 2.1. As the time- space lower bounds of \[Yes84; BC80; Abr91; Bea91\] are proven on _R_-way branching programs, a non-uniform analogue of the append-only transducer, they have only been shown to hold for the output tape model of Definition 2.1.<sup>6</sup>

In contrast to clean space algorithms, catalytic ones suggest a different natural output model. Instead of placing the output into an append-only output tape, XOR the output into a chunk of your dirty space. This output model allows for _composition_ of catalytic algorithms which read their input by having it XORed into dirty memory. As these changes to the catalytic tape can be reverted by running the algorithm again, there is no danger of irreparably altering the catalytic tape.

**Definition 2.2** (Dirty-XOR-output model)**.** A clean space _s=s(n_), catalytic space _c=c(n_) **dirty-XOR- output TM** _M_ computing a function family \(f_n:\{0,1\}^n\rightarrow\{0,1\}^\star\) has access to:

i) An _n_-bit input tape with a read-only random-access head.<tbc>

ii) An _s_-bit clean work tape with a read-write random-access head.<tbc>

iii) A _c_-bit catalytic work tape (arbitrarily initialized) with a read-write random-access head. Given input _x_, let _k_=|_f(x_)| and \(\tau\) be the first _k_ bits of the dirty tape at initialization. At the end of the computation, the first _k_-bit dirty space chunk should be \(\tau\oplus f(x)\). Each of the other remaining bits must be restored exactly.

The above is restricted only to algorithms with access to dirty space. This motivates a definition of a useful output model applicable to both clean and catalytic space algorithms, in which we can make a comparison between them. The following output definition retains a similar sequential access restriction as Definition 2.1 while incorporating the XOR-access feature of Definition 2.2.

**Definition 2.3** (_k_-output-pass model)**.** A space _s=s(n_) _k_**output-pass TM** _M_ computing function family \(f_n:\{0,1\}^n\rightarrow\{0,1\}^\star\) has access to:

i) An _n_-bit input tape with a read-only random-access head.<tbc>

ii) An _s_-bit work tape with a read-write random-access head.<tbc>

<sup>6</sup>Note that a time-space lower bound on non-uniform _R_-way branching programs could be mildly stronger than a time-space lower bound for the transducer model. Aside from being non-uniform, an _R_-way branching program models input query access operations as unit cost and all other operations as _free_. Thus, these time-space lower bounds apply for any space-bounded program with a "reasonable" measure of time. Furthermore, each input cell is assumed to lie in \(\{0,\cdots,R-1\}\) instead of just the boolean set {0,1}.

