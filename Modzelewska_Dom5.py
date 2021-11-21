
dic_gp = {
    "G": "A",
    "D": "E",
    "R": "Y",
    "P": "O",
    "L": "U",
    "K": "I"
}

dic_pr = {
    "P": "O",
    "L": "I",
    "T": "Y",
    "K": "A",
    "R": "E",
    "N": "U"
}


def szyfruj(tekst):

    odp = input("Czy chcesz podać własny szyfr? T/N: ")

    if odp == "T":

        dic_user = {}

        szyfr = input("Podaj szyfr w następujący sposób: XX-XX-...-XX ")

        if len(szyfr) % 3 != 2:

            return "Podano niepoprawny szyfr"

        for i in range(0, len(szyfr), 3):

            if szyfr[i] not in dic_user.keys() and szyfr[i] not in dic_user.values():

                if i != len(szyfr) - 2 and szyfr[i+2] == "-":

                    dic_user[szyfr[i]] = szyfr[i+1]

                elif i == len(szyfr) - 2:

                    dic_user[szyfr[i]] = szyfr[i + 1]

                else:

                    return "Podano niepoprawny szyfr"

        return zamiana_szyfrem(tekst, dic_user)

    elif odp == "N":

        odp = input("Chcesz skorzystać z szyfru GADERYPOLUKI czy z szyfru POLITYKARENU? G/P: ")

        if odp == "G":

            return "Wiadomość: " + zamiana_szyfrem(tekst, dic_gp)

        elif odp == "P":

            return "Wiadomość: " + zamiana_szyfrem(tekst, dic_pr)

        else:

            return "Niepoprawnie wybrany szyfr"

    else:

        return "Uruchom program ponownie i wpisz poprawną odpowiedź"


def zamiana_szyfrem(tekst, szyfr):

    tekst = tekst.upper()

    ans = ""

    for i in range(len(tekst)):

        for key, value in szyfr.items():

            if tekst[i] == key:

                ans += value

                break

            elif tekst[i] == value:

                ans += key

                break

        else:

            ans += tekst[i]

    return ans
