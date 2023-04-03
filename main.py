idade=int(input("digite sua idade:"))
if idade < 0 :
 print("impossivel!")
elif idade < 18:
 print("não precisa se alistar.")
elif 65> idade >18:
 print("não esqueça de votar na proxima eleição.")
elif idade > 65:
 print("vá descançar.")
else:
 print("eita!")
