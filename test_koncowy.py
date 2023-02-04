from os import system, name
import io
import random
import sys
import time

def clear():
 
    if name=='nt':
        _ = system('cls')
    else:
        _ = system('clear')

def hangman_menu(settings_lifes = 7, settings_difficult = 1):
    operation = 0

    while operation != 1:

        settings_lifes_input = "0"
        settings_difficult_input = "0"

        settings_lifes_description = str(settings_lifes)

        if settings_difficult == 1:
            settings_difficult_description = "niski "
        elif settings_difficult == 2:
            settings_difficult_description = "średni"
        else:
            settings_difficult_description = "wysoki"

        clear()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print("█                                                                         █")
        print("█            Witaj w grze WISIELEC!                                       █")
        print("█                                                  ▄▄▄▄▄▄▄▄▄▄             █")
        print("█                  USTAWIENIA                      █        ║             █")
        print("█                 Liczba żyć: " + settings_lifes_description + "                    █        O             █", sep="")
        print("█           Poziom trudności: " + settings_difficult_description + "               █       /█\            █", sep="")
        print("█                                                  █       / \            █")
        print("█                     MENU                         █                      █")
        print("█                   1. GRAJ!                       █                      █")
        print("█              2. Zmień liczbę żyć               █████                    █")
        print("█           3. Zmień poziom trudności           ▀▀▀▀▀▀▀                   █")
        print("█                                                                         █")
        print("█        Wpisz 'Quit' aby zakończyć grę                                   █")
        print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
        print("")
        operation = input("Wybierz opcję z menu: ")

        if operation.isdigit() and int(operation) == 1:
            return [settings_lifes, settings_difficult]
        elif operation.isdigit() and int(operation) == 2:
            while not settings_lifes_input.isdigit() or not( int(settings_lifes_input) > 2 and int(settings_lifes_input) < 8 ):
                clear()
                print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
                print("█                                                                         █")
                print("█            Witaj w grze WISIELEC!                                       █")
                print("█                                                  ▄▄▄▄▄▄▄▄▄▄             █")
                print("█                                                  █        ║             █")
                print("█                                                  █        O             █")
                print("█            USTAWIENIA: Liczba żyć                █       /█\            █")
                print("█                                                  █       / \            █")
                print("█           Maksymalna liczba żyć: 7               █                      █")
                print("█           Minimalna liczba żyć: 3                █                      █")
                print("█                                                █████                    █")
                print("█                                               ▀▀▀▀▀▀▀                   █")
                print("█                                                                         █")
                print("█        Wpisz 'Quit' aby zakończyć grę                                   █")
                print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
                print("")
                settings_lifes_input = input("Podaj liczbę żyć: ")
                if settings_lifes_input.isdigit() and int(settings_lifes_input) > 2 and int(settings_lifes_input) < 8:
                    settings_lifes = int(settings_lifes_input)
                elif not settings_lifes_input.isdigit() and settings_lifes_input.lower()=="quit":
                    print ("Koniec gry")
                    sys.exit(0)
        elif operation.isdigit() and int(operation) == 3:
            while not settings_difficult_input.isdigit() or not ( int(settings_difficult_input) > 0 and int(settings_difficult_input) < 4 ):
                clear()
                print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
                print("█                                                                         █")
                print("█            Witaj w grze WISIELEC!                                       █")
                print("█                                                  ▄▄▄▄▄▄▄▄▄▄             █")
                print("█                                                  █        ║             █")
                print("█                                                  █        O             █")
                print("█         USTAWIENIA: poziom trudności             █       /█\            █")
                print("█                                                  █       / \            █")
                print("█              1. Niski: Państwa                   █                      █")
                print("█       2. Średni: Państwa i kontynenty            █                      █")
                print("█   3. Wysoki: Państwa, kontynenty i stolice     █████                    █")
                print("█                                               ▀▀▀▀▀▀▀                   █")
                print("█                                                                         █")
                print("█        Wpisz 'Quit' aby zakończyć grę                                   █")
                print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
                print("")
                settings_difficult_input = input("Podaj poziom trudności: ")
                if settings_difficult_input.isdigit() and int(settings_difficult_input) > 0 and int(settings_difficult_input) < 4:
                    settings_difficult = int(settings_difficult_input)
                elif not settings_difficult_input.isdigit() and settings_difficult_input.lower()=="quit":
                    print ("Koniec gry")
                    sys.exit(0)
        elif isinstance(operation, str) and operation.lower()=="quit":
            print ("Koniec gry")
            sys.exit(0)


def hangman_countries(file = "countries.txt"):
    '''
    Loading countries
    '''

    countries = io.open(file, mode="r", encoding="utf-8")
    countries = countries.read()
    countries = countries.split("\n")

    i = 0
    while i < len(countries):
        countries[i] = countries[i].split("\t")
        i += 1

    return countries

def hangman_countries_draw(countries, settings_difficult):
    '''
    Draw country
    '''

    countries_random_number = random.randint(0, len(countries)-1)
    if settings_difficult == 1:
        return countries[countries_random_number][0]
    elif settings_difficult == 2:
        return countries[countries_random_number][0] + " " + countries[countries_random_number][1]
    else:
        return countries[countries_random_number][0] + " " + countries[countries_random_number][1] + " " + countries[countries_random_number][2]

HANGMAN7 = (
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █                      █
█ {1}    █                      █
█ {2}    █                      █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █                      █
█ {2}    █                      █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █                      █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █        █             █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █       /█             █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █       /█\            █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █       /█\            █
█ {3}    █       /              █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █       /█\            █
█ {3}    █       / \            █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")

HANGMAN3 = (
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █                      █
█ {1}    █                      █
█ {2}    █                      █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █                      █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █       /█\            █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █       /█\            █
█ {3}    █       / \            █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")

HANGMAN5 = (
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █                      █
█ {1}    █                      █
█ {2}    █                      █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █                      █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █        █             █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █       /█\            █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █       /█\            █
█ {3}    █       /              █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █       /█\            █
█ {3}    █       / \            █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")

HANGMAN6 = (
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █                      █
█ {1}    █                      █
█ {2}    █                      █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █                      █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █        █             █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █       /█             █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █       /█\            █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █       /█\            █
█ {3}    █       /              █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █       /█\            █
█ {3}    █       / \            █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")

HANGMAN4 = (
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █                      █
█ {1}    █                      █
█ {2}    █                      █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █                      █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █        █             █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █       /█\            █
█ {3}    █                      █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""",

"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                         █
█            Witaj w grze WISIELEC!                                       █
█                                                  ▄▄▄▄▄▄▄▄▄▄             █
█ {0}    █        ║             █
█ {1}    █        O             █
█ {2}    █       /█\            █
█ {3}    █       / \            █
█ {4}    █                      █
█ {5}    █                      █
█ {6}  █████                    █
█ {7} ▀▀▀▀▀▀▀                   █
█                                                                         █
█        Wpisz 'quit' aby zakończyć grę                                   █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")

def string_fill(string_original):
    len(string_original)
    return ( ( 45 - len(string_original) ) // 2 ) * " " + string_original + ( 45 - ( ( 45 - len(string_original) ) // 2 ) - len(string_original) ) * " "

countries = hangman_countries()

while len(countries) > 0:
    wrong=0 # counter to keep track of number of wrong guesses
    letters_tab =[] # list to keep track of letters already guessed
    setting=hangman_menu(7,1)
    lifes=setting[0]
    level=setting[1]
    word = hangman_countries_draw(countries, level)
    so_far = "_" * len(word)        
    new = ""
    empty = "                                             "
    for i in range(len(word)):
        if " " == word [i]:
            new += " "
        else:
            new += so_far [i]
    so_far = new



    while wrong < lifes and so_far != word:
        clear()
        
        if lifes==7:
            print (HANGMAN7[wrong].format(string_fill("HASŁO:"), string_fill(so_far), empty, string_fill("Liczba żyć:"), string_fill("❤ "*(lifes-wrong)), empty, string_fill("Wykorzystane litery:"), string_fill(" ".join(letters_tab).upper())))
        
        elif lifes==5:
            print (HANGMAN5[wrong].format(string_fill("HASŁO:"), string_fill(so_far), empty, string_fill("Liczba żyć:"), string_fill("❤ "*(lifes-wrong)), empty, string_fill("Wykorzystane litery:"), string_fill(" ".join(letters_tab).upper())))
        
        elif lifes==6:
            print (HANGMAN6[wrong].format(string_fill("HASŁO:"), string_fill(so_far), empty, string_fill("Liczba żyć:"), string_fill("❤ "*(lifes-wrong)), empty, string_fill("Wykorzystane litery:"), string_fill(" ".join(letters_tab).upper())))
        
        elif lifes==4:
            print (HANGMAN4[wrong].format(string_fill("HASŁO:"), string_fill(so_far), empty, string_fill("Liczba żyć:"), string_fill("❤ "*(lifes-wrong)), empty, string_fill("Wykorzystane litery:"), string_fill(" ".join(letters_tab).upper())))
        
        else:
            print (HANGMAN3[wrong].format(string_fill("HASŁO:"), string_fill(so_far), empty, string_fill("Liczba żyć:"), string_fill("❤ "*(lifes-wrong)), empty, string_fill("Wykorzystane litery:"), string_fill(" ".join(letters_tab).upper())))
        
        guess = input("Wpisz literę: \t")
        guess = guess.lower()

        if guess in letters_tab:
            print ("Litera już odgadnięta:\t", guess)
            time.sleep(2)
        elif guess in word.lower():
            letters_tab.append(guess)
            print ("Litera \", ", guess, "\" jest w haśle! ")
            time.sleep(2)

            # create a new so_far to include guess
            new = ""

            for i in range(len(word)):
                if guess.lower() == word [i]:
                    new += word[i]
                elif guess.upper() == word [i]:
                    new += word[i]
                else:
                    new += so_far [i]
            so_far = new
        elif guess.lower() == "quit":
            print ("Koniec gry")
            sys.exit(0)
        else:
            letters_tab.append(guess)
            print ("\nNiestety litery \" ", guess, "\" nie ma w haśle...")
            time.sleep(2)  
            wrong += 1

    clear()
    if wrong == lifes:
        print (HANGMAN7[7].format(empty, string_fill("PRZEGRANA..."), string_fill("Masz nieszczęście zostałeś powieszony"), string_fill("Cóż zmarłeś, więc... RIP?"), empty, string_fill("NIEODGADNIONE HASŁO:"), string_fill(word), empty))

    else:
        print (HANGMAN7[wrong].format(empty, empty, string_fill("ZWYCIĘSTWO!!!"), empty, string_fill("ODGADNIĘTE HASŁO:"), string_fill(word), empty, empty))

    time.sleep(4)