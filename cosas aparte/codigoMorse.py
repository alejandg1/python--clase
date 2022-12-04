#  * Crea un programa que sea capaz de transformar texto natural a código
#   morse y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar
#   la conversión.
# - En morse se soporta raya "-", punto ".", un espacio " " entre letras
#   o símbolos y dos espacios entre palabras "  ".
# - El alfabeto morse soportado será el mostrado en
#   https://es.wikipedia.org/wiki/Código_morse.


MORSE = {' ': ' ', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', }

def morse():
    mensaje = input("escriba un mensaje en morse o lenguaje natural..  ")
    mensaje = mensaje.upper()
    print(f"{mensaje}")
    if mensaje.__contains__(".") or mensaje.__contains__("-"):
        for i in mensaje:
            pass
    elif mensaje.__contains__("[a-zA-Z0-9]"):
        pass


if __name__== "__main__":
    morse()