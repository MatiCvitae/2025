def tuplas():
    tuplas=(1,2,3,4,5,6,7,8,9)
    conteo= tuplas.count (1)
    return dict(conteo=conteo, tuplas=tuplas)

def listas():
    frutas1 = ["manzana", "banana"]
    frutas1.append("naranja")
    print(frutas1)
    metodo1 = "append: Agrega un elemento al final de la lista"
    
    frutas2 = ["manzana", "banana"]
    frutas2.extend(["naranja", "kiwi"])
    print(frutas2)
    metodo2 = "extend: Agrega los elementos de otra lista (o iterable) al final"
    
    frutas3 = ["manzana", "banana"]
    frutas3.insert(1, "naranja")
    print(frutas3)
    metodo3 = "insert: Inserta un elemento en una posición específica"
    
    frutas4 = ["manzana", "banana", "naranja"]
    frutas4.remove("banana")
    print(frutas4)
    metodo4 = "remove: Elimina la primera ocurrencia del valor especificado"
    
    frutas5 = ["manzana", "banana", "naranja"]
    fruta = frutas5.pop(1)
    print(fruta)
    print(frutas5)
    metodo5 = "pop: Elimina y devuelve el elemento en la posición indicada"
    
    frutas6 = ["manzana", "banana", "naranja"]
    indice = frutas6.index("banana")
    print(indice)
    metodo6 = "index: Devuelve la posición de la primera ocurrencia del valor"
    
    frutas7 = ["manzana", "banana", "banana", "naranja"]
    cantidad = frutas7.count("banana")
    print(cantidad)
    metodo7 = "count: Cuenta cuántas veces aparece un valor en la lista"
    
    frutas8 = ["naranja", "banana", "manzana"]
    frutas8.sort()
    print(frutas8)
    metodo8 = "sort: Ordena los elementos de la lista alfabéticamente o numéricamente"
    
    frutas9 = ["manzana", "banana", "naranja"]
    frutas9.reverse()
    print(frutas9)
    metodo9 = "reverse: Invierte el orden de los elementos de la lista"
    
    return dict(frutas1=frutas1, metodo1=metodo1,
                frutas2=frutas2, metodo2=metodo2,
                frutas3=frutas3, metodo3=metodo3,
                frutas4=frutas4, metodo4=metodo4,
                frutas5=frutas5, metodo5=metodo5, fruta_extraida=fruta,
                frutas6=frutas6, metodo6=metodo6, indice=indice,
                frutas7=frutas7, metodo7=metodo7, cantidad=cantidad,
                frutas8=frutas8, metodo8=metodo8,
                frutas9=frutas9, metodo9=metodo9)