# Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.
raio = float(input("digite o raio do circulo"))
nmrpi = 3.14

def calcular_area_base(raio):
    calculo = (raio * raio) * nmrpi
    area = calculo

    return(area)


areadc = calcular_area_base(raio)

altura = float(input("digite a altura do cilindro: "))

def calcular_volume_cilindro(areadc):
    calculo = nmrpi * (raio * raio) * altura
    return(calculo)

volumeCilindro = calcular_volume_cilindro(areadc)
print(f"A area do circulo é: {areadc}")
print(f"Ovolume do cilindro é: {volumeCilindro}")