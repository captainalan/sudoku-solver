class Square:
    """Squares are comprised of nine tiles, each which contains a unique 
    integer between 1 and 9.
    
    Tiles are stored in an array. Here is a graphic representation:
    [
      [0], [1], [2],
      [3], [4], [5], 
      [6], [7], [8], 
    ]
    """

    def __init__(self, tiles):
        """Tiles should be a list of ints.
        Unknown values can be denoted with a string '?' 
        """
        self.tiles = tiles

        # Convenient names for rows/columns
        self.row1 = [self.tiles[0], self.tiles[1], self.tiles[2]]
        self.row2 = [self.tiles[3], self.tiles[4], self.tiles[5]]
        self.row3 = [self.tiles[6], self.tiles[7], self.tiles[8]]

        self.col1 = [self.tiles[0], self.tiles[3], self.tiles[6]]
        self.col2 = [self.tiles[1], self.tiles[4], self.tiles[7]]
        self.col3 = [self.tiles[2], self.tiles[5], self.tiles[8]]

        # Convenient names for rows/columns together
        self.rows = [self.row1, self.row2, self.row3]
        self.cols = [self.col1, self.col2, self.col3]

    def __eq__(self, other):
        return self.tiles == other.tiles 

    def isValid(self):
        """A valid Square violates no constraints."""

        unknown_count = 0
        for t in self.tiles:
            if t in range(1,10):
                continue
            elif t == '?':
                unknown_count = unknown_count + 1
            else:
                return False # Return false if bad values found

        if len(set([x for x in self.tiles if type(x) == int]))\
           + unknown_count == 9:
            return True
        else:
            return False

    def isSolved(self):
        """A solved Square is valid and contains no unknown values."""
        if self.isValid() and not '?' in self.tiles:
            return True
        else:
            return False

class Puzzle:
    """A puzzle is made of nine squares.
    Squares are stored in an array. Here is a graphic representation:
    [
      [0], [1], [2],
      [3], [4], [5], 
      [6], [7], [8], 
    ]

    Squares themselves have tiles arranged in an analogous way.
    """

    def __init__(self, tiles, isListOfInts=False):
        """By default, tiles is expected to be a list of Squares. If isListOfInts is
        True, expect a list of ints given row by row (as ppl read)."""

        if isListOfInts:
            self.squares = [Square([tiles[0],  tiles[1],  tiles[2],
                                    tiles[9],  tiles[10], tiles[11],
                                    tiles[18], tiles[19], tiles[20]]),
                            Square([tiles[3],  tiles[4],  tiles[5],
                                    tiles[12], tiles[13], tiles[14],
                                    tiles[21], tiles[22], tiles[23]]),
                            Square([tiles[6],  tiles[7],  tiles[8],
                                    tiles[15], tiles[16], tiles[17],
                                    tiles[24], tiles[25], tiles[26]]),
                            Square([tiles[27], tiles[28], tiles[29],
                                    tiles[36], tiles[37], tiles[38],
                                    tiles[45], tiles[46], tiles[47]]),
                            Square([tiles[30], tiles[31], tiles[32],
                                    tiles[39], tiles[40], tiles[41],
                                    tiles[48], tiles[49], tiles[50]]),
                            Square([tiles[33], tiles[34], tiles[35],
                                    tiles[42], tiles[43], tiles[44],
                                    tiles[51], tiles[52], tiles[53]]),
                            Square([tiles[54], tiles[55], tiles[56],
                                    tiles[63], tiles[64], tiles[65],
                                    tiles[72], tiles[73], tiles[74]]),
                            Square([tiles[57], tiles[58], tiles[59],
                                    tiles[66], tiles[67], tiles[68],
                                    tiles[75], tiles[76], tiles[77]]),
                            Square([tiles[60], tiles[61], tiles[62],
                                    tiles[69], tiles[70], tiles[71],
                                    tiles[78], tiles[79], tiles[80]])]
        else:
            self.squares = tiles 
        # Handle bad input

        # Convenient names for rows/columns
        self.row1 = self.squares[0].row1 + self.squares[1].row1 + self.squares[2].row1
        self.row2 = self.squares[0].row2 + self.squares[1].row2 + self.squares[2].row2
        self.row3 = self.squares[0].row3 + self.squares[1].row3 + self.squares[2].row3
        self.row4 = self.squares[3].row1 + self.squares[4].row1 + self.squares[5].row1
        self.row5 = self.squares[3].row2 + self.squares[4].row2 + self.squares[5].row2
        self.row6 = self.squares[3].row3 + self.squares[4].row3 + self.squares[5].row3
        self.row7 = self.squares[6].row1 + self.squares[7].row1 + self.squares[8].row1
        self.row8 = self.squares[6].row2 + self.squares[7].row2 + self.squares[8].row2
        self.row9 = self.squares[6].row3 + self.squares[7].row3 + self.squares[8].row3

        self.col1 = self.squares[0].col1 + self.squares[3].col1 + self.squares[6].col1
        self.col2 = self.squares[0].col2 + self.squares[3].col2 + self.squares[6].col2
        self.col3 = self.squares[0].col3 + self.squares[3].col3 + self.squares[6].col3
        self.col4 = self.squares[1].col1 + self.squares[4].col1 + self.squares[7].col1
        self.col5 = self.squares[1].col2 + self.squares[4].col2 + self.squares[7].col2
        self.col6 = self.squares[1].col3 + self.squares[4].col3 + self.squares[7].col3
        self.col7 = self.squares[2].col1 + self.squares[5].col1 + self.squares[8].col1
        self.col8 = self.squares[2].col2 + self.squares[5].col2 + self.squares[8].col2
        self.col9 = self.squares[2].col3 + self.squares[5].col3 + self.squares[8].col3

        # Convenient names for rows/columns together
        self.rows = [self.row1, self.row2, self.row3,
                     self.row4, self.row5, self.row6,
                     self.row7, self.row8, self.row9]
        self.cols = [self.col1, self.col2, self.col3,
                     self.col4, self.col5, self.col6,
                     self.col7, self.col8, self.col9]

    def toList(self): 
        # Doing this instead of folding so I don't have to import functools here
        return self.row1\
             + self.row2\
             + self.row3\
             + self.row4\
             + self.row5\
             + self.row6\
             + self.row7\
             + self.row8\
             + self.row9

    def __str__(self):
        args = self.row1 + self.row2 + self.row3\
             + self.row4 + self.row5 + self.row6\
             + self.row7 + self.row8 + self.row9

        # Admittedly not the prettiest way to do things...
        return """
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
---------------------
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
---------------------
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
        """.format(*args)

    def isValid(self):
        """A valid Puzzle violates no constraints.

        Hmm. I want to call the isValid() method on each Square... can this 
        be done with a map or a similar FP technique?"""

        # Check that all squares are valid
        for s in self.squares:
            if s.isValid():
                continue
            else:
                return False

        # Then check rows/columns
        # This has to take in unknowns ('?') into account.
        # Make sure all integers are unique though there can be multiple ?'s.
        for x in (self.rows + self.cols):
            if len(x) != 9:
                return False
            else:
                continue
        return True

    def isSolved(self):
        """A solved Square is valid and contains no unknown values."""
        # Make use of the methods to get rows/cols in Square
        for x in (self.rows + self.cols):
            if Square(x).isSolved():
                continue
            else:
                return False
        return True
