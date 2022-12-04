def invertir():
    cadena2=""
    cadena = input("escriba aqui... ")
    for i in cadena:
        cadena2=i+cadena2
    print(f"cadena invertida: {cadena2}")

def run():
    invertir()

if __name__ == "__main__":
    run()