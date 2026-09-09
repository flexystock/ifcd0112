def run():
    numero1 = input ('Introduce un número: ')
    numero2 = input ('Introduce otro número: ')

    print(numero1, '+', numero2, '=', int(numero1) + int(numero2))
    print(numero1, '-', numero2, '=', int(numero1) - int(numero2))
    print(numero1, '*', numero2, '=', int(numero1) * int(numero2))
    print(numero1, '/', numero2, '=', int(numero1) / int(numero2))
   
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
