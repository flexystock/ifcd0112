def run(input_date: str, base_year: int) -> str:
    mes, dia, ano_corto = input_date.split('/')
    
    # 1. Rellenar día y mes a 2 dígitos con ceros a la izquierda
    dia = dia.zfill(2)
    mes = mes.zfill(2)
    
    # 2. Sumar el año base y asegurarnos de que tenga 4 dígitos
    ano_completo = int(ano_corto) + base_year
    ano_str = str(ano_completo).zfill(4)
    
    # 3. Formatear la fecha final: DD-MM-AAAA
    return f"{dia}-{mes}-{ano_str}"

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
