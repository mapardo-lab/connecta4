def find_n(list_elements, needle, n):
    """
    Devuelve True si encuentra el n o más número de veces needle en list_elements
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
    Devuelve True si encontra uno o más nencias de needle en list_elements
    """
    return find_n(list_elements, needle, 1)


def find_strike(list_elements, needle, n):
    """
    Devuelve True si encuentra el n o más número de veces needle seguidos en list_elements
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


def find_one_old(list_elements, needle):
    """
    Devuelve True si encontra uno o más nencias de needle en list_elements
    """
    i = 0
    while i < len(list_elements):
        if needle == list_elements[i]:
            return True
        i += 1
    return False
