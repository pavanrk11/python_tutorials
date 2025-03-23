# Numpy basics
import numpy as np

# Array creation

    # converting from std python data structures


    a1D = np.array([1, 2, 3, 4])
    a2D = np.array([[1, 2], [3, 4]])
    a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])


    np.array([127, 128, 129], dtype=np.int8)


    a = np.array([2, 3, 4], dtype=np.uint32)
    b = np.array([5, 6, 7], dtype=np.uint32)
    c_unsigned32 = a - b
    print('unsigned c:', c_unsigned32, c_unsigned32.dtype)
    c_signed32 = a - b.astype(np.int32)
    print('signed c:', c_signed32, c_signed32.dtype)

    # intrinsic creation using numpy functions

    np.arange(10)
    np.arange(2, 10, dtype=float)
    np.arange(2, 3, 0.1)


    np.linspace(1., 4., 6)


    np.eye(3)
    np.eye(3, 5)


    np.diag([1, 2, 3])
    np.diag([1, 2, 3], 1)
    a = np.array([[1, 2], [3, 4]])
    np.diag(a)


    np.vander(np.linspace(0, 2, 5), 2)
    np.vander([1, 2, 3, 4], 2)
    np.vander((1, 2, 3, 4), 4)


    np.zeros((2, 3))
    np.zeros((2, 3, 2))


    np.ones((2, 3))
    np.ones((2, 3, 2))

    #from numpy.random import default_rng
    default_rng(42).random((2,3))
    default_rng(42).random((2,3,2))

    default_rng(42).random((2,3))
    default_rng(42).random((2,3,2))

    np.indices((3,3))

    # Replicating, joining, or mutating existing arrays

    a = np.array([1, 2, 3, 4, 5, 6])
    b = a[:2]
    b += 1
    print('a =', a, '; b =', b)

    a = np.array([1, 2, 3, 4])
    b = a[:2].copy()
    b += 1
    print('a = ', a, 'b = ', b)

    A = np.ones((2, 2))
    B = np.eye(2, 2)
    C = np.zeros((2, 2))
    D = np.diag((-3, -4))
    np.block([[A, B], [C, D]])

    # Reading arrays from standard formats
    # Creating arrays from raw bytes through the use of strings or buffers
    # Use of special library functions (e.g., random)

# Indexing on ndarrays

# I/O with NumPy
# Data types
# Broadcasting
# Copies and views
# Working with Arrays of Strings And Bytes
# Structured arrays
# Universal functions (ufunc) basics