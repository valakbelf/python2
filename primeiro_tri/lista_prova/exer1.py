X = int(input("digite um número de dois digitos (menor que 100: " ))
if x>=100:
    print("o número é maior que 100")
    else:
        dezena= x/100
        unidade= x%100
        soma = dezena + unidade 
        print(soma)
        

numero1 = int(input("digite o primeiro número: "))
numero2 = int(input("digite o  segundo número: "))
numero3 = (int(input("digite o terceiro número: "))

if numero1>numero2 and numero1>numero3:
    print("o maior número é o ",numero1)
    
    elif numero2>numero1 and numero2>numero3:
        print("o maior número é o ",numero2)
    else:
        print("o maior número é o ",numero3)
        
        
nota1 = int(input("digite a nota do 1° bimestre; "))
nota2 = int(input("digite a nota do 2° bismestre: "))
nota3 = int(input("digite a nota do 3° bimestre: "))
nota4 = int(input("digite a nota do 4° bimestre: "))

media = (nota1+nota2+nota3+nota4)//4
print("sua media foi ", media)


lado1 = float(input("digite a medida do primeiro lado: "))
lado2 = float(input("digite a medida do segundo lado: "))
lado3 = float(input("digite a medida do terceiro lado: "))

if lado1==0 or lado2==0 or lado3==0:
    print("suas medidas não correspondem com um triângulo.")
else:
    if lado1==lado2 and lado1==lado3
    print("seu triângulo é do tipo equilátero.")
elif lado1!=lado2 and lado1==lado3    
