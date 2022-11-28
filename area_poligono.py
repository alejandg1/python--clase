
def area():
    poligono = input("escriba que tipo de poligono medirá 1: triangulo  2.cuadrado 3. reactangulo ")
    
    match poligono:
        case "1":
            base = int(input("¿cuanto mide la base del triangulo? "))
            altura = int(input("ahora indique la altra del triangulo "))
            a = (base*altura)/2
        case "2":
            lados = int(input("¿cuanto miden los lados de su cuadrado? "))
            a = lados**2

        case "3":
            largo = int(input("valor del largo de su rectangulo "))
            ancho = int(input("escriba el ancho del reactangulo "))
            a = largo*ancho

    print(f'el area de su poligono es: {a}')

area()
            


