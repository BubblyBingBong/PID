import numpy as np
import matplotlib.pyplot as plt
from Util import System, PID, angle_wrap
from Optimizer import scipy_optimized_pid, casadi_optimized_pid


loop_time = 0.001  # seconds
run_time = 15
initial_state = [0, 0, 0, np.pi / 4, 0, 0]

sim = System(m=5, M=5, L=1, mu=0.3, initial_state=initial_state, dt=loop_time)

# -301.76846483 - 70.00286526 - 81.65334506 (500 ME) I empty
# -340.63140198  -35.19439898  -62.89543085 (500 RMSE) I empty

# -341.26151785  -93.4961236   -26.24533506 (500 RMSE) legit I full
# [-318.86706861 -103.8451677   -23.11037839 (500 RME) legit I empty

# p, i, d = scipy_optimized_pid()
# p, i, d = [-308.08161198,  -63.54809726,  -94.96419398]
# p, i, d = [-289.56760579,  -77.18117922,  -60.64829768]
p, i, d = [-289.57, -77.18, -60.65]
pid = PID(p, i, d, loop_time)


current_time = 0
applied_forces = []
while current_time < run_time:
    error = angle_wrap(sim.state[3])
    applied_force = pid.get(error)
    applied_forces.append(applied_force)
    sim.step(applied_force)  # -98 N keeps it constant at pi/4 radians
    current_time += loop_time


x, x_vel, x_acc, theta, theta_vel, theta_acc = np.array(sim.states).T
times = loop_time * np.arange(np.shape(sim.states)[0])

plt.figure(1)
plt.title("Rod Angle vs Time")
plt.plot(times, theta)
plt.ylabel("Rod Angle (rad)")
plt.xlabel("Time (s)")

plt.figure(2)
plt.plot(times, x)
plt.ylabel("meters")
plt.xlabel("Time (s)")
plt.legend(['Cart Position'])

plt.figure(3)
plt.title("Applied Force vs Time")
plt.plot(times, applied_forces)
plt.ylabel("Applied Force (N)")
plt.xlabel("Time (s)")

plt.show()
