from secrets import choice
from string import ascii_letters, digits, punctuation


def password(length: int, include_digits: bool, include_punctuation: bool) -> str:
    char_pool = ascii_letters

    if include_digits:
        char_pool += digits
    if include_punctuation:
        char_pool += punctuation

    return "".join(choice(char_pool) for _ in range(length))


def main() -> None:
    length = int(input("\nPodaj długość hasła (liczbę znaków): "))
    include_digits = str(input("\nCzy hasło ma zawierać cyfry? (t/n): "))
    include_punctuation = str(input("\nCzy hasło ma zawierać znaki specjalne? (t/n): "))

    include_digits = include_digits == "t"
    include_punctuation = include_punctuation == "t"

    print(
        "\nWygenerowane hasło: " + password(length, include_digits, include_punctuation)
    )

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
