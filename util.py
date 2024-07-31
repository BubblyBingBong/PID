import time
import casadi
import numpy as np
from scipy.optimize import minimize


class System:
    def __init__(self, initial_state, m, M, L, mu, dt):
        # x, x_vel, x_acc, theta, theta_vel, theta_acc, time
        self.state = initial_state
        self.m = m
        self.M = M
        self.L = L
        self.dt = dt
        self.mu = mu
        self.states = []

    def step(self, applied_force):
        g = 9.8
        fric_force = self.mu * g * (self.M + self.m)
        is_less_than_fric_force = casadi.if_else(applied_force < fric_force, 1, 0)

        if casadi.fabs(applied_force) < fric_force:
            net_force = 0.0
        elif applied_force > 0:
            net_force = applied_force - fric_force
        else:  # applied_force < 0
            net_force = applied_force + fric_force

        prev_x, prev_x_vel, prev_x_acc, prev_theta, prev_theta_vel, prev_theta_acc = (
            self.state
        )
        dt = self.dt

        x = prev_x + prev_x_vel * dt + 1 / 2 * prev_x_acc * dt**2
        x_vel = prev_x_vel + prev_x_acc * dt

        theta = prev_theta + prev_theta_vel * dt + 1 / 2 * prev_theta_acc * dt**2
        theta_vel = prev_theta_vel + prev_theta_acc * dt

        x_acc, theta_acc = self.get_accel(net_force)

        self.state = [x, x_vel, x_acc, theta, theta_vel, theta_acc]
        self.states.append(self.state)

    def get_accel(self, net_force):
        g = 9.8  # m/s^2
        theta = self.state[3]
        theta_vel = self.state[4]

        A = self.M + self.m
        B = -self.m * self.L * np.cos(theta)
        C = self.m * self.L * theta_vel**2 * np.sin(theta) - net_force
        D = -np.cos(theta)
        E = self.L
        F = -g * np.sin(theta)

        x_accel = (F * B - C * E) / (A * E - D * B)
        theta_accel = -(C + A * x_accel) / B
        return [x_accel, theta_accel]


class PID:
    def __init__(self, P, I, D, dt):
        self.P = P
        self.I = I
        self.D = D
        self.dt = dt

        self.error_int = 0
        self.prev_error = 0

    def get(self, error):
        error_deriv = (error - self.prev_error) / self.dt
        self.error_int += self.dt * error
        self.prev_error = error

        control = self.P * error + self.I * self.error_int + self.D * error_deriv
        return clip(control, -500, 500)


def clip(value, min, max):
    if value < min:
        return min
    if value > max:
        return max
    else:
        return value


def sigmoid(x, numer, frac):
    return numer / (1 + np.e ** -(x / frac))


def angle_wrap(angle):  # wraps between -pi and pi
    return (angle + np.pi) % (2 * np.pi) - np.pi
    # angle = casadi.MX.sym('angle')
    # Define the expression
    # return casadi.fmod((angle + casadi.pi), (2 * casadi.pi)) - casadi.pi
