is defined as the worst-case, over all nodes, number of rounds a node requires to produce an output and terminate.

## 2.2 Sleeping Model

We assume the sleeping model [17], where a node can be in either of the two states -- sleeping or awake. (At the beginning, we assume that all nodes are awake.) This is a simple generalization of the standard distributed computing model, where nodes are always assumed to be awake. In the sleeping model, each node decides to be either _wake_ or _asleep_ in each round (till it terminates), corresponding to whether the node can receive/send messages and perform computations in that round or not, respectively. That is, any node _v_ can decide to _sleep_ starting at any (specified) round of its choice. We assume that all nodes know the correct round number whenever they are awake. A node can _wake up_ again later at any _specified_ round and enter the _ awake_ state. We note that the model allows a node to cycle through the process of sleeping in some round and waking up in a later round as many times as it wishes. To summarize, distributed computation in the sleeping model proceeds in _synchronous_ rounds, and each round consists of the following steps: (1) Each awake node can perform local computation. (2) Each awake node can send a message to its adjacent nodes. (3) Each awake node can receive messages sent to it in this round (in the previous step) by other awake nodes.

Thus, the paper assumes the sleeping model in the CONGEST setting, called the SLEEPING-CONGEST model [24].

**Energy Complexity.** In the sleeping model, let _A<sub>v</sub>_ denote the number of awake rounds for a node _v_ before it terminates (i.e., finishes the execution of the algorithm, locally). A node utilizes significant energy only when it is awake. Hence we define the _(worst-case) energy (a.k.a) awake complexity_ as \(A_{max}=max_{v\in V}A_v\). Note that, for a randomized algorithm, _A<sub>v</sub>_ will be a random variable. We also define \(A_{avg}=\frac{1}{n}\sum_{v\in V}A_v\), i.e., the average of the _A<sub>v</sub>_ random variables. Then the expected _node-averaged energy complexity_ of the randomized algorithm is \(E[A_{avg}]=E[\frac{1}{n}\sum_{v\in V}A_v]=\frac{1}{n}\sum_{v\in V}E[A_v]\), where the expectation is taken over the random coin choices of the algorithm.

In this paper, we study _lower bounds_ on both the worst-case and the node-averaged energy complexity. For worst-case energy complexity, we study worst-case (per node) energy lower bounds for (Monte-Carlo) algorithms that succeed with constant probability. For node-averaged energy complexity, we study lower bounds on the expected node-averaged energy complexity. We note that lower bounds for node-averaged energy complexity also imply the same for worst-case energy complexity.

## 2.3 Basic Facts from Information Theory

We recall some facts from information theory that we rely on in the proofs of Sections 3 and 4. Additional details and proofs can be found in standard textbooks such as [18].

Here, we consider jointly distributed random variables _W_, _X_, _Y_ , and _Z_, and we follow the convention of using capitals for random variables and lowercase letters for values of random variables. We denote the _Shannon entropy of X_ by **H**[_X_], which is defined as

\(\mathbf{H}[X]=\sum_x\mathbf{Pr}[X=x]log_2(1/\mathbf{Pr}[X=x]).\) (1)

