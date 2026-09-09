PI = 3.14


def run(arc_A: float) -> float:
    return round((2 * arc_A / PI) ** 2, 10)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
