<tbc>where _U<sub>i</sub>(r_) is non-increasing as integer _r(r\>_0) increases. Intuitively, it means that higher order (smaller _r_) would generate higher degree of satisfaction for agent _i_.

The aggregate utility of students (or colleges) under outcome _o_ is then:

\(\pi_S(o)=\sum_{s\in\mathcal{S}}u_s(o),\forall o\in\mathcal{O};\)<br>
\(\pi_C(o)=\sum_{c\in\mathcal{C}}u_c(o),\forall o\in\mathcal{O}.\)

The _social welfare_ is defined as the aggregate utility of all participants in the mechanism, which can be written as follows:

\(\Pi(o)=\sum_{i\in I}u_i(o)=\pi_S(o)+\pi_C(o),\forall o\in\mathcal{O}.\)

We say matching outcome _o_<sub>1</sub> is more _efficient_ than _o_<sub>2</sub> if:

\(\Pi(o_1)>\Pi(o_2)o_1,o_2\in\mathcal{O}.\)

We further say mechanism M<sub>1</sub> is more _efficient_ than M<sub>2</sub> if M<sub>1</sub> can always induce a more efficient matching outcome than M<sub>2</sub> under any possible preference lists of agents. Generally speaking, an outcome would be more efficient if it induces higher ranked matching. In the context of college admissions, a mechanism which generates more first-choice matching for students is likely to be more efficient.

### 5.1 Simulation Settings

Suppose there are 10 students and 5 colleges with just one quota in each college. We assume the utility of each agent is as follows,

\(U_s(r)=11-r,r\in\{1,2,\dots,5\}\)<br>
\(U_c(r)=11-r,r\in\{1,2,\dots,10\}\)<br>
\(U_s(0)=U_c(0)=0.\)

Thus a first-ranked matching would bring in utility of 10 for either students or colleges. Notice that the efficiency upper bound is 100 since there are at most five pairs of students and colleges matched with each other.

The preference lists of students are generated as follows:

Student _s_ evaluates each college _c_ by this formulae,

\(g_s^c=\beta g^c+(1-\beta)g_s(c),\beta\in[0,1]\)

where (_g_<sup>_c_<sub>1</sub></sup>_,g_<sup>_c_<sub>2</sub></sup>_,g_<sup>_c_<sub>3</sub></sup>_,g_<sup>_c_<sub>4</sub></sup>_,g_<sup>_c_<sub>5</sub></sup>)=(100,90,80,70,60) denotes the social reputation of each college and _g<sub>s</sub>(c_) denotes the individual preference of student _s_,

