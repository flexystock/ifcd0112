def run(input_path: str) -> str:

    # 1. Abrimos el archivo de texto especificado en la ruta (input_path)
    # utilizando codificación "utf-8" para leer correctamente tildes y caracteres especiales.
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 2. El enunciado indica que ÚNICAMENTE se consideren como frontera de palabras
    # los siguientes símbolos: , . ; : ( )
    # Por lo tanto, reemplazamos cada uno de estos símbolos por un espacio en blanco
    # para que las palabras queden separadas correctamente.
    for symbol in [",", ".", ";", ":", "(", ")"]:
        content = content.replace(symbol, " ")

    # 3. Dividimos el texto modificado usando los espacios y saltos de línea como separación.
    # Esto genera una lista con todas las palabras limpias del documento.
    words = content.split()

    # Si la lista de palabras está vacía, devolvemos una cadena vacía para evitar errores.
    if not words:
        return ""

    # 4. Buscamos la palabra más larga cumpliendo la regla de los empates:
    # "Si hay varias palabras con la misma longitud, devuelve la última ocurrencia."
    longest_word = ""
    for word in words:
        # Usamos mayor o igual (>=) para que, si encontramos una palabra
        # con la misma longitud o mayor más adelante, esta reemplace a la anterior.
        if len(word) >= len(longest_word):
            longest_word = word

    # 5. Devolvemos la palabra más larga encontrada (la última en caso de empate).
    return longest_word


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
