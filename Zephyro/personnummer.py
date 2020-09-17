
def stripCentury(number):
    """Strips the number of the century

    Sometimes, personnummer is written including century.
    This is not included in the algorithm for calculating the
    final digit, and thus is removed by this function."""
    length = len(number)
    # print(f'stripCentury: length: {length}')
    if not number.isdigit():
        print('Error: input is not a number.')
        return None, False
    if length == 9:
        return number, False
    elif length == 10:
        return number, True
    elif length == 11:
        return number[2:], False
    elif length == 12:
        return number[2:], True
    else:
        print('invalid format')
        return None, False


def fixFormat(number):
    """Format the number in a predictable way.

    Fixes the problem with different ways of formatting the number.
    The resulting format is always yymmddnnn or yymmddnnnn depending on the
    input."""

    number = number.replace("-", "")
    number, full = stripCentury(number)
    # print(f'fixFormat: returning number: {number}')
    return number, full


def doubleAndSum(number):
    """Doubles a number and adds the digits in it

    Takes an integer and doubles it, and then adds the numbers together."""

    # print(f'    doubleAndSum: incoming number: {number}')
    number *= 2
    # print(f'    doubleAndSum: doubled number: {number}')
    if number >= 10:
        number = number // 10 + number % 10
    # print(f'    doubleAndSum: returning number: {number}')
    return number


def calculateControlDigit(number):
    """Calculate the control digit for a personnummer

    The control digit is calculated by multiplying every other number by two, (Starting with the first) then adding the
    separate digits. The control digit is then the difference
    between that sum and the closest higher multiple of ten. E.g. if the sum is 44, the control digit will be 50-44=6"""

    cumulative_sum = 0

    # Enumerate makes a tuple of index and element
    for index, digit in enumerate(number):

        # Make calculations possible
        digit = int(digit)

        if index % 2 == 0:
            cumulative_sum += doubleAndSum(digit)
        else:
            cumulative_sum += digit
        # print(f'calculateControlDigit: sum: {cumulative_sum}')

    # print(f'calculateControlDigit: final sum: {cumulative_sum}')
    # This is equivalent to taking the following multiple of ten minus the number
    control = ((cumulative_sum // 10 + 1) * 10 - cumulative_sum) % 10
    # higher = int(str(cumulative_sum)[0] + '0') + 10
    # control = higher - cumulative_sum
    return control


def printControlDigitMatch(number, control):
    last = int(number) % 10
    print('')
    if last == control:
        print("Personnumrets kontrollsiffra stämmer!")
    else:
        print(f"Personnumrets kontrollsiffra stämmer INTE!\nDen ska vara {control}, men är {last}")

# This statement means that the code below will not run if imported.
# This is good when running automated tests, which we will cover later


if __name__ == "__main__":

    number = input("Skriv in ett personnummer du vill testa eller ett ofullständigt som du vill generera:\n>> ")
    number, full = fixFormat(number)
    if full:
        control = calculateControlDigit(number[:-1])
    elif not full and number:
        control = calculateControlDigit(number)
    else:
        print('invalid number')
        exit()
    # print(f'main: control digit: {control}')

    if full:
        printControlDigitMatch(number, control)
    else:
        print(f"Det fullständiga personnumret är: {number}{control}")
