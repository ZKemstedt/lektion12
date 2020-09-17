# Uppgift
#   Skapa ett enkelt telefonboks-program enligt specifikationer.

# Specifikationer
#   1. Varje post ska innehålla namn, telefonnummer, epostadress och ålder
#   2. När användare startar programmet så ska hen skriva in ett namn. Då ska det finnas tre fall:
#       (a) Namnet finns -> Visa uppgifter
#       (b) Namnet finns inte -> Skriv in uppgifter
#       (c) Namnet lämnas tomt -> Avsluta programmet
#   3. När en användare visat eller skrivit in en post så ska ett nytt namn efterfrågas
#   4. Om en epostadress inte innehåller minst en punkt och precis ett '@' så ska ett nytt efterfrågas
#   5. Telefonnummer ska sparas som strängar som bara innehåller siffror
#   6. Ålder ska lagras som ett heltal (integer)
#   7. Programmet måste byggas enligt principen om att varje funktion endast gör en sak, eftersom det kan komma att
#      byggas ut senare
#   8. Av samma skäl som ovan så ska all hantering av exceptions ligga i huvud- funktionen

# Utförande
#   1. Börja med att skriva huvudloopen, men skriv det med funktionsnamn som inte finns.
#   2. Gå ett steg nedåt i taget genom att implementera(skriva) funktionerna som behövs
#   3. Tips på datastruktur: En dict med namn som nycklar, där varje post är en dict med fältnamn som nycklar

import re


class EmailError(Exception):
    pass


class PhoneNumberError(Exception):
    pass


class Entry(object):

    def __init__(self, name: str, number: int, email: str) -> None:
        self.name = name
        self.number = number
        self.email = email

    def __str__(self) -> str:
        text = (
            f'   Name: {self.name.rjust(10)}\n'
            f'   Number: {str(self.number).rjust(10)}\n'
            f'   Email: {self.email.rjust(10)}\n')
        return text


def input_email(retries: int = 3) -> str:
    email = input('Enter email\n>>> ')
    # match = re.match(r'[^@]+@[^@]+.[^@]+', email)
    match = re.match(r'.+[@].+[.].+', email)
    print(match)
    if not match:
        if not retries:
            raise EmailError('Invalid email adress! must contain exactly one `@` and at least one `.`')
        return input_email(retries=retries - 1)
    return email


def input_number(retries: int = 3) -> int:
    try:
        number = int(input('Enter phone number:\n>>> ').replace(' ', '').replace('-', ''))
    except ValueError:
        if not retries:
            raise PhoneNumberError('Invalid phone number! must be digits')
        return input_number(retries=retries - 1)
    return number


def main():
    book = {}
    while True:
        try:
            name = input('Enter contact name\n>>> ')
        except Exception as e:
            print(e)
        if not name:
            break
        if name in book:
            print(book[name])
        else:
            try:
                number = input_number()
                email = input_email()
            except Exception as e:
                print(e)
            else:
                book[name] = Entry(name, number, email)


if __name__ == "__main__":
    main()
