# 1.Se abre el archivo sequence.txt
file=open("sequence.txt")
# 2.Se crea una lista para guardar las secuencias sin adaptadores
seq_no_adapt= []
# 3. se itera sobre el mismo para eliminar los saltos de linea
for lines in file:
  lines=lines.strip()
# 4 se guardan las secuencias sin adaptadores(*para que concordaran los outputs los adaptadores son de 10 bp, no 14)
  seq_no_adapt.append(lines[9:])
# 5. se imprimen en pantalla la longitud de cada secuencia
  print(len(lines[9:]))

# 6. Se crea un nuevo archivo de texto y se escribe en él
with open("new_file.txt", "w") as newfile:
  for lines in seq_no_adapt:
   newfile.write('{}\n'.format(lines))

