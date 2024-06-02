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


# For 7. Colour Trio
def mix(colour_1, colour_2, trio=['r', 'b', 'y']):
    if colour_1 == colour_2:
        return colour_1
    else:
        return list(filter(lambda x: (x != colour_1 and x != colour_2), trio))[0]


def colour_trio(colours):
    c = colours

    while len(c) > 1:
        result = ""
        for index, colour in enumerate(list(c)[:-1]):
            result += mix(colour, c[index + 1])
        c = result

    return c


def extract_increasing(digits):
    current = 0
    previous = -1
    result = []

    for d in digits:
        current = 10 * current + int(d)
        # print(current)

        if current > previous:
            previous = current
            result.append(previous)
            current = 0
            # print(":)")
    return result


def is_subsequence(letters, word):
    letter_index = 0

    for c in word:
        if c == letters[letter_index]:
            letter_index += 1
            if letter_index == len(letters):
                return True

    return letter_index == len(letters)


def words_with_letters(words, letters):
    return list(filter(lambda word: is_subsequence(letters, word), words))


def taxi_zum_zum(moves):
    t = 0
    pos = [0, 0]

    for move in moves:
        if move == "R":
            t += 90
        elif move == "L":
            t -= 90

        if t >= 360:
            t -= 360
        elif t < 0:
            t += 360

        if move == "F":
            if t == 0:
                pos[1] += 1
            elif t == 90:
                pos[0] += 1
            elif t == 180:
                pos[1] -= 1
            elif t == 270:
                pos[0] -= 1

    return tuple(pos)
