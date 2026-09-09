from cmath import sqrt

def run(a: int, b: int, c: int) -> tuple:
    # TODO

    discriminant = b**2 - (4 * a * c)

    # Use cmath.sqrt to handle both real and complex roots cleanly
    x1 = (-b + sqrt(discriminant)) / (2 * a)
    x2 = (-b - sqrt(discriminant)) / (2 * a)

    # Convert complex results with 0 imaginary part to plain real numbers/floats
    if isinstance(x1, complex) and x1.imag == 0:
        x1 = x1.real
    if isinstance(x2, complex) and x2.imag == 0:
        x2 = x2.real

    return x1, x2


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
