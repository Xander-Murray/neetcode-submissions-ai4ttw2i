import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        z -= max(z)
        s = np.sum(np.exp(z))

        for i in range(len(z)):
            z[i] = (np.exp(z[i]) / s)


        return np.round(z, 4)
