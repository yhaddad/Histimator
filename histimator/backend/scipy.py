from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import scipy as sc


class scipy(object):
    def __init__(self, **kwargs):
        pass

    def tensor(self, array, name, dtype=np.float32):
        return np.asarray(array).astype(dtype)
