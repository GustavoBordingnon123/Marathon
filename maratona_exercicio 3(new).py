numero = int(input("digite um número: "))
contador = 2
verificador_float = 0
deu_certo = 0
fatores_primos = 0

while  numero > 1000000:
    numero = int(input("digite um número menor por favor: "))

primeiro_numero = numero


while numero !=1:
    numero = numero/contador
    numero_debugger = int(numero+1)
    numero_final = numero_debugger - numero
    if numero_final < 1:
            numero = primeiro_numero
            contador = contador + 1
            deu_certo = 0
    elif numero_final == 1:
        deu_certo = deu_certo+1
        if deu_certo < 2:
            fatores_primos = fatores_primos + 1

    primeiro_numero = numero

    
print("o resultado final foi:",numero)
print("fatores primos foram igual a:", fatores_primos)