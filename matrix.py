import math
from math import sqrt
import numbers

def zeroes(height, width):
    """
    Creates a matrix of zeroes.
    """
    z = [[0.0 for _ in range(width)] for __ in range(height)]
    return Matrix(z)

def identity(n):
    """
    Creates a n x n identity matrix.
    """
    I = zeroes(n, n)
    for i in range(n):
        I.z[i][i] = 1.0
    return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################

    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices larger than 2x2.")

        # TODO - your code here
        elif self.h == 2:
            return (1/(self[0][0]*self[1][1]-self[0][1]*self[1][0]))

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        if self.h > 2:
            raise(NotImplementedError, "Calculating trace not implemented for matrices larger than 2x2.")
        elif self.h == 2:
            return (self[0][0]+self[1][1])

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        elif self.h == 2 and determinant(self) == 0:
            raise NotImplementedError('This matrix does not have an inverse')
        else:
            if self.h==1:
                inverse = [[1/self[0][0]]]
            else:
                for i in range(self.h):
                    for j in range(self.w):
                        self[i][j] = (self[i][j])*determinant(self)

                inverse = [[self[1][1], -self[0][1]], [-self[1][0], self[0][0]]]

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []

        for j in range(len(matrix[0])):     # Start column loop as the outer loop
            col = []
            for i in range(len(matrix)):    # Row loop as the inner loop
                col.append(matrix[i][j])    # Column remians constant while row counter is incremented. Create column list
            matrix_transpose.append(col)    # Append each column as a list to build the transposed matrix

        return matrix_transpose

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same")
            #return None
        #   
        # TODO - your code here
        #
        else:
            result = []
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    row.append(self[i][j] + other[i][j])
                result.append(row)
            return result


    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        result = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(-self[i][j])
            result.append(row)
        return result

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same")
            #return None
        #   
        # TODO - your code here
        #
        else:
            result = []
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    row.append(self[i][j] - other[i][j])
                result.append(row)
            return result

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """

        if(self.w == other.h):
            # Then the dimensions match for multiplication!

            # Create a new matrix of zeroes of the appropriate size (self.rows x other.cols)
            self_times_other = zeroes(self.h, other.w)

            # iterate through the rows of self
            for i in range(self.h):

                # iterate through the columns of other
                for j in range(other.w):

                    # iterate through rows of other and sum
                    for k in range(other.h):
                        # multiply and sum step
                        self_times_other[i][j] += (self[i][k] * other[k][j])

                        # for debugging
                        #print(' i = ' + str(i) +', j = ' + str(j) + ', k = ' + str(k))
            return self_times_other
        else:
            print('Invalid matrix dimensions!')
            print('A_cols = ' + str(self.w) + ', and B_rows = ' + str(other.h))

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            for i in range(self.h):
                for j in range(self.w):
                    self[i][j] = (self[i][j])*other
            return self