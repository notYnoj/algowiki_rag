## A Detailed Discussion of The Experiment

We show some of the benchmarks from Termination Competition 2020 that are solved by MuVal but not by APROVE, Ultimate Automizer, and iRank- Finder. We also discuss the strength of our method.

### A benchmark containing a nonlinear operation.

Fig. 8a shows one of the benchmarks that contains a nonlinear operation `y = y \* y` but admits a linear ranking function. Although handling nonlinear operation is difficult in general, MuVal was able to verify termination. The reason can be understood as follows. (1) Our validator can find transition examples for this benchmark thanks to the recent development of SMT solvers. (2) Our synthesizer can work as usual because it is example-based.

### A benchmark that requires a long lasso-shaped non-terminating trace to prove non-termination.

Fig. 8b is a benchmark that is non-terminating. To prove non- termination of this benchmark, we need to find a long lasso-shaped trace that ends in the self loop when `i = range = 0`. Finding such a long lasso is difficult in general, but MuVal was able to find one in this benchmark: during CEGIS iterations, MuVal found the self loop (i.e. explicit cycle) and then collected transition examples that were needed to prove reachability of cycles.

Our method can naturally collect transition examples "backward" from the self loop (an explicit cycle). At the same time, our method collects transition examples "forward" from an initial state (in the benchmark of Fig. 8b, the pair of `i = 10` and `range = 20` is an initial state of the while loop). When transition examples that are collected backward and forward form a trace to the self loop, our method notice that the benchmark is non-terminating.

int main() {
int x = ?;
int y = 2;
int res = 1;
if (x < 0 || y < 1) { }
else {
while (x > y) {
y = y*y;
res = 2*res;
}
}
}
int main() {
int i = ?;
int range = 20;
while (0 <= i && i <= range) {
if (!(0 == i && i == range)) {
if (i == range) {
i = 0;
range = range-1;
} else {
i = i+1;
}
}
}
}
(a) A benchmark containing a nonlinear operation.
(b) A benchmark that requires a long lasso to prove non-termination

Fig.8: Some of the benchmarks

