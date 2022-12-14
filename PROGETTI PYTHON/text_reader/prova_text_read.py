contenuto="Oggièuna bellissima giornata!"
filel=open("esempiol.txt","w")
filel.write(contenuto)
filel.close()

nuova_stringa="python è una bomba!"
filel=open("esempiol.txt","a")
filel.write(nuova_stringa)

filel.close()
filel=open("esempiol.txt","a")
filel.write("\nNuova_riga")
filel.close()

var_lettura=open("esempiol.txt","r").read()
print(var_lettura)

var_lettura=open("esempiol.txt","r").readlines()

#------------------------------------------------#
# strumenti per leggere e scrivere in un documento
# w = Write = Crea o sovrascrive un file
# a = Append = aggiunge a un file una parola/frase
# r = Read = legge ciò che c'è scritto
#------------------------------------------------#