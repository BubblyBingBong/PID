<div align="center">   
  
# PID Optimization Using Lagrangian Mechanics
</div>


<h3 align="center">
  <a href="https://arxiv.org/abs/2310.00016">arXiv</a>
</h3>

https://github.com/BubblyBingBong/PID/assets/56773653/c3ec9d1c-9d0f-41ef-b38c-1ef65a2e7ec4

## Table of Contents:
1. [Abstract](#abstract)
2. [Anaysis](#analysis)
3. [News](#news)
4. [TODO](#todos)
5. [License](#license)
6. [Citation](#citation)
7. [Resource](#resource)

## Abstract <a name="high"></a>
- :computer: **Simulation**: Creating a simulation of a system enables the tuning of control systems without the need for a physical system.
- :trophy: **PID**: In this research, we employ Lagrangian Mechanics to derive a set of equations to simulate an inverted pendulum on a cart. The system consists of a freely-rotating rod attached to a cart, with the rod’s balance achieved through applying the correct forces to the cart. We manually tune the proportional, integral, and derivative gain coefficients of a Proportional Integral Derivative controller (PID) to balance a rod. To further improve PID performance, we can optimize an objective function to find better gain coefficients.

## Analysis <a name="analysis"></a>
- Using Lagrangian Mechanics, we successfully modele the motion of an inverted pendulum on a cart when forces are applied onto the cart, which allow us to simulate the system and develop PID controllers for the system.
- Both manual tuning and optimization-based tuning methods are used, we can use PID coefficients on optimization-based tuning, similar to those yielding positive results from manual tuning as the initial conditions, which facilitates the generation of highly optimized PID controllers.

## News <a name="news"></a>
- **`09/2023`** PID [paper](https://arxiv.org/abs/2310.00016) is available on arXiv.
- **`09/2023`** Code initial release `v1.0`.
- **`06/2023`** SIP (Science Internship Program) side project summer 2023

## TODO <a name="todos"></a>
- [ ] More sophisticated methods like linear quadratic regulator (LQR) and model predictive control (MPC) could have been used, which would allow for swing-up and swing-down of the rod [5].
- [ ] Learning-based controllers such as imitation learning and reinforcement learning can also be tried.
- [x] More accurate physics models can be derived with optimization or learning-based system identification techniques.
- [x] Compare simulation physics with real-life physics.
- [x] Bugs fix

## License <a name="license"></a>
All assets and code are under the [Apache 2.0 license](./LICENSE) unless specified otherwise.

## Citation <a name="citation"></a>
Please consider citing our paper if the project helps your research with the following BibTex:
```bibtex
@misc{kou2023pid,
      title={PID Optimization Using Lagrangian Mechanics}, 
      author={Ethan Kou and Majid Moghadam},
      year={2023},
      eprint={2310.00016},
      archivePrefix={arXiv},
      primaryClass={eess.SY}
}
```

## Resource
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
- [EKF](https://github.com/BubblyBingBong/EKF) (:rocket:Ours!)
- Visioli, A. (2006). Practical PID control. Springer Science & Business Media.
- Rawlings, J. B. (2000). Tutorial overview of model predictive control. IEEE control systems magazine, 20(3), 38-52.
- Samak, C. V., Samak, T. V., & Kandhasamy, S. (2021). Control strategies for autonomous vehicles. In Autonomous Driving and Advanced Driver-Assistance Systems (ADAS) (pp. 37-86). CRC Press.
- Brizard, A. J. (2014). Introduction To Lagrangian Mechanics, An. World Scientific Publishing Company.
- Bemporad, A., Morari, M., Dua, V., & Pistikopoulos, E. N. (2002). The explicit linear quadratic regulator for constrained systems. Automatica, 38(1), 3-20.
