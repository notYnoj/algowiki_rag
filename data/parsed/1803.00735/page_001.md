# A Quantum N-Queens Solver

**The** _N_**-queens problem is to find the position of** _N_ **queens on an** _N_ **by** _N_ **chess board such that no queens attack each other. The excluded diagonals** _N_**-queens problem is a variation where queens cannot be placed on some predefined fields along diagonals. This variation is proven NP-complete and the parameter regime to generate hard instances that are intractable with current classical algorithms is known. We propose a special purpose quantum simulator that implements the excluded diagonals** _N_**-queens completion problem using atoms in an optical lattice and cavity-mediated long-range interactions. Our implementation has no overhead from the embedding allowing to directly probe for a possible quantum advantage in near term devices for optimization problems.**

### 1 Introduction

Quantum technology with its current rapid advances in number, quality and controllability of quantum bits (qubits) is approaching a new era with computational quantum advantage for numerical tasks in reach [1-11]. While building a universal gate-based quantum computer with error-correction is a long-term goal, the requirements on control and fidelity to perform algorithms with such a universal device that outperform their classical counterparts are still elusive. Building special purpose quantum computers with near-term technology and proving computational advantage compared to classical algorithms is thus a goal of the physics community world wide [12]. Quantum simulation with the aim to solve Hamiltonian systems may serve as a building block of such a special purpose quan

tum computer [13-15]. In particular, adiabatic quantum computing [16-18] has been proposed to solve computationally hard problems by finding the ground state of Ising spin glasses [19]. Despite considerable theoretical [18] and experimental [20] efforts, quantum speedup in adiabatic quantum computing has not been demonstrated in an experiment yet [21]. Thus, demonstrating quantum advantage by solving optimization problems using quantum simulation tools is a crucial step towards the development of general programmable quantum optimizers [22, 23].

Here we present a scheme that aims at solving the _N_-queens problem, and variations of it, using atoms with cavity-mediated long-range in

Wolfgang Lechner: wolfgang.lechner@uibk.ac.at

