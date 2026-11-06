<tbc>package \[49\], building on prior work of Pate et al. \[28\]. Part of this (re)configuration support includes algorithmic ordering and partitioning of the graph, and KADMOS provides preset architectures to implement. Custom architectures that e.g. assign couplings to specific drivers or have deep nesting require manually defining new architecture presets. AGILE defines couplings to various execution layers (incl. RCE \[50\] and OpenMDAO \[8\] via OpenLEGO \[51\]), but focuses more on multi-institutional collaborative infrastructure \[52\]. These implementations therefore are not particularly suited for low-latency coupling of autodifferentiable models.

AeroSandbox \[53, 54\] similarly considers a computational graph and transformations thereof, but argues for a procedural programming interface -- on the grounds that a functional programming style requires careful ordering, significant boilerplate, and inflexible problem and constraint definitions during scripting. However, as the above references (\[25, 26\]) have shown, topological sorting can eliminate the first objection. As \[54\] notes, modular disciplines are increasingly attractive for high-fidelity and complex optimisation problems, such as we consider in this work. Furthermore, the adoption of a JAX-based approach removes any boilerplate-induced computational overhead. Lastly, a functional programming style maps naturally to a graph-based approach that precisely allows high flexibility in problem formulation, as shown by \[49\].

Beyond MDAO frameworks, (systems-level acausal) modelling languages such as Modelica \[55\] or ModelingToolkit.jl \[36\] similarly build a computational graph from equations, ordering automatically and resolving the induced functional cycles. However, the frameworks have different use-cases, often with a lower granularity (symbolic scalar equations instead of array-based opaque models), and because they are not geared towards (multidisciplinary) optimisation are not easily adapted to fusion design optimisation problems.

Fusion (integrated) design approaches typically feature custom frameworks. For example, PROCESS \[2, 3\] uses a fixed model order with hand-picked iteration variables and consistency constraints; FUSE \[11\], BLUEMIRA \[9, 12, 22\], and SYCOMORE \[4\] also hand-declare their analysis workflows. SIMSOPT \[23\] and DESC \[24\] are frameworks for stellarator optimisation which also require explicit manual ordering and MDAO architecture specification.

Overall, various MDAO frameworks have been considered as a basis for a stellarator design framework. As  I summarises, the available frameworks do not sufficiently fulfil the needs for our application. This has motivated the development of `cottax`, which will now be introduced.

\begin{tabular}{cccccc}
 & Design problem

agnostic & Automated

coordination & Flexible MDAO

architecture & Gradient

computation & Low overhead \\
OpenMDAO \[8\] & \(\unknown\) & ∼ within model

Group & ∼ any nesting,

manual & \(\unknown\) MAUD & ∼ Python

orchestration \\
GEMSEO \[25\] & \(\unknown\) & \(\unknown\) & ∼ presets & \(\unknown\) coupled adjoint & ∼ Python

orchestration \\
AGILE / KADMOS \[27, 49\] & \(\unknown\) & \(\unknown\) & ∼ presets & ∼ via exec. layer & - file-based \\
AeroSandbox \[54\] & ∼ procedural

script & - & - SAND only & \(\unknown\) AD & \(\unknown\) \\
PROCESS \[2, 3\] & ∼ modular code & - & - & ∼ FD & ∼ Python

orchestration \\
BLUEMIRA \[22\], SIMSOPT \[23\] & ∼ modular code & - & - & ∼ FD, partially

analytic & ∼ Python

orchestration \\
DESC \[24\], FUSE \[11\] & ∼ modular code & - & - & \(\unknown\) JAX / Julia

AD & \(\unknown\) \\
\end{tabular}

I: An overview of the open-source MDAO frameworks that have been considered as the basis for a future stellarator reactor design framework.

