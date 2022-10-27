def keysandvalues(Objeto):
    llaves = []
    valores = []
    marca = 0

    for nuevo in Objeto:
        if(len(llaves) == 0):
            llaves.append(nuevo)
            valores.append(Objeto[nuevo])
        else:
            for llave in range(len(llaves)):
                if(llaves[llave] > nuevo):
                    llaves.insert(llave,nuevo)
                    valores.insert(llave,Objeto[nuevo])
                    marca = 0
                else:
                    marca=1
                
        if(marca == 1):
            llaves.append(nuevo)
            valores.append(Objeto[nuevo])

    print(llaves)
    print(valores)

agenda = {
    "c" : 2222,
    "a" : 111,
    "b" : 33,
    "d" : 44
}

keysandvalues(agenda)
