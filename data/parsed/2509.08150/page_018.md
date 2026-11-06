`class Coordinate(BaseModel):`

`x: Annotated[int, Field(ge=0,lt=W)]`

`y: Annotated[int, Field(ge=0,lt=H)]`

`class WifiOutput(BaseModel):`

`coordinates: Annotated[list[Coordinate],`

`Field(min\_length=k,`

`max\_length=k)]`

### D.2 Prompts in the RAG task

The task prompt for VSGM in the RAG task is as follows:

`task\_prompt = (`

`f"Your task is to select {k} documents Y0..Y{k-1} "`

`+ f"from a list of documents X0..X{len(D)-1} "`

`+ "that helps answer a question Q. "`

`+ f"Select them in {k} steps. "`

`+ "In each step i, select Yi "`

`+ "based on what information is new on top of the documents that are already selected and "`

`+ "how the new information helps answer Q. "`

`+ "\\n"`

`+ f"Q: {Q}\\n"`

`)`

Kwicksselect performs Verbalized kwickselect algorithm for top-_k_ selection. It uses the comparison oracle which performs a following query for each pair (_X,Y_):

`comparison\_criteria = (`

`"We are collecting a set of documents that helps answer a question Q. "`

`"Is information X more helpful than information Y to answer Q?"`

`"\\n"`

`f"Q: {Q}\\n"`

`f"X:\\n{X}\\n"`

`f"Y:\\n{Y}\\n"`

`)`

### D.3 Ground Truth Cost Model of Wifi Task

Let _F_ be points on a \(H\times W\) discrete grid representing the floor map. Given _k_ APs at locations \(y_1,\cdots y_k\in F\), let the signal received from _i_-th AP at location \(x\in F\) be \(S(y_i,x)=\alpha+\beta log||y_i-x||_2+\gamma W(x,y_i)\in\mathbb{R}\), where _W_(**_x_**_,**y**<sub>i</sub>_) is the number of wall grids on the straight line path between **_x_** and **_y_**_<sub>i</sub>_. \(\alpha,\beta,\gamma\) are constants. The optimization objective is \(\sum_{x\in F}max_iS(y_i,x)\), which is submodular.

## E Hardware Details

Maximization and sorting experiments are performed on NVIDIA Tesla A100-80GB GPUs, while clustering and submodular maximization experiments are performed on NVIDIA Tesla H100 GPUs.

## F Effect of Prefix Caching on Sorting Task

A comparison query in VA sorting consists of a prompt, _x_<sub>1</sub>, and _x_<sub>2</sub>. Assume all strings being compared has a fixed length _L_=|_x_<sub>1</sub>|=|_x_<sub>2</sub>|, and that the length of the fixed prefix is _L<sub>p</sub>_. In the exhaustive pairwise comparison among _n_ strings (_O(n_<sup>2</sup>) comparisons, equivalent to insertion sort etc.), a naive inference engine requires _O_((_L<sub>p</sub>_+2_L_)<sup>2</sup>) runtime per each yes/no query, thus _O(n_<sup>2</sup>(_L<sub>p</sub>_+2_L_)<sup>2</sup>) runtime in total, without parallelism.

We analyze the runtime reduction due to kv-caches. Assume that an input query consists of _N+M_ tokens (prefix and suffix), and the kv-cache of _N_ prefix tokens is already available. Each _N+t_-th new input token attends to _N_+(_t_-1) existing tokens, which makes _N+M_+1-th token require \(\sum_{t=1}^M(N+(t-1))=O(NM+M^2)\) runtime. In other words, the runtime of each comparison query reduces to _O_(2_L<sub>p</sub>L_+4_L_<sup>2</sup>), totalling \(O(L_p^2+n^2(2L_pL+4L^2))\) runtime. Moreover, since _x_<sub>1</sub> is repeated _n_ times over _n_<sup>2</sup> comparisons, it further reduces to \(O(L_p^2+n(L_pL+L^2)+n^2((L_p+L)L+L^2))=O(L_p^2+n(L_pL+L^2)+n^2(L_pL+2L^2))\).

