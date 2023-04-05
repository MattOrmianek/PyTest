# %%cython -a
#cython: language_level=3
import cython
import numpy as np

@cython.cdivision(True)
@cython.boundscheck(False)
cpdef unsigned char [:,:] image_processing(unsigned char [:,:] image):
    cdef int i,j
    cdef unsigned char [:,:] output =  np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            output[i][j] = 2 * image[i][j]
    return output
