import numpy as np

class Matrix:
    """
    A 2D Matrix class supporting basic operations and broadcasting.
    Internally uses NumPy for performance but encapsulates it for educational purposes.
    """
    __slots__ = ['data']  # Optimization: reduces memory usage

    def __init__(self, data):
        if isinstance(data, list):
            data = np.array(data)
        if not isinstance(data, np.ndarray):
            raise TypeError("Data must be a list or NumPy array")
        if data.ndim == 1:
            data = data.reshape(1, -1)  # Broadcast 1D to 2D row
        if data.ndim != 2:
            raise ValueError("Only 2D matrices are allowed")
        self.data = data

    def __add__(self, other):
        if isinstance(other, Matrix):
            return Matrix(self.data + other.data)
        else:
            return Matrix(self.data + other)

    def __sub__(self, other):
        if isinstance(other, Matrix):
            return Matrix(self.data - other.data)
        else:
            return Matrix(self.data - other)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return Matrix(self.data * other.data)
        else:
            return Matrix(self.data * other)

    def __matmul__(self, other):
        if isinstance(other, Matrix):
            return Matrix(self.data @ other.data)
        else:
            return Matrix(self.data @ other)

    def __pow__(self, power):
        return Matrix(self.data ** power)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"Matrix({repr(self.data)})"

    def shape(self):
        return self.data.shape



A = Matrix([[1, 2], [3, 4]])
B = Matrix([5, 6])  # This will broadcast to shape (2,2)

# Compute: result = (A + B) @ (A - B) ** 2
result = (A + B) @ ((A - B) ** 2)
print("Result:")
print(result)