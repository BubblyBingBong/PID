import numpy as np
import matplotlib.pyplot as plt

L = 0.05 #length of rod in meters
mu = 0.1 #coefficient of rotational friction

#theta: pendulum angle
#theta_vel: pendulum angular velocity
#x_vel: cart velocity
#x_acc: cart acceleration
def get_angular_accel(data_sample):
    ignore, ignore1, x, theta, ignore2, x_vel, theta_vel, ignore3, x_acc = data_sample
    theta -= np.pi
    return ((-mu * theta_vel) + (6 * L * x_acc * np.cos(theta))
        - (6 * L * x_vel * np.sin(theta)) + (6 * x_vel * L * theta_vel * np.sin(theta))) / (7 * L ** 2)

sample = [1298131026,10000,0.0231,-1.74326,-3.38381,0.22,3.71223,0.,1.] #55
#time, ignore, x, theta, ignore, x_vel, theta_vel, ignore, x_acc
with open("data.txt", 'r') as f:
    data = np.array(eval(f.read()))

calculated_theta_vel = []
time_second = data[:, 0] / 10 ** 9
true_theta_vel = data[:, -3]
x_accel = data[:, -1]
data_size = np.shape(data)[0]

calculated_theta_vel = [true_theta_vel[0]] #initial velocity
#this loop generates the list of calculated theta velocities
for i in range(1, data_size):  #loop starting from next time step
    data_sample = data[i]

    theta_acc = get_angular_accel(data_sample)
    dt = time_second[i] - time_second[i-1]
    prev_theta_vel = calculated_theta_vel[i-1]

    calculated_theta_vel.append(prev_theta_vel + dt * theta_acc)

plt.figure(2)
plt.plot(time_second, true_theta_vel)
plt.plot(time_second, calculated_theta_vel)
plt.legend(['True Theta Vel', 'Calculated Theta Vel'])
plt.xlabel("time (s)")
plt.ylabel("rad/s")

plt.show()
