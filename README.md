# Sudoku Solver

This code is here is quite verbose/explicit, but also readable.  I started this
project while in an airplane racing against my girlfriend to solve a sudoku
puzzle. She finished before I finished writing this program, lol.

To run the tests, do:

```bash
python tests-basic.py
```

To solve a puzzle, use `solver.py` by running:

```bash
python solver.py
```

As of now, I am employing a simple brute force algorithm that works as follows:

1. For each square, gather the possible values that can complete that square.
   For instance, a square with the values 1 and 2 filled in can be completed
   in 7! ways. That is, 5040 different ways.
2. Try all the combinations, rejecting invalid squares. 
3. Return the first solution (fake lazy evaluation?).


