# Sudoku Solver

## Introduction

This Sudoku Solver project provides implementations of three different methods to solve Sudoku puzzles: Backtracking, Forward Checking, and Most-Recently-Used (MRV). Sudoku is a logic-based number-placement puzzle where the objective is to fill a 9x9 grid with digits from 1 to 9, ensuring that each row, each column, and each of the nine 3x3 subgrids contain all of the digits without repetition.

## Methods Used

1. **Backtracking:**
   - The classic recursive backtracking algorithm is used to systematically explore potential solutions, backtracking when a dead-end is reached.

2. **Forward Checking:**
   - Extends the backtracking approach by incorporating forward checking, which reduces the search space by immediately eliminating values that violate constraints.

3. **Most-Recently-Used (MRV):**
   - Utilizes the MRV heuristic, selecting the variable with the fewest legal values first to potentially reduce the search space.

## Usage

1. **Backtracking:**
   - Run `Sudoku.py` and input the unsolved Sudoku puzzle as a 9x9 matrix in the code.

2. **Forward Checking:**
   - Run `SudokuForwardChecking.py` and input the unsolved Sudoku puzzle as a 9x9 matrix in the code.

3. **MRV:**
   - Run `SudokuMRV.py` and 
