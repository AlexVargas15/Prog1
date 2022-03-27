'''Para que el lenguaje Python reconozca que estamos
creando una tupla es necesario agrega una coma al final del eletemto
como se muestra en el ejercicio ya que que si no se agrega la coma
el lenguaje interpretara que el elemento agregado es una tupla y cada caracater
es este caso cada letra ocupara una posocion empezando desde cero'''

miTupla = ("Alexander",)
print(miTupla[0])

vEdades = [2,7,58,7,42,26,10,8,56,57,97,
           19,11,53,3,99,62,78,29,9,37,
           42,56,86,28,86,95,26,49,67,21,
           815,67,10,58,512,24,92,89,67,
           53,10,9,83,1,44,10,77,98,73,57]


for i in vEdades:
    if i == 10:
        vEdades.remove(i)
print(vEdades)
