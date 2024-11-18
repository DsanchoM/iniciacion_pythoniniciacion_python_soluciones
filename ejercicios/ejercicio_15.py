def chop(list):
    if len(list) == 1:
        list.clear()

    if len(list) > 1:
        del list[-1]
        del list[0]

    return None


def middle(lista):
    if len(lista) > 1:
        return lista[1:-1]
    else:
        return []


userList = []
while True:
    value = input("Inserta un valor para la lista")
    if value == 'listo':
        break
    userList.append(value)

print(f"Lista creada: {userList}")
list2 = userList[:]
chop(userList)
print(f"Lista despues de usar chop: {userList}")
print(f"Lista creada con middle: {middle(list2)}")

