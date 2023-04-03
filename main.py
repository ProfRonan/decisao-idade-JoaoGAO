idade=int(input("Digite sua idade:"))
if idade < 0 :
 print("Impossivel")
elif idade < 18:
 print("Não precisa se alistar")
elif 65> idade >18:
 print("Não esqueça de votar na proxima eleição")
elif idade > 65:
 print("Vá descançar")
else:
 print("Eita!")