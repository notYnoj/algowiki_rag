`"The final score (coverage) is the sum of signal strengths over the entire floor. " +`

`"This coverage function is submodular. " +`

`"More concretely, it is computed by the following python code: \\n" +`

`""`

`_def signal\_strength(`

`grid: np.ndarray,`

`_ap: tuple[int, int],`_

`_) -\> np.ndarray:`

`_path\_loss\_exp: float = 2.0`

`_wall\_penalty: float = 5.0`

`_H, W = grid.shape`_

`_signal = np.full((H, W), -np.inf)`_

`_for i in range(H):`_

`_for j in range(W):`_

`_if grid[i, j] == 0:`_

`_continue_`

`_d = np.sqrt((i - ap[0])\*\*2 + (j - ap[1])\*\*2) + 1e-6`

`_walls = count\_walls(grid, ap, (i, j))`_

`_signal[i, j] = -10 \* path\_loss\_exp \* np.log10(d) - wall\_penalty \* walls`_

`_return signal_`

`_def coverage\_function(grid: np.ndarray, apps: list[tuple[int, int]], threshold: float = -70.0) -\> float:`

`_H, W = grid.shape`_

`_best\_signal = np.full((H, W), -np.inf)`_

`_for ap in apps:`_

`_sig = signal\_strength(grid, ap)`_

`_best\_signal = np.maximum(best\_signal, sig)`_

`_utility = np.maximum(best\_signal, threshold)`_

`_return float(utility.sum())`_

`"" +`

`"\\nLook at the floor map shown below. " +`

`"The letter '#' indicates a wall, and the letter '.' indicates an empty space. " +`

`"Assume that the top-left position is the origin. "`

`)`

Then each algorithm receives the following prompts. Let `floor\_text` be an ascii art representation of the floor map. VSGM uses the following prompt:

`task\_prompt = (`

`common\_prompt(k) +`

`f"Select {k} locations Y0..Y{k-1} " +`

`f"from a list of locations X0..X{len(C)-1} one by one. " +`

`"Answer the location of each AP as a x-y coordinate on the floor map. " +`

`"Note that the top-left position is the origin. " +`

`"\\nHere is the floor map: \\n" +`

`floor\_text +`

`"\\nHere are the names of available positions:\\n")`

The baseline uses the following prompt:

`prompt = (`

`common\_prompt(k) +`

`"Answer the locations of APs as a list of x-y coordinates on the floor map " +`

`"in the 'coordinates' value of a json dictionary. " +`

`"Do not select the same location twice. " +`

`"Do not select the locations in the walls. " +`

`"\\nHere is the floor map: \\n" +`

`floor\_text)`

Its output is constrained to the following Pydantic-based JSON schema:

