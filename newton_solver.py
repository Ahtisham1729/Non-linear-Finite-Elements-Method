import numpy as np

def G(y):
    y1, y2 = y[0], y[1]
    G1 = 4*y1**2 + y2**2 + 2*y1*y2 - y2 -2
    G2 = 2*y1**2 + y2**2 + 3*y1*y2 - 3
    return np.array([G1,G2])

def K(y):
    y1, y2 = y[0], y[1]
    K11 = 8*y1 + 2*y2
    K12 = 2*y2 + 2*y1 - 1
    K21 = 4*y1 + 3*y2
    K22 = 2*y2 + 3*y1
    K_matrix = np.array([
        [K11, K12],
        [K21, K22]
    ])
    return K_matrix

def newton_raphson(y0, max_iter=10, tol=1e-6):
    y = y0.copy()
    residual_norms = []
    incremental_norms = []
    for i in range(max_iter):
        res = G(y)
        stiffness = K(y)
        delta_y = np.linalg.solve(stiffness,res)

        res_norm = np.linalg.norm(res,2)
        incr_norm = np.linalg.norm(delta_y,2)

        residual_norms.append(res_norm)
        incremental_norms.append(incr_norm)

        print(f"Iteration {i+1}: y = {y}, ||G|| = {res_norm:.3e}, ||Δy|| = {incr_norm:.3e}")

        y = y - delta_y

        if res_norm < tol and incr_norm < tol:
            print("Converged")
            break
    return y

if __name__ == "__main__":
    # Initial Guess
    y0 = np.array([0.4, 0.9])
    print(f"Starting Newton Raphson solver...")
    y_final = newton_raphson(y0)
    print(f"\nApproximate solution after iterations: {y_final}")
