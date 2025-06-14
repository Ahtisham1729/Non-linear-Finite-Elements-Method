import numpy as np




def quadrature(f,matrix):
    F_ext_total = np.zeros((8,1))
    w_alpha = 1
    gp = 1 / np.sqrt(3)
    gauss_points = np.array([
        [-gp, -gp],
        [ gp, -gp],
        [ gp,  gp],
        [-gp,  gp]
    ])
    F_ext = []
    for xi1,xi2 in gauss_points:
        N = 0.25 * np.array([
            (1 - xi1)*(1 - xi2),
            (1 + xi1)*(1 - xi2),
            (1 + xi1)*(1 + xi2),
            (1 - xi1)*(1 + xi2)
        ])
        
        N_matrix = np.zeros((2,8))
        for i in range(4):
            N_matrix[0,2*i] = N[i]
            N_matrix[1,2*i+1] = N[i]
        
        #print(N_matrix)
        #print(N_matrix.shape)
        dN_dxi1 = np.array([
            -0.25 * (1 - xi2),
             0.25 * (1 - xi2),
             0.25 * (1 + xi2),
            -0.25 * (1 + xi2)
        ])
        dN_dxi2 = np.array([
            -0.25 * (1 - xi1),
            -0.25 * (1 + xi1),
             0.25 * (1 + xi1),
             0.25 * (1 - xi1)
        ])
        dN_dxi = np.array([dN_dxi1, dN_dxi2])
        #print(dN_dxi)
        jacobian = np.dot(dN_dxi,matrix.T)
        #print(jacobian)
        det_jacobian = np.linalg.det(jacobian)
        #print(det_jacobian)

        # compute dot product of shape function and gravity body load
        F_ext = np.dot(N_matrix.T,f)
        F_ext = F_ext*det_jacobian*w_alpha
        F_ext_total += F_ext
    return F_ext_total

rho = 300
g = 9.81
f = np.array([
    [0],
    [-rho*g]
])
a = 0
b = 0
l = 2
nodal_location = np.array([
    [a, a+3*l, a+3*l, a],
    [b, b, b+l, b+l]
])


r = quadrature(f,nodal_location)
print(r.shape)
print(r)




        

