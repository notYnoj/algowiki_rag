# Time-Optimal APSP and Matrix Multiplication in Classes of Linear Neighborhood Complexity

**Abstract**

The notion of _linear neighborhood complexity_ is a very general structural assumption on a graph class, covering most classes of sparse graphs such as planar graphs, graphs excluding a fixed (topological) minor, or bounded expansion graphs, as well as many structured classes of dense graphs, such as graphs of bounded clique-width, twin-width, merge-width, or flip-width.

In this work, we present O(_n_<sup>2</sup>)-time optimal algorithms for _n_-vertex graphs coming from a class of linear neighborhood complexity for the following problems:

\(\bullet\) All-Pairs Shortest Paths,

\(\bullet\) the multiplication of the adjacency matrix _M_ of the input graph with any \(n\times n\) matrix. More specifically, after a quadratic preprocessing, we can multiply _M_ with any _n_-vector in O(_n_) time.

This solves several questions raised in [Bonnet, Kim, Geniet, Moon; ICALP ’26], and improves and generalizes results in several other recent papers [Bonnet, Giocanti, Ossona de Mendez, Thomassé; STACS ’23], [Bannach, Marwitz, Tantau; STACS ’24], [Anand, van den Brand, McCarty; NeurIPS ’26], [Kozma, Oppler ’26], and [Cardinal, McCarty, Yuditsky ’26]. We also extend our results to classes of bounded VC density.

In classes of linear neighborhood complexity, we also give a triangle-detection algorithm in randomized linear time O(_n+m_) in _n_-vertex _m_-edge graphs, a _K_<sub>4</sub>-detection algorithm in randomized O(_n_log<sup>5</sup>_n+m_log_n_) or deterministic O(_n_<sup>2</sup>) time, and a _K_<sub>5</sub>-detection algorithm in randomized O(_n_log<sup>9</sup>_n+m_log<sup>5</sup>_n_) time.

<sup>∗</sup>CNRS, ENS de Lyon, Université Claude Bernard Lyon 1, LIP UMR 5668, 69342 Lyon, France. Homepage: `http://perso.ens-lyon.fr/edouard.bonnet`. Email: `edouard.bonnet@ens-lyon.fr`. <sup>†</sup>Institute of Informatics, University of Warsaw, Poland. Email: `j.duron@uw.edu.pl` <sup>‡</sup>Institute of Informatics, University of Warsaw, Poland. Homepage: `https://www.mimuw.edu.pl/~malcin/`. Email: `m.pilipczuk@uw.edu.pl`. <sup>§</sup>Max Planck Institute for Informatics, Saarland Informatics Campus, Saarbrücken, Germany. Homepage: `https: //mnbvmar.github.io`. Supported by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) grant number 559177164. Email: `msokolow@mpi-inf.mpg.de`. \(^\unknown\)Institute of Informatics, University of Warsaw, Poland. Homepage: `https://www.mimuw.edu.pl/~szymtor/`. Email: `szymtor@uw.edu.pl`.

Édouard Bonnet<sup>∗</sup> Julien Duron<sup>†</sup> Marcin Pilipczuk<sup>‡</sup> Marek Sokolowski<sup>§</sup> Szymon Toruńczyk\(^\unknown\)

August 27, 2026

