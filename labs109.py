# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":

def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust


def is_ascending(items):
    for index, item in enumerate(items):
        if index == 0:
            continue
        prev = items[index - 1]
        if not (item > prev):
            return False

    return True


def riffle(items, out=True):
    half_1 = items[0:len(items)//2]
    half_2 = items[len(items)//2:]

    result = []

    for i in range(len(items) // 2):
        if out:
            result += [half_1[i], half_2[i]]
        else:
            result += [half_2[i], half_1[i]]

    return result


def only_odd_digits(n):
    num = n

    while num > 0:
        last_digit = num % 10
        if last_digit % 2 == 0:
            return False
        num = num // 10
    return True


def is_cyclops(n):

    i = 1  # number of digits in the number

    while n // 10**i > 0:
        i += 1

    if i % 2 == 0:  # No numbers with even number of digits are cyclops numbers
        return False

    no_side_digits = i // 2  # number of digits on either side of middle digit

    num = n
    for i in range(no_side_digits):
        num = num // 10  # Trim digits on the right side so that middle digit is the last digit

    middle_digit = num % 10

    x = n
    while x > 0:
        last = x % 10

        if last == 0 and x != num:  # If there is any other number besides the middle number that is 0, it is not a cyclops number
            return False

        x = x // 10

    return middle_digit == 0


def domino_cycle(tiles):
    for index, tile in enumerate(tiles):
        if index == 0:
            prev = tiles[-1]
        else:
            prev = tiles[index - 1]
        if tile[0] != prev[1]:
            return False

    return True
