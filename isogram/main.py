def run(text: str) -> bool:

    texto_limpio = text.lower().replace("-", "")

    for caracter in texto_limpio:
        # find() busca desde la izquierda y rfind() busca desde la derecha
        if texto_limpio.find(caracter) != texto_limpio.rfind(caracter):
            return False

    return True
    


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
