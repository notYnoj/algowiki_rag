## IV. IMPLEMENTATION

The graph-based theory and extension of the dependency graph of Section III are implemented in the Python package `cottax`. It is designed to be extensible: it should support new types of conditional nodes (e.g. least-squares / derivative conditions), data structures (e.g. PyTrees [30] or something entirely different), and use-cases (_consumers_, e.g. exporting or running the graph, which may depend on each other).

The `core` module of the package is then generic: the mathematical graph checks and operations on it are written entirely in plain Python. The current _consumers_ are exporting (Section IVD), declaring (and manipulating and running) the graph with a convenient interface (Section IVE), visualising (Section IVF), using the architectures of Section IIIE (Section IVG), and executing the graph using JAX (Section IVH). Currently, the implemented conditional node types are relational and (experimental) ordinary differential equations (which can be combined in the same graph). PyTrees (a nested hierarchical Python structure) are the implemented data structure types. The software architecture is shown in Figure 11. Each use-case declares what it requires from a node or variable place (Appendix A1) type to work (e.g. the JSON export declares that it needs a way to convert a place to a string). The node or variable place extension registers its interface implementation if desired (dependency inversion). A final assembly file can define shorthand for the consumers (with e.g. some defaults already filled in and a place and conditional node types selected). Each of the consumers and types will be briefly described below.

The `cottax` package is available open-source with an MIT licence at `https://github.com/timobogaarts/cottax`.

Figure 11: Software architecture of `cottax`. Blue indicates generic in both conditional node types and data structure types. Red indicates a conditional node type and yellow a data structure type (they are generic in the other). These implement the interface of the consumers: the exporting (Section IVD), the declaration and surface interface (Section IVE), the visualisation (Section IVF), the architectures of Section IIIE (Section IVG), and the execution (Section IVH).

relational
ode
implements
implements
surface
declaration
core
execution
visualization
export
architectures
consumers
implements
pytree
generic
conditional-node type
datastructure type
built on
implements the interface of

