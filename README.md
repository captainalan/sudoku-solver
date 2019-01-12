Sudoku Solver
=============

This program solves Sudoku puzzles.

This code is here is quite verbose/explicit, but also readable (I
hope).  I started this project while in an airplane racing against my
girlfriend to solve a sudoku puzzle. She finished before I finished
writing this program, lol.

How it work?
------------

To run the tests, do:

```bash
python tests-basic.py

```

To solve a puzzle, use `solver.py` by running:

```bash
python solver.py

```

(I have yet to implement a CLI...)

Other Notes
-----------

### O(???)

As of now, I am employing random numbers/brute force to
follows:

1. For each square, gather the possible values that can complete that
   square.  For instance, a square with the values 1 and 2 filled in
   can be completed in 7! ways. That is, 5040 different ways.
2. Try random guesses.
3. Return the first solution that is found.

### Indices for ages

Notes to self for figuring out which indices this and that...

	0   1  2 |  3  4  5 |  6  7  8 
	9  10 11 | 12 13 14 | 15 16 17
	18 19 20 | 21 22 23 | 24 25 26

	27 28 29 | 30 31 32 | 33 34 35
	36 37 38 | 39 40 41 | 42 43 44
	45 46 47 | 48 49 50 | 51 52 53

	54 55 56 | 57 58 59 | 60 61 62
	63 64 65 | 66 67 68 | 69 70 71
	72 73 74 | 75 76 77 | 78 79 80
