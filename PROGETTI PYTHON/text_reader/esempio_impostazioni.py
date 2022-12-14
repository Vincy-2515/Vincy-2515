
print("SALVE")
print("scrivi scrivere per aggiungere al file")
U_input = input()

file=open("esempiol.txt","a")
file.write(U_input + "\n")
file.close()


var_lettura = open("esempiol.txt","r").readlines()
print(var_lettura)
