lista = []
while True:
   luku = input("anna luku:")
   print(luku)
   if luku == "":
      print(min(lista),max(lista))
      break
   else:
      lista.append(int(luku))
      