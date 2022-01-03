valor = float(input("Qual o valor? "))

unidades_medida = ['mm', 'cm', 'dm', 'm', 'dam', 'hm', 'km']
on = True


def conversao(num):
    if unidade_convertida == 'mm':
        numero_f = num

    elif unidade_convertida == 'cm':
        numero_f = numero / 10

    elif unidade_convertida == 'dm':
        numero_f = numero / 100

    elif unidade_convertida == 'm':
        numero_f = numero / 1000

    elif unidade_convertida == 'dam':
        numero_f = numero / 10000

    elif unidade_convertida == 'hm':
        numero_f = numero / 100000

    elif unidade_convertida == 'km':
        numero_f = numero / 1000000

    print(
        f'O valor de {valor}{unidade} convertido em {unidade_convertida} é igual a {round(numero_f, 2)}{unidade_convertida}'
    )


while on:
    unidade = input("Qual a unidade de medida? mm/cm/dm/m/dam/hm/km ")
    unidade_convertida = input(
        "Qual a unidade para conversão? mm/cm/dm/m/dam/hm/km ")
    if unidade in unidades_medida:
        pass
        if unidade_convertida in unidades_medida:
            on = False

        else:
            print("Por favor, insira unidades de medidas existentes! ")

    else:
        print("Por favor, insira unidades de medidas existentes! ")

if unidade == 'mm':
    numero = valor

elif unidade == 'cm':
    numero = valor * 10

elif unidade == 'dm':
    numero = valor * 100

elif unidade == 'm':
    numero = valor * 1000

elif unidade == 'dam':
    numero = valor * 10000

elif unidade == 'hm':
    numero = valor * 100000

elif unidade == 'km':
    numero = valor * 1000000

conversao(numero)
