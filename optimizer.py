from Util import System, PID, angle_wrap
import numpy as np
from scipy.optimize import minimize, basinhopping
import casadi
import time

loop_time = 0.001  # seconds
run_time = 15
initial_state = [0, 0, 0, np.pi / 4, 0, 0]

options = {"maxiter": 5000}


def objective(x):
    sim = System(m=5, M=5, L=1, mu=0.3, initial_state=initial_state, dt=loop_time)
    p, i, d = x
    pid = PID(p, i, d, loop_time)

    current_time = 0
    while current_time < run_time:
        error = angle_wrap(sim.state[3])
        cart_force = pid.get(error)

        sim.step(cart_force)  # -98 N keeps it constant at pi/4 radians
        current_time += loop_time

    error = np.array(sim.states).T[3]
    sum_weight = 0.0001 * (abs(p) + abs(i) + abs(d))
    return np.mean(abs(error)) + 0.0001 * sum_weight


def scipy_optimized_pid():
    start_time = time.time()
    sol = minimize(objective, x0=np.array([-300, 0, -100], dtype=np.float64))
    print(time.time() - start_time)
    print("loss: " + str(objective(sol.x)))
    print("PID coeffs: " + str(sol.x))
    return sol.x

    # [-1.603e+02 -2.814e+00 -9.468e+01]


def casadi_optimized_pid():
    p = casadi.MX.sym("p")
    i = casadi.MX.sym("i")
    d = casadi.MX.sym("d")
    obj = objective([p, i, d])
    nlp = {"x": casadi.vertcat(p, i, d), "f": objective}
    solver = casadi.nlpsol("solver", "ipopt", nlp)
    solution = solver(x0=[0, 0, 0])
    minimum = solution["f"]
    optimal_p = solution["p"]
    optimal_i = solution["i"]
    optimal_d = solution["d"]

    print(minimum)
    print([optimal_p, optimal_i, optimal_d])
    return [optimal_p, optimal_i, optimal_d]
