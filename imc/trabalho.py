x = float(input("digite uma altura: "))
y = float(input("digite um peso: "))

calculadora_de_imc = y/(x*x)
print( "o imc é: ",calculadora_de_imc)

if calculadora_de_imc < 18.5:
    print("abaixo do peso")
elif calculadora_de_imc > 18.5 and calculadora_de_imc < 24.9:
    print("peso normal")
elif calculadora_de_imc > 25.0 and calculadora_de_imc < 29.9:
    print("sobre peso")
elif calculadora_de_imc > 30.0 and calculadora_de_imc < 34.9:
    w = calculadora_de_imc * 0.2
    print("obesidade grau 1 , você precisa perder:",w)
elif calculadora_de_imc > 35.0 and calculadora_de_imc < 39.9:
     p = calculadora_de_imc * 0.3
    print("obesidade grau 2 (severa)")
else:
    print("obesidade grau 3 (mórbida)"


