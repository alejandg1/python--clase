peso = float(input("Por favor ingrese su peso en kilogramos  "))
estatura = float(input("Ahora escriba su estatura en metros  "))

imc = round(peso/(estatura**2), 2)



""" if (imc < 18.5):
    clasificacion = "bajo peso"
if ((imc > 18.5) & (imc < 24.9)):
    clasificacion = "peso normal"
if ((imc > 24.9) & (imc < 29.9)):
    clasificacion = "sobrepeso"
if ((imc > 29.9) & (imc < 34.9)):
    clasificacion = "obesidad I"
if ((imc > 34.9) & (imc < 39.9)):
    clasificacion = "obesidad II"
if (imc >= 40):
    clasificacion = "obesidad III" 
    
   
print(f" Tu indice de masa corporal es: {imc} y la clasificación de tu peso es: {clasificacion} ") """
print(f" Tu indice de masa corporal es: {imc} ")