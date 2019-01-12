import sudoku
import random

def solveSudokuPuzzle(puzzle):
    """Function returns solved puzzle.""" 
    # Check if argument is a valid puzzle
    if not puzzle.isValid():
        raise ValueError("Puzzle is no bueno!")

    # Find positions of unknowns.
    unknowns = []
    for index, val in enumerate(puzzle.toList()): # Testing!
        if val == '?':
            unknowns.append(index)
        continue

    # Now brute force solve for those unknowns!
    """Some improvements to make later:
    - Dont try all possible ints, look at the Square the unknown 
      is in and skip testing those values that are definitely
      not the case.
    """

    # RANDOM APPROACH.
    solved = False
    while not solved:
        attempt_list = puzzle.toList()
        for u in unknowns:
            attempt_list[u] = random.randint(1,9)
        attempt = sudoku.Puzzle(attempt_list, isListOfInts=True)
        if attempt.isSolved():
            return attempt

    print(unknowns) # Does it work?

    return "foo"
