''' 
multilinha 
comentario
aqui
'''
a = 10 
b = 2
val1 = 123456
val2 = "sopa de ....."
val3 = 123.123

print("\n")

# operadores logicos
print(a == b) # vc ja sabe oq eh
print(a != b) # vc ja sabe oq eh
print(a < b)  # vc ja sabe oq eh
print(a >= b) # vc ja sabe oq eh
print(a <= b) # vc ja sabe oq eh

print("\n")

# maths
print(a**b)           # pot 
print(a**(a + b))     # pot e parentss
print(a**(a + b) % 7) #pot e mod

print("\n")

#alguns tipos
print(type(val1)) # diz tipo da var
print(type(val2)) # diz tipo da var
print(type(val3)) # diz tipo da var
print(type(a))    # diz tipo da var
print(type(b))    # diz tipo da var

print("\n")

#strings
palavra = 'tecnologicamente_avancada' # strigs sao objetos em python
print(palavra[0]) # podem ser acessadas as letras desta forma
print(palavra[1]) # de veras
print(palavra[2]) # muito
print(palavra[3]) # tecnologicamente 
print(palavra[4]) # avancada
print(2 * palavra[5])  # 2x oq esta na pos 5
print(palavra[5:10])   # aquilo que estra entre a pos 5 e 10
print(palavra[:10])    # aquilo que vem antes da pos 10
print(palavra[10:])    # aquilo que ve dps da pos 10
print(palavra[1:10:2]) # entre pos 1 e 10 com increento de 2 
print(palavra[15::-1]) # da pos 15 pra baixo, ao contrario

print("\n")

#listas
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = [2, 4, 6, 8, 10, 12, 14, 16, 18]
print(type(lista1))
print(lista1[0] + lista2[1]) # soma, para elementos dentro das listas
print(lista1[4] + lista2[5]) # soma, para elementos dentro das listas
lista1 = lista1 + [0, 1, 2, 3] # juntar listas
print(lista1 + lista2)
print(lista1 + [123456]) #  junta
print(lista1)
print(lista1[-1]) # ultimo endereco
print(lista1[-2]) # penultimo endereco, etc...
print(lista1[3:-1]) # do index 3 ate o ultimo
print(len(lista1)) # tamanho da lista
lista2[0] = "dois" # re-atribuindo, (nao da com string)
print(lista2)
lista1 = lista1[0] + lista1[2] # devolve a soma
print(lista1)
lista2[1] = lista2[5] # tbm nao da com strings
print(lista2)

print("\n")

# listas de listas (matrizes)
linha1 = [0, 1, 2]
linha2 = [3, 4, 5]
linha3 = [7, 8, 9]
matriz = [linha1, linha2, linha3, [10, 11, 12 ,13]] # atrib de listas para ela
print(matriz)
print(matriz[0]) # printar na pos
print(matriz[1])
print(matriz[2])
#print(matriz[3])
print(matriz[0][2]) # printar na pos mais especifico
print(matriz[1][1]) # "chamar um elemento da pseudo matriz"
print(matriz[2][0])

print("\n")

# tuplas, NAO PODEM SER MUDADAS!!!
tuple = (0, 1, 2, 3)
print(tuple)
print(tuple[0])
print(tuple[1])
#tuple[0] = 2 | ISSO NAO PODE!!!
a1, b1 = 123, 'Teste' # packig-unpacking
print(a1) # eh como se as vars fossem iguais a
print(b1) # 123 e 'Teste' respectivamente
a1, b1 = b1, a1 # pode se trocar o calor de dois obj facilmente
print(a1)
print(b1)

print("\n")

# dicionarios
# se chama pelas chaves nao pelos enderecos
