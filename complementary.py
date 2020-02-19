#Se crea un programa que lee el archivo sequence, lo guarda en la var. Seq.
#Se obtiene la cadena complementaria a Seq.
Seq = open ("sequence.txt")

Seq = Seq.replace('A','t')
Seq = Seq.replace('T','a')
Seq = Seq.replace('G','c')
Seq = Seq.replace('C','g')

Seq = Seq.upper()

print('La cadena complementaria es:')
print(Seq)
