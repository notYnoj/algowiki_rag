<tbc>generation rules

\(T_1=\{\{\{C_{1,1}\},C_{2,1}\},\{\{C_{1,1}\},C_{5,i}\},\{\{C_{2,1}\},C_{3,i}\},\{\{C_{3,1}\},C_{1,1}\},\{\{C_{4,1}\},C_{1,1}\},\)<br>
\(\{\{C_{5,1}\},C_{6,1}\}\},\)<br>
\(T_i=\{\{\{C_{1,i}\},C_{2,i}\},\{\{C_{1,i}\},C_{5,i}\},\{\{C_{2,i}\},C_{3,i}\},\{\{C_{3,i}\},C_{4,i-1}\},\)<br>
\(\{\{C_{4,i}\},C_{4,i-1}\},\{\{C_{5,i}\},C_{6,i}\}\}\text{if}i>1.\)

The set _D_ of domination rules is empty except for all rules of the form \((\{C\},C')\) such that \(w(C)\ge w(C')\) and \(C\cap C'\neq\emptyset\). As starting coalition structure we have {_C_<sub>4_,k_</sub>}.

The dynamics are best understood when using the object movement graph instead of dealing with the single vertices. In Figure 1 we give the object movement graph of the first two gadgets to visualize the dynamics of the gadgets themselves as well as their interaction. We will analyze the dynamics of gadget 1. The subsequent gadgets work similarly. In the beginning there are no coalitions in gadget 1 so we first have a look at how to get some coalition to start from. Now every _C_<sub>4_,i_</sub> for _i\>_1 can only be used to generate _C_<sub>4_,i_-1</sub>. Note that in this case _C_<sub>4_,i_</sub> is not deleted. Thus in the beginning those _C_<sub>4_,i_</sub> are one by one created until we reach _C_<sub>4,1</sub>. With _C_<sub>4,1</sub> we can only generate _C_<sub>1,1</sub> (in gadgets _i\>_1 in this situation we might generate _C_<sub>4_,i_-1</sub> and then "wait" for _C_<sub>1_,i_</sub> to arrive). Next as _C_<sub>5,1</sub> is blocked by _C_<sub>4,1</sub> the only option is to generate _C_<sub>2,1</sub> and thus lose _C_<sub>1,1</sub> again. From there we can only generate _C_<sub>3,1</sub> while losing _C_<sub>2,1</sub> and _C_<sub>4,1</sub>. With the remaining coalition _C_<sub>3,1</sub> we can recover _C_<sub>1,1</sub> which now leads to creating _C_<sub>5,1</sub> and losing _C_<sub>1,1</sub> a second time. Next we can only create _C_<sub>6,1</sub> which causes the deletion of _C_<sub>3,1</sub> and _C_<sub>5,1</sub>. Finally _C_<sub>6,1</sub> can now be used to create _C_<sub>1,2</sub> which leaves gadget 1 empty. But at the latest after _C_<sub>3,2</sub> has been created in the next step _C_<sub>4,1</sub> has to be created again and we can rerun the dynamics for the gadget in the same manner.

C2,1
C3,1
C2,2
C3,2
C4,1
C4,2
C1,1
C5,1
C6,1
C1,2
C5,2
C6,2

**Fig.1. Object movement graph of gadget 1 and 2:** the thick edges symbolize domination rules and the dashed edges symbolize generation rules

