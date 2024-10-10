class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            real_part = self.real + other.real
            imaginary_part = self.imaginary + other.imaginary
            return ComplexNumber(real_part, imaginary_part)
        return NotImplemented

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

# Example usage:
num1 = ComplexNumber(2, 3)  # 2 + 3i
num2 = ComplexNumber(4, 5)  # 4 + 5i

result = num1 + num2
print("Sum:", result)  # Output: Sum: 6 + 8i

