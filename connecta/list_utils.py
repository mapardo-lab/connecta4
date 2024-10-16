def find_n(list_elements, needle, n):
    """
    Devuelve True si encuentra el n o más número de veces
    needle en list_elements
    """
    if n <= 0:
        return False
    count = 0
    i = 0
    while count < n and i < len(list_elements):
        if needle == list_elements[i]:
            count += 1
        i += 1
    return count >= n


def find_one(list_elements, needle):
    """
    Devuelve True si encontra uno o más veces
    needle en list_elements
    """
    return find_n(list_elements, needle, 1)


def find_strike(list_elements, needle, n):
    """
    Devuelve True si encuentra el n o más número de veces
    needle seguidos en list_elements
    """
    if n <= 0:
        return False
    count = 0
    i = 0
    while count < n and i < len(list_elements):
        if needle == list_elements[i]:
            count += 1
        else:
            count = 0
        i += 1
    return count >= n


def nth_elements(list_of_lists, position):
    """
    Devuelve los enesimos elementos de una lista de listas
    """
    list_position = []
    for i in range(len(list_of_lists)):
        list_position.append(list_of_lists[i][position])
    return list_position


def first_elements(list_of_lists):
    """
    Devuelve los primeros elementos de una lista de listas
    """
    return nth_elements(list_of_lists, 0)


def transpose(list_of_lists):
    """
    Transpone una listas de listas
    """
    list_transpose = []
    for i in range(len(list_of_lists[0])):
        list_transpose.append(nth_elements(list_of_lists, i))
    return list_transpose


def move_down(list_of_elements, n):
    """
    Mueve los elemenos de list_of_elements n posiciones
    desde la más alta a la más baja
    """
    list_new = list_of_elements.copy()
    for i in range(n):
        list_new.append(list_new.pop(0))
    return list_new


def move_down_one(list_of_elements):
    """
    Mueve los elemenos de list_of_elements una posición
    desde la más alta a la más baja
    """
    return move_down(list_of_elements, 1)


def move_down_list_of_lists(list_of_lists):
    """
    Mueve las listas de una lista el número de veces la posición de la lista
    La primera lista no se mueve, la segunda se mueve uno, la tercera dos y
    así sucesivamente
    """
    return list(map(lambda x, y: move_down(x, y), list_of_lists, range(len(list_of_lists))))


def reverse_list_of_lists(list_of_lists):
    """
    Cada lista de la lista de listas es invertida
    """
    return list(map(lambda x: list(reversed(x)), list_of_lists))


def find_one_old(list_elements, needle):
    """
    Devuelve True si encontra uno o más veces
    needle en list_elements
    """
    i = 0
    while i < len(list_elements):
        if needle == list_elements[i]:
            return True
        i += 1
    return False


def all_same(list_elements):
    """
    Devuelve True si todos los elementos de la lista son iguales
    o si la lista está vacia
    """
    if list_elements == []:
        return True
    else:
        first = list_elements[0]
        for i in list_elements:
            if first != i:
                return False
        return True
