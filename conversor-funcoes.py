unidades_medida = ['mm', 'cm', 'dm', 'm', 'dam', 'hm', 'km']
on = True

def manipular(num):
  if unidade == 'mm':
    num = valor

  elif unidade == 'cm':
      num = valor * 10

  elif unidade == 'dm':
      num = valor * 100

  elif unidade == 'm':
      num = valor * 1000

  elif unidade == 'dam':
      num = valor * 10000

  elif unidade == 'hm':
      num = valor * 100000

  elif unidade == 'km':
      num = valor * 1000000

  conversao(num)

def conversao(num):
    if unidade_convertida == 'mm':
        num_f = num

    elif unidade_convertida == 'cm':
        num_f = num / 10

    elif unidade_convertida == 'dm':
        num_f = num / 100

    elif unidade_convertida == 'm':
        num_f = num / 1000

    elif unidade_convertida == 'dam':
        num_f = num / 10000

    elif unidade_convertida == 'hm':
        num_f = num / 100000

    elif unidade_convertida == 'km':
        num_f = num / 1000000

    print(
        f'O valor de {valor}{unidade} convertido em {unidade_convertida} é igual a {round(num_f, 2)}{unidade_convertida}'
    )

valor = float(input("Qual o valor? "))

while on:
    unidade = input("Qual a unidade de medida? mm/cm/dm/m/dam/hm/km ")
    unidade_convertida = input(
        "Qual a unidade para conversão? ")
    if unidade in unidades_medida:
        pass
        if unidade_convertida in unidades_medida:
            on = False

        else:
            print("Por favor, insira unidades de medidas existentes! ")

    else:
        print("Por favor, insira unidades de medidas existentes! ")

manipular(valor)

