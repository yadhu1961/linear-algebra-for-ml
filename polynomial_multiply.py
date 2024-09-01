import numpy as np

def multiply(A, B):
    """
    Multiplies two polynomials

    Arguments:
    A: Coefficients of the first polynomial
    B: Coefficients of the second polynomial

    Returns:
    C: The coefficients of A*B
    """

    ### BEGIN SOLUTION

    # Find the coefficients of both the polynomials
    na = len(A)
    nb = len(B)

    # Pad the smaller array with 0s
    if na < nb:
        A = np.pad(A, (nb-na , 0))
    else:
        B = np.pad(B, (na-nb , 0))
        
    output_size = 2*len(A) - 1

    pad_size = output_size - len(A)

    A_pad = np.pad(A, (len(A)-1,len(A)-1))
    B_rev= np.pad(np.flip(B), (0,output_size-1))

    print(A_pad)
    print(B_rev)
    C = np.zeros(output_size)

    for i in range(output_size):
       C[i] = np.sum(A_pad*np.roll(B_rev, i))

    print(C)

    # Remove any extra 0s from the back of C
    C = np.trim_zeros(C, 'f')
    
    print(C)

    ### END SOLUTION

    return C

A = np.array([1, 2])
B = np.array([3, 4])
C_exp = np.array([3, 10, 8])
np.testing.assert_allclose(multiply(A, B), C_exp, rtol=1e-5, atol=1e-10)

A = np.array([5, 6])
B = np.array([1, 3, 5, 9])
C_exp = np.array([5, 21, 43, 75, 54])
np.testing.assert_allclose(multiply(A, B), C_exp, rtol=1e-5, atol=1e-10)
np.testing.assert_allclose(multiply(B, A), C_exp, rtol=1e-5, atol=1e-10)

print("All tests passed!")