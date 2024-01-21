class FractalNumber:
    def __init__(self, real, imag=None):
        self.real = real
        self.imag = imag if imag is not None else FractalNumber(0)

    def bind(self, transform):
        new_real = transform(self.real)
        new_imag = self.imag.bind(transform)
        return FractalNumber(new_real, new_imag)

    def square(self):
        return self.bind(lambda x: x**2).add(self.multiply(self))

    def add(self, other):
        new_real = self.real + other.real
        new_imag = self.imag.bind(lambda x: x + other.imag.real)
        return FractalNumber(new_real, new_imag)

    def multiply(self, other):
        new_real = self.real * other.real - self.imag.real * other.imag.real
        new_imag = self.real * other.imag.real + self.imag.real * other.real
        return FractalNumber(new_real, FractalNumber(new_imag))

    def modulus(self):
        return (self.real**2 + self.imag.bind(lambda x: x**2).real)**0.5


def mandelbrot(c, max_iter=100):
    z = FractalNumber(0)
    for n in range(max_iter):
        if z.modulus() > 2:
            return n
        z = z.square().add(c)
    return max_iter


# Example: Calculating a point in the Mandelbrot set
c = FractalNumber(-0.75, FractalNumber(0.11))
result = mandelbrot(c)
print("Mandelbrot set result:", result)
