X = int(input("digite um número de dois digitos (menor que 100: " ))
if x>=100:
    print("o número é maior que 100")
    else:
        dezena= x/100
        unidade= x%100
        soma = dezena + unidade 
        print(soma)
        
