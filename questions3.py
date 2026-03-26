import random

# Creamos diccionario/categorías
category = {
    "1. Fácil" : ["lista", "bucle"],
    "2. Medio" : ["funcion", "python", "entero", "cadena"],
    "3. Difícil": ["programa", "variable"]
    }

print("¡Bienvenido al Ahorcado!")
print()

# Mostramos categorías disponibles y dejamos elegir
print(f"Categorías disponibles: {list(category)}")
print()
pick = int(input("Elija una categoría (1,2 o 3):  "))

if pick == 1:
    word = random.choice(category["1. Fácil"])
elif pick == 2:
    word = random.choice(category["2. Medio"])
else:
    word = random.choice(category["3. Difícil"])

guessed = []
attempts = 6

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        print("Esa letra no está en la palabra.")

    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
