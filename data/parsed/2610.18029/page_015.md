graph of 156 vertices or fewer. In the next section, we will describe our efforts to further the classical preprocessing such that larger raw input sizes results in graphs small enough to implement on these devices, but for now, let us examine the current performance of these devices.

Running on _IBM Heron_ r3 machines (_Boston_ and _Aachen_), we train and run our modified QAOA circuits, requiring the same 64 qubits and 3500 two-qubit gates. Due to the noisy nature of current machines, we see a very high variance in the results from QAOA runs, but nonetheless we can see that it can clearly outperforms taking random shots, which in itself is surprisingly much faster than using an approximate classical algorithm that can produce a single MWC to yield a large set of MWCs. Crucially, the 20,000 shots we choose to use based on the resources we have available is very small in the scheme of quantum experiments and allows for the massive potential to scale up the final sampling run in order to obtain a much larger set of MWCs.

The random shot baseline draws each bit independently with probability 0.5 and applies the same postprocessing as for the QAOA samples. By sampling in this manner we uniformly sample from the space of all subgraphs.

## 5 Quantum Focused Preprocessing

In light of the limited capacity of quantum devices, the preprocessing of the input data to yield the smallest possible graph becomes especially important. Here, we look at extending the preprocessing in [5] to take into account reductions that isolate the difficult core of hard problem instances at the cost of extra processing and also utilise sophisticated optimisers.

450
425
400
375
# MWCs Found
350
325
300
275
250
Random Shots
Modified QAOA

Figure 5: Resulting number of MWCs found from 10 runs of 20,000 shots of random shots and from our modified QAOA

.

