Combustível = input("Insira o tipo de combustível(A para Alcool) ou  (G para Gasolina):")


quantidade = float(input("Insira a quantidade em litros de combustível: "))

if  Combustível == "A":
    if quantidade <= 20:
        total = float((quantidade * 1.9) * 0.03) + float(quantidade * 1.9)
    elif quantidade > 20:
        total = float((quantidade * 1.9) * 0.05) + float(quantidade * 1.9)
    else:
        print("Valor inválido")
elif Combustível == "G":
    if quantidade <= 20:
        total = float((quantidade * 2.5) * 0.04) + float(quantidade * 2.5)
    elif quantidade > 20:
        total = float((quantidade * 2.5) * 0.06) + float(quantidade * 2.5)
    else:
        print("Valor inválido") 


print("Combustível: ",Combustível, "\n" "Litros abastecidos: ", quantidade,"\n" "Valor total: ", total)