# Genetic Algorithm Optimizer

A Python application that uses a **genetic algorithm** to find the **maximum** of a given **quadratic function** over a specified domain.

This project includes:
- Binary-encoded chromosomes
- Roulette-wheel selection using binary search
- Single-point crossover
- Bit-flip mutation
- Elitist selection
- GUI with Tkinter
- Detailed evolution logging

##  Problem Description

The algorithm maximizes a second-degree polynomial:
f(x) = ax² + bx + c
The optimization is done over a closed interval with floating-point precision, using a genetic approach.

## Input Parameters

- **Population size**: Number of chromosomes
- **Interval [a, b]**: Domain of the function
- **Coefficients a, b, c**: For the quadratic function
- **Precision**: Decimal precision (e.g., 6 → 0.000001 steps)
- **Crossover probability**: e.g., 0.25 (25%)
- **Mutation probability**: e.g., 0.01 (1%)
- **Number of generations**: Evolution steps

## Output

The script outputs a detailed result in the file named `functionMax_output` containing:

- Initial population with binary and decoded values
- Fitness values for each chromosome
- Selection probabilities and chosen chromosomes
- Crossover events and offspring
- Mutation operations
- For each generation: max and average fitness

---

##  GUI Mode

To launch the graphical interface:
```bash
python gui.py


