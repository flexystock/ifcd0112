def run(player1: str, player2: str) -> int:
    # formateamos los inputs para que sean comparables (mayusculas, minusculas,etc)
    j1 = player1.lower().strip()
    j2 = player2.lower().strip()

    if j1 == j2:
        return 0

    reglas = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }

    # explicacion: j1 = 'rock' 
    # cuando hacemos reglas[j1] nos devuelve 'scissors' y si eso es igual a j2, 
    # entonces gana el jugador 1
    
    if reglas[j1] == j2:
        return 1

    return 2


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
