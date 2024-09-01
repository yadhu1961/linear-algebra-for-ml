import numpy as np

def beta(x, y, S):
    return x @ S @ y.T

def is_bilinear(x, y, z, S):
    lambda_factor = 10

    x_plus_lambda_z = x + (lambda_factor * z)
    return beta(x_plus_lambda_z, y, S) == beta(x, y, S) + (lambda_factor*beta(z, y, S))

def is_positive_definite(S):
    eig_vals, eig_vec  = np.linalg.eig(S)
    # print(eig_vals)
    eig_vals = eig_vals > 0
    return sum(eig_vals) == len(eig_vals)

def is_inner_product(x, y, z, S):
    return is_positive_definite(S) and is_bilinear(x, y, z, S) and (S == S.T).all()


S = np.array([[1, -0.5], [-0.5, 1]])

x = np.array([1, 2])
y = np.array([2, 3])
z = np.array([1, -1])

print(is_bilinear(x, y, z, S))
print(is_positive_definite(S))
print(is_inner_product(x, y, z, S))



