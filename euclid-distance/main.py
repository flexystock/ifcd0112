
def run(x1: float, y1: float, x2: float, y2: float) -> float:

    distance = sqrt(((x1-x2)**2)+(y1-y2)**2)
    return distance


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
