import unittest
import sudoku

class TestSudokuMethods(unittest.TestCase):

    def setUp(self):
        pass

    # Test Square class
    def test_Square_constructor(self):
        pass

    def test_Square_eq(self):
        foo = sudoku.Square([1,2,3,4,5,6,7,8,9])
        bar = sudoku.Square([1,2,3,4,5,6,7,8,9])
        self.assertTrue(foo == bar)

    def test_Square_isValid(self):
        # A good square
        validSquare = sudoku.Square([1,2,3,4,5,6,7,8,9])
        self.assertTrue(validSquare.isValid())

        # A good square with an unknown
        validSquareWithUnknown = sudoku.Square([1,'?',3,4,5,6,7,8,9])
        self.assertTrue(validSquareWithUnknown.isValid())

        # Duplicate of tile with val 9, no val 1
        invalidSquare = sudoku.Square([9,2,3,4,5,6,7,8,9])
        self.assertFalse(invalidSquare.isValid())

        # Non-int value
        nonIntSquare = sudoku.Square(['one',2,3,4,5,6,7,8,9])
        self.assertFalse(nonIntSquare.isValid())

    def test_Square_isSolved(self):
        # Should be true
        goodSquare = sudoku.Square([1,2,3,4,5,6,7,8,9])
        self.assertTrue(goodSquare.isSolved())

        # Contains invalid value
        invalidSquare1 = sudoku.Square(['one',2,3,4,5,6,7,8,9])
        self.assertFalse(invalidSquare1.isSolved())

        # Another invalid square
        invalidSquare2 = sudoku.Square([9,2,3,4,5,6,7,8,9])
        self.assertFalse(invalidSquare2.isSolved())

        # Contains unknown value
        unknownSquare1 = sudoku.Square(['?',2,3,4,5,6,7,8,9])
        self.assertFalse(unknownSquare1.isSolved())

        # Test Puzzle Class
    def test_Puzzle_constructor(self):
        pass

    def test_Puzzle_isValid(self):
         validPuzzle = sudoku.Puzzle(
             [sudoku.Square([4,3,5,6,8,2,1,9,7]),
              sudoku.Square([2,6,9,5,7,1,8,3,4]),
              sudoku.Square([7,8,1,4,9,3,5,6,2]),
              sudoku.Square([8,2,6,3,7,4,9,5,1]),
              sudoku.Square([1,9,5,6,8,2,7,4,3]),
              sudoku.Square([3,4,7,9,1,5,6,2,8]),
              sudoku.Square([5,1,9,2,4,8,7,6,3]),
              sudoku.Square([3,2,6,9,5,7,4,1,8]),
              sudoku.Square([8,7,4,1,3,6,2,5,9])])
         self.assertTrue(validPuzzle.isValid())

         validPuzzleWithUnknowns = sudoku.Puzzle(
             [sudoku.Square([4,3,5,6,8,2,1,'?',7]),
              sudoku.Square([2,6,9,5,7,1,8,'?',4]),
              sudoku.Square([7,8,1,4,9,3,5,6,2]),
              sudoku.Square([8,2,6,3,7,4,9,5,1]),
              sudoku.Square([1,9,5,6,8,2,7,4,3]),
              sudoku.Square([3,4,7,9,1,5,6,2,8]),
              sudoku.Square([5,1,9,2,4,8,7,6,3]),
              sudoku.Square([3,2,6,9,5,7,4,1,8]),
              sudoku.Square([8,7,4,1,3,6,2,5,9])])
         self.assertTrue(validPuzzleWithUnknowns.isValid())

         validPuzzleAllUnkowns = sudoku.Puzzle(
             [sudoku.Square(['?','?','?','?','?','?','?','?','?']),
              sudoku.Square(['?','?','?','?','?','?','?','?','?']),
              sudoku.Square(['?','?','?','?','?','?','?','?','?']),
              sudoku.Square(['?','?','?','?','?','?','?','?','?']),
              sudoku.Square(['?','?','?','?','?','?','?','?','?']),
              sudoku.Square(['?','?','?','?','?','?','?','?','?']),
              sudoku.Square(['?','?','?','?','?','?','?','?','?']),
              sudoku.Square(['?','?','?','?','?','?','?','?','?']),
              sudoku.Square(['?','?','?','?','?','?','?','?','?'])])
         self.assertTrue(validPuzzleWithUnknowns.isValid())

         invalidPuzzle = sudoku.Puzzle(
             [sudoku.Square([4,4,5,6,8,2,1,9,7]), # Two 4's in one square!
              sudoku.Square([2,6,9,5,7,1,8,3,4]),
              sudoku.Square([7,8,1,4,9,3,5,6,2]),
              sudoku.Square([8,2,6,3,7,4,9,5,1]),
              sudoku.Square([1,9,5,6,8,2,7,4,3]),
              sudoku.Square([3,4,7,9,1,5,6,2,8]),
              sudoku.Square([5,1,9,2,4,8,7,6,3]),
              sudoku.Square([3,2,6,9,5,7,4,1,8]),
              sudoku.Square([8,7,4,1,3,6,2,5,9])])
         self.assertFalse(invalidPuzzle.isValid())

    def test_Puzzle_isSolved(self):

        solvedPuzzle = sudoku.Puzzle(
             [sudoku.Square([4,3,5,6,8,2,1,9,7]),
              sudoku.Square([2,6,9,5,7,1,8,3,4]),
              sudoku.Square([7,8,1,4,9,3,5,6,2]),
              sudoku.Square([8,2,6,3,7,4,9,5,1]),
              sudoku.Square([1,9,5,6,8,2,7,4,3]),
              sudoku.Square([3,4,7,9,1,5,6,2,8]),
              sudoku.Square([5,1,9,2,4,8,7,6,3]),
              sudoku.Square([3,2,6,9,5,7,4,1,8]),
              sudoku.Square([8,7,4,1,3,6,2,5,9])])
        self.assertTrue(solvedPuzzle.isSolved())

        badSolutionPuzzle = sudoku.Puzzle(
             [sudoku.Square([7,3,5,6,8,2,1,9,4]),
              sudoku.Square([2,6,9,5,7,1,8,3,4]),
              sudoku.Square([7,8,1,4,9,3,5,6,2]),
              sudoku.Square([8,2,6,3,7,4,9,5,1]),
              sudoku.Square([1,9,5,6,8,2,7,4,3]),
              sudoku.Square([3,4,7,9,1,5,6,2,8]),
              sudoku.Square([5,1,9,2,4,8,7,6,3]),
              sudoku.Square([3,2,6,9,5,7,4,1,8]),
              sudoku.Square([8,7,4,1,3,6,2,5,9])])
        self.assertFalse(badSolutionPuzzle.isSolved())

        hasUnknownsPuzzle = sudoku.Puzzle(
             [sudoku.Square(['?',3,5,6,8,2,1,9,'?']),
              sudoku.Square([2,6,9,5,7,1,8,3,4]),
              sudoku.Square([7,8,1,4,9,3,5,6,2]),
              sudoku.Square([8,2,6,3,7,4,9,5,1]),
              sudoku.Square([1,9,5,6,8,2,7,4,3]),
              sudoku.Square([3,4,7,9,1,5,6,2,8]),
              sudoku.Square([5,1,9,2,4,8,7,6,3]),
              sudoku.Square([3,2,6,9,5,7,4,1,8]),
              sudoku.Square([8,7,4,1,3,6,2,5,9])])
        self.assertFalse(hasUnknownsPuzzle.isSolved())

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
