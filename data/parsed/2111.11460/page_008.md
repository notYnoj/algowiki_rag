<tbc>provide some notation to formalize this idea:

**Definition 4.3.** _Fix a protocol with a single initiator P_<sub>_i_<sub>1</sub></sub> _and a local complexity of_ 1_. We can describe an execution prefix of this protocol containing the first j transmissions with a single_ chain _of the form: X_=(_P_<sub>_i_<sub>1</sub></sub>_,m_<sub>1</sub>),(_P_<sub>_i_<sub>2</sub></sub>_,m_<sub>2</sub>)_,...,(P<sub>i<sub>j</sub></sub>,m<sub>j</sub>), where for each_ \(x,1\le x\le j\)_, P<sub>i<sub>x</sub></sub> is the x<sup>th</sup> player to receive a bit, and the bit it receives is m<sub>x</sub>. If x\<j, then m_<sub>_x_+1</sub> _describes the bit P<sub>i<sub>x</sub></sub> sent in response to receiving m<sub>x</sub>. Define players(X_)={_P_<sub>_i_<sub>1</sub></sub>_,P_<sub>_i_<sub>2</sub></sub>_,...,P<sub>i<sub>j</sub></sub>}. Because P_<sub>_i_<sub>1</sub></sub> _is an initiator, by convention we set_ \(m_1=\emptyset\)_. We use the notation_ \(X,(P_\ell,m)\)_, for some_ \(P_\ell\notin players(X)\)_, to indicate the concatenation of step_ \((P_\ell,m)\) _to the end of chain X._

When considering a chain _X_=(_P_<sub>_i_<sub>1</sub></sub>_,m_<sub>1</sub>),(_P_<sub>_i_<sub>2</sub></sub>_,m_<sub>2</sub>)_,...,(P<sub>i<sub>j</sub></sub>,m<sub>j</sub>_) that describes an execution prefix, we can label each _step_ \((P_\ell,m_j)\) in the chain with a _value pair_, (_x<sub>j</sub>,y<sub>j</sub>_), where _y<sub>j</sub>=j_ is the number of players involved in the chain up to and including \(P_\ell\), and _x<sub>j</sub>_ is the number of these players with an input bit of 1. The value pair for a given step captures, in some sense, a possible information scenario could generate that given step.

When considering the value pairs for a chain of an execution prefix of a protocol computing a threshold function \(f_n^k\), we say a pair of numbers (_x,y_) is _valid_ if two things are true: it is _well-formed_, in the sense that the observed values could show up as a value pair for a step in a chain (e.g., _x_ is not greater than _y_); and they are _bivalent_, in that the values are compatible with both an output of 0 or 1 as the chain extends, depending on the details of the extension. Formally:

**Definition 4.4.** _Suppose the function under consideration is_ \(f_k^n\)_. We say that a pair_ (_x,y_) _is_ valid _with respect to this function if the values are:_

1. Well-Formed: \(1\le y<n\) _and_ \(x\le y\).<tbc>

_2._ Bivalent: \(0\le x<k\) _and_ \((k-x)\le(n-y)\).

When considering chains for an execution of a protocol that computes a given \(f_k^n\) with a local complexity of 1, we might want to ask the question of what are the properties of input bit assignments could possibly lead to a given step (_P<sub>i</sub>,m_). We formalize this question by defining a set _D_ that captures all value pairs compatible with a given step:

**Definition 4.5.** _Given a protocol_ P _that computes a function_ \(f_k^n\) _with local complexity_ 1_, a player_ \(P_i\), \(1\le i\le n\)_, and bit_ \(b\in\{0,1\}\)_, we define the set D(P<sub>i</sub>,b_) _to contain every pair_ (_x,y_) _that satisfies the following properties;_

1. (_x,y_) _is valid with respect to_ \(f_k^n\)_, and_<tbc>

_2._ \(\exists\) _input assignment I for_ P _that induces a chain that includes a step_ (_P<sub>i</sub>,b_) _labeled with value pair_ (_x,y)._

Before tackling our main theorem, we have one last useful result to establish: that every valid pair for a given _k_ and _n_ value can show up in some chain.

**Lemma 4.6.** _Fix a protocol_ P _that computes a function_ \(f_k^n\) _with local complexity_ 1_. Let_ (_x,y_) _be any valid pair for_ \(f_k^n\)_. There exists a player P<sub>i</sub> and bit b, such that the set D(P<sub>i</sub>,b), defined with respect to_ P_, includes_ (_x,y)._

_Proof._ Fix a P, _k_, _n_, and (_x,y_) as specified by the lemma statement. By Lemma 4.2, every execution of P has a single initiator and can be described by a chain. We will create such a chain step by step, setting the input bit for each player in the chain only after they appear in the chain receiving their bit. In more detail, for the first _y-x_ players that show up in the chain, we set their input to 0. For the remaining _x_ players, we set<tbc>

