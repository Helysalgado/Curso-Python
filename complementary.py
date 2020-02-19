#Se crea un programa que lee el archivo sequence, lo guarda en la var. Seq.
#Se obtiene la cadena complementaria a Seq.
Seq = open ("sequence.txt")

# Si la secuencia viene en minusculas tu programa no funciona
# aqui te faltaria agregar una instrucción

Seq = Seq.replace('A','t')
Seq = Seq.replace('T','a')
Seq = Seq.replace('G','c')
Seq = Seq.replace('C','g')

Seq = Seq.upper()

## el programa pide el reverso también. No lo calculas

print('La cadena complementaria es:')
print(Seq)
