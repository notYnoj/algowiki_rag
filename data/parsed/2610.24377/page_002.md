## Contents

**1 Introduction 2**<tbc>

1.1 Our Results ..... 3<tbc>

1.2 Related Work ..... 5<tbc>

1.3 Proof Intuition ..... 6<tbc>

**2 Preliminaries 7**<tbc>

**3 Evaluating Low-Depth Circuits of Symmetric Gates 10**<tbc>

3.1 Fast SYM Circuit Evaluation ..... 10<tbc>

3.2 Application: Integer Multiplication ..... 11<tbc>

3.3 Application: Sorting ..... 12<tbc>

**4 Evaluating Low-Degree Arithmetic Circuits 13**<tbc>

4.1 Fast Low-Multiplicative-Depth Circuit Evaluation ..... 13<tbc>

4.2 Application: Fourier Transforms ..... 15<tbc>

4.3 Application: Matrix Multiplication ..... 17<tbc>

**5 Time-Space Tradeoff Lower Bounds 20**<tbc>

5.1 Separating catalytic and non-catalytic time-and-space-bounded complexity ..... 20<tbc>

5.2 Separating 1-pass and 2-pass catalytic time-and-space-bounded complexity ..... 21<tbc>

**A Quickly converting between registers over different moduli 26**

## 1 Introduction

**Catalytic computing.** In the model of catalytic computing, introduced by Buhrman, Cleve, Koucký, Loff, and Speelman \[BCKLS14\], an algorithm with a small amount of memory (e.g. _O_(log(_n_))-bits, where the input is of length _n_) is augmented with a large amount of "dirty" memory (e.g. poly(_n_) bits). The clean memory is initially empty, but the dirty memory begins full of arbitrary bits the algorithm cannot choose. The algorithm may use both the clean and dirty memory however it sees fit to solve the problem at hand, but it is required to set every bit of the dirty memory back to its initial value when it terminates. (A standard analogy for dirty memory is that one "borrows" a friend’s enormous hard drive full of precious digital memories in order to carry out a computation, but one does not want to lose a friend in the process, so one is careful to restore every bit of the hard drive when done.)

The initial impetus for defining this model was to prove that dirty space is not helpful for computation. This would make intuitive sense: in order to restore every bit of the initial dirty memory contents at the end of computation, one must maintain all of the information throughout the computation, so one cannot "free up" any space in general. However, remarkably, Buhrman, Cleve, Koucký, Loff, and Speelman eventually found ways to make use of dirty space, solving problems that we don’t know how to solve using clean space alone. \[BCKLS14\] defined CL ("catalytic logspace") to be the class of problems solvable with poly(_n_) bits of catalytic space and _O_(log_n_) clean space, and showed the contaminants \(\mathsf{TC}^1\subseteq\mathsf{CL}\subseteq\mathsf{ZPP}\). In particular, NL and BPL are both contained in CL, showing that poly(_n_) dirty space is sufficient to simulate both randomness and nondeterminism in the logspace setting.

This model has generated a large amount of excitement and work among complexity theorists in recent years. We do not aim to give an exhaustive survey here, but some highlights are:

• new algorithms placing more problems in CL (such as \[Pyn25; AM25; AFMSV25; AAV26\]),<tbc>

• new characterizations demonstrating CL is "robust" under natural extensions of the model (such as \[CLMP25; FMST25; KMPS25\]), and<tbc>

• new developments in classical space complexity leveraging catalytic ideas \[CM20; CM24; Wil25\].<tbc>

