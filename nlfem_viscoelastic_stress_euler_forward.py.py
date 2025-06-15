import numpy as np
import matplotlib.pyplot as plt

gamma = 10.0 # s^-1
eta = 10e5 # MPa
c = 1.0
n = 1.0
alpha = 10e5 # MPa s
sigma_not = 100 # MPa
start = 0
stop = 5
points = 100

t = np.linspace(start,stop, points)
dt = (stop - start) / (points - 1)


#print(t[1])
# print(t)
#print(len(t))
#print(delta_t)
#print(sigma[0])

sigma = np.zeros(len(t) + 1)
sigma[0] = 0
for i in range(0,len(t)):
    sigma[i+1] = sigma[i]*(1 - gamma*dt) + dt*eta*c # Euler Forward

sigma_analytical = (eta * c / gamma) * (1 - np.exp(-gamma * t)) # Exact Solution

plt.plot(t, sigma[1:], label="Euler Forward", marker='o')
plt.plot(t, sigma_analytical,'--', label="Analytical",color='black')
plt.xlabel("Time (t)")
plt.ylabel("Sigma")
plt.title("Euler Forward time integral")
plt.grid(True)
plt.show()
    


