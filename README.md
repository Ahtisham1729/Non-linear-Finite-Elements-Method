# Nonlinear Finite Element Method (NLFEM)

This repository contains an in-progress Python implementation of the Nonlinear Finite Element Method (NLFEM) for 2D structural problems.

The aim is to build a modular codebase that includes:

- Rod and Q4 elements
- External body force integration using Gauss quadrature
- Support for elastic and creep constitutive models
- Global system assembly for nonlinear problems

## Status

Current development focus:
- [x] Time integration schemes (Euler forward, Euler Backward, Midpoint Rule, Explicit second order Runge-Kutta)
- [x] External force vector using Gauss quadrature
- [ ] Element stiffness and internal force routines
- [x] Newton-Raphson solver
- [ ] Material model integration


## Requirements

- numpy  
- sympy  

Install dependencies with:

```bash
pip install numpy sympy
