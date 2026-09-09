def run(values: list) -> int:
     """Encuentra el valor mínimo de una lista sin usar min(), max() ni sort()."""
    
    # Asumimos que el primer elemento es el mínimo actual
    minimo = values[0]
    
    # Recorremos cada número de la lista para comparar
    for numero in values:
        if numero < minimo:
            minimo = numero  # Actualizamos si encontramos un número más pequeño
            
    return minimo


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
