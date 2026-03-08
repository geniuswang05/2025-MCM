# 2025 MCM/ICM Mathematical Modeling Project

This repository contains our solution to the 2025 Mathematical Contest in Modeling (MCM/ICM).

## Problem Overview
Original problem: [ICM_problem](2025_ICM_Problem_E.pdf)

We model the ecological interaction between crops, pest insects, and bats using a system of differential equations. Our goal is to analyze how biological control (bats), pesticide usage, and seasonal factors affect crop production and pest populations.

The model incorporates:

- seasonal crop growth
- pest population dynamics
- bat predation
- agricultural harvesting
- migration effects

## Mathematical Model

The system is formulated as a set of **nonlinear differential equations** describing the interactions among:

- Crops (P)
- Pest insects (H)
- Bats (C)

Key components of the model include:

- logistic crop growth
- predator–prey dynamics
- seasonal forcing functions
- harvesting and pesticide effects

The model is solved numerically using `scipy.integrate.odeint`.

## Paper

You can read the full paper here: [ICM_paper](2506979.pdf)
