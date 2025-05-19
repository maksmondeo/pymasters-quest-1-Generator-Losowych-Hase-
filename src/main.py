from secrets import choice
from string import ascii_letters


def password(length):
    return "".join(choice(ascii_letters) for _ in range(length))


def main():
    length = int(input("\nPodaj długość hasła (liczbę znaków): "))
    print("\nWygenerowane hasło: " + password(length))

    choice = ""
    while choice not in ["n", "t"]:
        choice = input("\nCzy chcesz wygenerować nowe hasło? (t/n): ")
        if choice == "t":
            main()
        elif choice == "n":
            print("\nDziękuję za skorzystanie z Generatora Haseł!")
        else:
            print("\nNieprawidłowa odpowiedź.")


print(
    "=== Generator Haseł ===\nWitaj! Ten program pomoże Ci wygenerować bezpieczne, losowe hasło."
)
main()
