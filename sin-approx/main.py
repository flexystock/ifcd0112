def run(x: float) -> float:
    numerador = 4 * x * (180 - x)
    denominador = 40500 - x * (180 - x)
    sin = numerador / denominador
    return sin


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
