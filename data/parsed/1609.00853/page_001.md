# A _q_-QUEENS PROBLEM V. SOME OF OUR FAVORITE PIECES: QUEENS, BISHOPS, ROOKS, AND NIGHTRIDERS

Abstract. Parts I-IV showed that the number of ways to place _q_ nonattacking queens or similar chess pieces on an \(n\times n\) chessboard is a quasipolynomial function of _n_ whose coefficients are essentially polynomials in _q_. For partial queens, which have a subset of the queen’s moves, we proved complete formulas for these counting quasipolynomials for small numbers of pieces and other formulas for high-order coefficients of the general counting quasipolynomials. We found some upper and lower bounds for the periods of those quasipolynomials by calculating explicit denominators of vertices of the inside-out polytope.

Here we discover more about the counting quasipolynomials for partial queens, both familiar and strange, and the nightrider and its subpieces, and we compare our results to the empirical formulas found by Kotˇešovec. We prove some of Kotˇešovec’s formulas and conjectures about the quasipolynomials and their high-order coefficients, and in some instances go beyond them.

### 1. Introduction

We apply our study of nonattacking chess pieces from Parts I-IV [3, 4, 5, 6] to standard chess pieces--the queen, bishop, and rook (even the rook is interesting)--and our favorite fairy chess piece, the nightrider, which moves any distance in the directions of a knight’s move. And to the "partial queens" and "partial nightriders" that, like the bishop and rook, have a subset of the queen’s or the nightrider’s moves.

The classic _n_-Queens Problem asks for the number of nonattacking configurations of _n_ queens on an \(n\times n\) chessboard. It has no practical general solution; the only known general formulas are the computationally impractical ones in Part II [4] and in [14]. We began our study by separating _n_, the board size, from _q_, the number of queens, arriving at the _q-Queens Problem_: In how many ways can _q_ queens be placed on an \(n\times n\) chessboard so that no queen attacks another? In Parts I-IV we developed a general geometrical theory of this number, _u_<sub>Q</sub>(_q;n_), as a function of integers _n_ and _q\>_0, for all chess and fairy chess pieces that, like the queen, bishop, rook, and nightrider, have moves of unlimited length. Such pieces are called _riders_ by the fairy chess community.<sup>1</sup> The problem, given a rider P, is this:

**Problem 1.** Find an explicit formula for _u_<sub>P</sub>(_q;n_), the number of nonattacking configurations of _q_ unlabelled pieces P on an \(n\times n\) board.

2010 _Mathematics Subject Classification._ Primary 05A15; Secondary 00A08, 52C07, 52C35. _Key words and phrases._ Nonattacking chess pieces, fairy chess pieces, Ehrhart theory, inside-out polytope, arrangement of hyperplanes. The first author gratefully acknowledges support from PSC-CUNY Research Awards PSCOOC-40-124, PSCREG-41-303, TRADA-42-115, TRADA-43-127, and TRADA-44-168. The latter two authors thank the very hospitable Isaac Newton Institute for facilitating their work on this project. <sup>1</sup>Fairy chess is chess with unusual pieces, rules, or boards.

SETH CHAIKEN, CHRISTOPHER R. H. HANUSA, AND THOMAS ZASLAVSKY

