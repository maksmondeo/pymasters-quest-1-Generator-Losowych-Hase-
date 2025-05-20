import contextlib
from secrets import choice
from string import ascii_letters, digits, punctuation

password_words = [
    "jabłko",
    "banan",
    "gruszka",
    "pomarańcza",
    "mandarynka",
    "winogrono",
    "truskawka",
    "malina",
    "borówka",
    "czarna porzeczka",
    "brzoskwinia",
    "nektarynka",
    "śliwka",
    "wiśnia",
    "czereśnia",
    "ananas",
    "mango",
    "kiwi",
    "grejpfrut",
    "limonka",
    "cytryna",
    "granat",
    "figa",
    "daktyl",
    "awokado",
    "kokos",
    "liczi",
    "papaja",
    "marakuja",
    "arbuz",
]


def easy_password() -> str:
    return (
        "".join(choice(password_words))
        + "-"
        + "".join(choice(digits) for _ in range(5))
        + "-"
        + "".join(choice(password_words))
    )


def hard_password(
    password_length: int, include_digits: bool, include_punctuation: bool
) -> str:
    char_pool = ascii_letters

    if include_digits:
        char_pool += digits
    if include_punctuation:
        char_pool += punctuation

    return "".join(choice(char_pool) for _ in range(password_length))


def main() -> None:
    password_type = ""

    while True:
        password_type = input(
            "\nJaki typ hasła chcesz wygenerować?\n"
            "1. Standardowe hasło (losowy ciąg znaków)\n"
            "2. Hasło łatwe do zapamiętania (format: słowo-liczba-słowo)\n\n"
            "Wybierz opcję (1/2): "
        )

        with contextlib.suppress(ValueError):
            password_type = int(password_type)

        if not isinstance(password_type, int) or password_type not in [1, 2]:
            print("\nNieprawidłowa wartość! Spróbuj ponownie.")
        else:
            break

    if password_type == 1:
        password_length = ""

        while True:
            password_length = input("\nPodaj długość hasła (liczbę znaków): ")

            with contextlib.suppress(ValueError):
                password_length = int(password_length)

            if not isinstance(password_length, int) and password_length <= 0:
                print("\nNieprawidłowa wartość! Spróbuj ponownie.\n")
            else:
                break

        include_digits = str(input("\nCzy hasło ma zawierać cyfry? (t/n): ")).lower()
        include_punctuation = str(
            input("\nCzy hasło ma zawierać znaki specjalne? (t/n): ")
        ).lower()

        include_digits = include_digits == "t"
        include_punctuation = include_punctuation == "t"

        print(
            "\nWygenerowane hasło: "
            + hard_password(password_length, include_digits, include_punctuation)
        )
    else:
        print("\nWygenerowane hasło: " + easy_password())

    new_passoword = ""
    while new_passoword not in ["n", "t"]:
        new_passoword = input("\nCzy chcesz wygenerować nowe hasło? (t/n): ")
        if new_passoword == "t":
            main()
        elif new_passoword == "n":
            print("\nDziękuję za skorzystanie z Generatora Haseł!")
        else:
            print("\nNieprawidłowa odpowiedź.")


print("Witaj! Ten program pomoże Ci wygenerować bezpieczne, losowe hasło.")
main()
