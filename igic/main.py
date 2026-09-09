def run(price_with_igic: float, igic: float) -> float:
    price_without_igic = price_with_igic / (1 + igic / 100)

    # Redondeamos el resultado final a 2 decimales
    return round(price_without_igic, 2)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
