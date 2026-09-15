def run(values: list) -> int:

   minimo = [0]

    for n in values:
    if n > minimo:
           minimo = int(n)
    

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
