#Se crea un programa que lee el archivo sequence, lo guarda en la var. Seq.
#Se obtiene la cadena complementaria a Seq. y se le aplica la reversa
Seq = open ("sequence.txt")

Seq = Seq.replace('A','t')
Seq = Seq.replace('T','a')
Seq = Seq.replace('G','c')
Seq = Seq.replace('C','g')

Seq = Seq.upper()
Seq = Seq[::-1] 

print('La cadena reversa complementaria es:')
print(Seq)
