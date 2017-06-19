def isValid_TC_ID(value):
    value = str(value)
    if (len(value) == 11 and value.isdigit() and not int(value[0]) == 0):
        digits = [int(d) for d in str(value)]
        if (sum(digits[:10]) % 10 == digits[10]):
            if (((((7 * sum(digits[:9][-1::-2])) + (9 * sum(digits[:9][-2::-2]))) % 10) == digits[9]) and (
                        ((8 * sum(digits[:9][-1::-2])) % 10) == digits[10])):
                return True

    return False


def main():
    print(isValid_TC_ID(11122233344))


if __name__ == '__main__':
    main()
