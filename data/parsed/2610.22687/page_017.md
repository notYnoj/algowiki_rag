## F. Visualisation

All figures in this paper are drawn with the visualisation use-case in `cottax`. It can generate both the figures in Sections III and V and interactive HTML versions that additionally step through a set of graph operations (see Section V).

## G. Architectures

The architectures of Section IIIE are implemented as a consumer (requirement 2). They are generic with respect to the conditional node and can be used both for algebraic relational and ODE solving and optimising (or even combining them). MDF/IDF/SAND are directly implemented, including the possible rules for cutting (Gauss–Seidel with given order, Gauss–Seidel with minimal coupling, or Jacobi), and are used in the PROCESS results directly (Section V).

They also do not require implementations for the functional and conditional nodes: the MDAO architecture can be defined with just the inputs and outputs of all functions and the conditions and unknowns of all conditional nodes defined.

## H. Execution

An execution layer is implemented using Python and can be executed eagerly for analysis workflows (using the Python interpreter as orchestration).

Most importantly, it can also be compiled and transformed directly using JAX [30]. During JAX tracing, the graph is traversed in Python and all array operations, functions, and the connections between them are recorded into a single program that JAX then compiles. Tracing thus removes the graph-based core from the executed program entirely: the final program is equivalent to a manual ordering, satisfying requirement 5. See Appendix B for a worked example of this equivalence. Trace time is very low (less than a second in Section V); compile time can be significant as it scales with the size of the program and has to be repeated for every change in the graph (but not for changing values; in Section V it is within 5 seconds in all cases).

The executable graph is then simply another JAX-compatible function and thus supports all JAX transformations. In particular, if all functions are in JAX, batching is trivial using the built-in `vmap` primitive: the entire executable

from cottax.assemblies.jax import (
SLSQP, Newton, Picard, Start)
drivers = SLSQP(), Picard(), Newton()
# (a) under MDF, from a dict
start = dict(z_1=5., z_2=2., x=1., y_1=1., y_2=1.,
f=None, g=None)
mdf = model_a + flat.mdf(opt_a) + flat.drive(*drivers)
out = flat.run(mdf, read_from={Start: start})
start = out.into(start)
# (b) under SAND, from and into its own structure
state = State(Design(5., 2., 1.), Coupling(1., 1.),
Metrics(f=None, g=None))
sand = model_b + absolute.sand(opt_b) + absolute.drive(*drivers)
out = absolute.run(sand, read_from={Start: state})
state = out.into(state)
print(f"f = {start['f']:.4f} (a), {state.metrics.f:.4f} (b)")
f = 3.1834 (a), 3.1834 (b)

Figure 13: Running the graph for two different architectures: default driver implementations are given, the starting values are given, the graph after the graph operations is created and it is run. Both architectures converge to the same result.

