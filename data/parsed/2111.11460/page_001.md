# On the Local Communication Complexity of Counting and Modular Arithmetic

**Abstract**

In standard number-in-hand multi-party communication complexity, performance is measured as the total number of bits transmitted globally in the network. In this paper, we study a variation called local communication complexity in which performance instead measures the maximum number of bits sent or received at any one player. We focus on a simple model where _n_ players, each with one input bit, execute a protocol by exchanging messages to compute a function on the _n_ input bits. We ask what can and cannot be solved with a small local communication complexity in this setting. We begin by establishing a non-trivial lower bound on the local complexity for a specific function by proving that counting the number of 1’s among the first 17 input bits distributed among the participants requires a local complexity strictly greater than 1. We further investigate whether harder counting problems of this type can yield stronger lower bounds, providing a largely negative answer by showing that constant local complexity is sufficient to count the number 1 bits over the entire input, and therefore compute any symmetric function. In addition to counting, we show that both sorting and searching can be computed in constant local complexity. We then use the counting solution as a subroutine to demonstrate that constant local complexity is also sufficient to compute many standard modular arithmetic operations on two operands, including: comparisons, addition, subtraction, multiplication, division, and exponentiation. Finally we establish that function _GCD(x,y_) where _x_ and _y_ are in the range [1_,n_] has local complexity of _O_(1). Our work highlights both new techniques for proving lower bounds on this metric and the power of even a small amount of local communication.

### 1 Introduction

In the standard study of number-in-hand multi-party communication complexity the input bits for a function _f_ of size _n_ are partitioned among two or more players. The goal is for these players to work together to compute _f_ over the input bits by transmitting information using network channels or a shared blackboard. In the deterministic context, the _communication complexity_ of a given protocol is the total number of bits transmitted or recorded in the worst case over all possible inputs.

More recently, a natural variation was introduced that instead counts the maximum number of bits sent or received by any one player [9, 4]. Though different names have been given to this measure, we call it _local (communication) complexity_. In [9], the authors show connections between this metric and efficient distributed pattern recognition. Later, in [4], the authors describe this metric as a "fundamental area to explore," noting that measures of global communication obscure the local load at individual players, a critical factor in settings where local processing is an important resource to conserve. They further underscore this importance by establishing formal theoretical connections between local complexity and multi-party secure computation, streaming algorithms, and circuit complexity.

Informally, this model consists of _n_ players connected by network channels. Each player gets a bit as input. They exchange messages according to some deterministic protocol to compute a function on these _n_

Bala Kalyanasundaram Georgetown University kalyan@cs.georgetown.edu

Calvin Newport Georgetown University cnewport@cs.georgetown.edu

