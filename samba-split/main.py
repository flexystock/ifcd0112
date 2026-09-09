def run(smb_path: str) -> tuple:
    # Quitar las dos barras iniciales '//' y dividir por la primera barra '/'
    partes = smb_path.lstrip('/').split('/', 1)
    
    host = partes[0]
    path = '/' + partes[1] if len(partes) > 1 else '/'
    return host, path


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
