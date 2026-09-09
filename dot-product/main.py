def run(u: list, v: list) -> float | None:
    if len(u) != len(v):
        return None

    dprod = 0
    for elem1, elem2 in zip(u, v):
        print(elem1, elem2)
        #multiplicamos los elementos uno a uno
        dprod = dprod + (elem1 * elem2)
        print(dprod)
    return dprod 


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
